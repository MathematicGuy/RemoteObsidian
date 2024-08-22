![[Pasted image 20240822162216.png]]
![[Pasted image 20240822162227.png]]



![[Pasted image 20240822163641.png]]

**Main Idea**
![[Pasted image 20240822163844.png]]

There are 2 Phrase:
1: Data collection
2: Training a DQN (Deep Q Network)
![[Pasted image 20240822164226.png]]

 ![[Pasted image 20240822164458.png]]
The MSE then backprop to the QNetwork. 


![[Pasted image 20240822164842.png]]
# Q-learning

value function: total reward -> determine Optimal Policy  (how agent behave in situations)

**Value-based Methods**
![[Pasted image 20240822165109.png]]

![[Pasted image 20240822165205.png]]
QLearning -> learning the state action value function
![[Pasted image 20240822165252.png]]
Goal: Learn these Q values such that total reward is maximized.
![[Pasted image 20240822165945.png]]
![[Pasted image 20240822165531.png]]
> Q value of State S1 is the total of the Sum of the reward in State S2 + (the maximum future reward value of State S2 with action a) * Gamme value
> + Gamme value: how we valuable the future reward.
![[Pasted image 20240822165901.png]]
+ maxQ(S,2 a): the best action available of the next state / the maximum action value in the next state. For S2, it 1.5. 
![[Pasted image 20240822170547.png]]

![[Pasted image 20240822170634.png]]
For the 2nd State. 
![[Pasted image 20240822171050.png]]
The process then continue over and over until the QTable are more optimal and stable.

**Target Policy:** the policy the agent is trying to learn.
**Behavior Policy:** the policy the agent uses to learn the target policy.

**Learn:**
+ The Bellman Equation
+ Temporal Different Learning

