## Phần 1: Trích xuất dữ liệu (Xml sang Txt)
Bước 1: Tải xuống [Dataset]( https://www.kaggl.com/datasets/akhatova/pcb-defects)
Bước 2: Cài đặt [công cụ XmlToTxt ](https://github.com/isabek/XmLToTxt) và đặt vào thư mục _Tool
Bước 3: Vào Thư mục **XmlToTxt** và chạy (cài đặt yêu cầu từ XmlToTxt)
```sh
python -m pip install -r requirements.txt
```
Bước 4: Sao chép toàn bộ Dataset từ **PCB_DATASET/Annotations** vào thư mục **XmlToTxt/xml**
Bước 5: Dán chú thích từng phần PCB làm tên lớp trong tệp **XmlToTxt/classes**
Ví dụ: Mở thư mục Missing_hole
![[Pasted image 20240606153552.png]]
Chọn một tệp ngẫu nhiên sau đó sao chép tên chú thích bên trong thẻ `<name>`
![[Pasted image 20240606153644.png]]
Paste the name into **classes.txt** file inside `Tools/XmlToTxt` folder
![[Pasted image 20240606153729.png]]
**Làm tương tự với mọi chú thích khác**


Bước 6: lấy đường dẫn tuyệt đối của thư mục XmlToTxt để chúng ta có thể chạy công cụ
```python
import os  
os.chdir("Tools\XmlToTxt")
!python xmltotxt.py -c classes.txt -xml xml -out out
```
Kết quả (tệp Txt) sẽ được lưu trữ trong thư mục **XmlToTxt/out**


Bước 7: Sao chép tất cả chú thích .txt từ **XmlToTxt/out** và dán vào thư mục
**PCB_DATASET/Annotations** (Nhớ xóa tất cả các thư mục cũ)
> Tùy chọn: Xóa Công cụ XmlToTxt vì bạn không cần nó nữa.


### Sắp xếp cấu trúc thư mục tập dữ liệu
> Thêm cấu trúc thư mục này vào thư mục dự án chính của bạn. (> nghĩa là bên trong)
```txt
Dataset
> images
	> train
	> val
> lables
	> train
	> val
```

note: Tỷ lệ dữ liệu đào tạo: 80% hình ảnh đào tạo và 20% hình ảnh sẽ là hình ảnh xác thực
> bạn cũng có thể thay đổi tỷ lệ thành 70%-30% hoặc 65%-35% hoặc 75%-25%


Bước 7) Kết hợp tất cả các hình ảnh với tệp txt
+ ? Đổi tên Annotation -> Annotation_txt
> sao chép tất cả các hình ảnh từ **PCB_DATASET/images** và di chuyển đến **PCB_DATASET/Annotations_txt** (tệp tự động trộn bên trong các thư mục)
+ $ Bây giờ mỗi tệp hình ảnh sẽ có một tệp txt
![[Pasted image 20240606161621.png]]
+ ? Sao chép và di chuyển thư mục Chú thích trong thư mục chính

Step 8) Di chuyển tập dữ liệu từ PCB_DATASET (Đừng lo, bạn không phải thực hiện thủ công)
+ ? **Run to_v5_directories()** để phân phối (di chuyển) dữ liệu
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


### Phân chia dữ liệu
>Chức năng này sẽ phân chia tập dữ liệu thành các tập dữ liệu đào tạo và xác thực cho mỗi Dữ liệu chú thích (thư mục)
```python
def split_dataset(directory):
    # os.listdir(directory) - returns a list of all files and folders in the directory
    for name in os.listdir(directory):
        # os.path.isdir(path) ret
        # urns True if the path is a directory
        if os.path.isdir(os.path.join(directory, name)):
            print(f"{name}")
            to_v5_directories("dataset-pcb/images/train", "dataset-pcb/images/val", "dataset-pcb/labels/train",
                              "dataset-pcb/labels/val", f"{directory}/{name}")
            print()
        else:
            print("Your directory path is not correct or not exist!")

split_dataset("../DataSet/PCB_DATASET/Annotations_txt")
```
Kết Quả
![[Pasted image 20240606172545.png]]

# # Phần 2: Xử lý dữ liệu (Đào tạo và Xác thực)
**Bước 8) Cài đặt yêu cầu**
Cài đặt thư viện cần thiết
```python
!pip install requests==2.31.0
!pip install imageio --upgrade
!pip install imageio --upgrade
!pip check
```
Download [Yolov5](https://github.com/ultralytics/yolov5)

Vào **thư mục yolov5** và cài đặt tất cả các yêu cầu
```python
%cd yolov5
!pip install -r requirements.txt
```

**Step 9) Huấn Luyện Dữ Liệu** (từ 50 tới 250 epoch)
```python
!python train.py --img 416 --batch 16 --epochs 50 --data dataset.yaml --weights yolov5s.pt --cache --name pcb_1st
```

**Bước 10) Xác thực và chạy dữ liệu thử nghiệm**
**Đánh Giá**
```python
import os

# validate every train
def validate_all_runs(runs_directory, data_config_path):
    # Ensure the runs directory exists
    if not os.path.isdir(runs_directory):
        raise ValueError(f"The directory {runs_directory} does not exist.")

    # Iterate through each directory in runs/train/
    for run_name in os.listdir(runs_directory):
        run_path = os.path.join(runs_directory, run_name)

        # Construct the path to the best.pt file
        best_weights_path = os.path.join(run_path, 'weights', 'best.pt')

        # Check if the best.pt file exists
        if os.path.exists(best_weights_path):
            print(f"Validating YOLOv5 model in {best_weights_path}")

            # Execute the validation command
            !python val.py --weights {best_weights_path} --data {data_config_path}
        else:
            print(f"Warning: {best_weights_path} does not exist, skipping this run.")

# Example usage
validate_all_runs('runs/train', 'dataset.yaml')
```
> Đặt hình ảnh PCB của bạn vào thư mục test_images
![[Pasted image 20240607131358.png]]

> Đảm bảo chuyển đổi Weight bằng torch nếu bạn sử dụng Window và gặp lỗi này: NotImplementedError: không thể khởi tạo 'PosixPath' trên hệ thống của bạn.
```python
import torch

ckpt = torch.load('runs/train/pcb3_250/weights/best.pt', map_location='cpu')
print(ckpt.keys())  # Inspect the contents of the checkpoint file

torch.save(ckpt, '../../dataset-pcb-runs/best2.pt')
```

Chạy thử nghiệm dùng weight mới lấy được:
```python
# Test every images inside test_images folder
def run_yolov5_on_directory(directory_path, train_name):
    # Ensure the directory exists
    if not os.path.isdir(directory_path):
        raise ValueError(f"The directory {directory_path} does not exist.")

    # Iterate through each file in the directory
    for filename in os.listdir(directory_path):
        # Construct the full file path
        file_path = os.path.join(directory_path, filename)
        print(file_path)
        # Check if the file is an image (you can adjust the extensions based on your needs)
        if filename.endswith(('.jpg')):
            print(f"Running YOLOv5 on {file_path}")

            # Execute the command
            !python detect.py --source {file_path} --weights runs/train/{train_name}/weights/best.pt

run_yolov5_on_directory('../test_images', 'pcb_2nd_100')
```


# Thiết lập Back-End

### Yêu cầu
- Python 3.8+
- Node.js 16+ / npm 8+
- PostgreSQL (hoặc DB khác tương thích với SQLAlchemy)
- Trọng số được đào tạo trước YOLOv5

1. **Tạo môi trường ảo**:
```bash
python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

2. **Cài đặt các phần phụ thuộc**:
```bash
pip install -r requirements.txt
```

3. Thiết lập FastAPI CLI
```sh
pip install "fastapi[dev]"
```
### 2. Thiết lập cơ sở dữ liệu
Đảm bảo PostgreSQL hoặc bất kỳ cơ sở dữ liệu tương thích SQLAlchemy nào khác đã được cài đặt. Tạo cơ sở dữ liệu có tên là `detect_anomaly_pcb`.
```sh
pip install sqlalchemy psycopg2
```
**Cấu hình cơ sở dữ liệu:** Trong tệp `database.py`, hãy đảm bảo bạn cấu hình cơ sở dữ liệu như sau:
```python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configure this to your own URL
SQLALCHEMY_DATABASE_URL = "postgresql://user:password@localhost/dbname"  # Update with your actual database URL

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
```

Cập nhật thông tin chi tiết về kết nối cơ sở dữ liệu trong `backend/database/database.py`.
Chạy lệnh sau để khởi tạo các bảng cơ sở dữ liệu:
```bash
python backend/database/init_db.py
```

### 3. Thiết lập trọng số YOLOv5
Tải xuống trọng số mô hình YOLOv5 và đặt chúng vào thư mục `backend/weights/`.
Bạn có thể tải xuống trọng số YOLOv5 từ kho lưu trữ YOLOv5 chính thức hoặc sử dụng trọng số được đào tạo tùy chỉnh của bạn.
### 4. Cài Đặt Database

Sau khi mọi thứ đã được thiết lập, bạn có thể chạy máy chủ phụ trợ bằng FastAPI:
```sh
cd backend
sh run.sh
```
or
```sh
cd backend
fastapi dev
```
> Nếu bạn muốn gỡ lỗi, hãy thêm docs vào cuối URL: http://127.0.0.1:8000/docs


# Thiết Lập Front-End
```sh
git clone https://github.com/MathematicGuy/PCB-Anomaly-Detection-using-YOLOv5.git
```

Cài đặt các phụ thuộc
```sh
cd frontend
npm install
```

chạychạy frontend
```sh
npm start
```

## Cách sử dụng

1. **Tải hình ảnh lên**: Vào giao diện, sử dụng mục "Tải hình ảnh lên" để tải hình ảnh của bạn lên. Những hình ảnh này sẽ được lưu trữ trong thư mục `images/test_images`.
2. **Xử lý hình ảnh**: Nhấp vào "Xử lý hình ảnh" để phát hiện các bất thường trong hình ảnh đã tải lên. Hình ảnh đã xử lý sẽ được chuyển đến thư mục `images/processed`.
3. **Xem hình ảnh đã xử lý**: Hình ảnh đã xử lý sẽ xuất hiện trong mục "Hình ảnh đã xử lý mới nhất".
4. **Tải xuống tất cả hình ảnh**: Nhấp vào "Tải xuống tất cả" để tải xuống tất cả hình ảnh từ thư mục đã xử lý mới nhất dưới dạng tệp zip.

## API Endpoint

- **Tải hình ảnh lên**: `/upload/` (POST) - Tải hình ảnh lên để xử lý.
- **Xử lý hình ảnh**: `/process/` (POST) - Chạy YOLOv5 trên hình ảnh đã tải lên.
- **Lấy thư mục được xử lý mới nhất**: `/latest-pros/` (GET) - Lấy thư mục được xử lý mới nhất.
- **Tải xuống thư mục được xử lý mới nhất**: `/download-latest-pros/` (GET) - Tải xuống tất cả hình ảnh từ thư mục được xử lý mới nhất.
- **Xóa hình ảnh**: `/delete/{filename}` (DELETE) - Xóa hình ảnh khỏi thư mục `images/test_images/`.

## Cấu trúc thư mục

- `backend`: Chứa tất cả mã API phụ trợ, bao gồm tích hợp YOLOv5 và mô hình cơ sở dữ liệu.
- `frontend`: Chứa ứng dụng React để tải hình ảnh lên, xử lý chúng và tải xuống kết quả.
- `images/test_images`: Lưu trữ hình ảnh đã tải lên để xử lý.
- `images/processed`: Lưu trữ hình ảnh đã được YOLOv5 xử lý.
- `images/uploaded`: Lưu trữ bản sao lưu của hình ảnh sau khi chúng được xử lý.