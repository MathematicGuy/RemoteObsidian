**Motivation** = Learn through Reinforcement by making mistakes and collecting data on those mistakes to learn how to improve. 

**Data:** state-action pair
**Goal:** Minimize future rewards over many time steps.

## Key Concepts
**Actions:** a move that agent make in the env. $a_{t}$
**Actions Space:** set of possible Actions an agent can make in the env.
**Observations:** of the env after taking actions. 
	**State changes:** set of states $S_{t} + 1$
	**Reward:** feedback that measures the success of failure of the agent's action. $r_t$  

Total Reward (return) :  

**Policy Gradient:** cho phép điều khiển tốc độ cho model trong ko gian action liên tục. 

# Deep Reinforcement Learning Practice  
**Driveless Car**
**agent:** Car Neural Network.
**action:** Turning degree, thrustle (go forward and backward), brake.
env: Training Road
state: stop, going forward, going left, going right, going backward, accelerating, deaccelerating.
reward function: Survive(+100), driving distance (+1.5/km), early_arrival_time (+5 per minute early), Correct Driving
Lane.
loss function: (penalty): Crash (-200), long_arrival_time <-> arrived late (-5 per minute), haven't arrived to the
destination in the upper limit time (-10), Wrong Driving Lane (-5 per minute), stay in a spot for too long when the env is
safe (-200)


Optimization: 
**Neural Network Input:** current state, obstacles 
- **Current State:** `[x_position, y_position, speed, direction, acceleration, lane_position]`
- **Obstacles:** `[distance_to_front_obstacle, distance_to_left_obstacle, distance_to_right_obstacle, distance_to_rear_obstacle]`
**End Condition:** arrived, out of time, crash, no progress within the specified time limit.
**Expected (kỳ vọng):**
- **Minimize Crashes:** The agent should prioritize safety.
- **Efficient Arrival:** The agent should learn to balance speed and caution, arriving quickly without unnecessary risk.
- **Correct Lane Usage:** Adhere to legal driving practices.
- **Obstacle Avoidance:** The agent should learn to avoid obstacles effectively.
**Learning Rate:** Medium
**Decay Strategy - Eploitation & Exploration** 
+ Explore at the start of the game. (explore all the moves and policy of the agent)
+ Exploit as the game progress. (use learned knowledge to predict the actions with the highest reward)

**Trainning Algorithm/Function:** Gradient policy ( Use when there are **continuous action space** like **car turning degree**, there on specific value just an continuous array of values) 

---
note: only use 1 Model for all action. (Only Gradient policy not both Gradient policy and Deep Q-Learning)

**Continuous Action Spaces:** Unlike discrete actions (e.g., move left, right), continuous actions involve a range of possible values. For example, the turning degree could vary smoothly from -45° to +45°, or the throttle could vary continuously from 0% to 100%.

**Gradient-Based Policies:** Methods like Policy Gradient, Actor-Critic, or Proximal Policy Optimization (PPO) directly optimize the policy, which can output continuous actions. These methods work by computing the gradient of the expected reward with respect to the policy parameters and then updating the parameters to improve the policy.
	(Dùng Phân Bổ Xác Suất, Tính Mean, Variance)
```ad-example
- **Policy Gradient (REINFORCE):** Directly optimizes the policy by using the gradient of the expected reward with respect to the policy parameters.
- **Actor-Critic Methods (e.g., A2C, A3C):** Combines a value-based approach (critic) with a policy gradient approach (actor), offering more stable and efficient learning.
- **Proximal Policy Optimization (PPO):** A popular variant that improves stability and performance by limiting the size of policy updates.
```

