# Part 1: Theory
> Teach and make agent to take actions in an env in order to maximize the notion of cumulative reward.
 + **Algorithm**: Deep Q Learning.

### Project Structure 
![[Pasted image 20240730103955.png]]

#### Reward:
+ Eat Food: +20
+ Die: -10
+ Else: 0

#### Action
[1, 0, 0] -> Straight
[0, 1, 0] -> Right
[0, 0, 1] -> Left

#### Tell snake about the evironment
State (11 values)
{ 
	danger straight, danger right, danger left,
	direction left, direction right,
	direction up, direction down,
	food left, food right,
	food up, food down
}

**Model**
![[Pasted image 20240730113612.png]]


#### Deep Q Learning 
![[Pasted image 20240730104647.png]]

#### Bellman Equation
![[Pasted image 20240730113002.png]]

#### The table below is a brief example of a Q-learning table with the snake game.
![[Pasted image 20240730112920.png]]

#### Q Update Rule Simplified
![[Pasted image 20240730113305.png]]
**MSE (Mean Square Error)**
![[Pasted image 20240730113435.png]]


# Part 2: Set up enviroment and implement snake game

0) Download and Setup Conda and CUDA
```sh
conda create -n snake-ai python=3.9
conda activate snake-ai
```
1) Download Requirements from requirement file

>requirements.txt
```txt
pygame
torch
torchvision
mathplotlib
ipython
```
	
>Terminal 
```sh
pip install -r requirements.txt
```

# Part 3: Implement Agent to Control Game


# Part 4: Create and Train Neural Network


