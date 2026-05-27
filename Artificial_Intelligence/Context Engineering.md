reference source: https://mirror-feeling-d80.notion.site/Context-Engineering-for-Agents-21f808527b17802db4b1c84a068a0976


+ ? LLM is like the CPU and its Context Windown is RAM. How can we optimize so that only important information get feed into the LLM. Context Engineer allow u to reduce the scope from everything else to what you only want.
+ $ Describe the context so good that the AI can have the same awareness as human. By defining its:
	+ **Define Tasks** the Agent should do. What to do step-by-steps.
		![[Pasted image 20250804104348.png| 433]] 
		![[Pasted image 20250804104415.png| 233]]
	+ **Input** (where does the input comming from, type of inputs)
	+ **What the Output** should contain which include the Output format e.g. bullet point 
	![[Pasted image 20250804104308.png| 333]]and Output Constaint e.g. limit to 300 tokens
	![[Pasted image 20250804104228.png| 244]]
	+ **Information Constrain:** what to focus on 
	![[Pasted image 20250804104638.png| 344]]
	+ **What to AWARE ?** Capability and Reminder, telling the Agent what are the different tools and knowledge bases that it have access to. And telling its reminder.
	![[Pasted image 20250804105055.png| 344]]


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
