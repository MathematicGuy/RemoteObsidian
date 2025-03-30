key: **index, course_id, user_id** 

**registered** - if a student has registrered for a course or not (Boolean)
**viewed** - if a student has viewed the course before registration or not (Boolean)
**explored** - if a student has explored the course content further than just viewing. explore course in detail or just skim through it. (Boolean)
**certified** - if the student has complete and received a certification of the course or not. (Boolean)

+ ? Geographical location
	**final_cc_cname_DI** - student hometown, country (string)
	**LoE_IE** - leval of education of the student (string) "Bachelor's," "Master's," etc.
	**YoB** - year of birth (string)

+ ? Academic performance
	**grade** - grade of the student in the current course. (float)
	**start_time_DI** - date that the student started the course (Data) - Datetime `YYYY-MM-DD HH:MM:SS`.
	**last_event_DI** - date of the last event the student attended - Datetime

+ ? Human-Computer Interaction - HCI -> specific student actions during learning process: 
	**nevent** - number of event student attended while interacting with the course (int)
	**ndays_act** - number of day the student active digitally - int
	**nchapters** - number of chapter of a course the student completed - int
	**roles** - role of the user in the course (student, instructor, staff, TA) - String 
	**incomplete_flag** - indicator of if there are unfilled informations in the student record for some reason (Boolean)


https://github.com/NilnGitHu/Predict-Online-Course-Engagement/blob/main/Predict_Online_Course_Engagement.ipynb


https://www.kaggle.com/code/muhammadfaizan65/course-engagement-prediction-eda-gbC

https://www.kaggle.com/code/asifpervezpolok/complete-guides-for-course-engagement-prediction

