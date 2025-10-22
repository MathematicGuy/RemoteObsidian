AWS - github for dataset ? 
**Problem**
1) **Team work:** How to work together on a set of data without conflict and waste downloading time. 
2) **Tons of work:** hard to work together. 


**Data Versioning pipeline**
![[Pasted image 20251002203416.png]]

**DVC** connect code, data and configuration version. 
![[Pasted image 20251002204135.png]]

**With & Without DvC**![[Pasted image 20251002204405.png]]'
Always add DvC first before git. Because git will update the data first and causes in-sync.

dvc .yaml - define stages of the machine learning pipeline. 
dvc push vs git push - for project with dvc setup, git push only save/upload meta to git while dvc push upload tracked data to remote storage (like aws s3, gcs)
To connect to aws with dvc we use - dvc push. 
Before running dvc repro you need: 
+ define dvc .yaml 
+ library: dvc, dvc-s3
+ git repo initialized

**DvC determine a stage need to rerun by** *comparing the stages* of the workspace *with the info stored in the dvc.lock file and the dvc.yaml* stage definition. In short, any changes in hash code, dependency or parameters defined in .dvc's stage trigger a rerun. 

---
**Data Leaking -** your model might have cheat if you have this, your training data includes infor that would not be available at prediction time in the real world, **unexpected data got leaked at model's prediction.** 
	Your model learns from the future, making it look very accurate during training but fail badly in the real world. 

**SDK vs REST API:** 
API - tools
SDK - provides envrionment & tools to build that system i.e. helper-function for re-create those tools & the API. 
	e.g. take MilvusDB SDK for example, it include document/guide book and function that you can called directly, some of that function have integrated API for saving your data to online Milvus DB.  ![[Pasted image 20251021213837.png# left | 555]]
SDK often wraps one or more APIs, providing extra ultilities so developer don't have to manually setting things up manually e.g. preprocessing, prediction, log, etc..

**Đánh giá Feast Doc:** 
+ Trong phần Intro (dẫn nhập ???) - nói dài dòng, trong 3 câu đầu không đi thẳng vào vấn đề mà công cụ giải quyết, ý chính muốn truyền đạt. (Lòng vòng). 
	VD intro 1 cách ngắn gọn: Feast giúp giải quyết 1 vấn đề chính là "Sự thiếu nhất quán trong logic xử lý đặc trưng giữa môi trường thử nghiệm (trái) và vận hành (phải) dẫn đến rủi ro sai lệch...khi `[NGỮ CẢNH]`". 

+ nêu quá nhiều luận điển, ý chính. Ý chính không được tập trung hay làm nổi bật. 
+ các Khái niệm mang chính technical cao -> khó hiểu cho nhiều người. Nên giải thích 1 cách chung dễ hiểu trước khi đi vào technical. 
+ Trong workflow có giải thích từng thành phần nhưng thiếu mũi tên mô tả flow  của các components chính "bên trong".
+ $ Next time, read the quiz first to see what you need or want to learn specificaly.

### Feast - help train ML/DL prediction model continously
Given that your prediction and trainining step use the same dataset, how to make sure the data that you used to train your model is clean and doesn't conflict with the data that used for prediction. Cause in a same dataset, its very likely for data leakage (model use future timeseries data for training thus achieve 100% accuracy). 
![[Pasted image 20251021204731.png]]
Given that we use *real-time dataset what get update over time*. 
+ Feast - is a Feature store serve as central hub for managing, storing and serving features consistently across training and production. 
+ Point-in-time - get data within a point-in-time because we need that 20% left for validation, not get the whole dataset. So just take all the data that exist more than 5 minutes, not the newest dataset.  
+ registry: the only brain of the system / coordination system for every components. 

#### Vai trò và Phạm Vi
**Feast** đóng vai trò là **1 lớp điều phối dữ liệu có khả năng tích hợp các nền tảng CSDL khác 1 cách linh hoạt** e.g. Snowflake, BigQuery cho Offline Store, Redis, DynamoDB cho Online store, thậm chí là tích hợp cả Airflow để lên lịch cho tác vụ nạp dữ liệu (Extract). **Basically a tool that help to build MLOps pipeline.** 
-> Ncl **Feast giải quyết Training-Serving Skew** trong đó Serving là dữ liệu cho prediction. 
![[Pasted image 20251021215927.png]]

**Project Folder Structure** where
Entity: represent the Object which the features describe ???? in a Database e.g. customer_id, product_id.  
![[Pasted image 20251021213933.png# left | 255]]

**Code Notes:**
+ FileSource() - define/connect dataset path at X timestamp. 
+ FeatureView() - nhóm/liên kết các đặc trưng và chỉ định data source. Note: FileSource() là 1 tham số trong FeatureView.  
+ **Registry is like the main function**, its store **Feast helper function metadata i.e. helper func parameters.** for Transform -> Storage -> Serving.

**Common Feast's CLI**
`feast init <tên_project>`: **Khởi tạo 1 Project Feast folder structure template** (một
Feature Repository).
`feast apply`: Đọc các định nghĩa (i.e. **Feast Object** definition like *feature views, entities and data sources*) Python trong repo, đăng ký chúng vào registry, và cập nhật hạ tầng *(ví dụ: tạo bảng trong Online Store*).
`feast materialize <ngày_bắt_đầu> <ngày_kết_thúc>`: **Nạp dữ liệu đặc trưng từ Offline**
**Store vào Online Store trong một khoảng thời gian nhất định** để chuẩn bị cho việc phục
vụ online.
`feast ui`: Khởi chạy một **giao diện web** để khám phá các đối tượng đã được đăng ký trong
Feature Store.

**Common retrieval func:**
`store.get_historical_features(...)`: Dùng để lấy **dữ liệu lịch sử từ Offline Store**
**để tạo ra bộ dữ liệu huấn luyện** hoặc thực hiện dự đoán theo lô. Hàm này thực hiện các
phép join point-in-time correct để chống rò rỉ dữ liệu.
`store.get_online_features(...)`: Dùng để **lấy vector đặc trưng mới nhất từ Online**
**Store với độ trễ thấp**, phục vụ cho việc dự đoán thời gian thực.
```python

					   ┌────────────────────────────────────┐
					   │            Registry                │
					   │ (Metadata + Definitions + Versions)│
					   └────────────────────────────────────┘
									   ▲
					 ┌─────────────────┼─────────────────┐
					 │                 │                 │
					 ▼                 ▼                 ▼
		 ┌────────────────┐   ┌────────────────┐   ┌────────────────┐
		 │ Transformation │   │   Storage      │   │    Serving     │
		 │ (Feature logic)│   │(Offline/Online)│   │ (Online/Batch) │
		 └────────────────┘   └────────────────┘   └────────────────┘
					 ▲                 ▲                 ▲
					 │                 │                 │
					 └──────────┬──────┴──────┬──────────┘
								│             │
								▼             ▼
						 ┌──────────────────────────┐
						 │   Data Sources (raw)     │
						 │  Parquet, BigQuery, etc. │
						 └──────────────────────────┘
```
![[Pasted image 20251021223950.png]]

For clarity, I want to Review Feast paper & slides.
Quick Playback review section of the main topic to see what it about. (*Extract main idea TA want to convey*)
-> Brain Storming Outline overview.  

-> Save Images for AIO Conquer Report.  
-> NoteLM for quick Outline overview 
-> Gemini to help me Summerize it all up for the Report.

