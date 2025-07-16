### [[RAG Road Map]]
### [[RAG Summarize]]
### [[Model in RAG (NLP and DL)]]

### [[Common Problems in RAG Systems and Their Solutions]]

### RAG Frameworks and Tools
+ [[RAG system in Production]]
+ [[Multimodel RAG]]
+ [[LangGraph for AI Agents]]

### [[LangChain]]

### [[RAG Implementation Documentation]]

### [[Context Engineering]] (NEW)


**Code:**
+ [Multi-Model RAG](https://colab.research.google.com/gist/alejandro-ao/47db0b8b9d00b10a96ab42dd59d90b86/langchain-multimodal.ipynb#scrollTo=91106e31)
+ [RAG Multiple Choice](https://colab.research.google.com/drive/1KtWMSZP_sEifMIJ63eBYk3aWqgNyvN30#scrollTo=sDF9UemkiM9t)

### Tools: always ask what problems do they solve ? 
[[LangChain]]
[llm prompting website](https://learnprompting.org/docs/basic_applications/mc_tutorial)

**Langchain:** provide basic components for a AI application. (e.g. API connection between model, Prompting, human to model Responses).  
![[Pasted image 20250618070959.png| 600]]
**LangGraph:** Allow dev to make prototype for AI application.
**LangFlow:** Workflow for Multi-Agent.
**LangSmith:** provide testing environment at all stages of development. Very detail and coherent debug enviroment. Allow you to track and trace every step.

---
**AIO RAG Goals:**
+ Improve retrieval and searching speed using FAISS
+ Customize prompt for 
	+ Whole PDF file Summarization 
	+ Multiple-Choice Question in json format,  
	+ Create HW base on given pdf (finish later) 
	
**Latex Docs Outline** (để viết đc outline, phải hiểu căn bản của từng thành phần lớn nhìn từ Top Down)
 1) Giải thích tổng quan mô hình RAG. 
+ Giải thích từng RAG's Components sử dụng ngôn ngữ trừu tượng (i.e. tiếng người)
+ Liệu kê những vấn đề tồn tại khi xây dựng mô hình RAG và giải pháp cơ bản của Native RAG, giải pháp LangChain đưa ra là gì ?   
+ Giới thiệu Langchain, vai trò của nó trong việc xây dựng RAG.
+ Giải thích căn bản về các syntax của Langchain. 
+ Giải thích "giải pháp của Langchain cho từng vấn đề tồn đc tại đề cập ở trên"
+ Demo kết quả mô hình RAG cơ bản. 
+ Phần Cải Thiện: 
	+ Prompting có  Structure 
	+ Các kiểu Prompt khác nhau
	+ Cuối cùng là cải tiến tốc độ truy vấn sử dụng FAISS. 
	
+ Tổng kết lại toàn bộ 
+ Kết Thúc 

---
**RAG Jargon**
+ "**Parse**" mean
	+ is the process of **turning one form of data** (usually a string of text or numbers or whatever) **into a meaningful data structure** (simple as that). 
		+ ? Example: to analyze and break down a string of text, code or data into smaller, meaningful parts (tokens) according to a set of rules (grammar) 
		
	+ Convert information into something understandable for human or machine, in programming its mean converting information in 1 form into another form that's easier to work for computer.  
		+ ? [e.g.](https://www.quora.com/What-exactly-does-parsing-mean-in-programming) To a computer this has no meaning, it is a '4' then a '+' then a '1' then a '0'. For the computer to perform the calculation it must first parse this expression and understand the calculation to be performed. A parser program would identify the '+' as meaning addition and from this it knows that the symbols it saw in front and after this '+' should be numerical digits and represent the two numbers to be added together. It will then make a new structure to represent this information better for the next part of the program to understand so "4" becomes the binary number 100 and "10" becomes the binary number 1010 and "4+10" becomes something like this: ADD 100 1010.
	
+ "**Protocol**" is a set of rules that governs how data is transmitted and received in a network (within devices or programs) ensuring they (i.e. the data) can communicate effectively. 
	
+ **Synchronous vs Asynchronous** often misleading because they *relate to Time Coordination, not necessarily Execution Flow in programming* (Tóm lại là Asynchronous không bắt đầu và kết thức 1 cách đồng thời)
	
	+ *Synchronous programming* (One at a Time) *in programming context, the start of one task is synchronized with the completion of the previous task* They happend in rigid, coordinated sequence. 
		+ $ operation execute task one by one, each task must complete before the next one can begin. 
		
	+ *Asynchronous* (Concurrent Task) in programming context, the start of one task is not synchronize with the completion of another task. They can overlap in their execution. 
		
		+ $ Operation in programming *allow a program to continue execute other tasks while waiting for another task to complete* (often long-running operation) without blocking the main thread.
		+ ? Note that when running Asynchronous in a single thread its just the single thread switches between different tasks creating the illusion of parallelism. 
		+ $ Benefits of Asynchronous mainly get recognized in User Interface. 


**Full-Stack RAG Web App Architecture Overview**
![[518011308_1297923515669551_604386552809920044_n.jpg]]

