![[Pasted image 20260117081557.png]]



Conv tham khảo và áp dụng các ý tưởng của Transformer như LayerNorm
Let Deep Dive into each Layer of ConvNeXt
![[Pasted image 20260113212545.png]]


Depthwise don't modify anything like Standard Conv, just extract with Conv
![[Pasted image 20260113212614.png | 444]]


Instead of Adding straight away, ConvNeXt apply the LayerNorm first, then Sum them up later. 
![[Pasted image 20260113212857.png]]

![[Pasted image 20260113230254.png]]
Point-wise - apply 1x1 conv to each features map, not to each image because 1 image can have multiple featuremap with each featuremap represent 1 portion of the image (e.g. car ear in 25x25 pixel within 125x125px cat image) . 
	Point-wise compress information across channels of the feature-map. 

Note: Layer-Norm apply normalization for each feature-map so the normalization distribution doesn't change (std & mean doens't change) -> only need to normalize once. Not like Batch-Norm which normalize a group of samples thus their distribution change after each layer. .

DropOut - Drop by Features 
[DropPath Regularization](https://medium.com/@akp83540/drop-path-regularisation-5dd01d23b2c1) - Drop by Layer
![[Pasted image 20260113223750.png]]


