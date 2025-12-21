## How Convolutional Network work from Scratch
Trick that **CNN** use for machine to **understand image**. Understand a image mean knowing **which Features make that image unique** and **able to Classify them.**
Note: [Deeper understanding about CNN Kernel - But what does a trained Convolution Neural Network actually learn ? VISUALIZED!](https://www.youtube.com/watch?v=kebSR2Ph7zg)


Feature match pieces of the images
![[Pasted image 20251218140319.png | 344]]
-> Call **Filtering: the math behind the pattern matching** 
1. Line up the feature and the image patch.
2. Multiply each image pixel by the corresponding feature pixel.
3. Add them up.
4. Divide by the total number of pixels in the feature.

**Apply Filtering**
If match then equal 1 - this mean the matched percentage is 100%. 
![[Pasted image 20251218140523.png]]
How about this pattern, this said 55% matched. 
![[Pasted image 20251218140604.png]]

+ ? **Convolution basically just mean move a Filter across the image to find Features that it might Match** 
	Its answer the question: **is this pattern existed within this image, if so how can I emphasize/activate it.**
![[Pasted image 20251218140730.png]]

Another example of apply diff Filter, we could extract or at least activate a similar pattern within the filted image.  
![[Pasted image 20251218141032.png]]
Simplified version of the image above.
![[Pasted image 20251218141431.png# left | 333]]

**Pooling: Shrinking the image stack to smaller image.**
1. Pick a window size (usually 2 or 3)
2. Pick a stride (usually 2)
3. Walk your window across your filtered images.
4. From each window, take the maximum value.

**Max Pooling:** picked out the max value from the filtered image/feature map. ie. *Out of all Features, only retrieve the most noticeble features.* 
![[Pasted image 20251218141711.png]]

**Normalization**: keep the math from breaking by tweaking each of the values just a bit. **Change everything negative to zero using ReLU.**
![[Pasted image 20251218141939.png]]

**Layers get stacked** 
The output of one becomes the input of the next. 
![[Pasted image 20251218142010.png]]

**Deep stacking**
Layers can be repeated several (or many) times. 
![[Pasted image 20251218142117.png]]
 
**Fully connected layer - How Deep Neural Networks Work**
+ ? [[What do Neural Network Learn]]
Every value gets a vote. Allow the Neural Network to learn Which 
![[Pasted image 20251218144124.png# left  | 544]]
This is how a simple NN classified a Class/Option.
![[Pasted image 20251218144414.png | 333]]

Next level of detail, if we just **depend on total value** we **can't really clasified base on their position** (both horizontal but 1 top & 1 bottom). 
![[Pasted image 20251218144542.png]]

Now we gonna **build Neuron, first we take all the input then add 'em up.** 
Give each NN Nodes a receptive fields to extract a specific feature. 
Postivei in white, negative in black, Zero -> zero line/value.
![[Pasted image 20251218145123.png | 434]]

**Activation Function:** map input value to another value Domain while still preserve its meaning. By using sigmoid we basically squashing all value larger then 1 back to 1 and smallar then -1 to -1.  
![[Pasted image 20251218145208.png | 444]]
**Squash the result**
![[Pasted image 20251218145354.png | 233]]
 
![[Pasted image 20251218145918.png]]

Note: Why Hidden layer use Sigmoid but not ReLU. 
+ $ With **ReLU**, we not only **reduce Gradient Vanishing problem** but also **Flip the value backward so the MLP can learn every pattern in reverse.** ![[Pasted image 20251218150203.png]]
	The 2nd layer upper nodes take the **sum of the black and white** node and getting **value of Zero (Grey)**.

+ ? Intuition Example of how MLP classified a image is horizontal.
![[Pasted image 20251218151105.png]]

#### How Optimization for ML Works
**Problem:** Tea drinking temperature to personal enjoyment. Right temperature -> High Enjoyment.  ![[Pasted image 20251218151417.png | 333]]To use these information as a Optimization problem, we flip all values downward, bc we're minimizing value in a value domain.
![[Pasted image 20251218151305.png | 333]]
+ ? Explain Gradient Descent using user feedback terminology. Have a lot of people drinking tea -> feedback -> update value to lower/increase the temperature.  ![[Pasted image 20251218151852.png | 233]]
A more advance method is to use curvative, by **calc the curvature in both size** you compare which side is steeper to go. ![[Pasted image 20251218152007.png# left | 133]]
**Global and Local Minima**
+ ? What if the value Domain have multiple Minima (ie. best temperature for tea enjoyment) 
![[Pasted image 20251218152150.png | 333]]
![[Pasted image 20251218152239.png | 333]]

+ ! What about have more feedback -> more Accurate but waste Too much resource. But using Gradient Descent is like guessing/assume this or that value is optimal. 
+ ? Is there a Middle ground to find the optimal value and avoid local minimal ? 
![[Pasted image 20251218152502.png]]

+ $ **Instead of trying to answer right, we try to be (answer) LESS Wrong** -> need define  **specific how wrong is my answer** (ie. in **What range of value make my guess RIGHT, $d_i$ for deviation -> Duh, that basically the Loss Function**) ![[Pasted image 20251218153221.png | 444]]

![[Pasted image 20251218153324.png | 433]]

+ ? **The Cost function** allow us to **estimate how wrong is my Guess**. As the example below show the total Cost of ours guesses. (Thats a simple example of numerical optimization)  ![[Pasted image 20251218153440.png]]

![[Pasted image 20251218153839.png | 444]]

![[Pasted image 20251218153905.png | 233]]

**However, there another Analycal shortcut to find what the best guess is.** 
![[Pasted image 20251218155318.png]]

**Backpropagation: calc change in Error given the change in Weight** (ie. calc derivative for a Weight)
+ $ This **doesn't tell us where the Local minimum** is but it does tell us **Which way is better to go.**
![[Pasted image 20251218155538.png]]
**Simplified and Visualize**
![[Pasted image 20251218155821.png]]
This Chain answer the Question, for the total error to decrease what need to change in weight z, in weight y and so on to weight a -> Help increase value to classified a specific image.
![[Pasted image 20251218155839.png]]
	Apply this information to the classified the horizontal edge image, its would mean changing all weights so that horizontal edge get emphasize when the horizontal image pass through the network.   

**This can also be stacked**
![[Pasted image 20251218160527.png]]

**Putting it all together:** A set of pixels becomes a set of votes. 
![[Pasted image 20251218160604.png]]

+ ? Remaining topic to explain -> Too much to Test, so there actually a fomula to choose. ![[Pasted image 20251218160746.png | 344]]
  Note: visualize and explain what Abstract feature look like. 
+ ! **Limitations:** ConvNets only capture local "spatial" patterns in data. If the data can't be made to look like an image, ConvNets are less useful. 



**Rule of thumb:**
If your data is just as useful after swapping any of your columns with each other, then you can't use Convolutional Neural Networks.
+ $ **ConvNets** are good at finding pattern and classifing image. 


# Introduce CNN from Scratch
![[1_CnNorCR4Zdq7pVchdsRGyw.png]]
+ **Color Channels**
	- ? **Grayscale** (`[black, white]`):
	    - Needs only **1 channel**, represented by **1 variable** with values in range `[0, 255]`.
		
	- ? **RGB** (`[Red, Green, Blue]`):
	    - Needs **3 channels**, represented by **3 separate variables**, each ranging `[0, 255]`.

+ ! **Clarification:** **Number of color channels ≠ CNN dimension**.
	+ Both **RGB (3-channel) and grayscale (1-channel) images use 2D CNN** because **CNN dimension refers to spatial dimensions** (height, width) only.
		
	+ A **3D CNN refers to processing multiple frames simultaneously,** capturing both spatial and temporal `([time, height, width])` information, not to the number of color channels.
	
**Example:**
- Single image (RGB): $[height \times width \times 3]$ → 2D CNN
- Multiple frames (video): $[frames \times height \times width \times channels]$ → 3D CNN

+ $ Total Parameters in a Network or Model is total number of weights + total number of bias.  
+ ? In CNN, beside weight and bias. We also perform "element-wise beteen kernel and image + a bias" in each color channel of the feature map. This mean, each feature map have 1 or 3 color channel, each feature map perform kernel and pixel multiplication.   
	Total parameters are calculated as the **sum of weights and biases**.
	+ **Formula (clearly explained):**  
$$[(k_w \times k_h) \times C_{in} + b] \times C_{out}$$
**Where:**
- $[k_w, k_h]$: width and height of kernel/filter.
- $[C_{in}]$: number of input channels.
- $[C_{out}]$: number of output channels (**number of filters**).
- $+ \space b$: represents one bias term per filter.

+ ? **Kernel and Filter** are the same. But really **Kernel is a sub-set of Filter,** for example in 2D Convolution for RGB image, each channel apply a kernel so there're **3 kernel (color) channel, but 1 filter**. Filter describe whole multiplication inside the Convolution layer.  ![[Pasted image 20250317074107.png]]
+ ? Example: For a convolutional layer with 32 filters and input having 3 channels (e.g., RGB):
	Total filters = 16
	Total kernels (channel-wise kernels) = 16 filters × 3 kernels per filter = 48 channel kernels.
```python
model = tf.keras.models.Sequential([
    # Note the input shape is the desired size of the image 300x300 with 3 bytes color

    #? This is the first convolution
    #? ((3 x 3) x 3 + 1) x 16 = (kernel_shape x total_channels + bias) x total_filter = 448
    #? Output shape: (298, 298, 16) because there is no padding meaning leaving 1 pixel/layer off from each size of width and height.  
    tf.keras.layers.Conv2D(16, (3,3), activation='relu', input_shape=(300, 300, 3)), 
    # Divided feature map by 2 
    tf.keras.layers.MaxPooling2D(2, 2), #? (149, 149, 16) 
```

**28x28x1 -> image 28 pixels in height and 28 pixels in width.** 
1) Go into a Convolution layer with padding = 1. and 3x3 kernel. Each kernel perform a 3x3 element wise multiplication to the 3x3 pixels grid inside the image, where **kernel is the Weight** + a bias -> $y = X.W + b$ with $X$ as the image's pixels, $W$ as kernel/weight, $b$ as bias. 
	note: weight or trọng số is a sub-set of parameters. (parameter is the general idea of function $y$ input, and weight is a input), in other word, we can call weight as a parameter.
	
	+ $ Basically Conv act as a Linear layer to extract features from the image. ![[Pasted image 20250317074107.png]]
	+ ? After this, we apply the ReLU function to the features map to activate (i.e. keep) positive value and remove negative value which represent un-important pixel. This is reasonable since pixels value range are within 0 to 255.
	
2) Feature extract by the Kernel turned into a feature map 32x28x28 Conv_1 -> 32 of 28x28 Feature Map. 
	Because **center kernel is the result of the multiplication sum** (i.e. element-wise) for a 3 by 3 grid, thus the **outlayer will not be consider in the next layer as you see below:** 
	+ $ This called **Receptive Feild** ![[1_k97NVvlMkRXau-uItlq5Gw.png]]
3) After Conv, Max Pooling layer act as a kernel slide though all feature maps and pick out the max value output a 2x2 grid. Therefor, reduce feature maps size by half.
4) This whole process repeat, then get Flatteed in to a (n, 1) shape vector
5) The whole vector then go into a Fully Connected Layer (i.e. MLP) for classification.

![[Pasted image 20250317072825.png]]

**2 Conv**
![[Pasted image 20250317084958.png]]

**Max Pooling**
![[Pasted image 20250317085020.png]]

### Back Propagation 
+ ? Explain why rotate 180 degree. 
![[Pasted image 20250317085400.png]]

![[Pasted image 20250317085413.png]]

![[Pasted image 20250317085430.png]]

+ ? Focus on how to update the Kernel. (Update a kernel value base on it previous kernel value) ![[Pasted image 20250317085514.png]]

![[Pasted image 20250317085655.png]]

![[Pasted image 20250317085713.png]]

Follow the same logic for all other weights/kernel value
![[Pasted image 20250317085814.png]]
Partial Derivative. Only the partial is value, everything else is constant
![[Pasted image 20250317085952.png]]
Apply the same logic for $w_1$ to $w_4$ 
![[Pasted image 20250317090025.png]]

![[Pasted image 20250317090053.png]]

Note that the first variable $a$ represent the first kernel multiplication.
![[Pasted image 20250317090115.png]]
+ ? For the ease of calculation, let rewrite these derivatives in matrix.
Repeat the matrix multiplication for each $z$ column. 
![[Pasted image 20250317090258.png]]
And calculate matrix mult to get the derivative of the first kernel. 
![[Pasted image 20250317090359.png]]

Finally update the weights (i.e. kernel value)
![[Pasted image 20250317090625.png]]
CNN Back Propagation in depth: https://youtu.be/z9hJzduHToc?si=cIVG_XCyMQbk6esM
Coding CNN from scratch: https://youtu.be/Lakz2MoHy6o?si=YgPaHUrBECJPjlrF


### 1 by 1 Convolution: Intuition and Explanation (Pointwise Convolution)
note: [1 by 1 Convolution Key Point Explanation](https://medium.com/analytics-vidhya/talented-mr-1x1-comprehensive-look-at-1x1-convolution-in-deep-learning-f6b355825578) 


- $ **Purpose:**  
    A **1x1 convolution** (often called a _pointwise convolution_) is a convolutional operation where the kernel size is **1x1**, but with a depth equal to the input feature map's channels. It primarily serves as a **feature-channel-wise transformation**, enabling the model to adjust the number of channels and combine information across channels.
    
- ? **Why 1x1 convolution?**
    - Reduces or expands the number of channels (dimensionality reduction or expansion).
    - Mixes features across channels without affecting spatial dimensions.
    - Efficiently increases network depth and non-linearity.
	
- **How it works:** Consider an input feature map of size:
    - Spatial dimensions: $H \times W$
    - Number of channels (depth): $C_{in}$
    
	We apply a set of 1x1 kernels. Each kernel will have dimensions:
    - Size: $1 \times 1 \times C_{in}$
    - Total kernels: $C_{out}$
    
    The resulting feature map after convolution will have dimensions:
    - Spatial dimensions remain: $H \times W$
    - Channels become: $C_{out}$


### Mathematical Representation:
Formally, a **1x1 convolution** at position $(x, y)$ is expressed as:
$$\text{Output}(x,y,k) = \sigma \left( \sum_{c=1}^{C_{in}} W_{k,c} \cdot \text{Input}(x,y,c) + b_k \right)$$

where:

- Output $\text{Output}(x,y,k)$ is the output at spatial position $(x,y)$ for the $k^{th}$ output channel.
- Input $\text{Input}(x,y,c)$ is the input at position $(x,y)$ for the $c^{th}$ input channel.
- $W_{k,c}$ is the kernel weight connecting input channel $c$ to output channel $k$.  
    _(Note: It's essentially a single number since kernel size = 1x1)_
- $b_k$ is the bias term for the output channel kk.
- $\sigma$ is an activation function (e.g., ReLU).

### Intuitive Interpretation:

- A **1x1 convolution** is equivalent to applying a small neural network (fully-connected layer) at each pixel independently, transforming the channel dimension without changing the spatial dimension.
- It does **not** perform spatial feature extraction but rather focuses on feature fusion and channel transformation.

### Summary (Concise):

- Kernel size: $1 \times 1 \times C_{in}$
- Channels: $C_{in}$ → $C_{out}$
- Spatial dimensions remain unchanged ($H\times W$).

Thus, a **1x1 convolution** reshapes feature depth and combines channel-wise information efficiently.
![[Pasted image 20250317091757.png]]
Diff name: 
+ **Feature Map Pooling Layer:** make sense because it act as a pooling layer for the feature map. 
+ **Cross Channel Parametric Pooling:** pooling layer across channels.
+ Linear Weighting or "Projection with Non-Linearity"

![[Pasted image 20250317092037.png]]

![[Pasted image 20250317092106.png]]

**Right:** bottle neck architecture which apply 1x1 Conv.
![[Pasted image 20250317092133.png]]

### 3D CNN and (2D + 1D) CNN
### 1. Giải thích các thuật ngữ

**a. 2D-CNN (2D Convolutional Neural Network):**

- Mạng nơ-ron tích chập 2 chiều, thường được sử dụng trong xử lý ảnh tĩnh. Các phép tích chập được thực hiện trên không gian hai chiều (chiều cao và chiều rộng của ảnh) để trích xuất đặc trưng không gian.​

**b. 3D-CNN (3D Convolutional Neural Network):**

- Mạng nơ-ron tích chập 3 chiều, mở rộng phép tích chập sang chiều thứ ba (thời gian) để xử lý dữ liệu video. Điều này cho phép mô hình hóa cả thông tin không gian và thời gian trong video.​

**c. Spatial Information:**

- Thông tin không gian, liên quan đến cấu trúc và đặc trưng của từng khung hình trong video, như hình dạng, màu sắc và kết cấu.​

**d. Temporal Information:**

- Thông tin thời gian, liên quan đến sự thay đổi và chuyển động giữa các khung hình trong video, giúp hiểu được hành động và diễn biến theo thời gian.​

**e. Optical Flow:**

- Biểu diễn chuyển động của các điểm ảnh giữa hai khung hình liên tiếp trong video, thường được sử dụng để trích xuất thông tin chuyển động.​

**f. RNN (Recurrent Neural Network), LSTM (Long Short-Term Memory), GRU (Gated Recurrent Unit):**

- Các loại mạng nơ-ron hồi tiếp, đặc biệt hữu ích trong việc xử lý dữ liệu tuần tự như video, giúp mô hình hóa thông tin thời gian.​

**g. Computation Cost:**

- Chi phí tính toán, đề cập đến tài nguyên cần thiết (như thời gian và bộ nhớ) để huấn luyện và triển khai mô hình.​

**h. Temporal Shift Module (TSM):**
+ Một module được đề xuất để cải thiện khả năng mô hình hóa thông tin thời gian trong các mạng 2D-CNN mà không tăng đáng kể chi phí tính toán.​[Viblo](https://viblo.asia/p/tsm-2d-cnn-mang-hieu-suat-cua-3d-cnn-trong-bai-toan-action-recognition-vyDZO6MdKwj)

