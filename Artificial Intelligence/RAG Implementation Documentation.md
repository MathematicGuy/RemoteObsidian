**Steamlit -** require no Front End experiment. Streamlit already handle front-end aspect with predefined layout so you can focus on developing your AI app and testing model.  
	Additionally Streamlit allow:
1. **Automatic Update Script** (like Live Server for HTML)  
2. **Built-in Backend:** Streamlit handle all the BE work like API, adding widget is the same as declaring variable. 
3. **Deploy Instantly** Deploy app for free using Streamlit.. 

[Streamlit Input Widget Docs](https://docs.streamlit.io/develop/api-reference/widgets)
[Streamlit Chart Docs](https://docs.streamlit.io/develop/api-reference/charts)
[Streamlit App Template](https://streamlit.io/gallery)
[Langchain Structure Output Methods](https://gmnithinsai.medium.com/structured-output-llm-routers-in-langchain-da26987b641a)

Streamlit multi-pages web structure:
![[Pasted image 20250627112723.png# left |200]]

Hệ thống có khả năng giải thích 1 câu hỏi đơn lẻ.  
Nhưng thiếu khả năng so sánh các thông tin chính xác với nhau. Hay truy vấn trên 1 thông tin. 
Ví dụ:
	Module Retrieval có vấn đề khi nó không thể truy vấn đúng thông tin cần thiêt đối với TỪ có cấu trúc giống nhau như 1NF, 2NF, 3NF -> Retrieval nhận diện cả 3 gần giống nhau. 

**Dataprep:** huấn luyện LLM để đảm bảo đầu ra output đưa ra luôn đúng định dạng. 

**Enum datatype (like python enumeration):** a special datatype that enable for a variables to be a set of predefined constants. If  initiate days in week as string, they will have value from 0 to 6 by default if not assigned. 
![[Pasted image 20250806145917.png| 544]]

