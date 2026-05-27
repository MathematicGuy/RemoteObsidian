![[Pasted image 20230821220308.png]]
> tài liệu: [Ma trận kề – Wikipedia tiếng Việt](https://vi.wikipedia.org/wiki/Ma_tr%E1%BA%ADn_k%E1%BB%81)

![[Pasted image 20230823103826.png]]
note: để chính xác trong python, cho các số trong dãy bắt đầu từ 0.
a) 
```python
import numpy as np  
  
# Số lượng nút  
n = 6  
  
# Tạo ma trận lân cận với tất cả các giá trị bằng 0  
adj_matrix = np.zeros((n, n))  
  
# Thêm các cạnh  
adj_matrix[0][1] = 
1  
adj_matrix[0][3] = 1  
adj_matrix[0][5] = 1  
adj_matrix[1][2] = 1  
adj_matrix[1][3] = 1  
adj_matrix[2][3] = 1  
adj_matrix[2][4] = 1  
adj_matrix[3][4] = 1  
adj_matrix[3][5] = 1  
adj_matrix[4][5] = 1  
  
# In ma trận lân cận  
print(adj_matrix)
```
![[Pasted image 20230822133710.png]]

b) 
```python
# Số lượng nút  
n = 6  
nodes = n + 1  
  
# Tạo danh sách lân cận với tất cả các danh sách rỗng  
adj_list = [[] for _ in range(nodes)]  
  
# Thêm các cạnh  
adj_list[0].append("null")  
  
adj_list[1].append("null")  
  
adj_list[2].append(1) # Node 0  
adj_list[2].append(4) # Node 0  
  
adj_list[3].append(2)  
adj_list[3].append(6)  
  
adj_list[4].append(3)  
adj_list[4].append(6)  
adj_list[4].append(5)  
  
adj_list[5].append(1)  
  
adj_list[6].append(5)  
adj_list[6].append(2)  
adj_list[6].append(1)  
  
# In danh sách lân cận  
print(adj_list)
```

![[Pasted image 20230822135147.png]]
### Graph
![[Pasted image 20230822135156.png]]

![[Pasted image 20230823104153.png]]
![[Pasted image 20230823103842.png]]

**c) Cài đặt BFS & DFS bằng python**
```python
# BFS algorithm in Python
import collections

# BFS algorithm
def bfs(graph, root):

    visited, queue = set(), collections.deque([root])
    visited.add(root)

    while queue:

        # Dequeue a vertex from queue
        vertex = queue.popleft()
        print(str(vertex) + " ", end="")

        # If not visited, mark it as visited, and
        # enqueue it
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


if __name__ == '__main__':
    # Let 0 to 8 indicate A - B,S - C,G, - D,E,F,H
    graph = {
        0: [1, 8],
        1: [0],
        8: [0, 2, 6],
        2: [8, 3, 4, 5],
        6: [8, 5, 7],
        3: [2],
        4: [2],
        5: [2, 6],
        7: [6],
    }
    print("Following is Breadth First Traversal: ")
    bfs(graph, 0)
```
![[Pasted image 20230822231121.png]]
![[Pasted image 20230823102613.png]]


### DFS
```python
# DFS algorithm
trace = []
def dfs(graph, start, visited=None):
	if visited is None:
		visited = set()
	visited.add(start)

	trace.append(start)
	for next in graph[start] - visited:
		dfs(graph, next, visited)


	return visited


graph = {
	'0': set(['1', '8']),
	'1': set(['0']),
	'8': set(['0', '2', '6']),
	'2': set(['8', '3', '4', '5']),
	'6': set(['8', '5', '7']),
	'3': set(['2']),
	'4': set(['2']),
	'5': set(['2']),
	'6': set(['8','5','7']),
	'7': set(['6']),

}

dfs(graph, '0')
print("Following is Depth First Search: ")
print(trace)

```
![[Pasted image 20230822231121.png]]
![[Pasted image 20230823103227.png]]


![[Pasted image 20230822143528.png]]
### Graph
![[Pasted image 20230823100046.png]]

**Tài liệu**
![[Pasted image 20230823003906.png]]


![[Pasted image 20230823105119.png]]
### BFS
```python
# BFS algorithm in Python  
import collections  

def bfs(graph, root):
	visited, queue = set(), collections.deque([root])
	visited.add(root)

	while queue:

		# Dequeue a vertex from queue
		vertex = queue.popleft()
		print(str(vertex) + " ", end="")

		# If not visited, mark it as visited, and
		# enqueue it
		for neighbour in graph[vertex]:
			if neighbour not in visited:
				visited.add(neighbour)
				queue.append(neighbour)


if __name__ == '__main__':
	# Let 0 to 8 indicate A - B,S - C,G, - D,E,F,H
	graph = {  
		1: [2, 6, 5],  
		2: [1, 6, 4, 3],  
		6: [1, 2, 4, 5],  
		5: [1, 6, 4],  
		4: [5, 6, 2, 3],  
		3: [2, 4],  
	}
	
	print("Following is Breadth First Search: ")
	bfs(graph, 1)
```
![[Pasted image 20230823104553.png]]

![[Pasted image 20230823105109.png]]
### DFS
```python
# DFS algorithm
trace = []

graph = {
  	1: [2, 6, 5],  
	2: [1, 6, 4, 3],  
	6: [1, 2, 4, 5],  
	5: [1, 6, 4],  
	4: [5, 6, 2, 3],  
	3: [2, 4],  
}

def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(set(graph[vertex]) - visited)
    return visited

print("Following is Depth First Traversal:")
print(dfs(graph, 1))

```
![[Pasted image 20230823101606.png]]

### Graph
![[Pasted image 20230823112226.png]]
![[Pasted image 20230823105042.png]]
```python
# Python program for Kruskal's algorithm to find
# Minimum Spanning Tree of a given connected,
# undirected and weighted graph


# Class to represent a graph
class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    # Function to add an edge to graph
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    # A utility function to find set of an element i
    # (truly uses path compression technique)
    def find(self, parent, i):
        if parent[i] != i:

            # Reassignment of node's parent
            # to root node as
            # path compression requires
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    # A function that does union of two sets of x and y
    # (uses union by rank)
    def union(self, parent, rank, x, y):

        # Attach smaller rank tree under root of
        # high rank tree (Union by Rank)
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x

        # If ranks are same, then make one as root
        # and increment its rank by one
        else:
            parent[y] = x
            rank[x] += 1

    # The main function to construct MST
    # using Kruskal's algorithm
    def KruskalMST(self):

        # This will store the resultant MST
        result = []

        # An index variable, used for sorted edges
        i = 0

        # An index variable, used for result[]
        e = 0

        # Sort all the edges in
        # non-decreasing order of their
        # weight
        self.graph = sorted(self.graph,
                            key=lambda item: item[2])

        parent = []
        rank = []

        # Create V subsets with single elements
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        # Number of edges to be taken is less than to V-1
        while e < self.V - 1:

            # Pick the smallest edge and increment
            # the index for next iteration
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            # If including this edge doesn't
            # cause cycle, then include it in result
            # and increment the index of result
            # for next edge
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
            # Else discard the edge

        minimumCost = 0
        print("Edges in the constructed MST")
        for u, v, weight in result:
            minimumCost += weight
            print("%d -- %d == %d" % (u, v, weight))
        print("Minimum Spanning Tree", minimumCost)


# Driver code
if __name__ == '__main__':
    g = Graph(6)
    g.addEdge(0, 1, 16)
    g.addEdge(0, 5, 21)
    g.addEdge(0, 4, 19)
    g.addEdge(1, 5, 11)
    g.addEdge(1, 3, 6)
    g.addEdge(1, 2, 5)
    g.addEdge(2, 3, 10)
    g.addEdge(3, 5, 14)
    g.addEdge(3, 4, 18)
    g.addEdge(4, 5, 33)


    # Function call
    g.KruskalMST()
```
![[Pasted image 20230823161609.png]]



![[Pasted image 20230823104838.png]]
### Graph 
![[Pasted image 20230823104002.png]]

![[Pasted image 20230823103953.png]]
![[Pasted image 20230823103916.png]]

![[Pasted image 20230823104018.png]]
![[Pasted image 20230823104030.png]]



![[Pasted image 20230823104054.png]]

![[Pasted image 20230823104042.png]]
**b) Dãy sắp xếp trong đồ thị có thể liên quan đến việc sắp xếp các đỉnh hoặc cạnh của đồ thị theo một tiêu chí nào đó.**

