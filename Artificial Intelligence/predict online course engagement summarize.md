# Data Understanding
**Load data**, encode catetorical fields.
**Evaluate datase (examine datas)**
	by checking number of missing value and their missing percentage.  
	Explore distribution in Categorical Data. 
![[Pasted image 20250401121905.png]]
![[Pasted image 20250401121913.png]]

**Data Cleaning**
+ ? DC include **remove high N/A** data field with more than 70% null samples and drop all N/A samples from a data field the missing % is less than 10%, like grade with 7%. 
+ ? **Encode Categorical** with integer to find correlation and model training. Categorical like `final_cc_cname_DI` (student's country) that have more than 10 values get re-categorize to 10 categories and encoded, new categories include 9 most present contries and 1 present other contry that up less than 2% 
+ ? **Check out for anomalies values** like negative grade, **outlier** values in `nevents`, `ndays_acts` and `nchapters`. We found and remove 1 outlier being  `197_757` from `nevents` while their mean is only `459`. 
Detect outlier using boxplot

+ ? **Impute Missing Numeric Data** for gender, level of education, year of birth. 

+ ? **Analyze and Impute Missing Data for Data fields with more than 25%** with probability distribution to reserve is original distribution while clear out missing value:10^21 `nchapters - 39.94%`, `nevents - 32.06%` using its correlation with `nchapters`, `ndays_acts - 25.38%`.

+ ? Impute missing `last_event_DI` with `start_time_DI` to indicate **student don't make any events since they started the course**.

+ ? Engineer new Data field `days_since_start` base on `start_time_DI` (course start time) and `last_time_DI` (last events datetime) 


+ $ Finally, drop original column that been imputed: `ndays_act, nchapters, nevents`, their name change to `ndays_act_imputed, nchapters_imputed, nevents_imputed` 

**EDA**
step include create 
+ overall dataset information
+ demographic analysis (gender, LoE, country, age)  
+ Engagement Analysis through `nforum_post, nchapters_imputed, nevents_imputed`
+ Temporal Patterns Analysis (time series data) from `start_time_DI`, `last_event_DI`
+ Correlation analysis for all attributes except IDs datafield and redundant attribute like registered (indicate someone has registerd a account buy  courses, but for get certified student must registered, thus this data field is redundant)
+ Statistics of cleaned attributes by certification status (0: no, 1: yes) 

**Connect and Load Data to MongoDB**
+ ? This step basicaly load processed data into MongoDB.

**Feature Engineering**: base on Correlation Matrix
![[Pasted image 20250401155305.png]]
+ $ Datetime data must be engineer since 
+ ? `days_since_start` was engineered to capture the total active duration of the students by **substracting the last active time by the first active time.** 

+ ? For highly skewed features like nevents, we use log to reduce skewness and bring nevents to 1 value range.

+ ? There high correlation between `ndays_act_imputed, nchapters_imputed and nevents_imputed` (> 0.6) and all to `certified` (> 0.65), thus we create a composite features (`engagement_score`) While `engagement_score` will fail to capture non-linearity its captures the general patterns of all 3 correlates features.
	So in a scenario where "a student with 2 active days but committed to read all chapters may be better than one with 10 low-effort days", `engagement_score` still remain high as complete more chapters also mean perform more events.
 + We decide to choose the weight 0.4, 0.3, 0.3 because `ndays_acts` values is low compare to `nevents` and consider more important than `nchapters` (0.66 correlation to certified compare to 0.65)

+ ? There is a 0.4 correlation between `ndays_act` and `days_since_start` thus we capture the `engagement_ratio` by dividing the ratio between **total activate days** `ndays_active_imputed` by **total days since start** `days_since_start`.

+ ? Because `viewed` (opened the course content) and `explored` (interact with the course content in detail) transfer the same ideas of have the students just view the course or beyond just vieing, we engineered them into combined features `engagement_flag` to clearly defines **3 distinct engagement levels:**
	1) no_view -> completely inactive
	2) viewed_only -> some interest, no deep interaction
	3) explored -> fully engageed
	
+ By combined feature, its help to improve clarity and reduce redundancy by combines 3 states into 1, while captures meaningful engagement levels. This also allow model to capture correlation between `certified` and `engagement` better since **student who with engagement tend to complete the course.**  
	
+ ? `time_since_last_event` was engineer to examine the correlation betwen **last active date** to `certified` to see **if an highly active student are more likely complete the course**. However its doesn't show a strong correlation to `certified`. 

**Correlation matrix between training features to certified**
![[Pasted image 20250401161114.png]]
+ ? These noticeble features was kept during training:  `'grade', 'ndays_act_imputed', 'nchapters_imputed', 'nevents_imputed', 'log_nevents', 'days_since_start', 'engagement_score', 'engagement_flag'`.

**Evaluate**



Ghi tiêu đề tổng quan -> tóm tắt nội dung -> phân tích chi tiết

Random Forest - boostrap creating many different dataset by randomly sampling from the original data. 

Accuracy - Out of all guesses how many of them was correct 

Precision - Out of **all predicted as positive**, how many of them are actually positive. (model predict positive (TP) / all positive prediction (TP + FP). 

Recall - Out of **all real positive**, how many of them was correctly classified. (TP / TP + FN)

F1 - Harmonic mean of Precision and Recall. Precision and Recall Correlation.  F1 score show to correlation between 
(**Out of all predicted as positve** how many of them are correctly guesses) / (**Out of real positive** how many of are correctly predicted.)
relationship between **positiveprediction and (predicted as positive / real positive)**


[[Machine Learning Model Time Complexity]]

**Random Forest Explaination**
**parameters:** tree depth, node size, number of features.  -> use to solve regression, classification problem.

made for collection of trees. 