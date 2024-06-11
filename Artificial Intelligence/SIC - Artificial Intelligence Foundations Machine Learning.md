# 1. Understand Machine Learning
**What we will achieve**
	Predict House cost in California
		Supervised Learing
		Linear Regression

Features that preduct selling price
+ Location
+ Age
+ Number of Bedroom
+ Ocean Proximity

![[Pasted image 20240611100743.png]]

# 2. Implementing a Machine Learning Solution
![[Pasted image 20240611101200.png]]
> Often Agile was used for SDLC

 ## Stages of Software Development Lifecycle (importance)
### 1. **Problem formation and understanding**
- Is machine learning an ethical solution?
- What are your inputs and outputs?
- What prediction error rates will you accept?

### 2. Data collection and preparation
 + ?  **Collection:** Source the data you need
	Internal data sources
	Provided data
	Open-source or public datastore
	Purchased data

+ ? **Preparation:** problem we will met in this step
	Raw data is not in a state that a machine can learn from
	Spend time annotating and wrangling the data (wrangling data: sắp xếp dữ liệu)
	Label data (gắn nhãn)
	Remove irrelevant features (loại tính năng ko liên quan: noise for example)
	Toss outliers (Ném bỏ ngoại )

> Once data in a statges Machine can learn from, you split the process in 3 subset:
1. Training (80%)
2. Validation (10%)
3. Testing (10%)
> This split is importance bc it be used to tested on the datas it wasn't trained on
### 3. Model training and testing
> Choose Machine Learning Algorithm for your processed data and start your training process

In this process you go through these step:
- Iterate and experiment
- Fine tune
- Evaluate
- Place your model into production
### 4. Model deployment and maintenance
> Once your Model deployed, you set up a Cadence (lịch) for Retraining and perform re-evaluate performance.
![[Pasted image 20240611102458.png]]

## Framming Machine Learning Problems
> Identify problem should use ML.
> -> If you can use simple rules, computations, or pre-determined steps to solve your problem, don't use machine learning.

**ML Work Best to:** 
- Predict an outcome (probability statistic)
- Uncover trends and patterns in data (probability statistic)
- Have rules and steps that can't be coded (let Machine learning the rule)
- Your dataset is too large to process by a human (machine can work 24/7)

note: feasibility (tính khả thi)
**Frame your problem**
- Define the questions for your model
- Define the required inputs and expected outputs

**Lastly, you need to estimate Budget for the long-term cost and maintenance ofr**
+ Your Model
+ Long-term cost
+ Maintenace

