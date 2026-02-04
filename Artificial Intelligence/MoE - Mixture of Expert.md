[[Foundation of Mixture of Expert in Statistical Learning in ML]]

### Overview

![[Pasted image 20260131200826.png | 344]]

MoE - nghiên cứu cho thấy trung bình chỉ cần 2 Experts trên 8 expert thoi, inference rẻ hơn Essemble. 

Vấn đề vẫn là tối ưu Gating Network để làm sao Dữ liệu (vấn đề) cần giải quyết đi đến đúng Expert. 

Làm sao để chọn đúng Expert sau mỗi Layer ???
![[Pasted image 20260131202853.png]]


**3 mô hình chính**
![[Pasted image 20260131202954.png]]
Dense - 
Sparse - 
Soft - phức tạp (nhiều toán), cách thiết kế bị phản biện có cách thiết kế tốt hơn nhiều. 

+ ? How to train that thing Gating ?? Bc its basically a Linear layer + Softmax. 
![[Pasted image 20260131203055.png]]
Linear - input go through gating.
1 (input component ROW) x input_dim x (input_dim x router_weight x number_of_expert). 
_The image shoiuld 3x4 matrix bc there are 3 experts.  
![[Pasted image 20260131203445.png]]

Xác suất chọn từng Expert cho Input.
![[Pasted image 20260131204042.png | 444]]

`Nhân % dự đoán của từng Expert` vs `% chọn từng Expert của Router` 
![[Pasted image 20260131204301.png]]

Trong các Experts sẽ chỉ có 1 số Expert thật sự tốt còn lại vô dụng cho 1 đầu vào X (ví dụ là thé) -> Làm sao để tập trung vào Đúng Expert TỐT. 
![[Pasted image 20260131210029.png]]

**Spare Mixture of Experts (SMoE)**
_Chọn Top-K Expert tốt nhất, còn lại Deactivate, ko cho học._ 
![[Pasted image 20260131210244.png]]
Model nhỏ để giải quyết từng local riêng -> giống cách nhà nc hoạt động, có trưởng làng cho địa phương. 
Có những model học sai -> càng học càng sai -> PHẢI loại đi. 
+ ! Bất lợi của Top-K là nó quá Bias cho những thằng đúng, vì ko thể chắn chắn những đứa ko tốt ko có chút ý kiến đúng nào dc (quá độc tài). 
-> Có thể làm MoE tập trung huấn luyện 2 Experts trong 4 Experts quá nhiều khiến các Experts khác ko dc huấn luyện. 

![[Pasted image 20260131211551.png]]
Top-K + Noise để dữ liệu khó hơn -> Chống Overfitting và Bias 1 số Expert quá nhiều. 
Mỗi Expert học 1 bài toán khác. 
Expert 2 học đầu ra của Expert 1. làm sao để các Expert làm việc với nhau ? Chạy for loop ? 
Để các Expert làm việc với nhau thì mình lấy đầu ra của Expert 2 học đầu ra của Expert 1 ạ ?  

### Gating Function (Solve Uneven Learning)
Context:
+ ? 1 số dữ liệu chỉ Expert 2 và 3 dc học và 1.4 ko dc học -> how to sovle this imbalance ? Nếu Expert 2 và 3 học nhiều thì phải điều chỉnh Loss như thế nào để công bằng cho 1 và 4 ?   
+ $ Loss Balancing - cân bằng Loss cho từng Expert. 
![[Pasted image 20260131213816.png]]
trong TH nào thì tunning alpha -> đọc bài báo gốc để hiểu. 
Dữ liệu phân phối ntn ? 


![[Pasted image 20260131214459.png | 644]]

Mỗi Expert sẽ phân loại những Class khác nhau hoàn toàn (Expert 1: phân loại quần, Expert 2 phân loại áo) hay  có thể giống nhau ? 
Làm sao để phân loại đúng dữ liệu cho Mỗi Expert ? hay mỗi Expert sẽ tự động học những vùng dữ liệu giống nhau ? 

## MoE cho ViT
+ ! Expert cho từng Patche -> ko có Global View, mỗi Expert chỉ nhìn dc Local view -> những Patch quan trọng bị Drop cho các Expert. 
![[Pasted image 20260131215452.png]]

Priority Scorer -> Drop những Patch background ko chứa thông tin của Mèo.
![[Pasted image 20260131215559.png]]

![[Pasted image 20260131215616.png]]



![[Pasted image 20260131215702.png]]
+ $ Ko giống Masking, nhưng bỏ từng pixel có chiến lược. Để chỉ chọn những Pixel có giá trị nhất -> GIẢM THIỂU Data khi training. 
Hơi giống Masking ? 
![[Pasted image 20260131215811.png]]
reference: https://research.google/blog/scaling-vision-with-sparse-mixture-of-experts/
Board: [[Scaling Vision Transformers with Sparse Mixture of Experts.excalidraw]]

Tunning khó vì tính bất ổn 
![[Pasted image 20260131220306.png]]
+ ! Noisy Top-K is unstable bc in Derivative, even a slight nudge of value change change the model decision. For example if 1 Expert is 0.8 and 1 is 0.81 then that nudge would change the entire decision -> Instability. ![[Pasted image 20260131222626.png]]
+ ? Some data are more complicated than other, if not distribute evenly some Expert would only learn hard and some would learn Easy. 


**Complexity of Routing**
![[Pasted image 20260131220528.png]]


## Gating Function - Soft Model
+ ? 1 trong những bài NỀN MÓNG của MoE.
![[Pasted image 20260131220621.png]]

![[Pasted image 20260131220811.png]]
+ ? Why MoE ? Because Data is not Hamornious and Generalize. Different type of data have different Patterns -> So its best ot classififed type of Patterns for each Expert. 
![[Pasted image 20260131221016.png]]

![[Pasted image 20260131221213.png]]


### Nơi kiếm báo hay SoTA cho MoE: ICML, ICLR, NeurIPS hoặc OpenReview.net
+ $ Rebutal - phần phản biện -> QUAN TRỌNG để xem paper có vấn đề gì ko.

Xem những bài trong thời giản 2 năm tr'c đó. Xem bài báo nào dc quan tâm nhiều nhất. 

----


![[Pasted image 20260202130649.png]]
Top-1 Routing lấy Top-1 Expert từ mỗi GPU -> Mỗi GPU có 1 Expert thì với batch 8192 token chia đều cho các GPU là 8192 / 8 = 1024.


![[Pasted image 20260202134117.png]]
C (dung lượng mỗi Expert có thể xử lý đc) -> (400 / 4) * 1.2 = 120 
Expert 1 nhận 150 token -> 150 (input) - 120 (capacity) = 30 token thừa (overflow)  
Expert 2 nhận 70 token -> 70 (input) - 120 (capacity) = -50  token thiếu (padding)  

![[Pasted image 20260202135500.png]]
4 GPU, mỗi GPU nhận 250 gửi cho các GPU còn lại 250 tokens 
-> 4 GPU nhận tổng 1000 tokens. Khi 1 GPU nhận tokens, các GPU còn lại nhận tổng 750 tokens.   

![[Pasted image 20260202150613.png]]
XS xử lý của expert A/B = xs chọn nhánh A/B * xs chọn Expert A/B

![[Pasted image 20260202152104.png]]
Y_perm là giá trị từ Permute_idx. 12 ở vị trí 2, 6 cũng ở vị trí thứ 2 trong list nghĩa là giá trị 6 có index 12. 

![[Pasted image 20260202152155.png]]
Công thức `Y[i]` nghĩa là nhân giá trị w và Y_perm tương ứng với index trong permute_index. 
20 * 0.7 + 40 * 0.3 = 26

![[Pasted image 20260202154221.png]]
XS tiên nghiệm là XS của Router chọn Expert: 0.4 cho Expert1 và 0.6 cho Expert2
Xác suất dc chọn của mỗi Expert: 0.8 * 0.4 + 0.6 * 0.2 = 0.44
Xác xuất Expert 1 dc chọn: 0.8 (xs dữ liệu phù hợp vs Expert) * 0.4 (XS route chọn Expert)
-> Sử dụng bayes cho h(1) = P(chọn expert 1) / P(xs mỗi expert)  = (0.8 * 0.4) / 0.44 = 0.7272727273

![[Pasted image 20260202155013.png]]

![[Pasted image 20260202154956.png]]

![[Pasted image 20260202155058.png]]