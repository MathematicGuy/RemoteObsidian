Source:
	[Youtube](https://www.youtube.com/watch?v=LB9SklRNDUA)
	[Github](https://github.com/MBDNotes/YOLOv5_PCB_Defects_Detection/blob/main/PCB_defects_Detection.ipynb)


Step 1: Download [Dataset]( https://www.kaggl.com/datasets/akhatova/pcb-defects)
Step 2: Install [XmlToTxt tool](https://github.com/isabek/XmLToTxt)
Step 3: Go to **XmlToTxt** Folder and run
```sh
python -m pip install -r requirements.txt
```
Step 4: Copying all Dataset from **PCB_DATASET/Annotations** to **XmlToTxt/xml** folder   
Step 5: Paste the each PCB part annotation as classes name in **XmlToTxt/classes** file
Example: Open Missing_hole folder
![[Pasted image 20240606153552.png]]
Pick a random file then copy name of the annotation inside `<name>` tag
![[Pasted image 20240606153644.png]]
Paste the name into **classes.txt** file
![[Pasted image 20240606153729.png]]
**Do the same for each annotations**

Step 6: get the absolute path of XmlToTxt folder so we can run the tool
```python
import os  
os.chdir("D:\CMC_UNI\CNTT\AI\ML 2024_2025\Tools\XmlToTxt")
!python xmltotxt.py -c classes.txt -xml xml -out out
```
The result (Txt file) will be stored in **XmlToTxt/out** folder

Step 7: Copy all the .txt annotation from **XmlToTxt/out** and paste it in 
**PCB_DATASET/Annotations**  folder (Remember to Delete all the old folders)
> Optional: Delete the XmlToTxt Tool as you don't need it anymore.

### Arrange Dataset Folder Structure 
> Add this Folder structure to your main project directory
![[Pasted image 20240606154607.png]]

Training Data Ratio: 80% Training images and 20% of images will be Validation images
> you can also change the ratio to 70%-30%  or 65%-35% or 75%-25%

Step 7) Combine all the images with txt file
> copy all the images from **PCB_DATASET/images** and move it to **PCB_DATASET/Annotations**
+ $ Now each file will have a txt file  
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



```python
!pip install requests==2.31.0
!pip install imageio --upgrade
!pip install imageio --upgrade
!pip check
```

Download [Yolov5](https://github.com/ultralytics/yolov5)
