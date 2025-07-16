**Problem for Agents:** 
+ Long-running tasks and accumulating feedback from tool calls
+ Agents often utilize a large number of tokens!
![[Pasted image 20250710082257.png# left | 543]]
**Probelm in LLM's Feedback** stack up each time you text ![[Pasted image 20250709152158.png# left]]
**Failures come from Longer context**  
+ **Context Poisoning:** when a hallucination makes it into the context.
+ **Context Distraction:** when the context overwhelms the tranining. (ngữ cảnh lấn át quá trình đào tạo - bias model)
+ **Context Confusion:** when superfluos context influences the response. (ngữ cảnh thừa thãi)
+ **Context Clash:** when parts of the context disagree. (ngữ cảnh ko đồng nhất)


`Cognition | Don't Built Multi-Agents`
+ ? Context Engineering is effectively the #1 job of engineers building AI agents. 
	_[Context engineering is the] ”…delicate art and science of filling the context window with just the right information for the next step.”_

Only passing tokens the LLM need to make the next decision
![[Pasted image 20250709160750.png]]

**Solution (Approaches)**
+ Save Context by **Writing Context outside** of the context window.
+ Select Context by **Pulling it into Context Windown**.
+ Compressing Context by **only retaining the tokens required to performe a task**. 
+ Isolating Context by splitting contexts to help an agent perform a task ????? WHY
![[Pasted image 20250710082914.png]]

As a human, when we 
