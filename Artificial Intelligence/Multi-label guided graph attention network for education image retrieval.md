note:
Retrieval doesn't mean Searching
Multi-label
+ ? Abstract: add relationship between label/class in the Image. 
	This research aim to find the relationship between label then concat label (dependency) and the image features for Fast amd more efficient Image Retrieval. 
+ $ Improvement: Multi-label using Graph Attention Netwrok for Image Retrieval)

---
#### Distinguishing between Classification & Ranking
Classification: choose 1 between the n.
Ranking: choose top n -> can ranking object in same/diff class (prioritize which is best)


#### Graph Convolution Network (GCN)
(develop from CNN)

**Features Aggregation** -> chọn lọc features
**Linear Transformation** 



#### Graph Attention Networks(GAT)
> transformer thì phi đồ thị hơn.
+ Attention work like usual, focus on those important.


#### Image Retrieval
subfield of Search

Multi-label Images solve
+ complex toplogy problem (e.g. relationship between human + phone) 
+ Highly corelated labels (e.g. ceiling fan ceiling -> ceiling)

Graph -> build dependency between labels where each node represents a label feature.
+ $ GCN learn interdependent between labels (sự phụ thuộc lẫn nhau).

#### Proposed Method
2 Part
+ Natural Language Word (label) -> GAT (Graph attention network) learn relationship between them.
Generated Classifiers (Increase D dimension)  -> for Matrix multiplication (between label & Image)
	i.e. label vector $\times$ image vector 


Global Max Pooling -> the whole image features 
Local Max Pooling -> 1 window feature


Classified inorder to increase retrieving speed. Case where student use phone and not use phone are classified into diff graph space. -> Less time retrieving.


Note: 
+ ? Increase action Accuracy base on Image Context. 
