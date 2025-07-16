**CODE Streamlit chatbot**
File code chính:
+ `rag_chatbot2.py` -> Prompt tạo sinh Câu trả lời trắc nhiệm
+ `rag_chatbot.py` -> Prompt tóm tắt nội dung truy vấn
Chạy code trong terminal:
```python

streamlit run rag_chatbot2.py
```

File code kết nối với code chính để xử lý các task khác nhau:
+ `load_llm.py` -> tải và khởi chạy mô hình Embedding và mô hình LLM.
+ `process_file.py` -> giúp upload files (pdf, zip file, file từ github, docx, excel) và 1 hàm truy vấn Text tự viết. 
+ `prompts` -> lưu các prompt khác nhau để sử dụng và thử nghiệm về sau. 
+ `requirements.txt` -> các thư viện cần thiết cho web app RAG. Tải trên môi trường Anaconda. 


**Cấu trúc Files của Blogs**, gồm **2 folder chính:**
```txt
content
	post
		2025
			Module1
				Week1
					index.md
				Week2
					index.md
				Week3
					index.md
				Week4
					index.md
```

e