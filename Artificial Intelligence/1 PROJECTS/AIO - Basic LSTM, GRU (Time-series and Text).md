+ ? Làm sao để giảm parameter mà ko giảm bộ nhớ


RNN: can be used to predict bitcoin dựa trên dữ liệu timeseries.
>Được phát triển giống như cách não ghi nhớ thông tin -> tập trung vào shorterm memory.
![[Pasted image 20241220200750.png]]

**Recurrent (hồi quy)** means **Feedback loops**
![[Pasted image 20241220201325.png]]
**Also mean Sharing Weights**. 3 neurons nhưng dùng chung 3 cái weights. 
![[Pasted image 20241220201448.png]]
RNN - R + NN: Recurrent + Neural Network
![[Pasted image 20241220201553.png]]

**Traditional NN vs RNN**
![[Pasted image 20241220201729.png]]
![[Pasted image 20241220201740.png]]
>This features allow NN to remember and predict the future better base on past experiment.

Instead of taking weight from inputs of the 1st layers, RNN take weight directly from the activation function.
![[Pasted image 20241220201922.png]]
By this method, weight and bias are Shared across every inputs. No matter how many times we unroll a recurrent NN, we never increase number of weights and bias to train.
![[Pasted image 20241220202004.png]]
A more intuitive way to look at RNN: previous layers not responding to making prediction but passing experience.
![[Pasted image 20241220202127.png]]

**Different types of RNNs** (the same method as above but Many)
![[Pasted image 20241220202348.png]]

![[Pasted image 20241220202816.png]]

predict word to word
![[Pasted image 20241220202825.png]]

### Why RNN is not use Often ?
Vì là tham số truyền tới tham số nên sẽ gây ra vấn đề Gradient Exploding.
![[Pasted image 20241220203033.png]]
Or Vanishing Gradient
![[Pasted image 20241220203149.png]]

### How to avoid Exploding-Vanishing Gradient 
By skipping connection: instead of go through one by one, each layers go directly to the last layers or n layer after it.

![[Pasted image 20241220203912.png]]

+ @ kind of Xây dựng dựa trên sơ đồ mạch điện 
![[Pasted image 20241220204125.png]]
purpose of multiplication block
![[Pasted image 20241220204522.png]]
**Forget Gate (white block): value range from 0 to 1**. use to determine how much information pass to the next layer.
![[Pasted image 20241220204635.png]]

Information pass through layer by layer (red line passing through)
![[Pasted image 20241220204809.png]]
+ đường trên cùng là long memory vì nó cho phép mình trực tiếp chuyển thông tin qua lớp sau. Còn short term chỉ truyền thông tin trong RNN. 
+ Input Gate, Output Gate, 
+ These block below represent short-term memory 
	![[Pasted image 20241220205853.png]]
+ **Sigmoid** used to **determind how much information in %** being pass to the next layer.
+ 3rd layer: Tanh activation func -> determine information proportion being added (with the 2rd layer)  
	![[Pasted image 20241220204957.png]]
+ 2 layers (after layer 1) represent additional information added
+ Block 2 and 3 directly help determine new long-term memory
	![[Pasted image 20241220205727.png]]
+ Combining long-term & short-term memory by Multiplying.  
	![[Pasted image 20241220205751.png]]

![[Pasted image 20241220210803.png]]

###  Long-Short Term Memory: Summarize
ht_1: shorterm




---


### Multi-step vs Iterative Forecasting

**Iterative:** dùng 1 tập tham số ở từng bước tr'c đó để dự đoán bước tiếp theo rồi cập nhật tập tham số mỗi lần dự đoán bằng dự đoán ở bước tiếp theo.
+ ? DỰ đoán từng cái 1
![[Pasted image 20241220215742.png]]
**Multi-step:** sử dụng 1 tập tham số để dự đoán nhiều tham số cùng 1 lúc.
+ ? Dự đoán nhiều cái 1 lúc
![[Pasted image 20241220215653.png]]

![[Pasted image 20241220220039.png]]


**Rolling window** (Cross-Validation)
Với 1 tập dự liệu lớn, mình quét từng đoạn qua dataset gọi là subdataset, dùng trong đoạn subdataset đó 1 phần chọn để train, 1 phần đc chọn để test. Theo thời gian (time series), mình sử dụng rolling window để đưa ra dự đoán thực tế dựa theo n tập dự liệu tr'c nó.  
![[Pasted image 20241220220053.png]]

transformer: giúp giải quyết vấn đề phải tính tuần tự trong **Stacked RNN** bằng cách tính song song.
![[Pasted image 20241220223438.png]]

---

### Step-by-Step LSTM

**Forget gate layer**
![[Pasted image 20250214135349.png]]
$f_{t} = 1$  represent "preserve all past information" and $f_{t} = 0$ represent "forget all past information"
Forget gate allow new/updated data preserve it meaning when changes occured through time. (e.g. conversation between human through time)


![[Pasted image 20250214140244.png]]

---

1) Image from Classroom Camera 
-> Pose Estimation
-> Person Detection

Skeleton Data
Bounding Box
-> Corrected Skeleton Data

Pre-processing Skeleton Data

Feature Extraction

Behaviour Classification
DNN Model -> Trained Model -> Bahaviour Result

---


+ ? **Câu hỏi bảo vệ dự án:**
So sánh phương pháp (giống và khác giữa các phương pháp)
Dataset (so sánh hiệu quả giữa các dataset khác nhau)

Ý nghĩa của các chỉ số Validation

Tham số ? 
Công thức nào đưa vào phải giải thích dc, so sánh vs công thức (mà cùng giải quyết đc 1 vấn đề)

Đồ án tốt nghiệp làm theo hình thức nhóm. 

**Đồ án của mình tốt hơn như thế nào ? khi mình mới làm đồ án**

Thầy Đông - xử lý ngôn ngữ tự nhiên 

