Agent: algorithm take a action, the enviroment give the agent a reward for set action and produces the next state. 
Ex:
Snake eat apple +20
Snake die in any way -10

![[Pasted image 20240808151913.png]]
> Sequence of State actions and rewards that end with the agent reaching the end goal is called an Episode.  
 
![[Pasted image 20240808152522.png]]
R -> reward. R2 after current R mean future reward.
Group the Future Reward -> Group of R after current R
	Ex: Every R after R1 can be group and seen as Group of Future reward.
Predict the Future return
Gamma: how important the future return are in ours calculation.
	Hight Gamma - Q value have More Weight
	Less Gamme - Q value have less Weight
Subtract the curernt Q value to the next Q value give us the gradient or rate of change.
Alpha - parameter that decided how large the gradient would be. The Larger Alpha is the larger Q value would changes.  


[Deep Q-Learning](https://www.youtube.com/watch?v=yR8N4AUEGoE)

