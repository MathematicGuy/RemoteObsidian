_AI Engineering_ book offers a *framework for selecting tools.* Includes trade-offs between diff solutions and the question u should ask when evaluating a solution.

How to Consume a Long Book Method: 
+ **1:3 Ratio Method** - 1hrs reading  == 3 hrs practice. 
+ document mistake while studying
+ Constant Review - *reviewing 30 minutes after reading*, 1 day later, 3 days later, and 1 week later.

+ Preview the Chapters first to identify core concepts - Create Visual Mindmap - Write down your understanding.  

**Fast Reading Technique:**
+ Stop Sub-vocalizing - limiting the metal sound of word -> just read them subconciously.
+ Fewer Fixations - use peripheral vision to read multiple chars at once. 
+ Targeted Focus - set 50 Deep Focus then 10 minutes break.

---

+ $ This book Focus on the Framework rather than the nitty gritty detail.
	
	**[AI Engineering vs. ML Engineering](https://www.google.com/search?client=firefox-b-d&q=AI+Engineering+vs.+ML+Engineering&mstk=AUtExfBXJjh8oMAsOh4WXUejEuMXFlr90tUxK2N4r3G-FCp7Ds4xc0cRiKAmLaIdcun6fXpCFeumZCf7V7r04fqfJjIhizgEsofFcCX9Ezo8dFFCdgTK-t1ETmmsAWYi1aRxvgTc-VHIWqUzPEiDY7JS6sT7GQVTFdfKsGFMRQhtityPveM&csui=3&ved=2ahUKEwi_tqOM-4-UAxUGk1YBHZ1oFRcQgK4QegQIAxAC):** Understanding that AI engineering is *less about model development and more about adapting pre-trained models*, focusing on evaluation, infrastructure, and user experience.
	
	**[Comprehensive Evaluation Techniques](https://www.google.com/search?client=firefox-b-d&q=Comprehensive+Evaluation+Techniques&mstk=AUtExfBXJjh8oMAsOh4WXUejEuMXFlr90tUxK2N4r3G-FCp7Ds4xc0cRiKAmLaIdcun6fXpCFeumZCf7V7r04fqfJjIhizgEsofFcCX9Ezo8dFFCdgTK-t1ETmmsAWYi1aRxvgTc-VHIWqUzPEiDY7JS6sT7GQVTFdfKsGFMRQhtityPveM&csui=3&ved=2ahUKEwi_tqOM-4-UAxUGk1YBHZ1oFRcQgK4QegQIAxAE):** Learning how to *evaluate open-ended models using LLM-as-a-judge*, functional correctness, and similarity measurements.
	
	**[RAG and Agentic Systems](https://www.google.com/search?client=firefox-b-d&q=RAG+and+Agentic+Systems&mstk=AUtExfBXJjh8oMAsOh4WXUejEuMXFlr90tUxK2N4r3G-FCp7Ds4xc0cRiKAmLaIdcun6fXpCFeumZCf7V7r04fqfJjIhizgEsofFcCX9Ezo8dFFCdgTK-t1ETmmsAWYi1aRxvgTc-VHIWqUzPEiDY7JS6sT7GQVTFdfKsGFMRQhtityPveM&csui=3&ved=2ahUKEwi_tqOM-4-UAxUGk1YBHZ1oFRcQgK4QegQIAxAG):** *Best practices for retrieval-augmented generation (RAG) and designing agents* that plan, use tools, and operate autonomously.
	
	**[Model Adaptation Strategies](https://www.google.com/search?client=firefox-b-d&q=Model+Adaptation+Strategies&mstk=AUtExfBXJjh8oMAsOh4WXUejEuMXFlr90tUxK2N4r3G-FCp7Ds4xc0cRiKAmLaIdcun6fXpCFeumZCf7V7r04fqfJjIhizgEsofFcCX9Ezo8dFFCdgTK-t1ETmmsAWYi1aRxvgTc-VHIWqUzPEiDY7JS6sT7GQVTFdfKsGFMRQhtityPveM&csui=3&ved=2ahUKEwi_tqOM-4-UAxUGk1YBHZ1oFRcQgK4QegQIAxAI):** Knowing *when to use prompt engineering vs. fine-tuning,* including parameter-efficient methods.
	
	**[Inference Optimization](https://www.google.com/search?client=firefox-b-d&q=Inference+Optimization&mstk=AUtExfBXJjh8oMAsOh4WXUejEuMXFlr90tUxK2N4r3G-FCp7Ds4xc0cRiKAmLaIdcun6fXpCFeumZCf7V7r04fqfJjIhizgEsofFcCX9Ezo8dFFCdgTK-t1ETmmsAWYi1aRxvgTc-VHIWqUzPEiDY7JS6sT7GQVTFdfKsGFMRQhtityPveM&csui=3&ved=2ahUKEwi_tqOM-4-UAxUGk1YBHZ1oFRcQgK4QegQIAxAK):** Techniques to *make models faster and cheaper*, such as distillation and KV cache optimization.
	
	**[Productionization Hurdles](https://www.google.com/search?client=firefox-b-d&q=Productionization+Hurdles&mstk=AUtExfBXJjh8oMAsOh4WXUejEuMXFlr90tUxK2N4r3G-FCp7Ds4xc0cRiKAmLaIdcun6fXpCFeumZCf7V7r04fqfJjIhizgEsofFcCX9Ezo8dFFCdgTK-t1ETmmsAWYi1aRxvgTc-VHIWqUzPEiDY7JS6sT7GQVTFdfKsGFMRQhtityPveM&csui=3&ved=2ahUKEwi_tqOM-4-UAxUGk1YBHZ1oFRcQgK4QegQIAxAM):** *Strategies to detect hallucinations, mitigate security risks* like prompt injection, and manage data and model adaptation
	
![[Pasted image 20260428140126.png]]

**How much Effort should we put on Eval ?**
*Vertical Scaling* maybe improve from 80% Expected Gain (ur metric) to 82%, 85%. But building a new feature could Gain so much more *(Horizontal Scaling).* 
	AI Eval is important where failures have catastrophic consequences at scale. Else 80% is enough. 

**CS is about system thinking -** using coding to sovle actual problem. When AI solve more stuff, the problem just get bigger bc you might be solved all the small problem.  
	AI might fail at coding when the problem is at another problem Space. e.g. Coding Agent working at Module 1, but the issue require understading between Module 1 and 2 -> AI coudn't see and understand the problem -> Fail to resolve the issuse. 
+ ? ML Engineere built model themselve whereas AI Engineer use existing models to build product ? 

