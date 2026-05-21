### Name Entitty Recognition - NER 
BIO Tagger Variant - BIOES 
B-Pr: Begin person
E-Pr: End Person
#### 1. IO Tagging (Inside-Outside)


#### 2. BIO Tagging (Beginning-Inside-Outside)


#### 3. BIOES Tagging (Beginning-Inside-Outside-End-Single)


**NER - Application**
Medical Information Extraction

### Quesion Answering - QA
*Input:* Question and Context
*Answer:* question answer
![[Pasted image 20260322204314.png]]

**QA Appoaches**
![[Pasted image 20260322204834.png]]
Fine the Exact Answer Location. e.g. extract "Ha Noi" word base on NER detected within the sentenhce for Question Q.

![[Pasted image 20260322212740.png]]
-100 cho padding (ignore_index=-100) vì ko cần quan tâm đến padding token. 

 


