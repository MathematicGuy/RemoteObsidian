**Edge Detection**: apply a certain filter to extract a certain image's area
![[Pasted image 20241215143555.png]]

**Strided Convolution**
Summarize Convolution (i.e. feature map) size
![[Pasted image 20241215143836.png]]
note: convolution sometime called as cross-correlation or convolution operator. 

## Convolutions Over Volume
**Conv and Kernel format:** Width $\times$ Height $\times$ Number of Channel (Depth)  
Ex: 6 blocks width x 6 blocks height x 6 colors channel ![[Pasted image 20241215144253.png]]
+ ? CNN's **parameters** are the weights and biases that the model learns during training. Each layer has its own set of parameters, which are determined based on its structure. 

Let’s break down how to calculate parameters for **convolutional**, **pooling**, and **fully connected** layers. **Note that kernel depth is depend on it image number of channel.**  
+ $ The Convolution layers, **each kernel will go through it corresponding color channels** (e.g. 1st kernel layer for red, 2nd layers for green and 3rd layers for blue) -> This mean for 1 kernel total parameters is 3x3x3 + 1 bias  = 28 parameters. 
+ $ For multiple kernel/filters, we simple multiply them. We have 2 kernels so the 1st CONV layer total parameters is 28 * 2  = 56 parameters.   
**Total Parameters Fomula:**
$\text{Kernel's Parameter} =  F_{w}*F_{h}*C_{in} + 1$ where $C_{in}$ is the number of inputs channels.
$\text{Total Parameter} = (F_{w}*F_{h}*C_{in} + 1) * N_{f}$ where $N_{f}$ is the number of kernel 


For multiple kernel, we just multipli it. 84 * 2 = 168 parameters.
Thus, 1st Conv layers have 168 parameters. 

## 2 Layers Convolutional Network Structure
![[Pasted image 20241215144901.png]]
+ (28, 28, 6) bc 32 - 5 + 1 = 28. Don't mistake kernel size with feature map depth / channel size.
+ `#parameters` is parameters of `filters = parameter_per_filter * total_filter`  
	Parameter per filter calc as $F_{w}*F_{h}*C_{in} + 1$ where $C_{in}$ is the number of inputs channels: $5.5.3 + 1 = 76$ * 6 because we have 6 filters, so 456 parameters in total.   
	
+ CNN use Average Pooling hence (5,5,6) 
![[Pasted image 20241215152929.png]]

