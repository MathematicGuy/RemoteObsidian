Link: https://youtu.be/5NgNicANyqM?t=146&si=dt6DHZ_-ndohAFA3
**AGENT** 
	entity that perceives its environment and acts upon that environment
	+ can be a car, person, Obj in general

**STATE**
	a configuration of the agent and its environment.
	+ Each sequence of action will be needed for each state

**INITIAL STATE**
	Starting state, then start to reason about its.

**ACTIONS**
	choices that can be made in a state
	+ We can defind action **as a Function f(x)**. 
		**action(s) returns the set of actions that can be executed in state s**

##### How can a State and Action related to one another ? In order to do that we introduct AI to the
**TRANSITION MODEL**
	a description of what state results from 
	performing any applicable action in any state.
	 + A Function but be able to take command 
		 **result(s, a) returns the state resulting from performing action *a* in state *s***
![[Pasted image 20230822062150.png]]


**STATE SPACE**
	the set of all states reachable from the initial state by any sequence of actions.

> **In PUZZLE**
![[Pasted image 20230822062442.png]]

> **In Graph: a state leading to another state**
![[Pasted image 20230822062514.png]]

## **GOAL TEST**
a way to determine whether a given state is a goal state.
+ Like the driving destination of a taxi, ending goal in a maze.

**PATH COST**
	numerical cost associated with a given path
>**It can be particular**
	![[Pasted image 20230822062801.png]]
	
>**Or constance cost**
	![[Pasted image 20230822062836.png]]

**SOLUTION**
	a sequence of actions that leads from the initial state to a goal state.
what we want to is the **OPTIMAL SOLUTION**
	a soution that has the lowest path cost among all solutions.

**NODE**
	a Data Structure that keeps track of 
	+ a state
	+ a parent (node that generated this node) 
		let us know what sequence we use to get to this state. 
	+ an action (action applied to parent to get node)
	+ a path cost (from initial state to node)

**APPROACH**
*Frontier - currently active node*
	+ Start with a frontier (biên giới) that contain the initial state
	+ Repeat:
		If the frontier is empty, then no solution
		Remove a node from the frontier.
		If node contains goal state, return the solution.
		Expand node, add resulting nodes to the frontier.

*Problem - Infinity Loop with Frontier is* [A, C, D]
	![[Pasted image 20230822064402.png]]
So we need a **approach that save all the Node that came before.**

**REVISED APPROACH**
*Frontier - currently active node
Explored set - Save Used Node*
	- Start with a frontier that contains the initial state.
	- Start with an empty explored set.
	- Repeat: 
		+ If the frontier is empty, then no solution.
		+ Remove a node from the frontier.
		+ If node contains goal state, return the solution.
		+ Add the node to the explored set.
		+  Expand node, add resulting nodes to the frontier if they
		aren't already in the frontier or the explored set.

**STACK**
	LIFO data type.
	+ Treat the Frontier like a Stack
	![[Pasted image 20230822065118.png]]

This is what we called 
**DEPTH-FIRST SEARCH** (Search to the bottom then backup and repeat)
	Go Deeper and Deeper in to the Tree. And if we hit a Dead end then we go back up and repeat. 
Cons: Might not recognize the Optimal solution while it avaiable
	![[Pasted image 20230822070003.png]]


**BREADTH-FIRST SEARCH (BFS)** (Scan Linearly)
	Search algorithm that always expands the shallowest node in the frontier.
	using **QUEUE - FIFO**: the earlier you in the earlier you out.

## A* Search
![[Pasted image 20230908072551.png]]

#### Have 2 navigator.
+ **g(n):** distance of blocks to goal.
+ **h(n):** Store value of each way. For example, 2 way of choice, calc total distance from goals of both way, if any of them have a **shorter estimate row** then choose that way.
![[Pasted image 20230908072459.png]]
#### Notice 
![[Pasted image 20230908072428.png]]




## TIC TAC TOES  
note: tạo 1 giá trị chung cho các hành động kế tiếp của cả 2 đối tượng.
![[Pasted image 20230908074211.png]]
+ Terminal(s) states is like Out of Move in chess, a Stale mate, Moving 3 times in a row, a side is winning. States that check will the game End.
+ Ultility: like score

## How can I maximize the score given the opponents action.
***Tính toán các giá trị của các bước đi để tối ưu điều kiện thắng***
VD: Trong cờ vua đi nước 3 điểm sẽ dẫn tới nước 20 điểm, hoặc đi nước 15 điểm sẽ dẫn tới nước 2 điểm. Tính toán cả những bước sau đó để đưa ra lối đi tốt nhất.
	( Áp dụng đc Bài toán tìm đường Max/Min))
+ The **Player** want to **Maximize the score**  -> take min as input (opponent action)
+ The **Opponent** want to **Minimize the score** -> take max as output
	**When the Player goes, it want to get the maximum values from all the minimum value its Opponents choosed.**
(Player - Green Prior Move Value; Opponent - Red Prior Move Value)
**Green choose the Max from Red. And Red Choose the Max from Green**
![[Pasted image 20230908080456.png]]


If the Opponent know the Minimum move value, And have found the that Value. It'll stop scanning for another values. (Found what It's want -> Stop)  
![[Pasted image 20230908081306.png]] 
This is called Alpha-Beta Prunning. (Don't Search everything, Optimize)

Path Finding Algorithm can apply to every Algorithm that want to find the Best value,  (Like in Graph, Tree Structure problems type)
	Ex: Find the Best choice in the Chess game.
![[Pasted image 20230908082802.png]]


## Depth-Limited Minimax
> Only move n moves ahead. 
![[Pasted image 20230908082840.png]]

[[Algorithm Problem]]