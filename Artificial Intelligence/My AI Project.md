
**Project Name:**  Persent (Performance + Sentiment)
	Sentiment aim to improve ur performance
**Goal**
	Ult Goal: Optimize teaching performance for Teacher  
	Do what:  Detect Student Emotion compare to Lecturer teaching method.
	Product Function 
	 + Detect student sleepiness, Emotion base on lecture received in class. 
	 + Visualize Class data and each Student data to find the best teaching solution. 
**Input:** (Text , Number, pre-recorded video with faces, 30 images in 1 short video)
**Output:** 
- **Primary:** List of detected emotions with confidence scores or probabilities (e.g., "Happy: 85%, Surprise: 10%, Neutral: 5%").
- **Optional:**
    - Visual representation over an image or video to highlight where the emotion is inferred.
    - Summarized report of emotional content trends over time.

+ **Initiation**
	**Theory, Fomula**
		On theory, a camara will detect a student emotion and action and write a description about that student. Then it analyze the Description to return final result if that student is interested (want to pay attention) in the lecture or not.   
    + Focus Area: 
        + **Facial Expression Analysis:**
            + Facial Action Coding System (FACS): A system for classifying facial muscle movements related to emotions.
            + Deep Learning (Convolutional Neural Networks): Models specifically trained to recognize emotion patterns in images.
        + **Text-based Sentiment Analysis:**
	        + Natural Language Processing (NLP) techniques: Analyzing word choice, syntax, and context.
			- Sentiment lexicons: Dictionaries that assign emotional values to words.
			- Machine Learning (e.g., Support Vector Machines, Naive Bayes): Training models to classify sentiment based on text features.
	+ **Experiment**
		1) Data
			+ Facial: ex. FD-0001, etc..
			+ Text: Twitter datasets with sentiment labels, movie/product reviews, etc.
		2) **Preprocessing:**
		    - **Facial:** Face detection, alignment, normalization
		    - **Text:** Tokenization, stemming/lemmatization, removing stop words.
		3) **Model Selection:**
		    - **Facial:** Pre-trained models (e.g., on VGGFace, ResNet), or create your own CNN architecture.
		    - **Text:** Start with simpler models (Naive Bayes, SVM), consider more complex ones (LSTM, BERT)
		4) **Training:** Split data for training/validation. Experiment with hyperparameters.
		5) **Evaluation:**
		    - **Metrics:** Accuracy, F1-score, confusion matrix.
	+ **Conclusion:**   
		  
		- Summarize findings, strengths, and weaknesses of your model.
		- Discuss potential biases in the training data and how they might affect results.
		- Areas for improvement and future work.
		
	- **Libraries:**
	    
	    - OpenCV (facial image processing)
	    - NLTK, Spacy (text processing)
	    - Scikit-learn (machine learning)
	    - TensorFlow, Keras, or PyTorch (deep learning)
	- **Start Simple:** Begin with a basic model on one input modality (text or image) to establish a baseline.
	    + Emotion 
	- **Iterate:** Experiment and improve your model progressively.
+ [[What I need to learn for Emotion Detector Project]]

**Additional Considerations:**
- **Ethical Implications:** How will you address privacy and use the data responsibly?
- **Real-world Applications:** How this might be used in mental health, market research, or human-computer interaction.


**Application of AI**
**Very Practical:** Nhận dạng + Thống kê cảm xúc khuôn mặt
	Phân loại cảm xúc.
	Thống kê cảm xúc trên sơ đồ graph 
-> Từ đó đưa ra đánh giá và chiến thuật cải thiện việc giảng dạy trên lớp.
Input: video 2-4s
Cons 
Pros


**DBSCAN**
là dựa trên mật độ của dữ liệu. Các cụm là đc định nghĩa là các vùng dữ liệu có mật độ cao và kết nối vs nhau. Giữa các cụm là các vùng có mật độ thấp hoặc rất thấp.

Để xd đc các cụm. Thuật toán DBSCAN sử dụng 2 tham số. 
	MinPts
	Epsilon 
	Việc hình thành các cụm đc thực hiện như sau: Xuất phát từ 1 điểm bất kì của dữ liệu chúng ta sẽ có hình cầu bán kính epsilon.
	Đếm xem trong hình cầu đó có tổng số điểm dữ liệu. Nếu có thì kết nạp số điểm các hình cầu đó
	Lặp đi lặp lại qtrinh đó với các điểm ở trong cụm. Đến khi ko tìm đc điểm nào nữa thì thôi.


Các điểm còn lại ko thuọc 
Thuật toán DBSCAN có thể phát hiện các cụm có hình dạng bất kì.Phất hiện ra cả các bất thường trong dữ liệu. 
Nhược điểm: Độ phức tạp tính toán O(n^2)

Việc xd MinPts và Epsilon là ko dễ. 

Đếm xem trong số hình cầu đó >= MinPts
Ci = {x1, x2, x3, x4,..,xn}


Nêu các phương pháp đánh giá chất lượng của các thuật toán. Và đánh giá kết quả.

