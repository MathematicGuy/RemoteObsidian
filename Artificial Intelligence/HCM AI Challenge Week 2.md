### Key Frame Selection, how to optimal ?
nhược điểm khi lấy Cố Định số Frames
+ Bị thừa Frames, chứa Frames ko truyền đạt nhiều thông tin
+ Video dài sẽ đầy dung lg.
-> Cần 1 hàm lọc Frames. **Xét độ tương đồng sau mỗi Frame quá giống nhau thì sẽ loại bỏ** -> Chỉ Lấy những Frames chứa thông tin mới -> Có nhiều thông tin hơn ->  Cần 1 Công thức toán hoặc thuật toán để lấy nhiều thông tin hơn.
![[Pasted image 20250811202133.png]]

**Cons:** lack temporal information, may be a important keyframes  
-> Need to incorporating additional constants to ensure certain required factor are satisfied like
+ Number of Object
+ Color, Location Information
+ ....
![[Pasted image 20250811202448.png]]

### Temporal Search
**Temporal:** thông tin về thời gian như di chuyển, chuyển động con người theo thời gian.

What a optimal Temporal Search Function ??

![[Pasted image 20250811202941.png|500]]
Thuật toán so sánh độ tương đồng của Frames sau Frames hiện tại tới T Frames phía sau nó. (T giống như N, nhưng đại diện cho Temporal Frames)
-> Độ tương đồng của T Frames liền kề phía sau. 

T tối ưu ko bik là gì -> Giả định T bằng 0,1,2,3, ....
Giả định T bằng 3 chẳng hạn, kết quả sẽ là gì ? T8 tốt hơn T3
![[Pasted image 20250811203148.png| 305]]

-> Adaptive Temporal Search Function ?  (hàm có thể Thích nghi)
![[Pasted image 20250811203252.png|333]]
Thêm Tolerance
và Best (Ảnh Tương đồng thấp nhất -> vì đang chọn ảnh mới, lọc ảnh giống)
+ $ **Tóm lại:** Từ Best hiện tại, nếu sau T bước ko có Best tiếp theo thì dừng lại.
Nghĩa là Tolerant càng cao, thì sao càng nhiều Frames phía sau sẽ đc so sánh điểm tương đồng vs Frames hiện tại. 
-> Tradeoff giữa 
+ Khám Phá (Exploraton - Tolerant cao) 
+ và Tốc Độ (Exploiration - Tolerant thấp)
![[Pasted image 20250811204137.png]]
+ @ Cần tận dụng Exploitation để tăng tốc độ truy vấn và áp dụng Khám Phá để tăng cường nhiều kết quả liên quan nhất. (note trừ tượng, cần note lại) 
	*Reference:* [Link] Tinh-Anh Nguyen Nhu, Tien-Huy Nguyen et al. CVPRW2025

### ReRanking
Cho phép thay đổi vị trí của các Kết quả mà mình trả về. Thằng Top10 -> Top 1 hoặc Top 2. **RẤT QUAN TRỌNG trong luồng Retrieval**.

VD: Cần 1 bước Rerank cho câu *"Khung cảnh trời mưa đang ngập lụt"*
![[Pasted image 20250811204650.png]]
Sử dụng những info khác như OCR hay Object Detection để rerank những kết quả lên Top Đầu.
+ ! Nếu OCR hay OD chưa đc huấn luyện tốt thì sao -> khi thêm 1 Class, Object mới sẽ gây nhiễu trong kq -> tốn chi phí, thgian.
+ ! Detect đúng nhưng Object tương đồng với nhau thì sao. Ví cái gậy xám và cái dao xám -> Gây Nhiễu kết quả.  
Note: Query có thể custom lại đc.


**Other Approach:** Làm sao để tăng độ chính xác nhận diện của model khi thêm FEATURES (i.e. TỪ) mới trong Reranking. 
+ $  Using additional V-LLM (Vision LLM). Dựa vào prompt ban đầu của user để đưa ra output tốt hơn, dùng nó làm 1 con score-er (model dùg để chấm điểm)  ![[Pasted image 20250811205503.png]] -> Hệ thống Nặng hơn, tốn kém hơn.

+ $ Using Cross-Encoder Model , model lấy image và text để tính similarity , có thể lấy similarity rồi rerank lại.

+ $ Using Cross-Model Region-Phrase Alignment. ![[Pasted image 20250811205712.png]]
-> Cho mô hình có thể BIỂU DIỄN *FEATURES (từ quan trọng)* tốt hơn. Dùng similarity của model này để reranking lại. 

+ ! Lúc nào cần Reranking lại phải Chạy lại, ko Tối Ưu.
![[Pasted image 20250811205928.png]]
+ $ Solution: SuperGlobal Reranking.
1) Chuyển Features -> vector.
![[Pasted image 20250811210043.png]]

2) **Từ vector đó duyệt lấy Top-K rồi refine feature sử dụng GeM (Generalized Mean)** Pooling = Max + Average Pooling.  Nghĩa là 
	Bước này Ko sử dụng bất cứ 1 model nào khác - resource friendly.
	 Giảm thiểu việc chạy đi chạy lại -> tăng latency, thời gian xử lý.
![[Pasted image 20250811210319.png]]
Note: Local Features là features nhỏ bên trong 1 Feature lớn:
![[Pasted image 20250811210418.png| 400]]

3) **Refined representations:** Xử lý tốt hơn mà ko cần sử dụng Local Features nào khác.  
![[Pasted image 20250811210500.png]]
![[Pasted image 20250811210507.png]]

### Conversational Chat
**User Feedback**
![[Pasted image 20250811210919.png# left| 655]]
**Target:** Cái related thì Cộng. Cái không related thì Trừ. 
	
Reference cho làm sao có thể sử dụng User Feedback 1 cách hiệu quả. 
1. NExT-Search: Rebuilding User Feedback Ecosystem for Generative AI Search
2. A Conceptual Framework for Conversational Search and Recommendation
3. A Survey of Conversational Search
4. ConvGQR: Generative Query Reformulation for Conversational Search

**Ensemble Search**
Dùng 1 model ko cho kết quả tốt -> Dùg sức mạnh nhiều model. 

**Filtering Mechanism**
We use metadata (Object Location, Quantity, Color, ASR, OCR,....) which we’ve extracted
before to filter current results.

**Pose Estimation**
Nhận diện hình dáng dựa trên Skeletal Keypoint (Khung Xương). Cho vài case bao gồm hình dáng người. 

**Segmentation**
Phân vùng Object để nhận diện tốt hơn. Cho Query bao gồm hình dáng. 
![[Pasted image 20250811211224.png| 344]]

**Tagging Search**
**Phân loại mỗi Object là 1 Tag** -> giống như Key Word, tối ưu và đơn giản hóa thông tin mà ko làm mất dữ liệu. 
![[Pasted image 20250811211417.png| 555]]
Giống cơ chế Search của google, 1 keyword -> các Tag tương đồng. Tra cứu Tương Đồng sử dụng Tag -> Đơn giản và tối ưu hơn thay vì search cả 1 câu. 
![[Pasted image 20250811211408.png]]

**Key Phrase:** khi keyword ko hoạt động -> fallback về Keyprhase để lấy thêm thông tin.
![[Pasted image 20250811211433.png# left ]]
Giống cách Tạo Sinh từ Tương đồng của Huân. Dự đoán trên Nhân Quả.
![[Pasted image 20250811211456.png# left| 344]]


**Query Enhancement**
+ $ Cải thiện cho "Văn Bản thiếu ngữ cảnh" để tăng cường thông tin cho Query. Bằng cách sử dụng 1 LLM để rephrase lại Input của mình chi tiết hơn, có nhiều thông tin hơn. 
![[Pasted image 20250811211615.png| 400]]
+ ? **Why:** Tiết kiệm Thời Gian khi nhập văn bản, TH ko dự đoán trước đc.
+ @ STA nói vs Query Enhancement mình viết ngắn thoi, quan trọng là keywords mô tả hình ảnh, rồi để AI nó viết nốt cho mình cũng được.  

### Yếu tố Hiện Thị (video mờ và tương đồng) - verify this
**Gom các Video tương đồng** lại rồi **Search Video theo nhóm**. 
vd: video thuộc nhóm nào ? Chỉ quan sát nhóm đó. 
	Lưu trữ ảnh với độ phân giải cao tốt hơn. Giảm từ 1024 -> 720


**Problem Statement**
![[Pasted image 20250811212351.png | 455]]

**Overall Workflow**
Temporal tr'c rồi reranking sau cũng đc. 
![[Pasted image 20250811212423.png| 555]]


## VQA Task
Giải pháp End-to-End sử dụng Agent.
![[Pasted image 20250811212754.png# left | 544]]
Bài toán: Video + Text -> Câu trả lời mô tả hình ảnh theo Question. 

Agent hoạt động ntn -> nói chi tiết trong buổi 2 Tập Huấn. 
![[Pasted image 20250811212818.png]]

![[Pasted image 20250812001439.png| 555]]

### Validation
Shot Validation: **Lấy top 1 Frame** làm input cho Agent -> Nhược điểm là quá **Phụ Thuộc lớn vào Top.** 
	Làm sao để chọn đc Grouth Truth Shot ? 
→ We need to develop a mechanism to be able to choose the ground truth shot.

Lấy tất cả Video *->* Average result *->* Rerank *->* Top-K *->* Top 1. 
+ ! Khi có quá nhiều ảnh tương đồng -> Kq bị ảnh hưởng.


**Propose Solution**
+ **Reranking Mechanism or N-Gram:** dùng 1 V-LLM để kiểm chứng, nếu top-1 ko trả lời đúng thì chuyển sang top-2, top-3 
	![[Pasted image 20250811213351.png | 333]]
	+ ! Phương pháp này ko hiệu quả khi Grounth Truth ở xa và ko tìm thấy đc -> chạy quá lâu. 

**Frame/Shot Input**
Frame -> tốt khi ko có tài nguyên lớn. 
N-Gram -> Tốm Tài nguyên hơn. 
![[Pasted image 20250811213607.png# left | 433]]


**Shot Summary** for enhancing input (tùy chọn) - dùng 1 LLM khác để tóm tắt lại Ví dụ và Prompt. 
![[Pasted image 20250811213516.png]]


### Prompting
+ ? Nếu Agent chưa trả lời đc thì sao ? Gọi thêm Tools để revised (ghi nhớ lại) Answer -> Prompting + Tools. Viết 1 Prompt để mô hình biết nên chọn những Tools nào để giải quyết vấn đề i.e. Input của người dùng (có thể là câu hỏi hoặc mô tả tìm kiếm 1 hình ảnh)  

**Few-Shot Prompt:** cho vài ví dụ
**Chain of Thought Prompting:**  giúp model tạo flow suy nghĩ và hành động (hành động -> kết quả -> lặp lại)

**Prompt mô tả công việc cho Agent.**
Tùy vào Input, Agent sẽ gọi 1 Tool khác nhau để phục vụ cho Câu Hỏi đó.
![[Pasted image 20250811213924.png]]
Note: **1 Tool là 1 Function hoặc 1 API,** nói chung là 1 service/dịch vụ **để giải quyết 1 hoặc nhiều vấn đề.** Ví dụ:
![[Pasted image 20250811214110.png]]

+ @  **Luồng của Agent sẽ tùy thuộc vào Độ khó của Input** vì **Agent có thể sử dụng nhiều công cụ khác nhau 1 cách Flexible**. Ncl giống con người. 

## Demo AI Agent workflow
High Level

Note: Translate VN -> EN. dùng input Tiếng Anh để tra cứu cho nhanh,. 

Prompt sao cho Model trích xuất ra các Visual Cues (dẫn chứng hình ảnh) - Top 1 đc lấy từ Similarity trung bình của N ảnh. 

Model nhận diện STA sử dụng là YOLOv11 sử dụng 80 Class của COCO. 

Flow của **Class VisualEventExtractor** trong code Baseline:
1) Trích xuất Tag trong Frames. 
	Mô hình Trích xuất TAG (Key Object) chứa trong từng Key Frame để giảm thông tin. 
	ví dụ TAG: ghế, bàn, người, túi, táo, xe máy, etc... (là từ khóa của Object)
	
2) Filtering KeyFrames dựa trên TAG cần truy vấn để trả lời Câu hỏi trong Input..
	
3) Lấy Keyframe chứa Tag cần truy vấn. 

Note: Có thể sử dụng SmallAgent đã phát triển trên HuggingFace. 

+ ? Làm sao để viết 1 câu query tốt ? 
	1 Câu nói Tạo ra Sự **Khác Biệt** -> **Bớt** những từ **Chung Chung** -> **Từ truyền đạt Nhiều thông tin hơn.** (**1 câu chứa nhiều thông tin gồm các từ khóa quan trọng và đc mô tả tốt**) 
	
+ @ **Goals:** viết query làm sao để truy vấn đc hình ảnh mà Btc mô tả. Lưu ý là Mình ko biết hình ảnh đó là gì, chỉ viết lại mô tả của Btc.  
+ **Note:** Giám Khảo sẽ đọc 1 câu hỏi và Mình cần viết lại câu hỏi đó sao cho hệ thống tìm kiếm ảnh Tra Cứu đc Ảnh đó. 
+ **Output** khi Truy Xuất 1 Frames (chứa ID Frames) -> Nộp ID frame truy vấn đc. Bên btc sẽ match theo ID của Frames, xong Video xem có đúng hay ko. 
	Note: Model BLIP cho truy vấn.


**Thực Hành viết query:**
![[Pasted image 20250811221953.png | 333]]
+ ! **Chung Chung:** Những *chiếc xe đỏ trắng đen* đang đậu trong bãi *đất trống lớn.*
+ $ **Cụ Thể:** Nhiều *Xe đỏ trắng và đen* *xếp* thành *hàng ngang* trên mặt đất bị mốc bên cạnh *sân vận động*. Góc *nhìn từ trên xuống*.


![[Pasted image 20250811222442.png]]
+ $ **Cụ Thể:** trẻ em mặc *áo trắng* tụ tập phía trước *tượng màu vàng* và trường học *màu đỏ nhạt*, ở giữa có phông đỏ trắng và chữ vàng
+ ? áo trắng tụ tập trước tượng vàng. Ở giữa có nhà màu đỏ nhạt và tờ giấy đỏ trắng , 

+ ! **Chung Chung:** kẹt xe ban đêm giao lộ thành phố, nhiều xe máy, xe buýt, biển quảng cáo màu xanh, biển quảng cáo màu đỏ, góc chụp từ trên cao


**Query dài tốt hay xấu True/False ?** ý kiến trong phần Chat:
+ như nãy giờ mình dẫn chứng thì **nhiều câu chỉ cần 1-2 từ nhưng đúng trọng tâm cũng search** ra rồi. e.g. có anh ghi Starlord và Redbull nhưng lại tra đc ảnh tắc đường, ảo quá ???
+ False **máy bị phân tán bởi những cái chung chung**, hoặc không phân biệt được quá, cần trọng tâm sự nổi bật
+ mình nghĩ **quá nhiều dữ kiện dẫn tới mô hình không tập trung vào trọng tâm**
+ multiple labels thì **searching sẽ lâu hơn**

![[Pasted image 20250811223721.png]]
-> **Mục Tiêu: Giảm thiểu Không Gian Search** (tượng trưng cho độ lớn của Data có thể truy vấn).
	*Ví Dụ Không Gian Search:* ko gian search màu đỏ chứa mọi kết quả giống Chó và Mèo.   ![[Pasted image 20250811224610.png| 455]]


**Yếu Tố Khác:**
+ **Ngủ Nhiều** -> đi vào **Flowstate** sâu hơn -> để **não nhận diện từ khóa nhanh hơn và tốt hơn** .
+ Luck, Confidence (STA nói Manifest để tự tin hơn), Mentality.

**Chiến Lược Tối Ưu**
+ Cần có sự chuẩn bị.
+ Mỗi thành viên đảm nhiệm 1 phần Search khác nhau.
	1 ng OCR,
	1 ng OD (Object Detection),
	
	Hoặc chia nhau ra search 1 Vùng Không Gian Search (mảng thông tin mà mình Search). Search để lấy thêm thông tin -> Họp nhóm -> Chọn Query tốt nhất. 

**Viết cụ thể giúp Giảm Chiều** Không Gian Search (Search Space) -> **có thể kiếm tra khó hơn vì Ko Gian bé quá**. Có thể **Filter mất Grount Truth trong đó**. 


**Khi bí thì sao ?**
Giảm Theshold cosine
Thử cách Search khác nhau
Chia thành viên:
+ 2 người phụ trách thử nghiệm.
+ 2 người viết Query.

**Luyện viết những từ Độc Lạ** để search cụ thể và chính xác hơn. 
![[Pasted image 20250811224911.png | 433]]

