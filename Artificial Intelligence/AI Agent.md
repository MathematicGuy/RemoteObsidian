Check Code for AI Agent ?  https://github.com/khanhnam-nathan/Pyneat
## LLMs Tools Calling 
### Agentic Tools (like Functions)
*@tool descrioption/context* (the text between `"""`). The agent uses this description to decide:
- **Whether to use the tool:** "Does this tool solve my current problem?"
- **How to call it:** "What arguments does it need?"
- **How to handle the result:** "What should I expect back (a list, a string, a dict)?"
-> So make sure your Description is Clear both in How to used it, What the Input and How to use the Output. 
	Think of Tool's output this way, Tool return its result to a Variable (e.g. result=tool()) so if you don't clarify the How the Agent could use the output, like human it would not know what to Extract.
![[Pasted image 20260515231133.png]]

### LLM Router - Intent/Comprehension LLM - like Decision Router (Understand)
Chuẩn hóa Cách Gọi Tools sử dụng MCP (Standard Tool Interface) - Từ Context để đưa ra Protocol (MCP Server có Tool cần dùng)
	Tool có thể là files, Database, Web APIs. 

LLM đóng vai trò Phân Tích Yêu Cầu (Request Classifier) - to direct itself to the Built-in tool. 
ToolCalling Instruction FT -> Teach LLM how to use tool efficiently. (Fine-tune for LLM to use Tool)
	kind of like RLHF and SFT.

demo ChatOllama `bind_tools` ![[Pasted image 20260515224718.png | 444]]

**Built in Tools** - 2 ways to use Tools. 
1st *JSON based Tool Calling* - from 3rd party API  ![[Pasted image 20260515230925.png]]
2nd *User-defined Custom* - you define the Format using *@tool Description.* ![[Pasted image 20260515230900.png | 555]]
**System Prompt for 3rd party Tool** ![[Pasted image 20260515231337.png]]
-> có thể dùng để hạn chế output, GIỚI HẠN tính năng của LLM. Đây là phần context, khi agent đã có tool trong phần code khác.

### Tool Calling Workflow (How to Call and Use Tool)
![[Pasted image 20260515231745.png]]

**1. How to get Tools and LLM**
LLM -> inference provider. 
Get Wolfram Tool for example, you login and get the APP ID> 
![[Pasted image 20260515231635.png]]


**2. Build Processing Function**
*Từng loại LLM sẽ tốt cho các bài Toán khác nhau* -> Tìm LLM có thể làm nhiệm vụ và gọi tool tốt nhấy. 
![[Pasted image 20260515231616.png | 555]]

How the Model understand and call the right Tool ? 
![[Pasted image 20260515231942.png]]

![[Pasted image 20260515232053.png]]

*Wolfram* ![[Pasted image 20260515231858.png]]

**3. Build LLM Built-in Tool Calling**
+ @ Trích Xuất Tool ccaafn dùng từ Output query của model.
![[Pasted image 20260515232250.png]]
Tool search có thể return về nhiều kq. 

Langchain have a database of Tool for you to use.
![[Pasted image 20260515233109.png]]

*Tool Raw:* Ngoài LLM thì *@tool* cũng có thể chạy từ hàm `invoke()` ![[Pasted image 20260515233303.png]]
*Bind Tool to LLM* - and invoke the LLM to use the tool. Note: You *could Inspect* which tool the LLM use from output result.  
![[Pasted image 20260515233347.png]]
![[Pasted image 20260515233505.png]]


### Tool Calling for Instruction Fine-tuning (Teach LLM how to Behave ie. use Tools) - SFT (finetune like normal)
[finetunning agent to use Tools dataset](https://huggingface.co/datasets/NousResearch/hermes-function-calling-v1)
![[Pasted image 20260515234344.png]]


### Tool Calling for Vision Task
![[Pasted image 20260515224913.png | 666]]
Define Tools -> Define System Prompt (YOLO for Object-Detection and SAM for Segmentation)
![[Pasted image 20260515235429.png | 777]]
![[Pasted image 20260515235448.png]]

Define Tool as JSON ??? ![[Pasted image 20260515235543.png]]
3. Define system prompt so the SLM Specialize only in Tool Calling. 
![[Pasted image 20260515235555.png]]

Output Example
![[Pasted image 20260515235647.png | 666]]

