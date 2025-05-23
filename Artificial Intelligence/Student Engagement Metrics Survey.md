+ ? **key (int)** 
	**index**: Unique row index of the dataset (autogenerated).
	**course_id:** Identifier for the specific course the student is enrolled in.
	**user_id:** Unique Identifier for each student. 

+ ? **Course Interation Status**
	**registered** - Indicates whether the student officially registered for the course **(Boolean)**
	**viewed** - Whether the students viewed the course after registration. A basic level of interaction **(Boolean)**
	**explored** - Whether the student interacted meaningfully with the content (e.g. watching videos, doing assignments). **(Boolean)**
	**certified** - Shows whether the student completed the course and receive a certificate. **(Boolean)** - This is the main prediction target.

+ ? **Demographic Information**
	**final_cc_cname_DI** - Student's origin country (e.g. Vietname, India) **(String)**
	**LoE_DI** - leval of education of the student (e.g. Bachelor, Master) **(String)**
	**YoB** - year of birth **(String)**

+ ? **Academic Performance**
	**grade** - Final grade by the student in the course (scaled between 0 and 1). Missing for studetns who did not complete the course (float)
	**start_time_DI** - Timestamp that the student first started the course (Datetime `YYYY-MM-DD HH:MM:SS`)
	**last_event_DI** - Timestamp of most recent interaction by the student in the course  - (Datetime `YYYY-MM-DD HH:MM:SS`)

+ ? **Engagement and Human-Computer Interaction (HCI)**: Specific student actions during learning process
	**nevent** - Total number of recorded interactions with the course content **(Int)**
	**ndays_act** - Number of days the student active digitally **(Int)**
	**nchapters** - Number of course chapters the interaction with. **(Int)**
	**roles** - Role of the user in the course (e.g. student, instructor, staff, TA) **(String)** 
	**incomplete_flag** - indicator of if some missing informations in the student record. **(Boolean)**


https://github.com/NilnGitHu/Predict-Online-Course-Engagement/blob/main/Predict_Online_Course_Engagement.ipynb


https://www.kaggle.com/code/muhammadfaizan65/course-engagement-prediction-eda-gbC

https://www.kaggle.com/code/asifpervezpolok/complete-guides-for-course-engagement-prediction

