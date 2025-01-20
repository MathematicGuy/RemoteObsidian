Section 2.2 of the excerpt (Trích đoạn) from "Medical image segmentation using deep learning: A survey" discusses various network function blocks that can be incorporated into convolutional neural networks (CNNs) to improve medical image segmentation.

**Dense connection:** Every layer receives input from all preceding layers, leading to richer image features. However, dense connection can decrease robustness and increase parameters

**Inception:** Uses parallel multi-scale convolution kernels and feature fusion to extract more image features without increasing network depth.
However, the inception structure is complex.

**Depth separability:** Improves generalisation and reduces memory usage, particularly for 3D data. Depthwise separable convolution breaks down vanilla convolution into depthwise separable convolution and pointwise convolution, decreasing computational cost. This can reduce accuracy, so methods like deep supervision are needed to improve accuracy.

**Attention mechanism:** Attention blocks selectively modify input or weight input variables based on their importance. This allows the network to focus on important image areas.
+ **Local spatial attention:** Computes feature importance for each pixel to extract key image information.
+ **Channel attention:** Recalibrates features by selectively emphasizing useful features and suppressing less useful ones based on learned global information.
+ **Non-local attention:** Uses a self-attention mechanism and a global aggregation block to extract information from the entire image during both up-sampling and down-sampling.


