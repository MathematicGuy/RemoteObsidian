## 1. What is AI - interpret human behaviour
	system design to seem intelligent?
		or they just pattern matching -> Symbolic approach
		![[Pasted image 20240528140950.png]]
	Different root from human intelligent

 When is computer system is intelligent?
	strong AI: 
		displays all person-like behaviour (like in sci-fi)
	weak AI
		can process very narrow task/certain task 
		like Expert System: remember a specific knowledge in a field to give insight and diagnoised
	Problem: One of the greatest challenges with symbolic expert systems is that every possibility needs to be programmed by an expert. When there are a lot of possibilities this can lead to an “combinatorial explosion.” This is when there are so many different scenarios that the possibilities can't all be recorded by an expert.

## 2. The Rise of Machine Learning
**AI learn by Sensing data**, taught it self strategy by playing itself.
ML system are just learning pattern through data
Data (most important resources)

**Artificial Neural Network**
	use hundreds of numericals dials
	structure: input layer,  hidden layers, output layer
Training neural network
Read data -> Adjust -> Output-> Repeat
+ ANN read image pixels to pixels -> if the pattern matched -> output.

## 3. Common AI Systems 
**Searching pattern in data**
AI feed on data to learn newthings
ML look on that data and find pattern
	in real life world business look at the data to see
		Customer interests
		Industry trends
		New products
		Improve features 
-> that why MS and GG depend on AI for there services

	The network might be sensing things that
	humans are unable to perceive.
-> This can be a problem with industries such as insurance and healthcare.
AI are not like HI. Same result but diff process.

**Robotics**
(old fashion robot) Symbolic Reasoning - (new robot) ML  
not a robotics problems, it a data problems.
	Get the car to stear left or right is difficult from making the car understand when to stear left or right

**Natural Language Processing**
	If you can tranfer 10% of what u intending then u r a master communicator.
 allow u to talk to a machine like u talk to a human
 For example: Searching a topic in google
	NLP give machine to understand the larger world. not just matching keyword
Can't communicate -> wasn't capable of natural communicator


**The Internet of Things (IoT)**
	Device that communicate with eachother through networking making it crucial for havesting realworld data. 
	Ex: Applewatch sensor human blood flow to diagnosed potential health problems.

## 4. Learn from Data
Labeled and unlabeled Data
Ex in Playing Chess
	Human what and learn or observation.
	Supervied Learning - have a knowledgetable tutor for ex someone know how to play chess.
		RL Ex: Find the pattern for what make a high spenders custormers
	Unsupervied Learning - have a large set of data for learning on its own using patterns ofc.
		  RL Ex: ML given access all customers datas to give its own pattern.

**Massive Datasets**
Use datas for filtering datas. 
How it works:
+ First ML use a small dataset with example (labled data) to detected spam msg. Once it show reliability.
+ Move to a larger dtas set (with no labled) and repeat. 
**Binary Classification Challenge** -> ML algo have only 2 options (like 0 and 1)
![[Pasted image 20240528145741.png]]
ML algo use statistic to find patterns on your data. Once your Machine identifies these patterns it can then classify datas base on what it learned.

## 5. Identify Patterns
**Classify data**
Ex: Shopee want to classify the profitest buyer, Google want to classify the most prefer choices.
-> *Made by Human-Create Group*
**Binary classification**
Ex: 
	Credit card. ML supervied is ur transc frau or not frau.
	Msg -> spam or not spam
	Need a lot of upfront effort to train the systems. But not ensure the prediction.
	->  Ur team need to feed the machine until its accurate enough.
In ML you classifying your labled data into prefedined categories.

**Cluster data**
	Al system's use of unsupervised learning to create its own groups of data.
	Ex: Buying a mouse -> recommed a keyboard.  CLustering base on ur shopping history.
-> *Clustering data made by Machine-Created group*. Clustering data create using connection between data it interact with even it unlabeled.

Ex: In the situation classifying a bag of candy that contain both knowed and unknowed cadies -> Supervised learning are impossibe to implement. 
+ In this case we use a unsupervised learning and create cluster base on the candy attributes like size and colors and etc..
![[Pasted image 20240528152328.png]]
The biggest advantage of clustering is there's a lot more unlabeled data. Cluster data can see pattern that human unable to create.

## Reinforcement Learning
	Machine learning algorithms that use rewards
	as a way to give the system incentive (khich lệ) to find
	new patterns
Ex: The Algo track **how long** u listen to a song, **type of song** you listen -> the reward for recommending those songs increased, meaning the system will recommed more song similar to the listened song. This is a example of Q-Learning:
![[Pasted image 20240528153507.png]]
+ **Reinforment learning** can **create strategies to find better patterns** in the data (live). **Unsupervised learning** just **tries to create clusters based on what it already sees** in the datas.
	
+ Reinforment learning need a lot of pre-classified or labeled data for the training set (so it can score the label)

## 6. Machine Learning Algorithms
**Common algorithms**
	Find the **right algorithm** for each **task**
-> Mix/Use the algorithm to get the best insight for your datas

**K-nearest neighbor** (KNN)
	Algorithm plot new data to the one you already had.
	Euclidean Distance
		A mathematical formula that can help see the
		distance between data points
	Ex: u have a 2D plane of dots represent dogs, related dogs data cluster together. Choose 5 most nearest dots (dog) -> you can classified the new dog's breed base on the similar trait its has around the 5 others dog.
		![[Pasted image 20240528161058.png]]
+ $ Classify unknown data against the closest data that you do know.
	This old saying is **one of the best ways to remember the key strength of K Nearest Neighbor**. This machine learning algorithm is a **quick way to classify data that's similar and might “flock together.”**



**K-Means Clustering**
	It's an unsupervised machine learning algorithm. It's used to create clusters based on what the machine sees in the data.
Ex: you want to cluster 3 groups of dog to send to 3 shelters.
1) K-Means Clustering choose 3 dogs (since there're 3 groups) as the "Centroid dog". 
2) The algo would try repeat over and over again to find the best centroid
3) At the end of each iteration the machine check the variance between each dog and the centroid. (base on the similar trait they got)
4) Once there're a good centroid, those dogs would be put in a social group. 
5) For the dog that don't get around any others dog, they just get put to whatever group having the closest trait to them.

Org can use this algorithm to find the group of
	Loyal customers
	Regular customers
	Low priced shoppers


**Regression**
	looking for a trend 
Regression Analysis: *A supervised machine learning algorithm*
*that looks at predictors and the outcome*
+ Outcome: SUVs (for winter), Convertabale (for summer) 
+ Predictor: elements the agorithm base on to predict trends. (Ex: car with V8 engine, car with roof, car color, etc..)
![[Pasted image 20240528162954.png]]
-> Allow me to see the relationship between real life trend and elements.  
(ex: relationship between dog sales and pet food sales -> So if the dog sales go up I should open a dog service store)


**Naive Bayes Algorithm**
	It naive bc its Assumes that all the predictors are
	independent from one another.
Using dog breed for example
![[Pasted image 20240528163304.png]]
**Predictors:** Height, Hairline and weight
Normally these predictor can be correlated (liên kết vs nhau): ex a tall dog can is heavier.
But in Naive Bayes algo see these predictors independently.

**Class predictor probability:** the algo predict breed of the dog base on each traits they have. 
-> Allow to see predictors independently to measures the likelihood to be each breed. 
![[Pasted image 20240528163817.png]]
Why use Naive Bayes: its makes so few assumptions it can look in an enormous amount of predictors 
	Ex: Spam filtering, instead of looking for all words to understand the mail Naive Bayes predict the frau ercentage base on predictors like:   
- **Keywords**: Presence of specific words like "offer", "winner", "free".
- **Sender**: Whether the email is from a known contact or not.
- **Formatting**: Presence of images, links, and unusual formatting.
Then calc the avg of each value to indicate if the mail is frau or not. 
### Benefits:
- **Fast and Simple**: Quickly computes the probabilities and classifies emails.
- **Effective**: Despite the independence assumption, it often performs well in practice.

