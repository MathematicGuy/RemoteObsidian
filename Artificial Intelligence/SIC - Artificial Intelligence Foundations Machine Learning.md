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
-> Only apply ML for complex problemsproblems
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

-> Clean the data and split them into 3 group: Training, Validation and Testing data.

### 3. Model training and testing
> Choose Machine Learning Algorithm for your processed data and start your training process

In this process you go through these step:
- Iterate and experiment (neccessary to find out what correct and should be avoid)
- Fine tune (Increase Model prediction ability)
- Evaluate (Check Model performance with diff input and output to see if the model meet the standard)
- Place your model into production (use the model)

### 4. Model deployment and maintenance
> Once your Model deployed, you set up a Cadence (lịch) for Retraining and perform re-evaluate performance.
![[Pasted image 20240611102458.png]]
> This step for Improvement 

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
	+ We can *Remove Duplicate features can improve Model performance* and improve Model's prediction capabilities. 
	![[Pasted image 20240611150027.png]]
	+ *Value closer to 0 -> low correlation*
	+ *Value closer to 1 -> high correlation*
	We want a heat map to be symetrical with the value on top left is the same as the bottom right.


### Features Engineer 
> is an Art that requires you to fully understand your data and the relationship between features.
+ ? *Tạo ra các features mới dựa trên những feature hiện có*. Ví dụ như feature màu đen và sống nội tâm., kết hợp lại ta sẽ có được người sống nội tâm thích màu đen qua côgn thức sống nội tâm / màu đen. 

- Manipulates data
- Add, removes and combines features
+ Create new features
-> Improve Mode Prediction


Feature with high correlation teach Model the same thing -> Remove one or combining both of them can optimize the training process.

+ ? How to deal with [[Missing value]]:
	+ Delete row with missing values
	+ Use ML to predict values
	+ Replace missing value with the mean or the avarge value.
	+ Using ML algorithm to handle missing data grafully. 



We need numerical data to calc so we turn Ocean proximity value in numeric using One hot encoding.
+ ! But *One-hot encoding can cause high cardinality* (số lượng lớn các giá trị duy nhất) (low cardinality: số lượng giá trị duy nhất ít) which *increase features* result in dimensionality. (dimensions increasement)

+ ? Features Enginerr:
	+ Added 5 new features
	+ Remove 1 features
	+ As features increaase it's harder for the model to learn thus increase costs


## Demo: Performing feature engineering
- Determine the missing data
- Use the K-nearest neighbors algorithm to impute missing values in small datasets

# 4. Training a Machine Learning Model

## Understanding learning algorithm and model training
Each training iteration called epoch, **refers to the one entire passing of training data through the algorithm**
	![[Pasted image 20240611204049.png]]

The data set ofetn have 80% for trainning and 20% is reserved for evaluation performance.
	![[Pasted image 20240611204124.png]]
Loss function **measure how good a Model is, in other word Loss function measure how far an estimated value is from its actual value**.
+ $ Housing dataset includes home costs
+ $ Loss func use to optimize training
+ ! Not for Judging Model Performance
After the Model have been trained, we use 20% reserved dataset to evaluate it. We can get good evaluation bc the Model practice on dataset it haven't seen before. (Old data can always be right, but new data can be not**)**

**Loss Function Evaluation Metrics**
- Mean squared error (MSE)
- Accuracy
- F1 score
- AUC
+ RA2
> Show wether or not you need to tweak hyperparameter (điều chỉnh siêu tham số) and start the training process again to improve performance.

**Algorithms use for Trainning**
+ **Linear Regression**
	- Solves regression problems
	- Is used to predict numeric values

+ **Linear Equation**
	+ Establishes relationships between independent and dependent variables or features by fitting it to a regression line

+ **Logistic Regression:**
	+ 1 or 0, True or False, etc..
	+ Value are between 0 and 1, the closer to 1 the more confident the prediction.
	+ Use in Classification Problem to predict probability.
	![[Pasted image 20240611204759.png]]

+ **Decision Trees:** use for classification and regression problems
+ **Random Forest:** 
	- A set of decision trees
	- Each tree is created from a different sample of rows
	- Each tree makes its own prediction
+ All the predictions are avaraged into a final result.

```ad-todo
Train a public safety mode, will this stop lead to an arrest
```
+ $ Step 1: Collecting Data
**Dataset:** Stop-and-search data from the UK
**Dataset Features:** 
- Location
- Gender
- Age
- Ethnicity
- Time of day

+ $ Step 2: Process the Dataset -> turn raw data into a format that your ML Model can learn from
- Impute (gán) missing values with K Nearest Neighbors (KNN) - gán giá trị còn thiếu bằng giá trị gần nó nhất.
- One-hot encoding the categorical data (turn number into Int datatype)
- Remove outliers
- Combine highly correlated features

![[Pasted image 20240611210537.png]]
>Create AWS account and Install Amazon Sagemaker to run code
+ AUC - Area Under Curve/Metric

## Reviewing Learning Algorithms For Regression
**Regression Problems**
+ Predict numeric values
**Use three common regression algorithm**
+ Linear regression
+ RadomForestRegressor
+ XGBoost

If you a home owner, do you often wonder how much your home will sell for in the current market: we can *Train a model to predict home selling price.* 
+ ? Again we will go through these steps:
	+ Process the raw dataset
	- Impute missing values
	- Use one-hot encoding of categorical data
	- Remove outliers
	- Combine correlated features
+ ? Now we can train the model using these Algorithm:
	+ Scikit-learn linear regression
	- RandomForestRegressor
	- XGBoost
+ $ After testing the data set with 3  Model, we seen:
	+ Diff learning algorithms perform differently
	+ XGBoost performed better
	+ XGBoost performed better against other regression models

## Examining Additional Learning Algorithms
### Unsupervised Learning
+ Doesn't use labeled data
+ It interprets unlabeled data
+ Machines figure things out independently by connecting similar features 

### Clustering 
- is a common unsupervised learning technique
- K-Means is a clustering algorithm (not to be confuse with KNN that group data close to the avarage or mean)
	K-Mean finds commonalities acress your dataset and puts each data point into a cluster.
+ ? All *data points in a cluster are homogeneous (đồng nhất)* and *heterogeneous (không đồng nhất) from data points in other clusters.*

### Unsupervised Clustering
+ K-mean output is the number of clusters representing segmented data
+ Define K by setting it as a hyperparameter
+ It's important to determine an optimal number for K
+ Experiment or use the [[elbow method]]

### Unsupervised Text Classification

**Text Classification Uses**
- Analyze movie and product reviews
- Organize support ticket urgency
- Review and organize posts by sentiment

Word2Vec (Word to Vector): used for text classification that creates
word embeddings, which are vectorized representations of text.
	![[Pasted image 20240611220217.png]]
 + A *single word* is transformed into a *numerical representation of that word*, also called a vector. (make it easier to *find similarities*, bc it enable us to use math)
+ $ Let use an algorithm to train a custom machine learning model.

## Demo: Training a custom machine learning model
	![[Pasted image 20240612100550.png]]


# Evaluating Model Performance

## Exploring common Classification Metrics
> Metrics are indicators of your model's performance 
> Metrics indicate if you need to tweak hyperparameter 
![[Pasted image 20240723211954.png]]

**Classification accuracy**
> Accuracy = correct_prediction / total number of predictions

**Binary Classification accuracy**
![[Pasted image 20240723211108.png]]
This show the definition between (Guess and Reality)
**True Positive**: a stop that does lead to an arrest.  
**True Negative**: a stop will not lead to an arrest and no arrest is made 
**False Positive**: a stop will lead to an arrest but it doesn't.
**False Negative**: a stop will not lead to an arrest but it does.  

Ways to handle imbalanced datasets
- Precision
- Recall
- F1 score

**Precision and Recall**
![[Pasted image 20240723211519.png]]
![[Pasted image 20240723211544.png]]

![[Pasted image 20240723211644.png]]

**Area Under the ROC Curve**
> measures accuracy and visualizes how well the predictions are ranked across true positive and false positive rates.

### Confusion matrix
> Show the accuracy of your model.
> And it Not a metric. It's a table showing a summary of the prediction results for a classification model.

![[Pasted image 20240723212159.png]]

![[Pasted image 20240723212208.png]]


### Exploring Common Regression Metrics
**Metric for Regression Problem**
![[Pasted image 20240723212847.png]]

$R^2:$ Calculates the difference between the actual values and the predictions made by the model.
- Mean square error and root mean square error are absolute measures
- MSE is an absolute number of how much your predicted results deviate from the actual number
- Root mean square error is the square root of MSE -> making MSE easier to interpret

![[Pasted image 20240723213051.png]]

### Determining feature importance

