##### Viết Đề Xuất Nghiên Cứu Trong 2 Giờ, Không Phải Một Ngày!  

Với sự hỗ trợ của AI, bạn có thể soạn thảo một đề xuất nghiên cứu vững chắc chỉ trong vài giờ thay vì nhiều ngày. Đây là cách làm:

Giả sử, chúng ta cần viết một đề xuất nghiên cứu về NLP (Natural Language Processing), phân loại các bài đăng trên mạng xã hội.
##### Bước 1: Chuẩn bị ý tưởng nghiên cứu
- Mở Perplexity Comet, duyệt aclanthology.org và tìm kiếm các từ khóa "social media"
- Mở tất cả các bài báo trong các tab mới trong Comet. Bây giờ tôi có 40 bài báo để đọc qua, không phải thủ công, mà với sự hỗ trợ của AI!
- Chat với "Comet" bằng prompt: `Research all open tabs and give me 10 research questions about classifications of social media posts. Cite the sources.`
    

Lưu ý:
- Thêm nhiều từ khóa hơn nếu cần như GNN, multimodal, sentiment analysis, misinformation, disinformation, BERT, transformers, v.v.
- Duyệt thêm các nguồn như các bài báo hội nghị ACM NLP, Google Scholar, ScienceDirect, v.v. nếu cần.

##### Bước 2: Thu hẹp xuống 3 ý tưởng nghiên cứu
- Đọc qua tất cả 10 ý tưởng nghiên cứu từ Comet và chọn 3 ý tưởng mà tôi thích nhất.
- Tinh chỉnh thủ công 3 ý tưởng nghiên cứu để làm cho chúng cụ thể hơn.

Chat với Comet bằng prompt:
Suggest a research proposal title and abstract based on the following 3 research questions:  
1. [Refined Research Question 1]  
2. [Refined Research Question 2]  
3. [Refined Research Question 3]  
  

##### Bước 3: Chuẩn bị thư mục làm việc

Cấu trúc thư mục trông như thế này:

research-proposal/  
├── main.tex  
├── Makefile  
├── styles/. # User-defined LaTeX styles, overleaf templates, etc  
├── references.bib # Bibtex file for references with `abstract` field included  
├── refereneces/ # Downloaded papers go here, not mandatory  
└── samples/ # Sample research proposals in LaTeX format for reference  

##### Bước 4: Chuẩn bị `references.bib`

- Sử dụng Comet để trích xuất các mục Bibtex từ tất cả các bài báo mà tôi đã mở trong Bước 1.
    

Phép màu tiếp theo bắt đầu ở đây:

##### Bước 5: Viết đề xuất nghiên cứu

Mở `Cursor` và sử dụng prompt sau để viết đề xuất nghiên cứu trong một lần:

Help me write a research proposal.  
  
Save your response to `main.tex`  
  
Create a Makefile to compile the LaTeX document with targets:  
- all: compile the document  
- pdf: compile to PDF  
- clean: remove auxiliary files  
- bib: compile the bibliography  
- view: open the compiled PDF  
  
Title: {}  
  
Research questions:  
1. [Refined Research Question 1]  
2. [Refined Research Question 2]  
3. [Refined Research Question 3]  
  
The structure o the research proposal should include the following sections:  
  
- Background  
- Current Research Landscape and Related Work  
- Research Motivation  
- Research Questions: Include the 3 research questions above  
- Methodology  
- Requirements  
- Timeline  
- References: Use the Bibtex entries from `references.bib`  
  
Requirements:  
  
- Only cite the papers from the `references.bib` file, don't make up any citations.  
- Compiled PDF file should be less than 6 pages.  
- Tone should be formal and academic.  
- `Methodology` section should explain how I plan to answer the research questions.  
- `Methodology` section should include a diagram illustrating the research framework using LaTeX packages like `tikz`  
- `Requirements` section should list the hardware, software, datasets, and other resources needed for the research.  
- `Timeline` section should include a Gantt chart showing the timeline of the research activities over 36 months, with milestones and deliverables using LaTeX packages like `pgfgantt`  
- make sure `make pdf` command works without errors.  
  
Additional requirements:  
  
- Refer to `samples/research-proposal1.tex` and `samples/*.tex` for formatting and structure guidance.  

##### Bước 6: Humanize và hoàn thiện

- Humanize văn bản. Tôi sử dụng `stealthwriter` hoặc `naturalwrite`
    

- Đọc `main.tex` và thực hiện các chỉnh sửa cần thiết để cải thiện tính rõ ràng, mạch lạc, làm thủ công