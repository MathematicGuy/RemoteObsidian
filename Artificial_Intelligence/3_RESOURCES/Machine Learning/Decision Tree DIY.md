[[Lecture_07_on_Decision_Trees.pdf]]
**Classification:** base on the inputs predict sth categorical (like spam or not spam label)
**Regression:** base on the inputs predict a number (like assign an accurate number)

![[Pasted image 20250420191858.png]]
![[Pasted image 20250420191911.png]]

## Data Analysis Methodology
There are 2 way to predict diabetes - by focusing on predicting people who have diabetes or by predicting people who doesn't.

+ ! Note: Excluding Outlier favor Bias. How to handle outlier. How to handle data imbalance (Outlier) -> Robust Scaler.
+ ! N/A data fill with "median by target/outcome"
+ ? Validation Method: k-fold validation. 
1) Visualize scatter plot 
2) Using real world information to identify areas that concentrate healthy/diebetes individual. (or using intuition)

---
## Feature Engineered Dataset (contribution 1)
![[Pasted image 20250505143425.png]]

![[Pasted image 20250505143442.png | ]]

### 1. Glucose: Impaired Glucose Tolerance (New_Glucose_Class_Prediabetes)
**Glucose**: *Plasma glucose* concentration a 2 hours in an oral glucose tolerance test
![[f89c3932cff665f76a4b52466dc2ffcb.jpg# left | caption | 500]]
**Set binary flag to 1** when the 2-hour plasma glucose (OGTT) falls into the prediabetes **range (140–199 mg/dL)**, and **0 otherwise**.


### 2. BMI: WHO/CDC Weight Categories (New_BMI_Range_Healthy / Overweight / Obese)
**BMI:** Body mass index **(weight in kg/(height in m)^2)**
- **Healthy**: 18.5 ≤ BMI < 25 kg/m²
    
- **Overweight**: 25 ≤ BMI < 30 kg/m²
    
- **Obese**: BMI ≥ 30 kg/m

### 3. Blood Pressure: Hypertension Stages (New_BloodPressure_HS1 / HS2)
**BloodPressure:** *Diastolic blood* pressure (mm Hg)

**New_BloodPressure_HS1**
+ **HS1 (Stage 1 Hypertension):** Diastolic blood pressure (DBP) is between **80-89 mm Hg 
	(80 ≤ DBP < 90 mm Hg)**
	**Untreated Stage 1** may be advised to make lifestyle changes.

**New_BloodPressure_HS2** 
+ **HS2 (Stage 2 Hypertension):** Diastolic blood pressure (DBP) is **90 mm Hg or higher**
	**(DBP ≥ 90 mm Hg)**
	**Untreated Stage 2** hypertension can lead to serious complications, such as heart attack, stroke, and kidney disease.

### 4. Skinfold Thickness: High Subcutaneous Adiposity (New_SkinThickness_1)
**SkinThickness:** *Triceps skin fold* thickness (mm) - **Triceps skinfold thickness** (TSF), a measure of subcutaneous fat, is **related to diabetes risk**. 

**New_SkinThickness_1:** A flag indicating whether the triceps skin-fold thickness exceeds a chosen threshold (for example, **> 30 mm to mark high subcutaneous fat**).

### 5. Insulin Response / Resistance (NewInsulinScore_1)
**Insulin:** *2-Hour serum* insulin (mu U/ml)
**NewInsulinScore_1:** serum insulin is above a threshold suggestive of insulin resistance (for example, > 125 $\mu U$/$mL$).

**HOMA-IR = (Glucose × Insulin) / 405**, set **NewInsulinScore_1 = 1 for HOMA-IR ≥ 2.0 (or the 75th percentile in your sample) and 0 otherwise.** 
+ ? Simplified from this fomula:![[Pasted image 20250505151013.png]]

### Model Performance to Encoding Technique
Note: [[One-Hot Encoding and Label Encoding]]
#### 1. Label Encoding
+ ? Use **when label's order matter**  e.g. `['low', 'medium', 'high']`
**Effect on splits**  
The tree only ever asks questions like
+ “Is `color_label` ≤ 1?”   
	which groups `{0,1}` vs `{2}` or `{0}` vs `{1,2}` depending on the threshold.

+ $ Pros: Less features (bc all color group into 1 column) thus fewer dimentionality and faster training.   

#### 2. One-Hot Encding
+ ? Use **when you want the model to treat each label as distict.** 
**Effect on splits**  
The tree can directly ask
+  “Is `is_blue` = 1?”  
	or  
+ “Is `is_green` = 0?”  
	capturing exactly “belongs to this category?” without any ordinal artifact.

+ $ More interpretable rules (if "color" == "red"), especially when bins (i.e. label value range) are meaningful. 
+ ! - **Higher dimensionality** → more features, deeper/wider trees, slower training and potentially more memory use.
    
- ! **Overfitting risk** on rare categories - trees may create a split just to “explain” a handful of examples in a one-hot column. 
	e.g. Only 2 value in range 500 and 700, while 99% of value are around 600 -> Decision Tree may create another branch just to classified these 2 cases.

| Factor                | Label Encoding                    | One-Hot Encoding                                   |
| --------------------- | --------------------------------- | -------------------------------------------------- |
| **Tree size & speed** | Smaller trees, faster to fit      | Larger trees, slower to fit (may require prunning) |
| **Splitting quality** | May create sub-optimal groupings  | Splits align perfectly with categories             |
| **Interpretability**  | Harder to read (why split at ≤1?) | Very clear (“is this category?”)                   |
| **Overfitting**       | Less likely (fewer features)      | Slightly higher risk on rare levels                |

---

**Introduct to decision tree and its characteristic**, why choosing decision tree for diabeties diagnolsed. 
**Advantages and Disadvantages** of decision tree. 
Basic Ad and Disad
![[Pasted image 20250505132500.png]]

---

Tabular Form -> Decision Tree.
Tyoes of Data Names: (but kind of the same) 
+ Table/Dataset/DataFrame/Matrix 
+ Columns/Characters traits/Attributes/Features

## Literature Review + Code
**Splitting Labels:** Find the best feature that best seperates the <=50k and >50k earners, moving left to right. If there're **2 best feature, its pick the first one.**
![[Pasted image 20250426170424.png]]
But for Race & Hours Per Week, we got the perfect split. So **what features does the algorithm picked, the answer is the *first* optimal feature they find, trees are greedy !**. Given our training data, **RACE IS USED AT THE ROOT NODE.**
![[Pasted image 20250426170554.png]]


Gini Impurity (using [[Gini Index]]) can also be understand as the prob for the model making mistakes. High is bad, Low is good.
Gini Impurity perfer imperfect (so marbels can have weight)
![[gini_impurity_image.png]]

## Bining
 To calculate Gini for continuous feature such as Age, the tree must first use a process called **Bining** to convert the numeric feature into mutiple classes (e.g. Age < 30), the step go as follow:
 1) **Sort the numeric data** (in ascending order from Low to High, bottom to top)
 2) **Exam a bunch of Split points and choose the one with Lowest Gini Score** (i.e. orange arrow) 
	![[Pasted image 20250427140300.png]]
	Age < 30 was the first optimal gini found for Age feature. 
	Then this Gini is stored and compared against the gini indexes of other features, if this proves the lowest gini, the root node will be Age < 30. ![[Pasted image 20250427140443.png]]
+ $ Inshort the algorithm calc Gini Impurity of each features in order to find the best split for each branch. 

## Decision Trees in Python
**Differences between the DecisionTreeClassifier and CART:**
+ DecisionTreeClassifier only works with numeric data. Categorical features must be transformed (i.e. encoded) to numerics form.


**One-Hot Encoding**
use `get_dummies()` from `pandas` to one-hot encode categorical data, prefix for extra annotation before each class name (for clearer class name). 
![[Pasted image 20250427143034.png]]
One-hot encoded multiple columns (for columns name in cat_features)
![[Pasted image 20250427143234.png]]

We want the most impurity the top node, so the lower we go the higher the purity. 

**Value on the right implies True "Yes", on the left implies False "No".** 
+ But the *"value variable"* inside each leaf mean represent just that.
	+ **value at index 0** mean there're n class that **sastisfied root class condition.**
	+ **value at index 1** mean there're n class that are **not sastisfied root the class condition**.
	e.g. On the bottom right leaf, `value = [323, 3057]` mean there are **323 rows** that are less `<= 50K` and there're **3057 rows** have label `> 50K`. That is why **leaf class label are > 50k** because there're more of them. 
	e.g. On the bottom left leaf `value = 2815, 236` mean there are **2815 rows**  `<= 50K` and **236 rows** `> 50K`. That is why the **leaf class is <= 50K**. 
	
![[Pasted image 20250427150700.png]]


$$z = \frac{x_i - \mu}{\sigma}$$