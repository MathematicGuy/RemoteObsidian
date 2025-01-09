# CNN Introduction
+ @ Tóm tắt cơ bản: MLP giúp phân loại nếu số features đầu vào ko quá nhiều. Đối vs dữ liệu ảnh có hàng triệu features, đầu tiên ta dùng **CNN để trích xuất hàng trăm features quan trọng nhất từ hàng triệu features** đó. Rồi mới **đưa vào MLP để phân loại hình ảnh**.    

Trong xử lý ảnh, mỗi ảnh có hàng ngàn pixels, mỗi pixles đc xem như 1 feature. Nếu ảnh có kích thước 1000x1000 thì sẽ có 1.000.000 features. Trong MLP có feed-forward NN vs mỗi layers, mỗi pixel trog 1 layer lại kết nối full-connected vs 1.000.000 pixels ở lớp tr'c. tức sẽ có $10^{6} \times 10^{6} = 10^{12}$  tham số mỗi layer. 
+ ? Bởi vì có quá nhiều tham số, mô hình sẽ dễ bị overfitted (học quá kĩ 1 lg dữ liệu đc cho) và cần lượng lớn data cho training và prediction.

+ $ CNN giúp model giải quyết hiệu quả việc xử lý dữ liệu ảnh bằng cách trích xuất những đặc điểm quan trọng nhất của hình ảnh và dùng nó để phân loại. Có 2 đặc tính của image hình thành nên cách hđ của CNN: 
![[Pasted image 20241208142005.png]]
+ **feature localization:** mỗi pixel hoặc feature có liên quan vs các pixel quanh nó
+ **feature independence of location:** mỗi features đều mang gtrị độc lập. 
-> **CNN xử lý vấn đề có quá nhiều tham số** vs **Shared parameters** (feature independence of location) của **Locally connected network** (feature loclization), đc gọi là Convolution Net.

cụm pixels: n by n pixles block 
+ $ **Locally Connected Layer:**  In the first hidden layer of a CNN, each node (or neuron) connects only to a small portion of the input image, rather than the entire image. This small portion is often referred to as the **receptive field** (*region of the image*). By limiting connections to these local regions, the model significantly reduces the number of parameters compared to a fully connected layer, making it more efficient

+ $ **Shared parameters:** In images, certain key features (e.g., edges, corners, or patterns) often appear repeatedly across different regions or feature maps. To efficiently capture these features, we use the same set of parameters (weights) across the entire image.
+ ? For example, in the inner curve of the digit "7," this pattern might appear in multiple locations across different feature maps. By sharing parameters, the CNN can detect these features regardless of their position, ensuring efficient and consistent feature extraction across the input.

Key Note: 
+ **Kernel:** a N by N grid slide though the images from left to right in order to extract a specific features (like a filter).
	In deeper layers of CNN, more complex kernels are incorporated to detect shapes, objects and complex structures which is done by leverage the previously generated feature maps and their detected simple features to build more complex ones. ![[Pasted image 20241208143921.png]]
	
+ **Convolutional + ReLU:** Convolution applied kernel across the image to create feature maps (i.e. each map contain a specific features) identifying patterns like edges or textures. then applies ReLU a non-linear transformation, setting all negative values to zero, which helps retain meaningful features while ignoring irrelevant parts.
	(Covolution layers identify image's features (each are unique) & ReLU highlight image's meaningful features)![[Pasted image 20241208142940.png]]
	
+ **Pooling:** Pooling reduces the size of feature maps by **selecting the most important value** (e.g., max or average) **from regions of the image**, preserving key features while minimizing computational complexity.
	+ **Max:** take the largest value out of 4 values ​​inside 2x2 grid
	+ **Average:** take the average value of 4 values inside ​​of 2x2 grid
	![[Pasted image 20241208143453.png]]
	
+ Fully Connected Layers (Classifier): Similiar to Feed-Forward network except rather than raw input pixels these are now high-level abstracted featrues from our input.  
	![[Pasted image 20241208150732.png]]
+ **Summary:** CONV and POOL help skim image's features into high-level features, Fully Connected Layers then using those high-level features to classifies images.
	
	+ CNNs clasified images by systematically extracting features maps using convolutional layers (Convs) and reducing these maps to their most meaningful features using poolings layers (Pools). Through this process, the model begins learning basic patterns like edges and gradually identifies more complex shapes (i.e. pixels that hold more information)  
		
	+ These features are then processed and aggregated (i.e. flattening, tổng hợp) through Fully Connected layers to classify what the image represents.
	(*This is similar to how human eyes might scan skimming throught the image, identifying key features that make the image unique*) ![[Pasted image 20241208150732.png]]
	
**CNN Structures** 
	![[Pasted image 20241208163921.png]]
	![[Pasted image 20241208164033.png]]

Unmentions Topic (note later):
![[Pasted image 20241208150944.png]]



