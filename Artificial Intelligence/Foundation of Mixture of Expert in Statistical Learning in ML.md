*MoE càng scale* lên trăm >100 tỷ tham số *càng khó (dễ fail)*. THông thường chỉ Scale ở hàng chục tỷ tham số. -> Chỉ 4 cty thành công. 

**Vấn đề chính: ROUTING (phân luồng Expert)** bị bias về 1 model khi 1 model hoạt động quá tốt. Dù có Loading Balancing nhưng vẫn ko giải quyết đc -> vấn đề 2.

*Shared Experts* (giống ý tưởng Skip-Connection) - *học nông* nhiều chuyên môn.
*Routed Experts* - *học sâu* 1 chuyên môn.

*MoE -> cheaper AI Model Scaling.*
Khả năng dự đoán và giải thích chuyên sâu của mỗi expert tốt hơn so vs 1 model đơn lẻ. 

Model đơn lẻ càng scale lên tính giải thích 1 chủ đề càng thấp so trí nhớ sụt giảm cho nhưng kiến thức đã học tr'c. 

**Note:** Tr'c khi dữ liệu vào Gate thì **chỉ Scale data thoi**, ko đưa về 1 Domain. 

---
E for Expert
moe - MoE
**MoE -> Bài toán phân loại cho Expert sử dụng softmax. (Giống Multi-Class Classification)**
Khả năng học của E ntn -> Hàm Loss ? 
Vs data có sẵn E học đc DOmain nào, tính chất nào của hàm ảnh hưởng tới khả năng học của Expert. 
học yếu tố nào ? 
Softmax -> assign Weight cho hàm f (linear or none-linear)
Gaussian -> tượng trưng cho Std -> phân loại E cho dữ piệu phân phối đó.

**Vấn đề:** Fit bao nhiêu Expert là đủ

Tối ưu hàm log softmax.
Có 3 đg thẳng mà có 10 E -> Data Collapse. 

**G** is the **Mixing Measure**. It is essentially the "blueprint" of the entire Mixture of Experts model. It **encapsulates everything the model doesn't know and needs to learn:**
- **The Router (Gating):** The weights β1i​ and biases β0i​ that decide how to distribute the input.
    
- **The Experts:** The parameters (ai​,bi​) that define each individual regression expert.
    
- **The Scales:** The variance/spread (σi​) of the Gaussian distributions.
    
- **The Complexity:** The number of experts k0​.

+ ? 3 đg phân phối Gaussian - mật độ các điểm của 3 đường thẳng -> Cần Fit đúng số Expert (3) trên tổng số 10 Expert cho 3 đg phân phối (Gauss) đỏ. 
	**Likelihood of the Mixture:** You aren't just maximizing the probability of picking the "right" expert (classification). You are *maximizing the probability* that the **combined weighted sum** of all experts explains the observed data Y.

![[Pasted image 20251219114720.png# left  | 433 ]]
+ ? Tính Loss của các Expert G_n và target G (đg đỏ Gauss). Khớp dự đoán mô hình với đường cong phân phối Gauss màu đỏ. 
+ ! Nhưng vì **G_n có quá nhiều Expert (k > $k_{0}$), nên nó có tham số "phụ" so với G. (Có nhiều tham số hơn vs G -> ko cân xứng**)

**Hàm Loss Voronoi** -> Giải quyết vấn đề tính Loss, có nhiều Expert (G_n) hơn so với Expert mong đợi G, nói cách khác  **Expert trùng lên nhau**
	Phân loại E và tham số của nó. 
	Cell phân loại dựa trên độ gần của đỏ + xanh. (expert so vs dữ liệu)
	Phân rã data thành 3 nhóm -> phân nhóm Model. 


Đánh giá độ phức tạp thuật toán 

**Rate of param estimation**
Độ phức tạp của expert theo n 
Note: học đg cong -> càng nhiều expert càng tốt. 

---
Làm sao có thể sử dụng Theory ở trên để cải thiện model Transformer ở dưới. 
## Improve self-attention to Transformer
**Apply to the FINAL LAYER:** **Non-Linear for Value V in Attention (Q, K, V)** e.g. ReLU, GeLU, etc..
![[Pasted image 20251219140533.png | 344]]


## Boosting Performance of LoRA
Simplified 4 variable into 2 shared parameters, 
Add Non-Linear