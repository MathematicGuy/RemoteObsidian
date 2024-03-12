**Target:** Xây dựng hệ thống thi code hỗ trợ chấm điểm tự động bằng chatGPT có kết hợp với người đánh giá.

Building a code exam system that supports automatic scoring using chatGPT in conjunction with reviewers.

---
- [ ] Find a way to help Xuan become the Chief so I can get more Reasearch Time. (Long Term Project + Team Benefit)
	+ Convert my Main Ideas and Strategies to Xuan
	+ Give Xuan the Why and Motive to do this.


Similiar Project: 
+ https://www.codegrade.com/

[[Science Research User Requirement]]
+ Todo: Lập 1 kênh đê các bạn báo cáo tình hình

[[Science Research - Design and Recommended Languages]]

Hải làm Activity Diagram dựa trên Screen Flow Diagram + Youtube Demo Video


### [[Simplified User Workflow]]


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


### Project Phrase
Thử Plan, Build 1 Dự Án Nhỏ để làm Demo.


+ ! **1. Project Initiation**

- **Problem Definition:** Clearly outline the problem the project intends to solve. **What pain points does it address, and for whom?** (giải quyết những điểm khó khăn nào, cho ai?)
	Outline what we don't understand and problems we have 

- **Goals & Objectives:** Define specific, measurable achievements that indicate project success.
	Identifying Goals of each Phrase


- **Scope:** **What features are essential (must-haves) vs. those that would be nice**, but not critical (nice-to-haves).
	Define features: Must have, Nice to Have
(Huy + Nhật)


- **[[Stakeholder Identification]]:** List out individuals or groups impacted by the project (users, managers, other teams, etc.).



+ ! **2. Planning**

- **Requirements Gathering:** Detail the specific functions the software must perform. User interviews, surveys, and observation can be vital here.


- **Technical Design:** Choose technologies, architecture patterns, and outline the overall structure of the system.
	+ Programming Language, Design pattern (Agile, Water Fall, etc..), Software Architecture (Use Case, Activity Diagram, User Flow, etc..)
	+ Project Folder Design, Work Flow, etc.. 


- **Resource Allocation:** Budget, team member roles, hardware/software needs,
	Assign Role
	Any Paymement


- **[[Science Research Project - Risk Assessment]]:** Identify potential roadblocks (technical, timeline, etc.) and devise mitigation plans.
	Find out potential Risks from team, code, phrase, etc..

- **Timeline & Milestones:** Create a schedule with key deadlines and deliverables
	Key Dealine + Milestones



**Project Management Tool**  
- **Git + GitHub:** Handles version control and basic collaboration. **(Trello but better)**
	
- **Discord:** For day-to-day team communication.
	
- **Trello:** To manage tasks and see who's working on what. **(temporary)**
	
- **Good README Files:** Emphasize clear documentation from the start.

**Technology & Framework**
+ FE
	HTML, Tailwind CSS, React.js
+ BE
	ASP.Net 




