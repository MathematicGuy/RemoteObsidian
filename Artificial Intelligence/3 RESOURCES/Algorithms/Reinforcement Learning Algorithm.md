# Q-Learning
Q-Learning is a model-free reinforcement learning algorithm used to learn the value of an action in a particular state. It aims to find the optimal action-selection policy for a given finite Markov decision process (MDP).
  
### 1. Core Concepts:
* **State (s):** The current situation of the agent.
* **Action (a):** The set of all possible actions the agent can take in a state.
* **Reward (r):** The immediate return received after transitioning from one state to another.
* **Q-Value (Q):** The expected future reward of taking a particular action in a given state and following the optimal policy thereafter.
  
### 2. The Q-Learning Equation:
  The Q-value for a state-action pair is updated using the following equation:
$$Q(s,a)←Q(s,a)+α[r+γ⋅max⁡_{a'}Q(s′,a′)−Q(s,a)]$$
**Where:**
* $α$ (Learning Rate): The extent to which newly acquired information overrides the old information.
	
* $\gamma$ (Discount Factor): The degree to which future rewards are considered. A value of 0 means only immediate rewards are considered, while a value close to 1 means future rewards are highly regarded.
	 
* $r$: The reward received after taking action a in state s.
	
* $s′$: The next state after taking action a.
	
* $max_{a′}​Q(s′,a′)$: The maximum expected future reward for the next state s′ across all possible actions a′
  

**Explain in Detail**:
+ $Q(s, a )$: Current State **s** and Action **a**
+ $ $δ=[r+γ⋅max​Q_{a'}(s′,a′)−Q(s,a)]$ is the Temporal Difference error (TD), denoted by $\delta$. It represent the error between the target value and the current estimate Q(s, a).
	+ ? **Temporal Difference** refer to $max(Q_{a'}(s', a'))$  refers to the maximum Q-value achievable from the next state **s'**, considering all possible actions **a'** that agent could take in that state. 
		+ **Next State s'**: When the agent take action **a** in the current state **s**, it transition to a new state **s'**.
		+ **Future Actions a'**: all the possible action in the  next state **s'**. 
		+ Maximum Q-Value $max(Q_{a'}(s', a'))$: find the action **a'** that yeild that the highest expected cumulative reward in the states **s'**. **the value represent the best possible future outcome that the agent can expect to achieve from state s'**.
	+ ?  $r+γ⋅max​Q_{a'}(s′,a′)$ represent the target Q-value, which is the best estimate of the true value of Q-function based on the current knowledge (included the future reward)
		+ ? $\gamma$  (ranging from 0 - 1) is pre-defined (by human) to determine if the future reward are very valuable or less valuable. This can make the **agent far-sighted ($\gamma$  closer to 1) or short-sighted ($\gamma$ closer to 0)**
	+ ? Why Substract Q(s, a ) in Update?
		+ **Correcting the Estimate:** $δ=[r+γ⋅max​Q_{a'}(s′,a′)−Q(s,a)]$ serve to calculate the error between the curernt estimate Q(s, a) and the target. The larget the error, the bigger the adjustment that need to be made.
		+  **Direction of Update**: if the target is higher than the current estimate (i.e Q-value is too low)  the update will increase Q(s, a). The opposite if the target is lower.
```ad-summary
$δ=[r+γ⋅max​Q_{a'}(s′,a′)−Q(s,a)]$ help calculate the differences between the current value and the estimated values, we called that Temporal Differences Error (TD). 
+ Q(s,a) tell us about the quality of the current **state s** and **reward a**. 
+ $max(Q_{a'}(s', a'))$ **refers to the best action a' in the next state s'** the agent should take considering all the possible action in the next state. However this does not explicitly account for all previous states, the learning process inherently captures the effect of the previous states (giá trị của quá trình tr'c đó đc kế thừa vào trực tiếp vào trong state hiện tại)
+ $\delta$ is a critical hyperparameter in Reinforment Learning algorithm that balances the importances of immediate versus future reward. **By setting $\delta$, you can influence the agent's learning process to prioritize short-term gains or long-term planning**.
```


### How $max⁡_{a′}Q(s′,a′)$ Fits Into the [[Q-Learning Update]] Rule

The Q-Learning update rule is:
$$Q(s,a)←Q(s,a)+α[r+\gamma.max_{a'}Q(s′,a′)−Q(s,a)]$$
$Q(s, a)$ represents the **expected cumulative reward** that an agent can achieve by taking action a in state s and following the optimal policy thereafter. The goal of Q-Learning is to learn this function so that the agent can make decisions that maximize the expected rewards over time.
	
- **Immediate Reward r:** The reward r is what the agent receives immediately after taking action a in state s.
	
- **Discounted Future Reward $\gamma \cdot \max_{a'} Q(s', a')$:** The term $\gamma \cdot \max_{a'}Q(s', a')$ represents the best possible cumulative reward the agent can expect to receive in the future, starting from the next state s′. The discount factor $\gamma$ reduces the influence of future rewards, reflecting the notion that immediate rewards are often more valuable than distant rewards.
	
- **Update Objective:** The update rule aims to adjust $Q(s,a)$ so that it better reflects the expected total reward of taking action a in state s. This involves considering both the immediate reward $r$ and the best possible future reward.

+ $ Therefor, at the few first iteration TD will be greater than the current estimate. 


### 3. Algorithm Steps:
#### 3.1 Initialize Q-Table:
Create a table where each cell Q(s,a) is initialized to zero or a small random value.

#### 3.2 Observe Current State s:
Start in an initial state s.

#### 3.3 Choose an Action a:
Select an action aa using an action-selection policy (e.g., epsilon-greedy).
Take the Action and Observe the Reward rr and Next State s′:
Perform the chosen action and observe the immediate reward r and the new state s′.


**Update Q-Value:** 
	Update the Q-value for the state-action pair (s,a) using the Q-Learning equation.
**Repeat:**
	Set the current state ss to the next state s′ and repeat the process until a terminal state is reached.
**Convergence:**
	The algorithm converges when the Q-values stabilize, meaning the agent has learned an optimal policy.


# Limitations
- [ ]  Can only learn from mistake once they're dead, not at a certain state.


---

![[Pasted image 20240823191154.png]]
![[Pasted image 20240823191218.png]]
**How many step are optimal to look ahead ?**

![[Pasted image 20240823191412.png]]
>Bellman Equation
![[Pasted image 20240823191518.png]]

![[Pasted image 20240823191533.png]]

Random  Exploration -> allow agent to find hidden reward.
Ex:
+ a road give 20 reward that lead to 20 reward
+ a road give 0 reward that lead to 100 reward (Better Choice, but can only be found with random exploration)

**Model-Free learning** 
+ An AI learn by it self without needing to create a model before hand. 
+ AI can **directly derive an optimal policy** from its interacting env **without needing to create a model before hand**. 

**Q learning** is a **model-free learning technique** that can be used to **find the optimal policy using a Q function.** 


**Temporal Difference Learning**
![[Pasted image 20240823202026.png]]

**reinforcement learning algorithms**
![[Pasted image 20240823202226.png]]

using 