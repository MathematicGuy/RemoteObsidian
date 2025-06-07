## Introduction
Các mảng trong môi trường Python. 
![[Pasted image 20250607071337.png]]

## Data Representation in Python
**Variable Type:** Integer, Float, String, Boolean 
**Variable:** 1 cái tên đại diện cho 1 giá trị nào đó.
+ ? Value should be represent by a variable name (giá trị phải có tên biến) 
![[Pasted image 20250607071754.png]]

### Overflow & Underflow
**Overflow** (số quá to) là khi một số lớn hơn giới hạn của kiểu dữ liệu mà nó được khai báo. Tuy nhiên python có thể điều chỉnh tự động các giá trị số nguyên rất lớn mà không bị tràn. e.g. làm tròn về `inf`
**Underflow** (số quá bé) là khi một số nhỏ hơn giới hạn của kiểu dữ liệu mà nó được khai báo khiến giá trị đó bị "làm tròn về không" dẫn đến mất mát độ chính xác và kết quả ngờ tới. 

### Text Representation with Python
Các kí tự String hay số đều được encode bằng UNICODE (e.g. 1 giá trị byte nào đó) nên khi dữ liệu truyền qua internet nó sẽ được truyền qua dạng những con số, còn khi hiển trị dữ liệu cho người dùng, giá trị byte sẽ được dịch trở lại dạng text. 
![[Pasted image 20250607072707.png]]


### List
Bao gồm value (giá trị trong list) và index (vị trí của giá trị trong list, bắt đầu từ 0)
![[Pasted image 20250607073216.png]]

### Dictionary
Như dictionary bao gồm từ và ý nghĩa của từ đó, dictionary trong bao python bao gồm key và value 
+ ? Trong đó value là có thể là 1 hoặc 1 list các giá trị còn key là giá trị đại diện cho toàn bộ giá trị chứa trong nó. 
+ ? Khái niệm key:value cũng có thể hiểu là trong 1 cuốn sách key là tiêu đề trang và value nội dung của trang. 
![[Pasted image 20250607073417.png]]

### Other Data Representation
**Tabular and Image**
![[Pasted image 20250607073851.png]]


### Function
+ $ **Tên Hàm** thường được đặt bằng **1 Động Từ.**
![[Pasted image 20250607074150.png]]
Miêu tả qua về hàm. 

Ngoài các hàm mình tự khai báo thì **Python** có **bao gồm rất nhiều các hàm có sẵn, trong đó các hàm liên quan đến nhau thường được gọi thông qua 1 Module**  
+ ? e.g. `random`,  `sqrt` functions from `math` module. 
```python
import math # have log() function, random() function
print(math.log(math.e)) # output 1.0 because log(e) = 1

""" you can import a function directly for convinient """
from math import e, log
print(log(e))
```


### Ứng dụng của Log trong Machine Learning
![[Pasted image 20250607075513.png]]
+ ? Log tăng trưởng mạnh sau khi log(x) > 1 -> **Giá trị được khếch đại nếu log(x) > 1**
+ $ Nhiều khi việc tìm giá trị Loss nhỏ nhất quá khó, người ta sẽ **dùng log để khuếch đại sự khác biệt giữa các giá trị** -> Ngoài Loss, log có thể dùng để **Highlight các sai số giữa giá trị thực và giá trị dự đoán**, hoặc **phát hiện ra liệu có điểm dữ liệu lớn/nhỏ bất thường hay không**. 
+ Hình dáng khác đi nhưng giá trị nhỏ nhất và lớn nhất vẫn là 0 (không đổi) 
![[Pasted image 20250607075338.png]]

### Ví dụ thực tế: Thiết kế 1 hàm Loss
**Đánh giá độ bất ngờ**, nghĩa là khi bốc 1 quả bóng ngẫu nhiên mà không nhìn, **đánh giá xem trong 2 TH bóng đỏ và bóng xanh, bóng nào có khả năng đoán trúng thấp hơn.** 
+ $ Nếu xác suất cho mình biết khả năng xảy ra 1 sự kiện nào đó, thì Độ bất ngờ cho mình biết khả năng 1 sự kiện nào đó không xảy ra, vì nếu nó xảy ra mình sẽ rất bất ngờ như khi trúng xổ số. 
+ ? **Độ bất ngờ** đơn giản cho mình hiểu  **mình sẽ bất ngờ hơn khi chọn trúng màu bóng nào.** Vì công thức xác suất thể hiện khả năng 1 sự kiện có thể xảy ra. (e.g bốc bóng xanh), **ta có thể tính Độ bất ngờ bằng việc chia** `1 / xác suất xảy ra sự kiến đó` 
trong đó `P(E)` đại diện cho xác suất `p` của sự kiện `E` (E for Event) 
$$
Suprise(E) = \frac{1}{p(E)}
$$
 Vì xác suất `P(E)` có thể bằng 0, nên $Suprise(E) \in [1, \infty]$ ($\frac{1}{0} \approx \infty$). Tuy nhiên trong toán học ta không thể chia hết được cho không, nên mình sẽ thay không bằng 1 số cực bé (0.000001) tiến gần đến không, nói cách khác ta lấy 1 chia cho âm vô tận, và nếu 1 chia cho 1 số cực bé ta kết quả sẽ là 1 số cực lớn $\frac{1}{-\infty} = \infty$ (tính tay hoặc bấm máy tính để xác nhận)
 
 
+ ? Sẽ ra sao nếu sử dụng log cho $Suprise(E)$, mình sẽ có 1 cách khác để tính độ bất ngờ ?
![[Pasted image 20250607083538.png]]
Khi ta không quan tâm đến giá trị của hàm `1/P(E)` mà chỉ quan tâm đến vấn đề giá trị `b < a` ta cũng có thể dùng `-log(p(E))` để đánh giá độ bất ngờ. *note: Log(1) trở về 0*  

Note: để hiểu phần Information Theory trong slide, xem [Shannon Entropy](https://youtu.be/0GCGaw0QOhA?si=FFLaDfJHUN9djPwL)

### Bảo toàn độ lớn của các giá trị
+ ? 1 cách khác để tính toán các số quá lớn, ta có thể dùng log để đưa các giá trị về cùng 1 thước đo rồi tính. (Note: để hiểu vì sao cần tìm hiểu rõ hơn về log)
![[Pasted image 20250607084104.png]]
+ @ `sqrt` - tìm hiểu ý nghĩa của hàm căn bậc hai trong bài **Object Detection** ad gửi (hiểu squrt có thể dùg như thế nào, để làm gì) -> tóm tắt: tính khoảng cách di chuyển nhiều hay ít của đối tượng nhỏ và lớn bằng cách trung hòa khoảng cách sử dụng Căn bậc 2. 

### Ví dụ Thực Tế tính phần trăm
**Vấn đề 1: giá trị âm**
>Trong thực tế sẽ có người bị nợ và tài khoản bị âm: -10 thì sẽ tính phần trăm như thế nào -> dùng $e^x$ để tính, trong đó $x$ là số tiền -10 trong tài khoản.  
![[Pasted image 20250607085316.png]]

**Vấn đề 2: Giá trị quá lớn dẫn tới tràn số**
note: 
+ mối tương quan âm -> 1 giá trị tăng, giá trị kia giảm.
+ mối tương quan dương -> cả 2 đều tăng.
+ mối tương quan 0 -> cả 2 không đổi.  

+ ? Tuy nhiên, sử dụng mũ e dẫn đến giá trị rất lớn dẫn đến Overflow. 
![[Pasted image 20250607085103.png]]

### Cấu Trúc 1 Hàm trong Python
![[Pasted image 20250607085742.png]]

### Dấu trong Python (để so sánh các giá trị)
![[Pasted image 20250607085848.png]]

### Branching (Phân Nhánh) in Python
+ ? Q: Làm sao để người mới code có thể Tự Viết 1 hàm như ReLU. 
+ $ A: Thay vì viết code luôn, mình mường tượng ra workflow của code trước sử dụng các block. Đặt câu hỏi, thử nghiệm xem các giá trị đi vào đâu, ra ở đâu, với kết quả này thì mình hi vọng đạt được kết quả gì.![[Pasted image 20250607090154.png]]
Rồi sau đấy mới triển khai code: 
![[Pasted image 20250607090329.png]]


### Phương pháp thay thế cho If Else
+ ? Bằng việc nhân tích vô hướng, mình có thể áp dụng (ánh xạ) các giá trị với các công thức tương ứng. **ví dụ:** `v_0 = [1, 0, 0]` có 1 ở vị trí 0 nên sẽ nhân với `b^2` ở vị trí 0 trong list `u`. ![[Pasted image 20250607090649.png]]

**Python Operation Summary**
![[Pasted image 20250607091206.png]]
