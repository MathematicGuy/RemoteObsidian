Lecturer: Nguyen Thai Ha (Ph.D)
Date: 21/06/2025 (Sat)
Supporter: Nguyễn Thọ Anh Khoa (Ph.D Candidate)
**Note Objective:** write note so good that even someone don't even watch AIO2025 can understand the concepts clearly.  
	Use memes for simplification (if capable like [this blog](https://ancient-homburg-f58.notion.site/Coding-Methodology-in-Python-20cbdb2c0896802a9fbefef9bd35ec59))
	Give example for each concept or problem
	Explain like you are explain to yourself or your friend
	Always simplified technical concepts and breaking down jargon (từ ngữ chuyên ngành) 

---
## Introduction
**Learning Object**
1) **Unix/Linux Basic**
	Understand Unix philosophy 
	Folder Structure and Shell -> Essential tool for data analysis
	**Agenda:** Linux and its role in data analysis, common linux's distribution, Unix philosophy,  basic shell, folder structure. 
	
2) **Proficient with common terminal commands**
	Basic file operation to text processin, grep, awd, sed and data processing pipeline tools.
	**Agenda:** file/folder management, view content, search/retrieve data, vi/vim editor, processes management and decentralization (phân quyền)
	
3) **Mining and process diverse datas**
	Download from API, process CSV/JSON, download and work with data file, compress file. 
	**Agenda:** Pipe and redirect, filter data with `grep/awk/sed,` process CSV/JSON, `xargs` for parallel processing, data downloading, working with compressed file.


## Unix/Linux Overview 
### What is Linux ? Why it is important ?


### Common Linux Distribution 


### Unix Phiopsophy 


### What is Shell ?



### Linux Folder Structure



### Part 1 Unix/Linux Overview Summary
```ad-summary
summary of part 1
```



## Basic Commands
**Why basic commands ?** for file/folder management, view content, search/retrieve data, vi/vim editor, processes management and decentralization (phân quyền)

### Basic Commands for Data Science
**Lệnh làm việc với thư mục**
`cd, pwd, ls, mkdir` - giúp di chuyển, hiển thị và tạo thư mục mới một cách nhanh chóng
-> goes deeper 

**Lệnh quản lý files**
`touch, cp, mv, rm` - tạo, sao chép, di chuyển và xóa files để tổ chức dữ liệu hiệu quả
-> goes deeper 

**Lệnh tìm kiếm và xem dữ liệu**
`cat, head, tail, grep, find `- xem nội dung, lọc và tìm kiếm thông tin trong files dữ liệu 
lớn.
-> goes deeper 

**Lệnh xử lý dữ liệu**
`sort, uniq, wc, cut, sed, awk` - sắp xếp, loại bỏ trùng lặp, đếm và xử lý dữ liệu theo cột
-> goes deeper 

**Lệnh quản lý hệ thống**
`ps, top, chmod, chown` - quản lý processes và phân quyền files khi làm việc với dữ liệu nhạy cảm
-> goes deeper 

### Create and Manage files/directory



### View files contents




### Search files and data


### Interact with basic text data 


### Edit files with vi/vim


### Enviroment variables


### Permission and files permission


### Processes Management for Data Science Project
`ps aux | grep python`
Liệt kê tất cả các processes Python đang chạy, giúp theo dõi các script phân tích dữ liệu và model training đang hoạt động

`top -u username`
Hiển thị processes theo thời gian thực của user cụ thể, hữu ích khi theo dõi tài nguyên CPU/RAM cho các tác vụ ML nặng

`kill -9 PID`
Dừng process theo ID khi model training bị treo hoặc script xử lý dữ liệu chiếm quá nhiều tài nguyên

`nohup python train.py &`
Chạy script huấn luyện model ở background và duy trì chạy kể cả khi đăng xuất khỏi server, kết quả được lưu vào nohup.out


### Exercise 1
**Objective:** practice basic commands to establish a data analysis project folder structure, include folder structure, config (cấu hình) access permission, files search, verify system structure. 
```txt
1. Tạo cấu trúc thư mục dự án
Tạo một cấu trúc thư mục đã định sẵn cho dự án bao gồm các thư mục con data, scripts, và results bên trong một thư mục
chính tên là project
2. Thiết lập quyền bảo mật
Thay đổi quyền truy cập cho tất cả các tệp trong thư mục project/scripts/ thành 750 (cho phép chủ sở hữu đọc, ghi, thực thi;
nhóm đọc, thực thi; những người khác không có quyền)
3. Tìm tất cả file CSV
Tìm và liệt kê tất cả các tệp có đuôi .csv bên trong thư mục project và các thư mục con của nó.
4. Kiểm tra cấu trúc và quyền truy cập
Xác minh lại cấu trúc thư mục và quyền truy cập của các tệp và thư mục trong project
```
![[Pasted image 20250627152647.png]]



### Part 2 Basic Command Summary 
```ad-summary
```


## 3. Process Data with Command Line
**How ?** Pipe and redirect, filter data with `grep/awk/sed,` process CSV/JSON, `xargs` for parallel processing, data downloading, working with compressed file.

### Pipe and Redirect - Powerful Tools


### Filter commands for Data


### Extract data from large files


### Process JSON data with `jq` 


### Process CSV data with command line


### Combine complex commands


### `xargs` - parallel processing 


### CASE STUDY: Process Real Data



### Download Data from Internet (`wget,` `curl`)



### Working with compressed files



### Decompress and Process multiple files



### Exercise 2
**Objective:** focus on real data processing skill with command line: CSV analysis, process JSON, analyze logs and automate report procedures
```txt
1. Xử lý file CSV người dùng
Xử lý users_2023-01-01.csv: Đếm người dùng theo khu vực. Lọc người dùng theo "Active". Sắp xếp theo tần suất truy cập
(giảm dần).
2. Phân tích dữ liệu JSON thời tiết
Phân tích file weather_hanoi.json. Trích xuất nhiệt độ, độ ẩm theo ngày. Tính nhiệt độ & độ ẩm trung bình.
3. Tạo báo cáo hiệu suất mô hình
Phân tích file model_logs.txt để tổng hợp precision, recall theo ngày và phát hiện xu hướng suy giảm (Đếm precision < 0.75 và
recall < 0.75 theo ngày)
4. Tự động hóa quy trình báo cáo
- Tạo thư mục project/reports.
- Kết hợp lệnh, lưu kết quả vào project/reports/weekly.txt.
- Tạo file data (region_counts.dat) cho biểu đồ.
- Dùng gnuplot vẽ biểu đồ người dùng theo khu vực (users_by_region.png)
```
![[Pasted image 20250627153335.png]]


### Part 3 Process Data with Command Line Summary
![[Pasted image 20250627153427.png# left|500]]



## Overall Unix Linux for Data Science Summary
![[Pasted image 20250627153528.png]]
**reference resources:** ...



