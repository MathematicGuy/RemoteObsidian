10. Nghiên cứu, xây dựng trợ lý ảo cho tạp chí khoa học có tích hợp học máy
https://github.com/DAIKOOH12/bot_rasa
https://sites.google.com/a/ctu.edu.vn/luu-tien-dhao/chatbot
https://www.miai.vn/2019/09/03/rasa-series-1-ai-cung-co-the-lam-chatbot-sieu-ngon-khong-lo/
https://github.com/thangnch/AI_Voicebot

# System Design
**Virtual Assitant:** 1 Chatbot for PDF Analysis, 1 Chatbot for finding document.
**MongoDB/SQLServer:** Read & Write Data.
**VD:** người dùng muốn tra cứu tài liệu về SVM, hệ thống sẽ trả về các tài liệu liên quan đến SVM.
**s** Lamdma/RASA


## RASA Python Chatbot Development Beginner Tutorials
![[Pasted image 20240805130507.png]]

### Data folder
**nlu file** -> training data for the chatbot
	for bot to undertstand words intend (meaning of the word) using nlu
+ ? RASA NLU is the interpreter which processes the user input and identifies the intents and extracts the entities from it.
**rules file** -> make the rule for the chatbot
	Example: the bot say goodbye when I said goodbye
		![[Pasted image 20240805125731.png]]
**stories file**: allow user to modify the how chatbot interact given a story using intent and action.

### How to train Model





# Mastering RASA: Entities, Slot and Custom Actions Explained 


**Slot:** Store Conversation Data for Longer Period of Time.  (for later access)
**Entities:**  (like City, New York) Can train the Entity using RASA Training Entity.
