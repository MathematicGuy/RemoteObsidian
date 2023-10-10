
# Array
Array is like a container that can store all of the data types
![[Pasted image 20230919150918.png]]
Index start from 0

# ArrayList 
### list size automatic ajust. 
Ex: Moving an item, decrease. Adding an item, increase


# LinkedList (like a Chain - DONE)
- If nothing connect to the next. The next fall apart

![[Pasted image 20230925112436.png]]
	Instead, each element points to the next. It is a data structure consisting of a collection of nodes which together represent a sequence.


### Type of Linked List
1. Single Linked List
	Contain Current Node 
	and Node pointed to the Next Node.

> Node(data):
> 	Create new Node with Value = data.
```python
# Create 1 Node. Of a singly linked list. 
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
```

2. Double Linked List
	Have Add function. To add 1 more Node.
	Declare Tail and Head 

**Add Node ot the Tail of the List**
 *Add():*
 	If *List is Empty*:
 		 then make the **first Node become Tail Node**
 	Else:
 		- *Change the pointer* - 
 		**Get the New Node -> Node(data)** 
 		Change the **Current Node Tail next Node to New Node**
 		**New Node.previous = its previous Node** (Because Tail Node have pointed to)
 		**NewNode next Node to None** (bc its a tail)
 		*Change Node State* 
	 		 **change List Last Node is New Node.**
	 		 
```python
# Python3 program to illustrate
# creation and traversal of
# Doubly Linked List

# structure of Node
class Node:
	def __init__(self, data):
		self.previous = None
		self.data = data
		self.next = None


class DoublyLinkedList:
	def __init__(self):
		self.head = None
		self.start_node = None
		self.last_node = None

	# function to add elements to doubly linked list
	def append(self, data):
		# is doubly linked list is empty then last_node will be none so in if condition head will be created
		if self.last_node is None:
			self.head = Node(data)
			self.last_node = self.head
		# adding node to the tail of doubly linked list
		else:
			new_node = Node(data)
			self.last_node.next = new_node
			new_node.previous = self.last_node
			new_node.next = None
			self.last_node = new_node

	# function to printing and traversing the content of doubly linked list from left to right and right to left
	def display(self, Type):
		if Type == 'Left_To_Right':
			current = self.head
			while current is not None:
				print(current.data, end=' ')
				current = current.next
			print()
		else:
			current = self.last_node
			while current is not None:
				print(current.data, end=' ')
				current = current.previous
			print()

# Driver code
if __name__ == '__main__':
	L = DoublyLinkedList()
	L.append(1)
	L.append(2)
	L.append(3)
	L.append(4)
	L.display('Left_To_Right')
	L.display('Right_To_Left')

```

Check If empty: Current.next = None -> Empty

### Delete Node
*(Adjust Current previous Node POINTED to current NEXT NODE. since no node pointed to Curent. It deleted)*
*remove(key)*
>Check if any Node == Key_Node:
	 Check if the Node is the Head:
> 		then Change List head to the List Head's Next Node
> 	If found the Key:
> 		Change its key's previous Node to the Key Node
> 		
```python
def remove(self, key):
	"""
		Removes Node containing data that matches the key
		Returns the node or None if key doesn't exist
		Takes O(n) time
	"""
	current = self.head
	previous = None
	found = False

	# while current isn't None and found is False
	while current and not found:
		if current.data == key and current is self.head:
			found = True
			# make the next node the Head. Thus make the Current Head deleted
			self.head = current.next_node
		elif current.data == key:
			# Set the Previous node -> Next_node
			found = True
			previous.next_node = current.next_node
		else:
			# replace
			previous = current
			current = current.next_node
	return current
```


### 3. Circular Linked List (List's tail pointed to head)
A circular linked list is that in which the last node contains the pointer to the first node of the list.
![[Pasted image 20230925115328.png]]

### 4. Double Circular Linked List (list tail + head pointed eachother)
![[Pasted image 20230925115425.png]]


### 5. Header Linked List
**A header linked list is a special type of linked list that contains a header node at the beginning of the list.**
![[Pasted image 20230925115452.png]]




# HashMap


# Stack (LIFO)
Implement using Linked List
**The Last thing u Put In is the first thing that u put out.**

### [Infix, Post-Fix, Pre-Fix](https://prepinsta.com/data-structures/stack-infix-and-prefix-conversion/)

**1. First Start scanning the expression from left to right**

**2. If the scanned character is an operand, output it, i.e. print it**

**3. Else**
    **- If the precedence of the scanned operator is higher than the precedence of the operator in the stack(or stack is empty or has'(‘), then push operator in the stack**
    **- Else, Pop all the operators, that have greater or equal precedence than the scanned operator. Once you pop them push this scanned operator. (If we see a parenthesis while popping then stop and push scanned operator in the stack)**

**4. If the scanned character is an ‘(‘, push it to the stack.**

**5. If the scanned character is an ‘)’, pop the stack and output it until a ‘(‘ is encountered, 
and discard both the parenthesis.**

**6. Now, we should repeat the steps 2 – 6 until the whole infix i.e. whole characters are scanned.**

**7. Print output**

**8. Do the pop and output (print) until stack is not empty**


![[Pasted image 20230925120806.png]]


# Queue (FIFO)

![[Pasted image 20230926111024.png]]


# Graph

![[Pasted image 20230927085518.png]]

### Minimum Spanning Tree (Prism's algorithm)

if == size. Can pick any of those
Pick a Node. Choose the Edge with the Smallest value.



![[Pasted image 20230927093716.png]]