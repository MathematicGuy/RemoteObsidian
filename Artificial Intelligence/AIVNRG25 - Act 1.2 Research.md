### Rlaif: Scaling reinforcement learning from human feedback with ai feedback
1) [1st Research Homework](https://docs.google.com/document/d/1u9ZklyXffriuCk-9KTsqp9dAwK-nZKGHm0PDrlj8z9s/edit?tab=t.0)
2) [Notion](https://www.notion.so/2546ba5bfab180c28774e7853659bedd?v=2546ba5bfab181c3af32000c61b558d1&p=2546ba5bfab1816fb4ebeff29c02db04&pm=s)
3) [Viblo Note for easier Homework](https://viblo.asia/p/llm-paper-reading-rlaif-scaling-reinforcement-learning-from-human-feedback-with-ai-feedback-0gdJzDaGVz5)


**RLAIF WORKFLOW FOR RL (Reinforcement Learning from AI Feedback)**
```txt
1) Pretrain / SFT Base Model
   |
   v
2) Generate Candidate Responses (Policy outputs multiple responses for each prompt)
   |
   v
3) AI Feedback Labeling (Off-the-shelf LLM provides preference ranking or scores)
   |
   +--> Distilled RLAIF: Train Reward Model on AI preference labels
   |         |
   |         v
   |   Reward model outputs scalar reward
   |
   +--> Direct RLAIF: Use AI scores directly as reward signal
   |
   v
4) Policy Optimization (RL step)
   - Algorithm: REINFORCE/PPO-like
   - Reward: From Reward Model or Direct AI Score
   - KL-penalty: Keeps updated policy close to base model
   |
   v
5) Evaluate & Iterate
   - Check performance (summarization, helpful/harmless dialogue)
   - Optionally repeat labeling + RL for further improvements
   |
   v
6) Deployment
   - Fine-tuned aligned LLM deployed with better alignment & lower cost
```

**Iterative RLAIF Feedback Loop**
```txt
[Start with Base Model]
   |
   v
[Generate Candidate Responses]
   |
   v
[AI Labeler provides preferences (AI Feedback)]
   |
   v
[Train Reward Model or use Direct AI Scores]
   |
   v
[Policy Optimization with RL (REINFORCE/PPO)]
   |
   v
[Evaluate Performance]
   |
   +--> If performance needs improvement:
   |       Repeat cycle with updated policy
   |    (generate new responses, re-label with AI, retrain)
   |
   +--> If performance is good enough: 
   Stop and Deploy

Key Idea: Multiple iterations may yield "additional gain"
- Better responses -> Better AI labels -> Improved policy
```


----
## Reinforcement Learning with Human Feedback clearly explain Power Point
### 3. Quá trình Viết lại Bài báo Khoa học
Thử thách khi viết Proposed Method