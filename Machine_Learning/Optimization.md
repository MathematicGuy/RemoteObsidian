

> Choosing the best option from a set of option
![[Pasted image 20230921140833.png]]

 ## Hill Climbing Algorithm
![[Pasted image 20230921143057.png]]
> *Find the Highest Hill among its neighbors. If not, Stop. return current Hill as Highest.*
![[Pasted image 20230921143157.png]]
#### Method
![[Pasted image 20230921145048.png]]
**Problem: cannot distinct the real Highest Hill. 
Benefit-> Able to find a pretty good solution. But not 100% accurate everytime.**
Technique that increase the Change to find the global max/min
## Simulated Annealing
![[Pasted image 20230922073722.png]]

![[Pasted image 20230922074234.png]]
> Take a random neighbor, if it better set it as current



## Traveling Salesman

**Turn this**
![[Pasted image 20230922074923.png]]
**To This**
![[Pasted image 20230922074938.png]]
	Adjusting variable direction for better result


## Linear Programming
![[Pasted image 20230922075111.png]]

![[Pasted image 20230922075334.png]]
**Simpified in Function**
![[Pasted image 20230922075518.png]]
can also reverse the constraint 
![[Pasted image 20230922075547.png]]
+ **Constraints:** hạn chế
## Constraint Satisfaction
+ constraint example : A,B,C can't happened at the same time
![[Pasted image 20230922080228.png]]
So on and so on we have this Graph
![[Pasted image 20230922080259.png]]
**When B connected to D meanning that, whatever the value B take on cannot be the value D take on.**

![[Pasted image 20230922080449.png]]

Fomulation of a constraint sasatisfaction problem.
![[Pasted image 20230922080612.png]]

mostly deal with hard constraints 
![[Pasted image 20230922080702.png]]

> Thể hiện 1 vào kết quả có thể đc ưu tiên tr'c các kqua khác.
![[Pasted image 20230922080720.png]]

>**Constrain that just have 1 varible**
![[Pasted image 20230922080838.png]]

> Variable A connect to Variable B make a binary constraint.
![[Pasted image 20230922080906.png]]
![[Pasted image 20230922080927.png]]


![[Pasted image 20230922081003.png]]
+ So for **each of the variables inside of our constraint satisfaction problem, if all of the values satisfy the unary constraints for that particular variable, we can say that the entire problem is node consistency.** 

**A, B are Unary constraints so the condition of A do not affect B, and so on.**
![[Pasted image 20230922081411.png]]
> **Result of reinforce node consistency**
![[Pasted image 20230922081404.png]]


![[Pasted image 20230922081553.png]]
> **Out of all possible choice x have. y also have some possible choice in that.** But they cannot be the same.
![[Pasted image 20231006063107.png]]
 -> A = Tue | B = Wed (Removing Wed from A)

From Arc Consistency we have this code:
![[Pasted image 20231006063655.png]]

![[Pasted image 20231006063728.png]]
	Only considering Binary constraint between 2 nodes;
**Goal of this: To find the right constraint for each node in the big problem**

**CPSs as Search Problems**
![[Pasted image 20231006064118.png]]

## Backtracking Search

