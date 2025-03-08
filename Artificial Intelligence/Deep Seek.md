AIME - logic and prob solving
Codeforce - code
GQPA - teaching, multi-task


Sparse Model - seperate (specialize) model for each task 

Chatgpt: FP16 or 32.
DeepSeek: FP8 -> more efficient. (why lower) -> input value is not that matter -> priortize model output (not human input) -> improve more than 10 billion FLOP/s compare to ChatGPT (20 vs 10).
-> ques: 1 + 1 -> 100ms for DS, 300ms for GPT

**Integrationbility**: everywhere

## LLM Reasoning: DeepSeek R1
Representator: Nguyen Le Minh (researcher at JAIST)

Improvement/Breakthrough from Young (exelent people)

LLM to DeepSeek Model 
**Average**
Foundation Model (LLM) -> Fine tunning 

**Deep Seek**
Deep Seek is multi-model
1) First build all the Foundation Model  
2) Reasoning/Code/Math Model  -> R0 -> R1
1 + 2 -> R1 (reasoning)

Deep Seek V3 breakthrough 
+ Key-Value Memory Compression via Multihead Latent Attention (MLA)
+ **Low-Precision Computation (FP8) - NEWS**
+ MoE (Mixture of Expert) 
+ **Group Relative Policy Optimization (GRPO) - NEWS**
+ Distilation
+ Pure Reinforcement Learning for Reasonning

Attention -> Latent Attention (A Compression Technique)
Muti-Token Prediction (Important)

**Basic**
Reinforcement Learning base on Human Feedback (RLHF) 
**Deep Seek**
Group Relative Policy Optimization (GRPO) - instead of calc 1 by 1, calc only the representator.
Reasning Model -> longer Inference 
Distilled -> bad if apply to diff language. Distill for Eng can be great but vn isn't.

---
[presentator source](https://ai4life.hust.edu.vn/lenp-2-2/)
### Are foundation model are really powerfull and reliable ? 

Mảng kiến thức nền tảng yêu cầu cho nghiên cứu y tế / ngôn ngữ (các hướng nghiên cứu)
1 số kiến thức nền tảng quan trọng nhất 
nền tảng vs chuyên ngành



ICD Code  + Clienical Note (docter note) + Other Modality (personal infor)
+ ! Data Driven, not focusing in model reasonning or generalization ability (suy diễn, tổng quan)
+ ? Giải pháp: LLM cho y tế
CARER
1) Multimodel Encoding
2) Clinical Reasoning

Khó khăn của CARER

HARMONIC: predict weather data base on pre-trained model + some of the best and lastest information (Historical best-track)
> Not use ViT

có ngành nhìn mô hình AI no a blackbox. ???

Graph Theory & Discrete Mathematics
Advanced Linear Algebra & Matrix Factorization
Optimization & Numerical Methods
Projective & Differential Geometry

Lý thuyết đồ thị & Toán rời rạc
Đại số tuyến tính nâng cao & Phân tích ma trận
Tối ưu hóa và Phương pháp số
Hình học xạ ảnh & Vi phân

