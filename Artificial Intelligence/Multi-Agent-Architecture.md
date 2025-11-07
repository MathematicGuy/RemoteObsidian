**Multi-Agent System (MAS)** là kiến trúc nơi nhiều agent hoạt động độc lập nhưng cùng hướng đến một mục tiêu chung, thường là thông qua giao tiếp, phối hợp và chia sẻ tri thức.

Trong AI, đặc biệt với LLMs và RAG, ta có thể tổ chức mỗi agent như:
- Planner: Phân tích task & phân chia công việc
- Retriever: Truy vấn tri thức
- Critic: Đánh giá kết quả trung gian
- Executor: Thực hiện hành động cụ thể
- Memory agent: Quản lý tri thức hoặc trạng thái của các tác vụ

Dưới đây là một flow thực tế cho một hệ thống RAG-based AI Agent sử dụng kiến trúc 
User Prompt
   ↓
🧭 Task Planner Agent
   ├──> 🔍 Retriever Agent (truy xuất từ vector DB)
   ├──> 🧠 LLM Agent (viết câu trả lời từng bước)
   └──> 📦 Memory Agent (giữ state giữa các vòng hội thoại)
   ↓
🧑‍⚖️ Critic Agent (đánh giá output, phát hiện lỗi logic)
   ↓
🏁 Final Answer trả về User

----

1) Plan: multi-query -> simplified query
2) Retrieve -> dynamic for text, image + text, etc..
3) Refine -> rerank initial result for best evidence 
4) Reflect -> agent summarize finding and update its research history for revision (cumulative understand of the problem)
5) Critique: a policy agent inspects revision history -> decide to continue the current research step or not, revise its plan if it hits a dead end or finish. 
6) Synthesize -> Summarize result, gathered evidence from all src into a single file, comprehensive and citable answer. 
