**Đinh Nhật Thành**

**Role: Backend System, Frontend**

Xây dựng hệ thống thi code hỗ trợ chấm điểm tự động bằng chatGPT có kết hợp với người đánh giá.

Building a code exam system that supports automatic scoring using chatGPT in conjunction with reviewers.


Frontend (HTML, CSS, JavaScript) to create the exam interface.

Backend (Node.js, Python/Flask, Django, etc.) to handle server-side logic, user sessions, and database interactions.

Similiar Project: 
+ https://www.codegrade.com/


**Simplified User Workflow**

1. **Exam Setup:**
    
    - Instructors create exams with multiple questions (open-ended coding tasks, problem-solving with code snippets, etc.).
    - They set guidelines for both ChatGPT and human reviewers (what aspects to score, level of feedback detail).
    
2. **Candidate Takes Exam:**
    
    - The system presents questions and a code editor interface.
    - Candidates submit code solutions for each question.
    
3. **Automated Scoring (ChatGPT Stage)**
    
    - **Execution:** The system attempts to run the submitted code (with test cases if applicable).
    - **ChatGPT Analysis:** Submitted code is sent to ChatGPT with carefully crafted prompts that guide it to provide:
        
        - Functionality assessment (Does the code solve the problem?)
        - Efficiency suggestions (Are there simpler, more optimized approaches?)
        - Style & Readability Critique (Is the code well-organized, does it follow good practices?)
        
    
4. **Human Reviewer Stage:**
    
    - Reviewers access submitted code alongside ChatGPT-generated analysis.
    - They use interface tools to add ratings based on pre-defined criteria (correctness, time complexity, special focus areas).
    - Reviewer input:
        
        - Confirm or amend ChatGPT feedback
        - Offer more tailored suggestions specific to the candidate's skills or common pitfalls
        
    
5. **Score Presentation & Feedback:**
    
    - System compiles a final score based on automated scores and human input.
    - This is presented to the candidate with both ChatGPT's initial feedback and the reviewer's annotations.
    

demo: https://youtu.be/bIHyktT_GGs?si=Xg7Bfoe-NDHPN0ZS


**Behind the Scenes: Technical Aspects**

- **Server-Side Logic:** Handles question/answer storage, submission tracking, and routing code submissions to ChatGPT for analysis.
- **Test Case Execution:** Automated test cases (provided by the instructor) verify if submitted code produces the expected outputs.
- **NLP Prompts:** The core challenge and creativity of this system lie in how you prompt ChatGPT to analyze code. Example types of prompts:
    
    - "Does this code function correctly? If not, explain the error."
    - "Suggest two ways to improve this code's readability."
    - "Is this code bot generated"


**Caveats** (lưu ý)

- **Complexity:** A full-fledged system like this is a significant project. Start with a smaller proof-of-concept then iterate.
- **ChatGPT Evolves:** OpenAI may shift their models, requiring prompt adjustment and system tweaking.
- **Security:** Take meticulous precautions preventing exam content leaks and cheating attempts.