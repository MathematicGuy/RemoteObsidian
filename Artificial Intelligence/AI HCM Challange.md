**Tổng quan về cuộc thi**
![[Pasted image 20250804203112.png]]

Tổng quan VLM: https://huggingface.co/blog/vlms-2025

### Problem Statement
**Problem Statement for VQA:**
```
Visual Question Answering (VQA): this task type asks specific questions about a particular video or video collection, which are intended to be submitted as a manually entered text (by a human). For example, 'How many nights do we see passing in the video until this segment ?'..... It requires manual inspection and interactive/ automatic exploration.
```


**Problem Statements Known-Item Search (KIS):**
	A single video clip (a few seconds long) is randomly selected from the dataset and visually presented - this is known as **visual KIS (KIS-V)**. The participants need to find exactly the single instance presented. A variation of this task is **textual KIS (KIS-T)**, where instead of a visual presentation, the searched segment is described only by text given by the moderator (and presented as text via the projector).


**Problem Statements for Textual KIS Example:**
	A sequence of shots taken from a moving motorbike.In the first shot we see a view under the rider’s left arm, the handlebar, both mirrors and the rider’s hands are visible.The motorbike moves along a country road, and a red triangular street sign indicates a railway crossing coming up. The following shot is a view down to the road on the right side of the motorbike, first showing the right part of the
	handlebar and then moving forward.

**Requirements:**
+ Each query (Visual KIS, Textual KIS, VQA) is given a time limit of 5 minutes.
- Host competition used metrics calculated by: time and rank of target moment in returned topk submission



**2 Hướng nộp bài:**

![[Pasted image 20250805004357.png| 433]]

![[Pasted image 20250805004411.png| 433]]


### Retrieval MethodsMethods
**Known-Item Search (KIS):** 
+ Video KIS: a video chosen from dataset and 

**Ad-hoc Video Search (AVS):** find as much similar features (instance) between 2 mention context the better.  


![[Pasted image 20250804203635.png|555]]


**Model for Video Retrieval:**
![[Pasted image 20250804203658.png]]



**Inputs:**
+ q -> query 
**Temporal Search**
How to optimal 

**CLIP Embedding Model (VLM)**
![[Pasted image 20250804210408.png]]

VLM + Temporal Search -> Reduce memory Usage. 

![[Pasted image 20250804211218.png]]

**Textual KIS query**
![[Pasted image 20250804212330.png]]
Only save Important information, NOT ALL. 

**Query Enhancement** -> Improve query with Retrieved Information

RA PAPER dưới dạng Ứng Dụng. 

Automation pipeline
**Advantage to be a WINNER**
**Advanaced:** Temporal search, Reranking. 
Query Enhancement
Filtering Mechanism 

### Software
Streamlit - React - FastAPI
Thiết kế trước lượt đồ API

**High-Level Architecture**
![[Pasted image 20250804215758.png]]
**Service** có **3 thành phần chính**.

**Application Object**
![[Pasted image 20250804220010.png|455]]

[HCM AI Baseline github](https://github.com/AIVIETNAM-Hub/HCMAI2025_Baseline)
Note: lưu thông tin truy vấn qua 1 class.
Cấu trúc web BE thông thường. Clean Code

response.py chứa các class cho response.
Input → Google Translate Vietnameses to English
BE: thường sẽ sử dụng Java, C#.
Startup hay Demo: Python → dùng để phát triển bản backend đơn giản. Mì ăn liền so với Java, C#.
  

Support:
- Mỗi nhóm sẽ có Mentor hỗ trợ 1 by 1.
- Support về Ý tưởng, cải tiến và kinh nghiệm cá nhân.

Notice:
- Lấy 1 prototype của FE, BE Clean Code, rõ ràng rồi bảo ChatGPT học theo đó.

Resource:
- Tiền tham gia hội nghị từ 3tr - 6tr đồng.
- 2 tài khoản Collab Pro: nhóm 3 - 5 người đều thuộc AIO là đc.
- Nếu vào Top Rank sẽ đc server 12GB và tiền ĐI ĂN 1 buổi.
	Năm ngoái tỷ lệ chọi là: 100 → 50 → 10

Question: vậy chắc Mô hình sẽ deploy trên Google Cloud a nhỉ ? Sợ máy laptop yếu quá chỉ có 4VRam ko biết tham dự cuộc thi như thế nào ? :((

---

Thay vì tích hợp Google Search Engine -> tích hợp luon ChatGPT API. hoặc Google Image API.
![[Pasted image 20250806110242.png]]

Filter Video theo vị trí và thời gian dựa trên context trong hình ảnh. -> chỉ Tra cứu video có thông tin tại địa điểm Hy Lạp. 

Tìm Frame nào có cả ví và người phụ nữ.
Kết hợp Weight -> 

Best Practice: thu hẹp scope.
Mỗi ng ngồi search sẽ khác nhau. 
Kết hợp công cụ tìm kiếm như Google Image.
Kết hợp ChatGPT để truy vấn VQA.

Keyframe hay I-Frame gồm 1 frame đầy đủ của 1 video, ko chứa video tr'c đó .
![[Pasted image 20250806110827.png|435]]


![[Pasted image 20250806111055.png|444]]

CLIP Features
![[Pasted image 20250806111112.png|]]
Thiết kế hệ thống hiệu quả, đảm bảo không có Bottle Neck. 
![[Pasted image 20250806111409.png| 544]]

Vấn đề về đường truyền - chuẩn bị trước Mạng 4G, 5G để tốt nhất, mạng của nhà tổ chức có thể yếu vì nhiều người dùng.

**Thành phần chính sinh viên cần hiểu:** base-line code, training sử dụng công cụ btc cung cấp, cố gắng tham gia đầy đủ tập huấn, HIỂU CÔNG CỤ mình đag có. Team có thể dùng model gì cũng được. 

Được sử dụng mọi phương pháp để đạt hiệu quả cao nhất. 

Phải ngồi xem toàn bộ video - AIAgent trích xuất nội dung chính. 
