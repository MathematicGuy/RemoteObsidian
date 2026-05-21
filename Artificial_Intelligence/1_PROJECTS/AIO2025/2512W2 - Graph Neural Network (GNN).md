More Reading:
+ [Gentle and Intuitive Introduction to GNN](https://distill.pub/2021/gnn-intro/)
+ [Understand Graph Machine Learning in the Era of Large Language Model](https://isamu-website.medium.com/understanding-graph-machine-learning-in-the-era-of-large-language-models-llms-dce2fd3f3af4) 
## What is Graph Data Around Us
All features in a node -> embedding vector
**Isomorphism** - 2 graph is Isometric to each other although they look different. 
	e.g. Two graphs are isomorphic if they are structurally equivalent, meaning there is a one-to-one mapping between their nodes that preserves all edge connections.
![[Pasted image 20260511155458.png]]

## Understand Graph Neural Network
#### Tasks on Graph Data
![[Pasted image 20260511130927.png]]

**Edge-level task** - predict connection between note/entity or the opposite ie. trimmed link to simplified the graph.  
![[Pasted image 20260511120426.png]]

#### Fundamental Idea of GNNs
**Representation Learning:** Learning a neural networks suitable represenation of graph data - or how to combine Graph with Neural Network.

Other way to create a Graph is through Spare Graph Representation using Adjacent List -> Fast but hard to implement. 
![[Pasted image 20260511133400.png ]]
-> for simplicity we just use adjacent matric in this note. 

#### How do Graph Neural Network Work ? 
Building a GNN start from 3 steps:
1. Sampled Neightborhood
2. Aggregation
3. Update
to Embed the input Graph with meaningful relation with every other node that close to it. 

**Overview:** Each node gathers features from its neighbors then enrich representation of its neighbour then use them to enrich the current node itself. Repeat for every Node for each Epoch.
	**Sampled Neightborhood** - sample the intermediate/nearest neightbour node (e.g. A to B, C, D).
		Input: A
		Output: B, C, D
	**Aggregation** - aggregate neighbours node (e.g. Neighbour node of B is A and C) pass them through a Neural Network (grey box) to produce a new "richer" representation of node B. 
		Input: neightbour node of A
		Output: richer representation of the Neighbour node of A (ie. B,C,D) 
	**Update** - use those richer representation neighbour to update A. 
		Input: richer presentation of B, C, D.
		**Output: richer representation of A that "knows" about its immediate surroundings.** 
![[Pasted image 20260511134232.png]]
By doing this, each Node have the information of their surrounding nodes.
![[Pasted image 20260511141656.png]]
Help Transformer the connections strength between nodes
![[Pasted image 20260511141826.png]]

Overview of how GNN work - [arxiv paper](https://arxiv.org/pdf/1812.08434.pdf)
![[Pasted image 20260511141410.png]]
Finding Neighbour method  $\neq$ CNN Kernels.



**Sample Layers Level:**
+ ? So why not sample all Layer for each Node -> Noise, Node Similarity/Relationship and Computation Efficiency, the farther the Node the lesser the similarity to the current node.   ![[Pasted image 20260511140851.png | 555]]
+ ! The result is Oversmoothing -> Meaning *Computational Graph (used for update each node) shared the same information making them redundancy bc 2 or more graph share the same Embedding information*. Example for 1 Layer: ![[Pasted image 20260511142227.png]]
+ @ Explaination, GNN generalize around similar group, if 2 different group getting compute at with eachother, their Computation Graph to find a middle groud to accomodate them all. 
+ $ GNNs are designed to aggregate information from neighbors (message passing).
	While this works for similar nodes (homophily), stacking too many layers forces the network to aggregate information from far-away nodes and different clusters. The network loses its discriminative power, averaging node features across the entire graph into a single, homogeneous "middle ground" representation.
+ !  As Layer leve growth larger Computational Graph with the same neightbour increased more in number. Example for 2 Layers: ![[Pasted image 20260511142258.png]]

+ $ Like Cluster in K-Means, we want to classified in Group. ![[Pasted image 20260511142402.png]]

**How to Detect Oversmoothing ?**
![[Pasted image 20260511142735.png]]
![[Pasted image 20260511143135.png]]


**How to Counter Oversmoothing ?** - a elegant solution is to add a MLP after the GNN to apply non-linearity which extract better representation of the node. **Why this work ?**
1. GNN focus on gathering structure information (each node understand the representation of their neighbour nodes. )
2. *MLP focuses on transforming those features into discriminative representations.*
![[Pasted image 20260511143147.png]]
Performance actually increase quite a lot for vanilla GNN. 
![[Pasted image 20260511144550.png]]

#### Message Passing as a Math Function
![[Pasted image 20260511145949.png | 777]]
The step are the same but with math where
	$u$ mean Update (node), the target node currently being updated. 
	$v$ is the neighbour node providing information
	$k$ is the iteration/layer number
	$N(u)$ is the set of node connected to $u$.
	$h_{u}^k$ is Node $u$ at step $k$. If we update the firsts node at step 1 then it would be $u=1$ and $k=1$.  
		$h^k_{u}$ also represent Feature vector (hidden state) of node $u$ at layer (or step $k$)
	$h_{1}^{k+1}$ is Node 1 at step $k+1$ (e.g. you could understand as the second udpate bc k + 1 = 2)
	.
	$UPDATE^{(k)}(\text{input1}, \text{input2})$ is the update function at step $k$, it take in 2 input, the 1st one is the Node idnex $u$ at step $k+1$ by the aggregate 
		$UPDATE$  function could be a Mean, Max, NN or RNN function 
	.
	$\text{AGGREGATE}^{(k)}$ mean at step $k$ apply aggregate function (ie. Mean/Max/Norm Sum/NN) to ALL the sampling neighbours/vertex $v$ of node $h$ $(\{h_{V}^{k}\},\forall \space v \in N(u))$. 
		Note: $V$ in $h_{v}^k$ mean vertex $v$ of node $k$, basically neighbour node of node $k$. 
	$\mathcal{N(i)}$ - total number of variable $i$. If there 3 $i$, the this = to 3.  
![[Pasted image 20260511144619.png]]
+ ? for $UPDATE$ make sure to use a Differentiable/Updatable function to update gradient.
![[Pasted image 20260511151114.png]]

Note: $h_{i}'=[h_{i}||h_{\mathcal{N_{(i)}}}]$ - mean **CONCATINATE** $h_{i}$ to $h_{\mathcal{N(i)}}$

### Application: Cora Citation Classification - [Data&Code](https://drive.google.com/drive/folders/16Q2TxCgBGIexLIODJC0Zbb6an9OahQUZ)
Classified relationship between Paper (node) by citation (node classification)
![[Pasted image 20260511153803.png | 666]]
MLP -> 0.59 accuracy.
**GNN with Dropout ->** 0.815 accuracy.
![[Pasted image 20260511154116.png]]
![[Pasted image 20260511154008.png]]

**What NEXT ?** Currently Edge Information are just Binary (is this CONNECTED or NOT). In the next lesson we'll discover more about Edge Feature in GNN.
-> How we use Embedding as Aggregation.  ![[Pasted image 20260511154304.png]]
**GNN Survey**
![[Pasted image 20260511155055.png]]
GNN Question example format: 
![[Pasted image 20260511161114.png]]
GNN Model Code (Just Import the GCNConv module instead of CNN Module - similar structure to CNN)
![[Pasted image 20260511163203.png]]

## What this mean for Continual Learning ?
Continual Graph Learning (CGL) aims to balance forward knowledge transfer with knowledge retention, where prior data are inaccessible.
Update dependency ??? 

**Standard Challanges:**
	Scaling and Memory cost - *computationally expensive.* Require Graph-sampling and mini-batching to train -> require careful memory management.
	*Long-Range dependencies* - standard GNNs often struggle to learn from nodes that are far apart in the graph, limiting reasoning capability. 
	 
Other Problems:
	**Non-Euclidean Data** - Complex neighborhood structures are hard to replay.
	**Topology Evolution** - Graph structure changes over time, not just features.
	**Catastrophic Forgetting** - New graph tasks overwrite old graph knowledge.
	**Storage & Privacy** - Storing large, connected, private graphs is difficult.

# Advanced Graph Neural Network (GCN, Graph Relational, Attention & Level-Prediction)
[Quiz part 2](https://docs.google.com/forms/d/e/1FAIpQLSe0JYSHmpLGE-CiVeOiONSc3GDK9MKkz_IGtHjJpPpAykSe3g/viewform)

## Edge Feature in GNN



## GNN Review: Edge Weight in GNN
+ ? How a NN can process a graph directly. 
+ ! Diminishing or exploding problem in a NN


### Edge Weight in GNN



### From CNN to GNN



## Relational GNN


## Multidimensional Edge Feature


## Attention in GNN
### Attention in Graph Neural Network


## Graph-level prediction: Example and Code