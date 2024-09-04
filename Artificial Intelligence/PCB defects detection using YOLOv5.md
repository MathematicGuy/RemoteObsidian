#todo
+ Connect App to a Database
+ What Algorithm YOLOv5 used

Source:
	[Youtube](https://www.youtube.com/watch?v=LB9SklRNDUA)
	[Github](https://github.com/MBDNotes/YOLOv5_PCB_Defects_Detection/blob/main/PCB_defects_Detection.ipynb)

# Part 1: Extract Data (Xml to Txt)
Step 1: Download [Dataset]( https://www.kaggl.com/datasets/akhatova/pcb-defects)
Step 2: Install [XmlToTxt tool ](https://github.com/isabek/XmLToTxt) and put it in _Tool folder
Step 3: Go to **XmlToTxt** Folder and run (install requirements from XmlToTxt)
```sh
python -m pip install -r requirements.txt
```
Step 4: Copying all Dataset from **PCB_DATASET/Annotations** to **XmlToTxt/xml** folder
Step 5: Paste the each PCB part annotation as classes name in **XmlToTxt/classes** file
Example: Open Missing_hole folder
![[Pasted image 20240606153552.png]]
Pick a random file then copy name of the annotation inside `<name>` tag
![[Pasted image 20240606153644.png]]
Paste the name into **classes.txt** file inside `Tools/XmlToTxt` folder
![[Pasted image 20240606153729.png]]
**Do the same for every other annotations**


Step 6: get the absolute path of XmlToTxt folder so we can run the tool
```python
import os  
os.chdir("Tools\XmlToTxt")
!python xmltotxt.py -c classes.txt -xml xml -out out
```
The result (Txt file) will be stored in **XmlToTxt/out** folder

Step 7: Copy all the .txt annotation from **XmlToTxt/out** and paste it in 
**PCB_DATASET/Annotations**  folder (Remember to Delete all the old folders)
> Optional: Delete the XmlToTxt Tool as you don't need it anymore.

### Arrange Dataset Folder Structure 
> Add this Folder structure to your main project directory. (> mean inside)
```txt
Dataset
> images
	> train
	> val
> lables
	> train
	> val
```


Training Data Ratio: 80% Training images and 20% of images will be Validation images
> you can also change the ratio to 70%-30%  or 65%-35% or 75%-25%

Step 7) Combine all the images with txt file
> copy all the images from **PCB_DATASET/images** and move it to **PCB_DATASET/Annotations** (file automatically mix inside folders)
+ $ Now each image file will have a txt file  
![[Pasted image 20240606161621.png]]
+ ? Copy and Move Annotations folder in the main directory

Step 8) Move the dataset from PCB_DATASET (Don't worry, you don't to do it manually)
+ ? **Run to_v5_directories()** to distribute (move) the data
```python
from random import choice
import shutil
def to_v5_directories(images_train_path,images_val_path,labels_train_path,labels_val_path, dataset_source):
    imgs =[]
    xmls =[]
    # trainPath = images_train_path
    # valPath =  images_val_path
    crsPath = dataset_source
    train_ratio = 0.8
    val_ratio = 0.2
    totalImgCount = len(os.listdir(crsPath))/2
    for (dirname, dirs, files) in os.walk(crsPath):
        for filename in files:
            if filename.endswith('.txt'):
                xmls.append(filename)
            else:
                imgs.append(filename)
    countForTrain = int(len(imgs)*train_ratio)
    countForVal = int(len(imgs)*val_ratio)
    trainImagePath = images_train_path
    trainLabelPath = labels_train_path
    valImagePath = images_val_path
    valLabelPath = labels_val_path
    for x in range(countForTrain):
        fileJpg = choice(imgs)
        fileXml = fileJpg[:-4] +'.txt'
        shutil.copy(os.path.join(crsPath, fileJpg), os.path.join(trainImagePath, fileJpg))
        shutil.copy(os.path.join(crsPath, fileXml), os.path.join(trainLabelPath, fileXml))
        imgs.remove(fileJpg)
        xmls.remove(fileXml)
    for x in range(countForVal):
        fileJpg = choice(imgs) 
        fileXml = fileJpg[:-4] +'.txt' 
        shutil.copy(os.path.join(crsPath, fileJpg), os.path.join(valImagePath, fileJpg))
        shutil.copy(os.path.join(crsPath, fileXml), os.path.join(valLabelPath, fileXml))
        imgs.remove(fileJpg)
        xmls.remove(fileXml)
    print("Training images are : ",countForTrain)
    print("Validation images are : ",countForVal)
#     shutil.move(crsPath, valPath)
```

> Get the Project Directory and Update all the path to the function
```python
# Get the Directory for easy access
os.chdir("D:\CMC_UNI\CNTT\AI\ML 2024_2025\Project\Detect_Anomaly_In_PCB")
os.getcwd() # get directory path
to_v5_directories("dataset/images/train", "dataset/images/val", "dataset/labels/train", "dataset/labels/val", "Annotations\Missing_hole") # Replace all the parameters with the right folder paths 
```
Now Run to see the result:
![[Pasted image 20240606172545.png]]

# Part 2: Process Data (Train and Validate)
**Step 8) Install requirements**
Install necessary library
```python
!pip install requests==2.31.0
!pip install imageio --upgrade
!pip install imageio --upgrade
!pip check
```
Download [Yolov5](https://github.com/ultralytics/yolov5)

Go to **yolov5 directory** and install all the requirements
```python
%cd yolov5
!pip install -r requirements.txt
```

**Step 9) Train Data**
```python
!python train.py --img 416 --batch 16 --epochs 50 --data dataset.yaml --weights yolov5s.pt --cache --name pcb_1st
```

**Step 10) Validata and run test data**
**Validate**
```python
# Validate dataset using the best weight file  
!python val.py --weights runs/train/pcb_1st/weights/best.pt --data dataset.yaml
```
> Put your PCB images to  test_images directory 
![[Pasted image 20240607131358.png]]

> Then run the code 
```python
# Run test dataset from test_images using the best weight file  
!python detect.py --source ../test_images/test_1.jpg  --weights runs/train/pcb_1st/weights/best.pt
```


## Full Code
### Part 1: Setup and Preprocessing 
```ipynb
#%% md  
# # Download Dataset  
#%%  
# !Dataset URL: https://www.kaggl.com/datasets/akhatova/pcb-defects  
#%% md  
# # Convert XML to txt  
#%%  
# Set-up Paths  
root_dir = "D:/CODE/ML_2024_2025/Machine-Learning-2024/Project/Detect_Anomaly_In_PCB"  
tool_dir = "Tools/XmlToTxt"  
yolo_dir = "yolov5"  
#%%  
# git clone https://github.com/isabek/XmLToTxt  
#%%  
import os  
os.chdir(root_dir) # make sure we at the root dir  
os.chdir(tool_dir) # clone XmLToTxT to Tool folder os.getcwd()  
#%%  
# Put .xml file to "xml" folder > Run this command > Output .txt file will be in "out" folder # !python xmltotxt.py -c classes.txt -xml xml -out out  
#%%  
os.chdir(root_dir)  
os.getcwd()  
#%%  
from random import choice  
import shutil  
def to_v5_directories(images_train_path,images_val_path,labels_train_path,labels_val_path,dataset_source):  
    imgs = []  
    xmls = []  
    # trainPath = images_train_path   
    # valPath =  images_val_path  
    crsPath = dataset_source  
    train_ratio = 0.8  
    val_ratio = 0.2  
    totalImgCount = len(os.listdir(crsPath))/2  
    for (dirname, dirs, files) in os.walk(crsPath):  
        for filename in files:  
            if filename.endswith('.txt'):  
                xmls.append(filename)  
            else:  
                imgs.append(filename)  
    countForTrain = int(len(imgs)*train_ratio)  
    countForVal = int(len(imgs)*val_ratio)  
    trainImagePath = images_train_path  
    trainLabelPath = labels_train_path  
    valImagePath = images_val_path  
    valLabelPath = labels_val_path  
    for x in range(countForTrain):  
        fileJpg = choice(imgs)  
        fileXml = fileJpg[:-4] +'.txt'  
        shutil.copy(os.path.join(crsPath, fileJpg), os.path.join(trainImagePath, fileJpg))  
        shutil.copy(os.path.join(crsPath, fileXml), os.path.join(trainLabelPath, fileXml))  
        imgs.remove(fileJpg)  
        xmls.remove(fileXml)  
    for x in range(countForVal):  
        fileJpg = choice(imgs)   
        fileXml = fileJpg[:-4] +'.txt'   
shutil.copy(os.path.join(crsPath, fileJpg), os.path.join(valImagePath, fileJpg))  
        shutil.copy(os.path.join(crsPath, fileXml), os.path.join(valLabelPath, fileXml))  
        imgs.remove(fileJpg)  
        xmls.remove(fileXml)  
    print("Training images are : ",countForTrain)  
    print("Validation images are : ",countForVal)  
#     shutil.move(crsPath, valPath)  
#%% md  
# # Split Dataset to Train and Validation  
# This function will split the dataset into training and validation datasets for each Annotations Data (folder)  
#%%  
os.getcwd()  
#%%  
def split_dataset(directory):  
    # os.listdir(directory) - returns a list of all files and folders in the directory  
    for name in os.listdir(directory):  
        # os.path.isdir(path) ret  
        # urns True if the path is a directory        if os.path.isdir(os.path.join(directory, name)):  
            print(f"{name}")  
            to_v5_directories("dataset-pcb/images/train", "dataset-pcb/images/val", "dataset-pcb/labels/train",  
                              "dataset-pcb/labels/val", f"{directory}/{name}")  
            print()  
        else:  
            print("Your directory path is not correct or not exist!")  
  
split_dataset("../DataSet/PCB_DATASET/Annotations_txt")
```


### Part 2: Training & Valication
```python

```


### Part 3: Test and Deploying
```python

```