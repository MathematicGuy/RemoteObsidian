[Learn how to Design and Build RAG](https://www.youtube.com/watch?v=ZREt9MAozho)
[AI System Design](https://www.youtube.com/watch?v=CyLYY_xb5bQ)
[How to choose an LLM](https://www.aihero.dev/how-to-choose-an-llm)
[RAG System Variant](https://medium.com/@kyle.zarif/designing-rag-systems-patterns-tradeoffs-and-code-examples-95c33a8b2df7)
[How agentic search helps AI understand long documents](https://www.outerport.com/blog/agentic-search)
[Saas Template to launch your app faster (Supabase, NextJS)](https://youtu.be/ad1BxZufer8?si=WAU2astuipWpwt63)
**RAG System Types of Questions**
	`[problem]` + `[constrain]` + `[current resource]`. Đưa ra giải pháp, cho biết lý do và giải thích vì sao lại chọn thiết kế đó (so sánh với các thiết kế khác) ? 
	Câu hỏi khá đa dạng -> dựa vào nền tảng rồi tự đưa ra đánh giá và thiết kế 

---
### Detail Example
![[Pasted image 20260428173636.png]]
CSAT - customer satisfaction score
p50, p95 < 1s - response rate for `X%` customer below `t` second. 
have a DB for frequently asked question  

Define list of tools and API in somewhere else.
Policy and Guardrails -> Check if the requirements fit with the policy.
How to track CSAT, p50 metrics across the systems.

**CRUD with Relational DB**
![[Pasted image 20260428182519.png]]
**Looping to Human:** Delegate most task to LLM. But Emotional Support for HUMAN. 
![[Pasted image 20260428182541.png | 400]]
Agent Function Calling 
![[Pasted image 20260428182718.png | 400]]

*Tools and APIs Asernal*
![[Pasted image 20260428182816.png | 400]]



**Final Overview**
![[Pasted image 20260428182315.png]]



![[RAG System Design]]

