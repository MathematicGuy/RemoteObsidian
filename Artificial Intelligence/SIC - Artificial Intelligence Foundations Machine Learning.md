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
### 1. Problem formation and understanding
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
1. Training (80%) -> Data use for training model
2. Validation (10%) -> Correct data use to validata training data
3. Testing (10%) -> Data use to test the Model after a training section was complete
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

## Identifying a pre-built model
> Use a model that is tested and proven to save time and money

**Image Classification Problems**
- Use a pre-built model
- Use a process called transfer learning
	![[Pasted image 20240611104952.png]]
	Inherent Knowledge from a Model to a new Model.

But where can I find pre-trained Mode -> here where [Model Zoo](https://modelzoo.co/) and Hugging Face

## Understanding Tools used to train a Model
What if trained data not solve your problems? then make sure to have
	A Large enough data set
	Enough compute processing power before you start
Simple Models -> Local Machine
Complex Models -> Great GPUs from Cloud Provider


Library you will use to processing data
![[Pasted image 20240611105806.png]]
After that you can Visualize your data using
- Use plotting charts and graphs
- Matplotlib
- Seaborn

For Model training purposes you can use
- Scikit-learn
- TensorFlow
- MXNext
- pyTorch
- Keras


```ad-summary
**What I have learned in Chapter 2: Implementing a Machine Learning Solution**
> Not every Problems should use Machine Learning bc ML is not always the most optimal solution.

There're 4 Stages in SDLC:
1) Problem formation and understanding -> Suitable ML algo and method for ur problems
2) Data Collection and Processing -> Collect data (either buy or get raw data) and process it. Make sure the data is usable. Split data into 3 group (Training, Validation, Testing)
3) Model training and testing -> This include Understand ur Model, Fine tune, Evaluate and train your model using ur process datas. 
	+ I can either create a Model from Scratch or use a pre-built model to save time and money.
1) Model Deployment and Maintenance -> Set a schedule for model retraining and performance re-evaluation.

Before trainning a Model make sure I have:
+ Enough processed data (clearn and minimal noise data)
+ Enough processing unit to train my Model
```

# Preparing Data for Machine Learning
## Obtainning Data
Data Sources: 
- Internal datastore
- Client provided data
- Open-source
- Public datasource

**Data for California House Price Prediction include these features:**
- Income
- Population
- House occupancy
- Location
- Number of bedrooms
- Number of rooms
> This is ours Labeled Data: contains target values the machine learns to predict.
 +  Our target is Median House Value, the machine reviews features (variables) to predict the target.

*Histogram: biểu đồ* 
*Outlier (Ngoại lệ): distince value that much more distant than the avarage value.*

Remove outlier to stop them from impacting the performance of your Model
Heat map -> show correlation of a features. how 1 features interacting with others features.
+ ! If *2 features are highly correlated*, it mean *those features are teaching the model the same thing.*
	+ We can *Remove Duplicate features can improve Model performance* and improve Model predictability. 
