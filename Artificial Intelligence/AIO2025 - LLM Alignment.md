**MUST DO:** [code practice](https://drive.google.com/drive/folders/1UjqMhvAXZQ-GAUC44Bp_je-ne3R-9Oap?usp=drive_link)
+ [RL + CL](https://cameronrwolfe.substack.com/p/rl-continual-learning)

## Alignment with Reward Models (RLHF & Challange)

### Proximal Policy Optimization (PPO)
![[Pasted image 20260418204431.png]]
Data distribution between 2 model ($\pi_{\theta}$ Current Training model - $\pi_{\text{ref}}$ Frozen origin model)
KL Diver trong RLHF -> *phân phối của các token giữa 2 model* (not weights)
+ ! Depend on Human feedback


**RL from AI Feedback (RLAIF)** - optimize resource but reduce quality.
![[Pasted image 20260418204932.png]]
+ ? RLAIF vs Distillation ???
	- **RLAIF** focuses on **alignment**, teaching a model to adhere to human preferences by using an AI to rate outputs instead of humans.
		
	- **Distillation** focuses on **model compression**, teaching a small student model to behave like a large, capable teacher mode
- ? *"soft labels" (the probability distribution*/logits of the teacher) rather than just the *final answer ("hard labels").*
![[Pasted image 20260418205245.png]]
	(TA Thắng) Theo e thì concept là khá giống nhau - đều có ý muốn đưa kiến thức của một mô hình lớn sang mô hình nhỏ hơn. Nhưng còn về mặt kỹ thuật thì thông thường KD sẽ dùng logits (soft labels) để đưa kiến thức xuống còn ở đây e nghĩ chỉ dùng hard labels thôi. Nếu có dùng probs distribution thì cũng để sampling r đưa ra hard labels.

**Challanges for RLHF**
*Misaligned Evaluators*
	Tractable Difficulty selecting representative humans
	Tractable Evaluators may have harmful biases
	Tractable Individual evaluators can poison data
	
*Difficult Oversight*
	Tractable Humans make mistakes due to limited time/attention
	Fundamental Humans cannot evaluate difficult tasks well
	Fundamental Humans can be misled and gamed
	
*Data Quality Issues*
	Tractable Data collection introduces biases
	Fundamental Inherent cost/quality/quantity tradeoffs


![[Pasted image 20260418205716.png]]

## Alignment without Reward Models
### Direct Alignment Algorithms (DPO)
![[Pasted image 20260418210930.png]]

![[Pasted image 20260418211213.png | 485]]
	Ask Gemini explain about math, ie. what I can conclude after each transformation. 


fomula 3 -> reward model Loss Function to optimize reward of y1.
fomula (5) look like Sigmoid -> turn into Sigmoid (6) as final function.
![[Pasted image 20260418212250.png | 666]]

![[Pasted image 20260418212330.png | 777]]
Maximize the inner function (orange)
y_w - user preference response 
y_l - (reverse) user dis-preference response
the divide - làm  cái pi theta và pi ref - gần với nhau. 
`-` sign to **turn a maximization problem (maximizing the probability of human preference) into a minimization problem** that can be solved using gradient descent
Công Việc đơn giản -> mô hình reward tốt hơn. 

### Limitations of Direct Alignment Algorithms
...
### How to Choose: RLHF or DPO ?
**When to choose one ? RLHF vs DPO**
+ low training data - the same
+ if *policy is ambiguous* -> *DPO* better
+ when *reward model is weak* -> *RLHF* better bc it avoid errors better.
![[Pasted image 20260418213413.png | 555]]

Practical Guideline
![[Pasted image 20260418213654.png]]


## AI Safety and Alignment
[initinitialize LLM reference](https://keras.io/keras_hub/api/models/gemma/gemma_causal_lm/)

model toxicity increase by Parameters
reward hacking - model optimize reward rather than reality. e.g. too ethical, overfitting. 
	"how to kill a python process", model focus on "kill" token rather than the whole sentence context. 
![[Pasted image 20260418221109.png]]
ưu tiên chosen (current training) hơn reference (base model). 
Ko cần reward model -> DPO

Paper *-> tìm ra vấn đề trước.* 
hướng nghiên cứu hiện tai còn tồn tại vấn đề gì.
các vấn đề liên quan đã giải quyết vấn đề tồn tại chưa ?
-> Khi đọc paper chỉ cần biết Paper này giải quyết vấn đề gì chưa.
Chạy code paper mình thích nhất và chạy 

Trick : Apply giải pháp từ lĩnh vực khác sang của mình. 
Cần nhiều rule của con người -> RLHF -> Nhưng mà cần Align đúng Value của con người. 

DINO là model thuộc JEPA (self-supervised learning)
embedding of DINO is manifold. JEPA add a head for fine-tune.

## Learning Roadmap Latent Space
**1. Understand Dimensionality Reduction (Foundation) - PCA**
-> understand how data can be compressed. 
	learned concept: PCA and *Manifold Hypothesis,* this mean although data seems to live in very high-dimensional spaces, it actually lies on much lower-dimensional structures called Manifold embedded within those spaces. *ie. see data from high-dimensional space through the lense of low-dimensional space.* ![[Pasted image 20260511115753.png | 777]] 
+ ? For example, images might contain millions of pixel values, but the set of meaningful images occupies only a tiny subset of all possible pixel combinations. 
+ $ By *mapping raw data into representations that better capture "manifold" structure*, NN can *seperate classes, compress informtion and generate realistic smaples.*  ![[Pasted image 20260511112105.png | 555]]


**2. Learn Autoencoders (basic model)**
Understand the Architecture - Encoder (compresses input to latent vector) -> latent space -> decoder (reconstruct input)
+ ? Bottleneck forces the model to learn a good representation

**3. Explore Generative Models (VAEs and GANs)**
+ **VAEs** (Variational Autoencoders) - learn prob distribution over the latent space -> making it continous and useful for sampling new data.
	
+ **GANs** (Generative Adversarial Network) - a generator create data from latent vetor while the discriminator verify it, resulting in high-quality generation.
	
+ **Latent Diffusion Models** - how tools like Stable Diffusion work - applying diffusion within a compressed latent space to save compute. 

**4. Understand vector embedding (NLP)**
Concept - word2vec, BERT and Transformer
Key Idea: word/sentence are mapped to high-dim spaces where vector math (e.g. King - Man + Woman = Queen) works. 

**Core Concepts to Master**
+ **Continuous vs. Discrete Space:** good latent spaces allow smooth interpolation -> *moving slightly in the space results in a slight change* in the output -> Better generalization. 
	-> Minimum Loss when update. 

+ **Disentanglement** - a well-leanred representation where *each individual dimension control a specific semantic factors.* (e.g. 1 dim control roration, another control lighting)

+ **Reconstruction Loss** - the penalty a model gets when it cannot reconstruct the input well from the latent vector. 

![[Pasted image 20260418225108.png | 777]]

**Latent Memory:** Investigating how models can build long-term memory structures within latent representations (e.g., MemGen).

**Bias Mitigation:** Researching how to map features to a latent space that eliminates protected attributes while preserving necessary information for fair decision-making


#### Latent Space Reasoning & Thinking in LLMs
**Continuous "Thought" Loops:** frameworks like COCONUT (Continuous Thought) that enable LLMs to *feed internal hidden states back into the model* to form loops of thought, **bypassing discrete language constraints.**

**Latent Space Reasoning (LaST):** how LLMs can perform reasoning steps directly in latent space, achieving *better performance by using more compute* without generating unnecessary language tokens.

**Latent RL Optimization:** Developing reinforcement learning methods (e.g., Latent RL or HRPO) tailored for continuous latent reasoning rather than discrete output generation.

## Building Vietnamese Chatbot using LLMs and RLHF
![[Pasted image 20260421172840.png]]
1. Introduction to Chatbot? What is Chatbot using LLMs ?
2. How to fine-tuning LLMs for a Chatbot applications (conversation data).
3. How to improve response from a Chatbot (using LLMs) with RLHF ?
4. How to implement a Chat Interface for a complete Chatbot application ?

**RLHF workflow**
![[Pasted image 20260421172959.png]]

train LLM on vietnamese conversation data + improve model response to human preference using RLHF
![[Pasted image 20260421173041.png | 666]]

## Labs Practice (Focus Here)
**Basic Setup:** setup hugging -> ini model (using FastLanguageModel) -> apply QLoRA -> Load Dataset -> Preview Data -> Process Data -> SFT (Supervised Fine-tunning) -> Save Model -> Inference  (Practice Along - *Understand base code and workflow*)

**RLHF (Self-Study):** 
![[Pasted image 20260421173539.png]]
Ask Gemini to explain
![[Pasted image 20260421173711.png | 888]]

**OpenRLHF** - setup for Reward Model
![[Pasted image 20260421173808.png | 455]]

**RAY - Architecture**
![[Pasted image 20260421173931.png]]

**Building Chat Interface** - gradio + llamac++ and open-webui
1. vLLM with Gradio
2. Ollama with OpenWebui - [huggingface](https://huggingface.co/docs/hub/en/gguf)
![[Pasted image 20260421174102.png | 555]]
3. HF to GGUF (slide) 
	-> push to huggingface or github 
	-> run GGUF model -> run multi-model