**Definition**
+ same instance: same problem
+ [[fine-tuning]]: adding a adjusted datasets just enough for model to recognize new pattern while not disrupt knowledge it has learned.  (avoid overfitting by lowering LR while fine-tuning )
+ Mouse_bite 01. Trường Hợp 01, Trường Hợp 02
	![[Pasted image 20240912151758.png]]
+ Annotation Format `<class_id> <x_center> <y_center> <width> <height>` this images have 4 defects. (all widths and heights are normalized)
	Ex:  <defect_type_id> <x_coor> <y_coor> <bounding_box_span_width_in_percents> <bounding_box_span_height_in_percents>
	![[Pasted image 20240912155931.png]]
+ [[XML_vs_TXT]]: use XML for details information (car detection include class like car_type, env, weather, light, etc..) and TXT for light weight and high processing speed (surveilliance camera include class like person, object) - note: each class include their their coordinate and confident_rate.


---

**FADS System (Flexible Anomaly Detection System)**
> FAD - System help detecting anomaly in objects/products base on labled datasets.
> Require retrain model for each Objects (Ex: re-train Model to detect anomaly in Water Bottle, PCB, Metal Plate, etc..)

## 1. Understanding the Anomaly Detection Problem
+ **Labeled data:** data labeled by human, exist in text format along with the image. Ex: PCB image with a txt file store the defects coordinate in the image.
	
+ **Anomalies:** Anomlies are unusual pattern that deviate from the expected bahaviour. (e.g. defective product)
	
+ **Flexibility:** Flexibility mean the system able to detect defect/anomalies from various product or object.

## 2. Types of AI Models for Anomaly Detection
2 Hướng tiếp cận, hệ thống có thể hoạt động theo 2 hướng:
+ **Mô Hình học có giám sát (yêu cầu dữ liệu gán nhãn):** 
	+ **Mô hình phân loại** (như ResNet hay Random Forests)
		
	+ **Huấn Luyện Lại:** Mô hình sẽ cần huấn luyện lại để duy trì sự chính xác khi người dùng muốn xác định bất thường trên 1 loại vật thể mới.  (có thể huấn luyện thêm thay vì huấn luyện lại hay không)

+ **Mô Hình học không giám sát (cho dữ liệu không cần gán nhãn)**
	+ **Autoencoder hoặc Isolation Forests:** các mô hình này tìm hiểu các mẫu thông thường và gắn cờ bất cứ thứ gì sai lệch là bất thường.
		
	+ **Tự động nhận diện bất thường:** mô hình không cần gắn nhãn và nhận diện những ngoại lệ trên sự lệch chuẩn của mẫu đã học. Tuy nhiên, nếu bản chất của sản phẩm hay môi trường thay đổi, mô hình sẽ cần tinh chỉnh và đào tạo lại.
+ ? Can I do transfer learning on trained weight? Why can't I add more data rather than re-train


## 3. Steps to Build a Flexible Anomaly Detection System
+ ? Thêm phần định hướng thiết kế hệ thống vào power point. Ex: câu hỏi dẫn tới hướng thiết kế này.
+ ? Tiêu chuẩn đánh giá: lỗ bị thiếu, chuột cắn, mạch hở, mạch ngắn nhánh, đồng giả.

Step 1: Data Collection & Preprocessing 
- Upload Image (Collect Data)
- Preprocess data
+ Feature Engineering: Extract relevant features from the product images or data.  (can use traditional techniques or ResNet Model to extract features)
