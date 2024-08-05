## Introduct to optimization
Find the Optimized Point (Like the Elbow Point for K-Means)
![[Pasted image 20240719180004.png]]

**Local and Global Minimum**
**Local:** current minimum of the slope (all 4 point in the image)
**Global Minimum:** the minimum slope of all slope (the 3rd point in the image)
![[Pasted image 20240724153121.png]]


## Optimization of squared loss - The one powerline problem 
![[Pasted image 20240719180818.png]]

![[Pasted image 20240719181039.png]]
So the distance to a is: x - a 
and b is b - x
![[Pasted image 20240719181414.png]] 

We have to find x to minimize the cost function: (x-a)^2 + (x+ b)^2 -> So we have to moving x from left to right to that till we find the smallest value -> Let use Derivative (since it help us to find the smallest value between 2 point)  
 ![[Pasted image 20240724122938.png]]

![[Pasted image 20240724123327.png]]
> Applied Derivative, we found out yes put x in the middle it the right choice.

## Optimization of squared loss: The three powerline problem
![[Pasted image 20240724123930.png]]
$$x = \frac{a + b + c}{3}$$
**Visualize the my answer: smallest point**
![[Pasted image 20240724124232.png]]
And if it too far to the right
![[Pasted image 20240724124158.png]]
or Left
![[Pasted image 20240724124222.png]]

![[Pasted image 20240724124305.png]]
> Help to find the Minimal value (position) between the original/current point to n other point. (n as  point number). Ex: Optimal position to 2 other positions.

# Optimization of log-loss
## Optimization of log-loss Part 1

![[Pasted image 20240724130751.png]]
> What maximize the chace of achieving this: head 7, tail 3
![[Pasted image 20240724131032.png]]

There are 2 ways to approach this: 
+ ? Both use Product Rule then appiled the Chain Rule
**Traditional method**
![[Pasted image 20240724134416.png]]
**Logarithm**
![[Pasted image 20240724134403.png]]
Useful function in machine learning
![[Pasted image 20240724134515.png]]
+ ? The reason that we actually take **negative g of p instead of g of p** is that **logarithm of p is actually a negative number when p is in between zero and one.**
+ $ We want **negative g of p to be a positive number**, and instead of maximizing it, like we did here, we **minimize negative g of p.**


**Why the Logarithm ?** because it optimize traditional derivative method. (Log compare to the traditional method is like compare GPU to a CPU). It allow to calc the derivative of all function at once. ![[Pasted image 20240724142312.png]]

**More Reasons to use Logarithm**
![[Pasted image 20240724142347.png]]


