Goal - Design a MVP AI System
	RAG must be production-ready - what are a Production Ready System.
	Decision and safety layers are critical

*Video Turtorials & Guides:* 
+ [[AI Agent System]] - [AI Agent System](https://youtu.be/CyLYY_xb5bQ?si=vd_y2X2P0laU6exl) (Understand the Whole System)
+ [[AI Coding]] - [Workflow for AI Coding (Essential)](https://www.youtube.com/watch?v=-QFHIoCo-Ko) 
+ [[Building in a World of Slop]] (Minimal AI Agent TERMINAL that SAVE TOKEN) - [pi](https://pi.dev/)
+ [[How to Design a AI Agent System - RAG, Vector Database, Evals, Function Calling]]

*AI Engineer*
+ [[AI Engineer by Chip Huyen]] - 800 pages book intro to AI Engineer

*How to use Coding Agents:* 
+ [[No Vibes Allowed - Solving Hard Problems in Complex Codebases]] - [author docs](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/ace-fca.md) 
	Problem - How to use Coding Agent in Complex and Large Codebase
	"frequent intentional compaction" - keeping utilization in the 40-60% range, and building in high-leverage human review at exactly the right points.
	Context Compression for Large & Complex Codebase
	Code Review for Mental Alignment and its should be Simple
+ [[Software Fundamentals Matter More Than Ever - Matt Pocock]]
	How to vibes coding efficiently  - how to vibe code what you want by Understand the main vibe coding problem:
	P1: Noboday know what they want -> have the LLM askes relentlessly about every aspect of your requirements to your metal model is align with the LLM.
	P2: Ambiguous Terminologies -> define a `ubiquitous_language.md` -> avoid confusion and miss understanding. Like how Dev and Domain Expert.
	P3: Code/Question that doesn't work/good -> Have a feedback loops (Human define the problem)
	P4: Coding Agent doing too much -> TDD (Test Driven Development) -> Take small feedback. Never take on a task that's too big
	P5: AI doesn't understand my code -> Good Codebases are EASY to Test and Verify -> apply Deep Modules but *SIMPLE INTERFACE.* 
	P6: Too much code ->  Design the interface but not gonna review the implementation (code) too much. As long as you have a testable boundary around it.

*Interview Questions:*
+ [LLM Interview Questions and Answers Hub](https://github.com/KalyanKS-NLP/LLM-Interview-Questions-and-Answers-Hub)
+ [RAG Interview Question](https://github.com/KalyanKS-NLP/RAG-Interview-Questions-and-Answers-Hub)

### 3-Part of RAG Interview Framework
**What is RAG ?**  Retrieval Augment System from Internal Data sources 
**RAG System Types of Questions**
	`[problem]` + `[constrain]` + `[current resource]`.
	Đưa ra giải pháp, cho biết lý do và giải thích vì sao lại chọn thiết kế đó ? 
	Giải thích RAG Framework 
	Giải thích RAG Modules (các Method trong mỗi RAG Modules)
	Nêu ra các bước để cài đặt giải pháp 
[Types of RAG Framework](https://github.com/ApexIQ/RAG-types-of-RAGs/tree/main)


**RAG Workflow Guideline** - [VN AI Blog](https://aichatbot.com.vn/di-tim-cach-trien-khai-tot-nhat-cho-rag/#:~:text=C%C3%A1c%20k%E1%BB%B9%20thu%E1%BA%ADt%20RAG%20(Retrieval%2DAugmented%20Generation)%20%C4%91%C3%A3,%E1%BA%A3o%20gi%C3%A1c%20v%C3%A0%20n%C3%A2ng%20cao%20ch%E1%BA%A5t%20l%C6%B0%E1%BB%A3ng) - [Arxiv Source](https://arxiv.org/html/2407.01219v1)
![[Pasted image 20260428175518.png | 777]]
	[Example RAG project by Ba Ria Vung Tau University](http://thuvienso.bvu.edu.vn/bitstream/TVDHBRVT/21097/1/Le-Quoc-Khanh-20LT.pdf)

#### 0st. Data Assessment (data quality inspection)
**Data Quality:** Checking for completeness, accuracy, and consistency.
**Data Preprocessing Needs:** Identifying steps for *cleaning, transforming, and normalizing data* to be suitable for AI models. e.g. into a JSON/HTML format.
**Data Storage Solutions:** Determining the best storage solutions, such as cloud databases or data lakes, to manage large datasets efficiently. I dunnu. 

#### 1st. Knowledge Layers 
For storing Internal docs and privates sources
Vector database for semantic search
Metadata-based filtering

#### 2nd. Retrieval Layer
Query embedding
Retrieval method
Domain and Access filtering (Retrieve only the domain knowledge)

#### 3rd. Validation Layer -> where RAG become enterprise RAG
Citation source -> Confidence Scoring -> Knowledge-based validation before output

#### Enterprise Design Example
Incident remediation knowledge base
Agent retrieve runbooks and operational docs
Validation ensures safe remediation suggestions

#### Interview Keyword Lines
Validated retrieval not just plain retrieval
Internal knowledge with security controls
Citations and confidence scoring
Human approval for high-risk tasks

#### Architecture Flow Explaination
User request
LLM plans retrieval steps

---

