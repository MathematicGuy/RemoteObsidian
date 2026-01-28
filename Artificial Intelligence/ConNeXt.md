## ConNeXt: A ConvNet for the 2020s - Paper Explain
**From ConvNets to ConvNeXts**
In ConvNeXt paper, ViT wa s mis-interpret by not training on augmentations -> This show with enough data, even a old model can achieve good accuracy.
![[Pasted image 20260121123234.png | 444]]
+ ? ConNeXt author argue that the model should be comparing to the 2021 SoTA EfficientNet not 2015.
+ $ In fact, EfficienNet does achieve better result. Look like EfficientNetV2 is the ConvNeXt of the 2020s.  ![[Pasted image 20260121123039.png | 433]]


**1x1 Convolution** (Downsampling)
+ ! Problems: Use more Filter (each filter have 3 kernel) to Extract more Feature Map -> Channels increase -> Computation Increase.
![[Pasted image 20260121151227.png | 544]]

+ $ Need a solution to Maintain number of features while saving computation resource. Where 1x1 Conv come in.
![[Pasted image 20260121144124.png | 344]]
+ ? Why perform Convolution across Channels (ie. Multiple Feature Map) ?
1) *Pointwise Convolution:* apply a 1x1 kernel but across all channel help *aggregate features* across multiple feature maps.
2) *Cross Channel Parametric Pooling:* unlike pooling, 1x1 conv have learnable params $W_{c}$ so its can learns to agreegate importantn features like eyes in channels 10 and nose in channels 20 to create face features at the output while ignore noisy channels by adjust/reducing channels weight.
$$Output(x, y) = \sigma\left( \sum^{C_{in}}_{c=1} W_{c} \times Input(x, y, c) + b\right)$$
+ @ In short, 1x1 conv work similar to a 1 layer Fully Connected Neural Network.


**Bottleneck Architecture**
![[Pasted image 20260121150850.png]]


**ConvNeXt inspiration: Swin Transformers**
1x1 Convolution: maintain number of features while saving computation resource.
