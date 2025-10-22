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


