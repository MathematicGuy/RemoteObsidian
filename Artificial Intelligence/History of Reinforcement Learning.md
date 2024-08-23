Discrete value: Giá Trị Rời Rạc
	Chia giá trị ra thành các phần.

State of the word: Perception of the world.
Agent: 
Policy(state) = action (quy luật)

Hard to Learn because
+ Each State have to be repeated many time in oder to learn.
+ More State -> Harder to Learn

**Original Idea:** Computer calc all chess move to play the best
Instead: made the bot to predict the future of the game to find the best move.

**Given any board States:** Evaluate each state from -1 to 1 show how likely it leads to a win versus a loss.

Create a Value function Shannon (the author) started with some well-know chess rule:
+ **p:** piece count, **pv:** piece value, **m:** mobility, **k:** how expose your king is - > each of these is a features and together they can define a equation.
	V(s) =  Multiply each features by it important or weight/coefficients (in neural network)  
	![[Pasted image 20240812214650.png]]
	His Features output the value for that position.
+ ? Although this method not allow the machine to learn. Every value is just a constant. How to optimize this?
+ $ One possibility is to have a higher program to learn and optimize the terms and weight involved in the evaluation function. 
	+ Each features importance will have the ability to learn from experience -> sense of direction.  ![[Pasted image 20240812215231.png]]

 **TD Gammom (Grerald Tesaruo)** - TD Learning
![[Pasted image 20240813084131.png]]
Compare the current move winning chance to it future move winning change. Then Update the value of the current move closer to the future move if the future move have higher winning chance.
-> Learning from your own guesses. Temporal difference Learning. 
-> As the machine trained, it become better at predicting future pattern. Then it start to predict the future backward, form end game to openning game. (This is call Bootstraping)

+ ! But Learnning a highly complex game on a continues problem for robotic is impossible.
	Bc this algorithm focus on the State Quality, Not Action Quality. So a key improment was given:
	![[Pasted image 20240813084841.png]]
	Instead of learning the value of a state, you should **focus on the value of a specific action in a state. This call Action Quality or Q Learning/Q Function**.
+ $ Lead to a faster and more stable result.

	Q-Learning can break down a continuous control problem where the action phrase within the choice of few button but a range of possible action. (discrete action)
	![[Pasted image 20240813085653.png]]


Policy Gradient approach.

Use Randomization to generalize the Machine expertise.
