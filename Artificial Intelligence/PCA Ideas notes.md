Principal Component Analysis - allow to distribute each Cel seperatly
![[Pasted image 20240417103920.png]]
High collerate group together

**X axis > Y axis (show more different)** 
> If the distance between Red and Yellow in X-axis are equal to Red and Sky Blue in y axis. Then Red and Yellow are more different from each other.
![[Pasted image 20240417104010.png]]


Why use PCA for Image Compression?

Principal Component Analysis (PCA) is a valuable tool for image compression due to its ability to identify and exploit redundancy within image data:

Dimensionality Reduction: Images often contain correlated pixels; neighboring pixels tend to have similar values. PCA pinpoints the directions of the greatest variance within the image data (the principal components). These components effectively capture the most significant information. By projecting the image onto a smaller set of these principal components, we can achieve a compact representation.

Information Preservation: PCA prioritizes preserving the most crucial visual information. The top principal components explain the major variations within an image. By retaining only a subset of these, we can maintain a high level of visual fidelity while reducing the overall data needed for representation.

Lossy Compression: PCA supports lossy compression, where a degree of quality degradation is acceptable in exchange for a substantial decrease in file size. This trade-off is often beneficial for web images or storage-constrained scenarios.  
  
Computational Efficiency: PCA involves well-established linear algebra operations. Compared to some more complex compression techniques, it offers a relatively computationally efficient approach.

In summary, PCA excels in identifying the underlying structure in an image while allowing modification of the degree of compression. This allows for efficient compression by focusing on the essential features and a balance between file size reduction and image quality preservation.