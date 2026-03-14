When to apply Continual Learning - 1 Concepts per Section

**Argument:** if a system have good Embedding (good Classification) and Retrieval System. Is there a need for Continual Learning if we could just embed and retrieve data.
+ ? Continual Learning used when model Input Context alone isn't enough anymore.
+ $ Continual Learning is more ultilize for the Bigger Picture problem like LLM (neddle-in-a-haystack) 


**Continual Learning or Continual Fine-tunning vs RAG**
centralized, monolithic models 

**Question to ask before building a Continual Learning system ?**
Top Questions: *Is this system required long-dependency context* (e.g. long-converstation, stock prediction. timeseries dataset)
+ Is this systems required continual training for a model or not? 
+ Could this problem be solved using RAG alone

Do you want a ultimate model or a moduler systems ? 
*The problem is not could this system but SHOULD this system.*
DO this system require *periodic re-training ?* 
	Usecase: LLM task, needle-in-a-haystack

Clear Problems -> design system that could learn continually. 

### Continual Learning problems
Online Continual Learning for 3D Semantic Segmentation
Semantic segmentation in 3D point clouds (Sec. 3.1) and offline continual learning

### Three Key Research Directions in Continual Learning (continual learning problem types)
![[Pasted image 20260312180513.png]]
**Continual Learning (namely Continual Pre-Training)**
fine-tunning multi-model (MLLM) 
+ ! Data Drift in multi-model.

**Continual Fine-Tuning** 
continual fine-tune using online-data: CIL, TIL, DIL

**Continual Compositionality & Orchestration,**
MoE - finetune the router. 


**Disadvantages of Continual Learning**
+ ! Continuous learning is not portable - [what is so hard about continual learning](https://www.seangoedecke.com/continuous-learning/)
	Say you have Claude-Sonnet-7-continuous running on your codebase for six months and it’s working great. What do you do when Anthropic releases Claude-Sonnet-8? How do you upgrade ?
	.
	Everything your model has learned from your codebase is encoded into its weights. At best, it might be encoded into a technically-portable LoRA adapter,

---

**Research Question:** 
**Khi nào cần áp dụng Continual Learning:** Is this system required long-dependency context ? e.g. need LLM to solve needle-in-a-haystack problem, required to finetune 1 model continously (answered)
**Research Purpose:** build a system that could learn continually across ... 
**Key Research Direction:** 

**Mục tiêu** là có được 1 bài toán cụ thể (explicit research problems) 
	Mô tả bài toán càng rõ ràng

