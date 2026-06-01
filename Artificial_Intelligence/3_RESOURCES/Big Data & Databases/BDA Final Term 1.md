### Topic and Requirements
**Phân tích dữ liệu giáo dục (Phân tích tỷ lệ hoàn thành khóa học trên các nền tảng học trực tuyến**, Xác định các yếu tố ảnh hưởng đến kết quả học tập, Đánh giá sự hài lòng của học viên dựa trên phản hồi, …)

**Sản phẩm:**
- Báo cáo (định dạng .pdf) trình bày chi tiết kết quả thực hiện đề tài (có bảng phân công công việc của nhóm).
- Tệp tin nén gồm **dữ liệu,** **code**, và **hướng dẫn sử dụng** (nếu có) 
- **Slide** thuyết trình **(10-15 slide)** 
+ ! Chỉnh sửa bìa của báo cáo sau cùng

### Document
1) **OVER VIEW (Analysis and Solution Proposal)** 
	- State the problem clearly
	- State possible solutions and tools
	- Select solutions and tools: analyze advantages and disadvantage and reasons for choosing the solution. 
	
2) **METHODOLOGY (Solution Implementation)**
	+ State specific analysis requirements 
	+ Analyze implementation step and introduce used tools.
	+ Review program method and Evaluation result
	
3) **EXPERIMENT AND RESULT EVALUATION (Evaluation)**
	- Evaluation result discussion and difficulty encounter
	
4) **CONCLUSION AND FUTURE WORK**:
	+ Improvement Recommendation. Conclude pratical applications from evaluation result. 
	
+ appendix

## Dataset
+ ? [Online Course Student Engagement Metrics](https://www.kaggle.com/datasets/thedevastator/online-course-student-engagement-metrics) is a gold mine to analyze student behaviour, engagement and performance in online courses. 

| Column name           | Description                                                                                                 |
| --------------------- | ----------------------------------------------------------------------------------------------------------- |
| **registered**        | Indicates whether a student has registered for a particular course or not. (Boolean)                        |
| **viewed**            | Indicates whether a student has viewed the course content after registration. (Boolean)                     |
| **explored**          | Indicates whether a student has explored the course content beyond just viewing. (Boolean)                  |
| **certified**         | Indicates whether a student has successfully completed and received a certificate for the course. (Boolean) |
| **final_cc_cname_DI** | The country of the student. (String)                                                                        |
| **LoE_DI**            | The level of education of the student. (String)                                                             |
| **YoB**               | The year of birth of the student. (Integer)                                                                 |
| **gender**            | The gender of the student. (String)                                                                         |
| **grade**             | The final grade of the student in the course. (Float)                                                       |
| **start_time_DI**     | The date when the student started the course. (Date)                                                        |
| **last_event_DI**     | The date of the last event the student participated in the course. (Date)                                   |
| **nevents**           | The number of interactive actions a student had within the course. (Integer)                                |
| **ndays_act**         | The number of days a student was active in the course. (Integer)                                            |
| **nchapters**         | The number of chapters a student interacted within the course. (Integer)                                    |
| **nforum_posts**      | The number of posts a student made on the course forum. (Integer)                                           |
| **roles**             | The role of the user in the course (e.g., student, instructor, staff). (String)                             |
| **incomplete_flag**   | A flag indicating if there is any missing information in the student's record. (Boolean)                    |
+ @ Understand more about each data field in [[Student Engagement Metrics Survey]]  

This data set support Education Research, help researchers understand trends in online education.
+ ? There are **2 research path way**: 
	
	+ **Student Demographics:** with attribute like Year of Birth (YoB), Leval of Education (LoE_DI), Gender and Country of the Student (final_cc_cname_DI) - researchers can take challenge for demographics based analysis. 
	
	+ **Student Engagement:** Use metrics like numer of forum post (nforum_posts), number of days the student was active/enfated with course content (ndays_act), whereas its number of content student explored or viewed before registration  (view and explored flags) and **how many chapters they interacted with during their engagement period** (nchapters)

### Visualization Projects
+ Visualize demographic distribution
+ Create **engaging visuals** showing **correlation between different fields** such as **Level Of Education vs Grade obtained**
+ **Factors contribute most towards completing a course.** (PCA)

+ ? Take note of temporal patterns like when do student start a course, when are they most active throught time-series and more?
+ $ Always remmeber, the **first step before start any dataset is understanding it**. Thoroughly go **through each data fields to question its purpose and its relevance to your project.**   


### Predictive Modeling

+ **Predict Course Completion:** using attributes such as level of education, registration status (is regis and is follow and is performce well), engagement timelines and distribution (time and day student engage the most, average engagement time to complete a course, etc..). We could predict of student are likely to finish a course. The *'certified'* fied indicates whethere a student have complete a course can be use as a label for supervised learning model training. 

+ **Perdict Performance:** features indicate user interactions like 'nevent', 'nchapters', 'ndays_act' could indicate user engagement which can help predict if student score higher grades (*'grade'*)


## Problem & Method: Predict Course Completion Rates (descriptions and tools)
+ ! **Problem Identification:** We observe a major issue with **student course completion rate**. Many students attend courses but do not complete them. The underlying issue is unclear making it challenging to enhance student engagement or improve completion rates. 
+ ? **Resolution:** We aim to address this by performing a comprehensive analysis of student demographic and engagement patterns to accurately predict which students are likely or unlikely to complete a course, thereby providing additional insight to improve student retention and completion rate. 

+ $ **Propose METHODOLOGY Involves:**  
	1) **Data Understanding**
		- Examine each attribute's meaning and relavance 
		- Identiy missing or inconsistent data
		
	2) **Exploration Data Analysis** (EDA):
		- Visualize demographic distributions (age, education, country)  
		- Examine correlations (engagement vs completion)  
		- Analyze temporal patterns (when students engage the most)
		
	3) **Feature Engineering:**
		- Create meaningful metrics (e.g., days between start & last event)  
		- Aggregate interaction metrics (e.g., interactions per active day)  
		- Encode categorical variables (e.g., country, education level)
		
	4) **Machine Learning Model Development:**
		- Logistic Regression (baseline)  
		- Random Forest (interpretability)  
		- Gradient Boosting (accuracy)  
		
	5) **Model Evaluation and Validation:** 
		+ Accuracy, Recall, Precision, F1-score, ROC-AUC to select the best performing model for deployment.
		+ Cross-validation & tuning for robustness
		
	6) **Interpretation & Actionable Insights**
		+ Identify most influential features (e.g., using SHAP values)  
		- Provide recommendations to enhance student completion


---

### [[BDA Final Term Steps]]

### [Main Steps in Data Analysis Process](https://careerfoundry.com/en/blog/data-analytics/the-data-analysis-process-step-by-step/)
Before analyze any problem in Machine Learning, it critical to understand and have insight about your data. First we cover how to define your goal, collect data and carry out an analysis.  
1) First and formost, what do you want. **Define the Questions**
2) Second, what do you need. **Collecting the Data**
3) Third, how you need them to be. **Cleaning the Data**
4) Forth, what do potential do you see (in the data). **Analyzing the Data**
5) Fifth, is your result authentics. **Sharing your results**
6) Sixth, what more can you offer. **Embracing failure**
7) Seven, you done well, look back. **Summary**

**Insight & Visualize Step**
**Step 1:** Turn Raw data into Visualized Data to visualize trend, behaviour
**Step 2:** Tell a Story (For when revenue go up ask yourself  why is that)
**Step 3:** Break down the metric (down to it fomula)
![[Pasted image 20250327080840.png]]
+ ? By visualize that way, we can see Q3 growth is depend on ...number of units sold, since selling price have remain the same over the years.  

note: Remember all column name and re-explain each column to understand and get deeper insight. 

![[Pasted image 20250330163532.png]]

----
### Resources
+ [Data Analysis - Handling Missing Data](https://www.linkedin.com/pulse/when-how-handle-missing-inaccurate-values-dataset-machine-abdallah)

### Final Improvement
+ [Pattern Discovery using Apriori algorithm](https://www.geeksforgeeks.org/apriori-algorithm/)
+ [Apriori Algorithm](https://www.geeksforgeeks.org/apriori-algorithm/)
+ [Gaussian Discrimination Analysis](https://github.com/gmortuza/machine-learning-scratch/blob/master/machine_learning/bayesian/gaussian_discriminative_analysis/Gaussian%20Discriminative%20analysis.ipynb)
+ [[Person Correlation]]

---

[[BDA Cleaned dataset info]]

---
## Main Problem: Personalized Course Recommendations + Completion Prediction

### Improvement: Problem & Method 2: Recommendation System
+ ! **Problem Identification:** 

+ ? **Resolution Method:** We aim to address this by ...

+ $ **Propose Solution:** our strategies involves
	+ **Exploration Data Analysis** (EDA):
		
	+ **Feature Engineering:**
		
	+ **Machine Learning Model Development:**
		
	+ **Model Evaluation and Validation:** Accuracy, Recall, Precision, F1-scpre, ROC-AUC to select the best performing model for deployment. 
	
+ @ **Advantages and Disadvantages:**
- State the problem clearly
	- State possible solutions and tools
	- Select solutions and tools: analyze advantages and disadvantage and reasons for choosing the solution. 

```txt
### RESPONSES ###
Act as a Data Analysis specialized in Machine Learning, Data Science and MongoDB.

### If I ASK ###
Guide me through the each problem with Intuitive explanation, make sure to visualize the problems if I show signs of misunderstanding (to your idea). 

### PERSONALITY ### 
A Mentor, A Friend

### IMPROVEMENT ###
(Optional) Make sure to ask me if my question is too complex or hard to understand. Then think twice , 1st for your first Answers/Response, 2nd to check and refine yours Answers/Replies (to me) 
```

- [x] check BDA report Latex
	**Missing content:** Impute with emperical probability distribution.
	
- [ ] [[predict online course engagement summarize]]
- [ ] Make Canvas Slides
- [ ] Prep for my Presentation
- [ ] Prepare to make Slides for NLP