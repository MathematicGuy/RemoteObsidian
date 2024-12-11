Overfitt -> overly obey child that do exactly what he was taught.
![[Pasted image 20241211202819.png]]

**Modern AI Father** (3 người tự tạo ra 3 nhánh :))
![[Pasted image 20241211203027.png]]
orther great people: FeiFei Li (Image Net)

**Model Generalization**
**Trick 1:** "Learn hard" - randomly add noise to trainning data. Since real life have a lot of noise.
![[Pasted image 20241211204054.png]]
Ex1: Add a **random black box** 
![[Pasted image 20241211204143.png]]
```python
# scale(min, max) diện tích của h.chữ nhật đen từ min tới max
```
+ ! Tuy nhiên mọi dữ liệu phải dùng pytorch và đc pytorch hỗ trợ.
**Result**
![[Pasted image 20241211211855.png]]


**Trick 2:** Batch Normalization
batch normalization: giúp luồng dữ liệu mượt hơn để dễ nhìn và train hơn. 
`Ngoài ra, nếu có bias = 1 thì kết quả luon ra bằng 0???`
![[Pasted image 20241211205239.png]]
note: check moving average

![[Pasted image 20241211205753.png]]

i nghĩa là số lượng trừu tượng. e.g. 1,2,3,...,i với i là số lớn nhất.
![[Pasted image 20241211210649.png]]
+ ? Tại sao Batch Norm cải thiện kết quả test trong khi dữ liệu test ko liên quan tới kết quả train. 
+ $ 
![[Pasted image 20241211211815.png]]



**Trick 3:** Dropout (*n%* of nodes) - only apply when training
>*~50%* nodes randomly selected in the *i-th* layer are set to zeros (kind of noise adding). Kinda like pooling, but for neural network.
![[Pasted image 20241211211920.png]]

![[Pasted image 20241211212733.png]]
![[Pasted image 20241211212823.png]]
+ ? dropout is a old technique. 
Apply for CIFAR-10 dataset, we got 
![[Pasted image 20241211213311.png]]

**Trick 4: Kernel regularization** (L1 or L2 regularization basically)
![[Pasted image 20241211213414.png]]
**result**: *train_acc* drop a bit but *val_acc* increase a little
![[Pasted image 20241211213702.png]]

**Trick 5: Data augmentation**
>Cover more real life scenario using Data augmentation. Ex: objects at diff light conditions, object at diff angles, etc...
![[Pasted image 20241211213750.png]]
![[Pasted image 20241211214858.png]]

**others improvement method**: add more hidden layers, and skip connection

**Trick 6: Reduce learning rate**
>learning rate decay, learning rate scheduling.
![[Pasted image 20241211215336.png]]

**Quizz**
![[Pasted image 20241211220454.png]]

![[Pasted image 20241211221404.png]]
Basically, LeCun say neural network with 7 inputs and 3 output nodes is just like CNN with 1x1x6 inputs and 3 kernels (both using softmax)
![[Pasted image 20241211221739.png]]


format(sâu, cao, rộng) - 128 là chiều sâu.
![[Pasted image 20241211222702.png]]
VGG Model Construction
![[Pasted image 20241211222741.png]]

**Discussions**
+ Augmentation có thể giảm train_acc vì độ khó tăng lên. 
+ Lý do acc tặng đột ngột ở giữa -> learning giảm (maybe)
	![[Pasted image 20241211223300.png]]

**Trick 7: Increase model capacity (and use more data augmentation)**
![[Pasted image 20241211223338.png]]

**Trick 8: Using skip-connection**
![[Pasted image 20241211223417.png]]
![[Pasted image 20241211223431.png]]
Lên 100? -> coi kiến trúc trên như 1 block, nối nhiều block lại tăng độ chính xác. Miễn là số block ko quá nhiều, vì input dataset quá đơn giản cho việc model trừu tượng hóa dữ liệu.

**Summary**
![[Pasted image 20241211223841.png]]

