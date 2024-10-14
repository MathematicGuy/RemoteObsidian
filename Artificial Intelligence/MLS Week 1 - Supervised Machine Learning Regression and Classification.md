# Supervised vs Unsupervised ML
## Supervised
>**Definition:** Model learn from a label dataset where each input is associated with the ouptut. The goal is to predict output from the input based on example input-output pairs. (like teaching a baby)

**Common Algorithms:**
**Linear Regression** - predicts continuous value (type of ml where task is predict number)
	Prediction house price based on size, Price by Marketing Prediction, etc..
**Logistic Regression** - predict binary outcome (yes or no, 0 or 1)
	Predict Spam or not spam email (based on a boundary value i.e. >0.5 true else false)
**Decision Trees**: Learns decision rules based on input features.
	 
**Support Vector Machines (SVM)**: Finds the optimal boundary to classify data points.
	Classify Study and No Study group of student
**Neural Networks**: Deep learning models that work well for complex tasks like image classification.

## Unsupervised
>Trained on unlabeled dataset, meaning training without a given example (labeled data). the goal is to identify pattern, structure or relationship in the data. 

**Common Algorithms**:
**K-Means Clustering (nhóm)**: Groups data points into clusters based on their similarity.

**Hierarchical Clustering**: Builds a tree of clusters to represent data hierarchically.

**Principal Component Analysis (PCA)**: Reduces the dimensionality of the data by identifying important features. 
	Image compression, compress data
**Autoencoders**: Neural networks used for unsupervised learning tasks such as data compression or anomaly detection.

# Regression Model
## Linear Regression
> Fitting a linear equation to the observed data. (predict the right equation by tweaking $w$ and $b$)

**Regression vs Classification Model**
+ Regression model predict number, can handle large amount of features (e.g. predict salary base on n features) - infinite possible of outputs.
+ Classification predicts categories data (go in) with small number of possible outputs. (e.g. hair color (red, blonde, or black)

![[Pasted image 20241014093306.png]]
$\hat{y}$: prediction for $y$ (target variable)
Univariate linear regression (Linear regression with 1 model) with Uni mean 1 in latin. (fancy way to call it)
>1 variable as for 1 input. 
![[Pasted image 20241014093706.png]]

Week again noise, 1 outlier can affect the lin equation a lot.
![[Pasted image 20241014105705.png]]
## Cost Function
w and b: coeffient, parameter
	b: y-intercept (because it always cross y-axis)
	w: the slope of that line.
		say that x = 2 and we get y = 1. 
Goals: choose w and b so that the line as close to all data points as possible.
![[Pasted image 20241014095055.png]]
> The cost function is consist of $\hat{y}$ and $y$. by taking the sum of  $\hat{y}$ subtract $y$ dviding by m we are calculating the average error (i.e. distance from the line to each point) of all point to that line. 
> note: divided by 2 to remove the 2 hat when derivative thus making calc easier.![[Pasted image 20241014095035.png]]
> notice $\hat{y}$ is is same function as $y$ but with other input value x, we can re-write cost function to:![[Pasted image 20241014095335.png]]
> So by calc the sum of distance of all point to the current value and their average, we can move the equation $J(w, b)$ closest to all point.
> note: w and b are the parameter can be adjust.

#### cost function intuition
Given that b=0, the line pass through 0. So let focus on minimize $J(w)$
![[Pasted image 20241014102458.png]]
Because b=0, cost function simplified to $\frac{1}{2m} \sum^{m}_{i=1} wx^{(i)}-y^{(i)}$ and if w=1, the cost function will be just be 0.
![[Pasted image 20241014102818.png]]
Example:
![[Pasted image 20241014103437.png]]

>**The cost function resemble a parabol if you calc all of its value from largest to lowest** (0).
![[Pasted image 20241014112735.png]]
For example If w is negative the cost funtion equal a large number: 5.25 
![[Pasted image 20241014113105.png]]

#### Visualize cost function
Cost function have the similar shape to a bow.
![[Pasted image 20241014113304.png]]
The height of the surface above is J(w, b)
**Contour Map:** show the high or depth using flat plain. 
![[Pasted image 20241014110254.png]]
Using a contour map, we can plot the cost function value, the closer it is to the center the lower the cost (see it as a 3D parabol)
![[Pasted image 20241014113413.png]]


# Train Model with Gradient Descent
## Gradient Descent
![[Pasted image 20241014135803.png]]

![[Pasted image 20241014135949.png]]

### Learning rate
![[Pasted image 20241014140411.png]]
Fomula comefrom the partial derivative with respect of w and b
![[Pasted image 20241014140640.png]]

