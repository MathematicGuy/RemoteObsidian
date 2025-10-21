AWS - github for dataset ? 
**Problem**
1) **Team work:** How to work together on a set of data without conflict and waste downloading time. 
2) **Tons of work:** hard to work together. 


**Data Versioning pipeline**
![[Pasted image 20251002203416.png]]

**DVC** connect code, data and configuration version. 
![[Pasted image 20251002204135.png]]

**With & Without DvC**![[Pasted image 20251002204405.png]]'
Always add DvC first before git. Because git will update the data first and causes in-sync.

dvc .yaml - define stages of the machine learning pipeline. 
dvc push vs git push - for project with dvc setup, git push only save/upload meta to git while dvc push upload tracked data to remote storage (like aws s3, gcs)
To connect to aws with dvc we use - dvc push. 
Before running dvc repro you need: 
+ define dvc .yaml 
+ library: dvc, dvc-s3
+ git repo initialized
**DvC determine a stage need to rerun by** *comparing the stages* of the workspace *with the info stored in the dvc.lock file and the dvc.yaml* stage definition. In short, any changes in hash code, dependency or parameters defined in .dvc's stage trigger a rerun. 

---
**Data Leaking -** your model might have cheat if you have this, your training data includes infor that would not be available at prediction time in the real world, **unexpected data got leaked at model's prediction.** 
	Your model learns from the future, making it look very accurate during training but fail badly in the real world. 

**SDK vs REST API:** 

### Feast - help train ML/DL prediction model continously
Given that your prediction and trainining step use the same dataset, how to make sure the data that you used to train your model is clean and doesn't conflict with the data that used for prediction. Cause in a same dataset, its very likely for data leakage (model use future timeseries data for training thus achieve 100% accuracy). 
![[Pasted image 20251021204731.png]]

Feast - is a Feature store serve as central hub for managing, storing and serving features consistently across training and production. 


