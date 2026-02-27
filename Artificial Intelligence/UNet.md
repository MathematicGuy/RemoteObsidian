## Introduct to UNet
**Types of Image Segmentation (Phân khúc)**
![[Pasted image 20260226165530.png]]


**Model for Image Segmentation**
Cons of Pooling -> make detail pixels generalize with its neighbour. bc you're taking the average of every 4 pixels -> make the image smaller and less detail.

**Encoder - Decoder Model Proposal**
![[Pasted image 20260226170218.png]]
(Encoder: VGG) - (Decoder: Inverse VGG), result:
![[Pasted image 20260226170522.png]]
+ ! Khi đưa về Feature map nhỏ (1x1) thì *khó khôi phục lại được. Nhưng Vẫn có khả năng.* -> Nếu encode ảnh từ 512 -> 1 rồi mới khôi phục sẽ rất khó. 
+ $ Sẽ làm sao nếu mình các lớp ra, và khôi phục (kp) lại theo lớp. ie. Khôi phục lại trực tiếp tại từng lớp như 512, 256, 128, 64, 32, 16. Chứ ko truyền từ 512 -> 16 rồi mới khôi phục. ![[Pasted image 20260226171000.png]]

Example for the top layers of UNet. *Encoder -(Up Conv 2x2)-> Decoder:*
![[Pasted image 20260226171533.png]]
But we need a method to preserve the Dimensionality of the image when Down/Up Sampling.

**Convolution**
![[Pasted image 20260226171833.png]]

**Transposed Convolution (ngược lại của conv)**
![[Pasted image 20260226171931.png]]
How ? like conv but you mult the "Input/ downsample featuremap" to the whole kernel pixel by pixel (left -> right, top -> bottom). 
e.g. the first calc is $2 * [[1,1], [1,1]]$ with input value as 2 and kernel size of 2 value 1. This mean value 2 will be kommen 2x2 matrix within the 3x3 matrix (ie. 2x2 matrix + padding).
![[Pasted image 20260226172020.png]]

The code is quite simple, `in/out_channel` determine how many channel you have incase you want to up/down_sampling (e.g 512 -> 256), `kernel_size` is the kernel each of the input pixels will be multiply to and bias is just bias.
![[Pasted image 20260226172529.png]]

**Padding in Tranpose Convolution Substract margin (reverse padding, i guess)**
![[Pasted image 20260226172859.png]]
Padding in code:
![[Pasted image 20260226172919.png]]

**Stride in Tranpose Convolution is the reverse of Stride, again**
+ Stride = 1 make 2x2 `input * kernel` *stacked* on top of each other. Because there is no where to move. 
+ Stride = 2 is just `input * kernel`, bc each of the 2x2 matrix are 2 steps away from its previous matrix left pixel (ie. first pixel).
![[Pasted image 20260226173153.png]]

*Just add stride* to the code then you can use it. 
![[Pasted image 20260226173530.png]]

**Padding & Stride (what if u add both ?)**
![[Pasted image 20260226173822.png]]
Fomula explain:
+ MxN represent width and heigh
+ Logic in $H_{out}$ (the height) apply the same for $W_{out}$ (the width).
+ $(M-1)*S$ because we only take account for 1 column (ie. the right column) at a time when adding stride. Remember if S = 3 then only 1 column get added to the feature map. The $+1$ is the remaining column on the left.
+ $-2P$ because we *substract both the left & right padding* 
+ $(K - 1)$ when multiplying 2x2 matrix with 2x2 kernel, we only take a  column (on the right) for the multiplication. If you notice, for a 1x1 matrix to become a 2x2 matrix, we just need to add 1 columns, in other word subtract kernel size K by 1. 

**UNET Model Code demo**
Conv Block is still conv block.
![[Pasted image 20260226175525.png]]
**Encoder Code Block**
![[Pasted image 20260226175638.png]]
**Encoder Visualization**
![[Pasted image 20260226175709.png]]

**Decoder Code Block**
![[Pasted image 20260226175822.png]]
**Decoder Visualization**
![[Pasted image 20260226175842.png]]

**Concatination gộp feature map của Encoder và Decoder** - cứ gộp feature map của 2 mô hình thì dùng Concatination. 

Note: down/up for each UNet layers.
	Downsampling use MaxPooling2D 
	Upsampling use TransposeConvolution2D.
	
Unet work well with limited training data because it just learn segmentation from same image i different scenario (ie. domain). This mean UNet heavily relies on data augmentation and skip connections. 
	
Kernel_size for transpose conv is 2x2.
Kernel size for conv is 3x3.
	
Activation at Unet final layer for binary segmentation is Sigmoid (between 0 and 1), note that ReLu take 0 or 1 not between. 
	
Note: without skip-connections between layers, feature is lost and hard to recover. 

Chiều của Decoder giống Encoder nhưng thêm 1 chiều feature map. e.g. Encoder là 64x64 thì Decoder là `số featuremap ở lớp dưới`x64x64. Vì Chiều đầu vào và ra phải giống nhau.  
+ Featuremap pải có kích thước 64x64 để bằng chiều SkipConnection.
+ Phải có 256 vì đấy là chiều của lớp. 
![[Pasted image 20260226181001.png]]

![[Pasted image 20260226181241.png]]

Phân tích hàm `ConvTranspose2d`
`upscale_factor` - dùng chiều rộng (HxW) để bù cho chiều sâu. HxW tăng thì chiều sâu $C_{out}$ giảm.
![[Pasted image 20260226181604.png# left | 555]]

Khi validate segmentation thì ignore background pixel đi. e.g ignore màu trắng 255.

---

