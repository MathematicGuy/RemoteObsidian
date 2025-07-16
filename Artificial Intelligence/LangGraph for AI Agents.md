+ ? Use to create pre-define workflow for LLM like LangChain, but leverage Graph (with Node and Edge) to design complicated workflow for AI Agent

Workflow - perform repeated procedure to optimize result. 

- **Nodes:** Đại diện cho các bước hoặc giai đoạn trong quy trình hoạt động của agent. Mỗi node có thể là một **task** (công việc), **state** (trạng thái) hoặc **action** (hành động) cụ thể mà agent cần thực hiện. Ví dụ: "Chào người dùng", "Tìm kiếm thông tin", "Trả lời câu hỏi", v.v.
	
- **Edges:** Đại diện cho các kết nối giữa các node, xác định luồng di chuyển của agent. Edges có thể là **direct** (trực tiếp) hoặc **conditional** (có điều kiện), ví dụ "nếu điều kiện A đúng thì đi đến node X, ngược lại đi đến node Y".

**LangChain vs AutoGen vs LangGraph competition Framework**
+ **LangChain** is a base framwork, easy to learn.
	+ ! **Disadvantage**: limited in processing complicated procedure, not so powerful state management (still good), not optimized for multi-agent collaboration. 
	
+ **AutoGen** specialized for Multi-Agent and Conversation.
	+ $ **Advantage** Optimize for multi-agent collaboration, support natural conversation between agents, support .NET and Python.
	+ ! **Disadvantage** state management less powerful than LangGraph in processing complicated procedure, its *architecture focus on Converstation* doesn't fit for every app. 
	