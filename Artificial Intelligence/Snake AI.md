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
Revison: [[Python OOP (Object Oriented Programming)]]

```python
import pygame  
import random  
from enum import Enum  
from collections import namedtuple  
  
pygame.init()  
font = pygame.font.Font("asset/PressStart2P-Regular.ttf", 17)  
  
# reset  
# reward  
# play(action) -> direction  
# game iteration  
# is_collision  
  
  
# directions  
RIGHT = 1  
LEFT = 2  
UP = 3  
DOWN = 4  
  
# rgb colors  
WHITE1 = (255, 255, 255)  
WHITE2 = (200, 200, 200)  
RED = (200, 0, 0)  
BLACK = (0, 0, 0)  
GREEN = (0, 255, 0)  
  
BLOCK_SIZE = 20  
SPEED = 10  
  
  
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
  
  
class SnakeGame:  
    def __init__(self, w=1040, h=680):  
        self.w = w  
        self.h = h  
  
        # init display  
        self.display = pygame.display.set_mode((self.w, self.h))  
        pygame.display.set_caption("Snake")  
        self.clock = pygame.time.Clock()  
  
        # init game state  
        self.direction = RIGHT  
  
        self.head = Point(self.w / 2, self.h / 2)  
        self.snake = [self.head,  
                      Point(self.head.x - BLOCK_SIZE, self.head.y),  
                      Point(self.head.x - (2 * BLOCK_SIZE), self.head.y)]  
  
        self.score = 0  
        self.food = None  
        self._place_food()  
  
    def _place_food(self):  
        x = random.randint(0, (self.w - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE  
        y = random.randint(0, (self.h - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE  
        self.food = Point(x, y)  
  
        if self.food in self.snake:  
            self._place_food()  
  
    def _is_collision(self):  
        # hits boundary  
        if self.head.x > self.w - BLOCK_SIZE or self.head.x < 0 or self.head.y > self.h - BLOCK_SIZE or self.head.y < 0:  
            return True  
  
        # hits itself  
        if self.head in self.snake[1:]:  
            return True  
  
        return False  
    def _update_ui(self):  
        self.display.fill(BLACK)  
  
        for pt in self.snake:  
            pygame.draw.rect(self.display, WHITE2, pygame.Rect(pt.x, pt.y, BLOCK_SIZE, BLOCK_SIZE))  
            pygame.draw.rect(self.display, WHITE1, pygame.Rect(pt.x + 4, pt.y + 4, 12, 12))  
  
        pygame.draw.rect(self.display, RED, pygame.Rect(self.food.x, self.food.y, BLOCK_SIZE, BLOCK_SIZE))  
  
        text = font.render(str(self.score), True, WHITE1)  
        text_rect = text.get_rect(center=(self.w / 2, 25))  
        self.display.blit(text, text_rect)  
        pygame.display.flip()  
  
    def _move(self, direction):  
        x = self.head.x  
        y = self.head.y  
        if direction == RIGHT:  
            x += BLOCK_SIZE  
        elif direction == LEFT:  
            x -= BLOCK_SIZE  
        elif direction == DOWN:  
            y += BLOCK_SIZE  
        elif direction == UP:  
            y -= BLOCK_SIZE  
  
        self.head = Point(x, y)  
  
    def reset(self):  
        # init game state  
        self.direction = RIGHT  
        self.head = Point(self.w / 2, self.h / 2)  
        self.snake = [self.head,  
                      Point(self.head.x - BLOCK_SIZE, self.head.y),  
                      Point(self.head.x - (2 * BLOCK_SIZE), self.head.y)]  
        self.score = 0  
        self.food = None  
        self._place_food()  
  
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
  
    def user_input(self):  
        # user input  
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:  
                pygame.quit()  
                quit()  
  
            if event.type == pygame.KEYDOWN:  
                if event.key == pygame.K_LEFT:  
                    self.direction = LEFT  
                elif event.key == pygame.K_RIGHT:  
                    self.direction = RIGHT  
                elif event.key == pygame.K_UP:  
                    self.direction = UP  
                elif event.key == pygame.K_DOWN:  
                    self.direction = DOWN  
  
    def check_if_game_over(self):  
        # 3. check if game over  
        game_over = False  
        if self._is_collision():  
            game_over = True  
            return game_over, self.score  
  
            # 4. place new food or just move  
        if self.head == self.food:  
            self.score += 1  
            self._place_food()  
        else:  
            self.snake.pop()  
  
        return game_over  
  
    def play(self):  
        # 1. Create User Input  
        self.user_input()  
  
        # 2. Update Snake Moment and Size by BLOCK  
        self._move(self.direction)  # update the head  
        self.snake.insert(0, self.head)  
  
        # 3. check if game over  
        game_over = False  
        if self._is_collision():  
            game_over = True  
            return game_over, self.score  
  
            # 4. place new food or just move  
        if self.head == self.food:  
            self.score += 1  
            self._place_food()  
        else:  
            self.snake.pop()  
  
            # 5. update ui and clock  
        self._update_ui()  
        self.clock.tick(SPEED)  
  
        # 6. return game over and score  
        return game_over, self.score  
  
  
if __name__ == "__main__":  
    game = SnakeGame()  
  
    # main game loop  
    while True:  
        game_over, score = game.play()  
  
        if game_over:  
            game.show_game_over_screen(score)  
            game.reset()  
  
    print("Final score:", score)  
    pygame.quit()
```

Code Node:

```python
self.frame_iteration > 100*len(self.snake
```
# Part 3: Implement Agent to Control Game
