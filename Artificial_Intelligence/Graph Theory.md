**Degree** - total nodes connected to it.
![[Pasted image 20240809102444.png]]

**Path** - sequence of vertices connected by edges.
**Path Length** - number of nodes in path
![[Pasted image 20240809102517.png]]

**Cycle** - path that **starts and ends at the same vertex**
> All Cycle are path but not all path are cycle
![[Pasted image 20240809102558.png]]


**Connectivity** - 2 evertices are connected if a path exist between them.
	A graph is connected when all vertices are connected.
+ ? The Image below are not Graph. Just **Connected Component**: a subset of vertices of the (can be) graph that is connected. 
![[Pasted image 20240809102719.png]]
![[Pasted image 20240809102853.png]]

## Types of Graphs
Undirected and Directed Graph
+ ? Simply **Graph with No Direction and Graph with Direction**.![[graph.png]]

**There are 2 kinds of Directed Graph**
+ ? One with Cycle and One with No Cycle
![[Pasted image 20240809103108.png]]

**Weighted Graph**
>Graph with Length between each node for example. Each node's weight are the sum of path length connected to them. 
![[Pasted image 20240809103306.png]]

**Trees**
![[Pasted image 20240809104111.png]]
+ Acyclic mean no cycle.

 
**Adjacency Matrix** 
+ ? Graph a Node Zeros Matrix with each point are a graph as rows and cols full of zeros. Assign 1 for connected nodes.    
![[Pasted image 20240809104309.png]]

**Edge Set**
![[Pasted image 20240809104734.png]]

**Adjacency List**
+ ? Each node show its adjacency Node. Great for Sparse Graphs (Đồ thị thưa thớt) which is most Graph in the real world.
+ $ Social Network for example: each vertex have few edges (only few thousands) 
![[Pasted image 20240809104809.png]]

Therefor we'll use Adjacency Grapth for representation going forward:
![[Pasted image 20240809110106.png]]

