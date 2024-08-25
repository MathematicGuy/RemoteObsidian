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


### Results
![[Pasted image 20240825104035.png]]
```python
MAX_MEMORY = 800_000 # Store n samples. 
BATCH_SIZE = 1000 # n samples in a batch. 
LR = 0.0001  # Learning Rate
```

**Result after 175 Iterations**
![[Pasted image 20240825110002.png]]

**400 Iters**
![[Pasted image 20240825112429.png]]


## Whole code
```python
// snake.py
import pygame
import random
from enum import Enum
from collections import namedtuple
import numpy as np

pygame.init()
font = pygame.font.Font("asset/PressStart2P-Regular.ttf", 17)

# reset
# reward
# play(action) -> direction
# game iteration
# is_collision


# rgb colors
WHITE1 = (255, 255, 255)
WHITE2 = (200, 200, 200)
RED = (200, 0, 0)
BLACK = (0, 0, 0)
GREEN1 = (0, 255, 0)
GREEN2 = (0, 200, 0)

BLOCK_SIZE = 20
SPEED = 2000


class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4


Point = namedtuple('Point', 'x, y')


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


def replay(play_again_rect):
    # wait for the user to click play again
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # Reset if Mouse Click is close to play again text
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if play_again_rect.collidepoint(mouse_pos):
                    return


class SnakeAI:
    def __init__(self, w=1040, h=680):
        self.w = w
        self.h = h

        # init display
        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption("Snake")
        self.clock = pygame.time.Clock()
        
        #Initialize game state
        self.reset()    

    def _place_food(self):  #? note: _ mean private class/method
        x = random.randint(0, (self.w - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        y = random.randint(0, (self.h - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        self.food = Point(x, y)

        if self.food in self.snake:
            self._place_food()

    def is_collision(self, pt=None):
        if pt is None:
            pt = self.head

        # hit boundary
        if pt.x > self.w - BLOCK_SIZE or pt.x < 0 or pt.y > self.h - BLOCK_SIZE or pt.y < 0:
            return True

        # hits itself
        if pt in self.snake[1:]:
            return True

        return False

    def _update_ui(self):
        is_head = True
        self.display.fill(BLACK)

        for pt in self.snake:
            if is_head:
                pygame.draw.rect(self.display, GREEN2, pygame.Rect(pt.x, pt.y, BLOCK_SIZE, BLOCK_SIZE))
                pygame.draw.rect(self.display, GREEN1, pygame.Rect(pt.x + 4, pt.y + 4, 12, 12))
                is_head = False
            else:
                pygame.draw.rect(self.display, WHITE2, pygame.Rect(pt.x, pt.y, BLOCK_SIZE, BLOCK_SIZE))
                pygame.draw.rect(self.display, WHITE1, pygame.Rect(pt.x + 4, pt.y + 4, 12, 12))

        pygame.draw.rect(self.display, RED, pygame.Rect(self.food.x, self.food.y, BLOCK_SIZE, BLOCK_SIZE))

        text = font.render(str(self.score), True, WHITE1)
        text_rect = text.get_rect(center=(self.w / 2, 25))
        self.display.blit(text, text_rect)
        pygame.display.flip()

    def _move(self, action):
        # [straight, right, left]
        clock_wise = [Direction.RIGHT, Direction.DOWN, Direction.LEFT, Direction.UP]
        index = clock_wise.index(self.direction)  # track snake direction in clockwise

        if np.array_equal(action, [1, 0, 0]):
            new_dir = clock_wise[index]  # no change
        elif np.array_equal(action, [0, 1, 0]):  # right [0, 1, 0]
            next_index = (index + 1) % 4
            new_dir = clock_wise[next_index]  # right turn r -> d -> l -> u
        else:  # left [0, 0, 1]
            next_index = (index - 1) % 4
            new_dir = clock_wise[next_index]  # left turn r -> u -> l -> d

        self.direction = new_dir

        x = self.head.x
        y = self.head.y
        if self.direction == Direction.RIGHT:
            x += BLOCK_SIZE
        elif self.direction == Direction.LEFT:
            x -= BLOCK_SIZE
        elif self.direction == Direction.DOWN:
            y += BLOCK_SIZE
        elif self.direction == Direction.UP:
            y -= BLOCK_SIZE

        self.head = Point(x, y)

    def reset(self):
        # init game state
        self.direction = Direction.RIGHT  # Ini Direction
        self.head = Point(self.w / 2, self.h / 2)
        self.snake = [self.head,
                      Point(self.head.x - BLOCK_SIZE, self.head.y),
                      Point(self.head.x - (2 * BLOCK_SIZE), self.head.y)]
        self.score = 0
        self.food = None
        self._place_food()
        self.frame_iteration = 0

    def _render_text(self, text, font, color, center):
        rendered_text = font.render(text, True, color)
        text_rect = rendered_text.get_rect(center=center)
        self.display.blit(rendered_text, text_rect)
        return text_rect

    def show_game_over_screen(self, score):
        self.display.fill(BLACK)

        self._render_text("GAME OVER", font, RED, (self.w / 2, self.h / 2 - 50))
        self._render_text("Score: " + str(score), font, WHITE1, (self.w / 2, self.h / 2))

        play_again_rect = self._render_text("Play Again", font, BLACK, (self.w / 2, self.h / 2 + 50))
        play_again_text = font.render("Play Again", True, BLACK)
        button_rect = play_again_rect.inflate(20, 10)  # padding around the text
        pygame.draw.rect(self.display, WHITE1, button_rect)
        self.display.blit(play_again_text, play_again_rect)

        pygame.display.flip()

        replay(play_again_rect)

    def play(self, action):
        self.frame_iteration += 1

        # 1. Check if we want to keep the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # 2. Update Snake Moment and Size by BLOCK
        self._move(action)  # update the head
        self.snake.insert(0, self.head)

        # 3. check if game over
        reward = 0
        game_over = False
        # Check the length of the snake through frame_iteration incase it doesn't grow
        if self.is_collision() or self.frame_iteration > 100 * len(self.snake):
            game_over = True
            reward = -10
            return reward, game_over, self.score

        # 4. place new food or just move
        if self.head == self.food:
            self.score += 1
            reward = 10
            self._place_food()
        else:
            self.snake.pop()

            # 5. update ui and clock
        self._update_ui()
        self.clock.tick(SPEED)

        # 6. return game over and score
        return reward, game_over, self.score

// agent.py
import torch
import random
import numpy as np
from collections import deque  # use to store data
from snake import SnakeAI, Direction, Point
from model import Linear_QNet, QTrainer
from helper import plot
import os
import sys


MAX_MEMORY = 400_000 # Store n samples. 
BATCH_SIZE = 1000 # n samples in a batch. 
LR = 0.0002  # Learning Rate
SPEED = 20000  # Increase the frame rate
INPUT_SIZE = 12
HIDDEN_SIZE1 = 256
OUTPUT_SIZE = 3
FILE_PATH = 'model/model5.pth'
ARGS = sys.argv

class Agent:
    """
    The Agent class represents an agent for the SnakeAI Game.
    
    Attributes:
        n_games (int): The number of games played by the agent.
        epsilon (float): The randomness factor for exploration.
        gamma (float): The discount rate for future rewards.
        memory (deque): A deque to store game data. (deque is a list-like container with fast appends and pops on either end)
        model (object): The model used for prediction.
        trainer (object): The trainer used for training the model.
    Methods:
        get_state(game): Returns the current state of the game.
        remember(state, action, reward, next_state, done): Stores game data in memory.
        train_long_memory(): Trains the model using long-term memory.
        train_short_memory(state, action, reward, next_state, done): Trains the model using short-term memory.
        get_action(state): Returns the action to take based on the current state.
    """

    def __init__(self):
        self.use_old = False
        self.n_games = 0
        self.epsilon = 0  
        self.gamma = 0.9  
        self.memory = deque(maxlen=MAX_MEMORY)  # save data to deque
        self.model = Linear_QNet(INPUT_SIZE, HIDDEN_SIZE1, OUTPUT_SIZE)  # 11 input, 256 hidden, 3 output

        if os.path.exists(FILE_PATH) and len(ARGS) == 2 and str(ARGS[1]) == 'load':
            self.model.load_state_dict(torch.load(FILE_PATH))
            self.model.eval()
            self.use_old = True

        self.trainer = QTrainer(self.model, lr=LR, gamma=self.gamma)  # QTrainer object

    def get_state(self, game):
        """
        Returns the state of the game for the agent in 0 and 1 format.
        
        Parameters:
            game (Game): The game object representing the current state of the game.
        Returns:
            state (numpy.ndarray): An array representing the state of the game. The array contains the following elements:
                Danger Direction: True if there is a danger straight/right/left/below ahead in the current direction, False otherwise
                Food Location: True if the food is to the left/right/above/below of the snake's head, False otherwise.
        """

        head = game.snake[0]
        point_r = Point(head.x + 20, head.y)
        point_l = Point(head.x - 20, head.y)
        point_u = Point(head.x, head.y - 20)
        point_d = Point(head.x, head.y + 20)

        dir_r = game.direction == Direction.RIGHT
        dir_l = game.direction == Direction.LEFT
        dir_u = game.direction == Direction.UP
        dir_d = game.direction == Direction.DOWN

        state = [
            # Danger straight
            (dir_r and game.is_collision(point_r)) or
            (dir_l and game.is_collision(point_l)) or
            (dir_u and game.is_collision(point_u)) or
            (dir_d and game.is_collision(point_d)),

            # Danger right
            # Ex: True if there is a danger to the right in the current direction, False otherwise
            (dir_u and game.is_collision(point_r)) or
            (dir_d and game.is_collision(point_l)) or
            (dir_l and game.is_collision(point_u)) or
            (dir_r and game.is_collision(point_d)),

            # Danger left
            (dir_d and game.is_collision(point_r)) or
            (dir_u and game.is_collision(point_l)) or
            (dir_r and game.is_collision(point_u)) or
            (dir_l and game.is_collision(point_d)),

            # Danger down
            (dir_r and game.is_collision(point_r)) or
            (dir_l and game.is_collision(point_l)) or
            (dir_u and game.is_collision(point_u)) or
            (dir_d and game.is_collision(point_d)),

            # Move Direction
            dir_l,
            dir_r,
            dir_u,
            dir_d,

            # Food Location (start from head location)
            game.food.x < game.head.x,  # food left
            game.food.x > game.head.x,  # food right
            game.food.y > game.head.y,  # food up
            game.food.y < game.head.y,  # food down
        ]

        return np.array(state, dtype=int)  # Turn State (True or False boolean) into 0 and 1

    def remember(self, state, action, reward, next_state, done):
        # append a list of tuple
        self.memory.append((state, action, reward, next_state, done))  # popleft if MAX_MEMORY is reached

    """
    Train_long_memory & Train short memory

    Args:
        state (np.array): The current state of the game.
        action (int): The action taken.
        reward (float): The reward received.
        next_state (np.array): The next state of the game.
        done (bool): Indicates if the game is done.

    Returns:
        the action to take based on the current state.
    """

    def train_long_memory(self):
        """
        This method is responsible for training the agent using the samples stored in the long-term memory.
        If the number of samples in the memory is greater than the batch size, a mini-batch of size BATCH_SIZE is randomly selected.
        Otherwise, all the samples i n the memory are used.
        """
        if len(self.memory) > BATCH_SIZE:  # if have more than BATCH_SIZE samples
            mini_sample = random.sample(self.memory, BATCH_SIZE)  # list of tuples
        else:
            mini_sample = self.memory

        states, actions, rewards, next_states, dones = zip(*mini_sample)  # Extract every samples existed
        self.trainer.train_step(states, actions, rewards, next_states, dones)  # Train with every samples existed

    def train_short_memory(self, state, action, reward, next_state, done):  # 1 step
        self.trainer.train_step(state, action, reward, next_state, done)

    def get_action(self, state):
        """
        Returns a one-hot encoded list representing the action to take based on the given state.
        
        Parameters:
        - state: The current state of the game.
        Returns:
        - final_move: A one-hot encoded list [0, 0, 0] where only one element is 1, indicating the direction to move.
        Explain:
            Random moves: tradeoff exploration / exploitation
            if random < epsilon: explore 
            else: exploit
        """

        self.epsilon = 69 - self.n_games  # epsilon get smaller as the game progress

        final_move = [0, 0, 0]
        # if random.randint(0, 200) < self.epsilon:
        #     move = random.randint(0, 2)
        #     final_move[move] = 1
        # else:
        #     # convert raw values into tensor format and predict (torch require float tensor) 
        #     state0 = torch.tensor(state, dtype=torch.float)
        #     prediction = self.model(state0)
        #     # convert max value into 1 other values 0.
        #     move = torch.argmax(prediction).item()
        #     final_move[move] = 1

        if self.use_old == False:
            self.epsilon = 69 - self.n_games
            if random.randint(0, 200) < self.epsilon:
                move = random.randint(0, 2)
                final_move[move] = 1
            else:
                state0 = torch.tensor(state, dtype=torch.float)
                prediction = self.model(state0)
                move = torch.argmax(prediction).item()
                final_move[move] = 1
        else:
            state0 = torch.tensor(state, dtype=torch.float)
            prediction = self.model(state0)
            move = torch.argmax(prediction).item()
            final_move[move] = 1

        return final_move
    
    


def train():
    """
    Trains the snake AI agent by playing the snake game.
    This function iteratively plays the snake game and trains the agent's neural network model.
    It keeps track of the scores and records, and updates the agent's memory for training.
    After each game, it resets the snake game and trains the agent's long-term memory.
    """

    plot_scores = []
    plot_mean_scores = []
    total_score = 0
    record = 0
    agent = Agent()
    snake = SnakeAI()

    while True:
        # get old state
        state_old = agent.get_state(snake)

        # get move
        final_move = agent.get_action(state_old)

        # perform move and get new state
        reward, done, score = snake.play(final_move)
        state_new = agent.get_state(snake)

        # train short memory
        agent.train_short_memory(state_old, final_move, reward, state_new, done)

        # remember
        agent.remember(state_old, final_move, reward, state_new, done)

        if done:
            # train long memory. replay memory
            snake.reset()
            agent.n_games += 1
            agent.train_long_memory()

            if score > record:
                record = score
                agent.model.save()

            print('Game', agent.n_games, 'Score', score, 'Record:', record)

            plot_scores.append(score)
            total_score += score
            mean_scores = total_score / agent.n_games
            plot_mean_scores.append(mean_scores)
            plot(plot_scores, plot_mean_scores)


if __name__ == '__main__':
    # Create an instance of your model
    model = Linear_QNet(12, HIDDEN_SIZE1, 3)

    # Load the state dictionary from the file
    # model.load_state_dict(torch.load(FILE_PATH))

    # Set the model to evaluation mode (optional, but recommended for inference)
    model.eval()

    train()

// model.py
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import os

FILE_PATH = 'model5.pth'

#TODO: Learn How to Modify Q-Learning 
class Linear_QNet(nn.Module):
    def __init__(self, input_size, hidden_size1, output_size):
        super().__init__()
        self.linear1 = nn.Linear(input_size, hidden_size1)
        self.linear2 = nn.Linear(hidden_size1, output_size)

    def forward(self, x):
        print(f"Input shape: {x.shape}")
        x = F.relu(self.linear1(x))  # Apply ReLU activation after the first linear layer
        x = self.linear2(x)
        return x

    #? Save Training Result to model.pth (pytorch file format) 
    def save(self, file_name=FILE_PATH):
        model_folder_path = './model'
        if not os.path.exists(model_folder_path):
            os.makedirs(model_folder_path)

        file_name = os.path.join(model_folder_path, file_name)
        torch.save(self.state_dict(), file_name)


class QTrainer:
    def __init__(self, model, lr, gamma):
        self.lr = lr
        self.gamma = gamma
        self.model = model
        self.optimizer = optim.Adam(model.parameters(), lr=self.lr)
        self.criterion = nn.MSELoss()  # mean square error

    def train_step(self, state, action, reward, next_state, done):
        state = torch.tensor(state, dtype=torch.float)
        next_state = torch.tensor(next_state, dtype=torch.float)
        action = torch.tensor(action, dtype=torch.long)
        reward = torch.tensor(reward, dtype=torch.float)
        # (n, x)

        if len(state.shape) == 1:
            # (1, x) append 1D in the beginning
            state = torch.unsqueeze(state, 0)
            next_state = torch.unsqueeze(next_state, 0)
            action = torch.unsqueeze(action, 0)
            reward = torch.unsqueeze(reward, 0)
            done = (done,)  # define 1 value tuple

        # 1: predicted Q values with current state
        pred = self.model(state)
        target = pred.clone()

        for index in range(len(done)):
            Q_new = reward[index]
            if not done[index]:
                Q_new = reward[index] + self.gamma * torch.max(self.model(next_state[index]))

            target[index][torch.argmax(action[index]).item()] = Q_new

        # 2: Q_new = r + y * max(next_predicted Q value) -> only do this if not done  
        # pred.clone() -> get current state for prediction
        # preds[argmax(action)] = Q_new -> index of 1 in action (one-hot encoded) get send to Q_new
        self.optimizer.zero_grad()
        loss = self.criterion(target, pred)
        loss.backward()

        self.optimizer.step()
        
// helper.py
import matplotlib.pyplot as plt
from IPython import display

plt.ion()

def plot(scores, mean_scores):
    display.clear_output(wait=True)
    display.display(plt.gcf())
    plt.clf()
    plt.title('Training...')
    plt.xlabel('Number of Games')
    plt.ylabel('Score')
    plt.plot(scores)
    plt.plot(mean_scores)
    plt.ylim(ymin=0)
    plt.text(len(scores) - 1, scores[-1], str(scores[-1]))
    plt.text(len(mean_scores) - 1, mean_scores[-1], str(mean_scores[-1]))
    plt.show(block=False)
    plt.pause(.1)
```