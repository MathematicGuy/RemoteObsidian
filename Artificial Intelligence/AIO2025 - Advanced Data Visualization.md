**2 Main Question:** 
+ What **problem/information** need to **visualized ?** 
+ How to choose the right **chart type ?** 
	We have a lot of but what determind chart type we choose ? 
		Type of data
		Relationship between variables
		purpose of visualize
		who the audience we want to visual
	-> Appropriate Chart type

**Step 1 Determine type of dt** 
Quantitive Data - numberical dt
Categorical dt - yes/no (0,1,2,3 for yes, no, maybe, definitely option)
Temporal Data - time series data (tabular data)
Spatial data - location dt


**Step 2 What informations u want to visualize -> Identify the relationship between variables (of that information)**
Message you want to convey through data visualization 
	if u want to
	+  show a trend over time ? -> line, area chart 
		e.g electrical consumption through out the day
	+ compare data point -> bar chart or column chart
	+ distribution -> histogram or a box plot
	  
What data do u have: trend, distribution, comparison or distribution.

**Step 4: Identify the Audience** (that the main purpose, to convey data)

**Step 5: Select the appropriate chart type** - 
try to chose a graph that fit best to your data, bc there no one-size-fits-all solution. 
-> (Experiement) Compare diff chart types to see what best. Or Experience if in the past.

**Example: ETTh Dataset (Time Series)**
1. determine goal: time with highest Electric cosumption.
2. find relationship between variables
3. understand the data distribution
4. percentage of error-neous data 

![[Pasted image 20250801204018.png]]

**Highly Customisable Plot Chart using Matplotlib** 
Time with highest *ES - Energy consumption*
![[Pasted image 20250801204410.png|555]]
+ ? the chart above Circled wanted to survey data areas
`df.data[start_data_range: end_data_range]`
line connect each data can be adjust with
+ color, linewidth, linestype='--' (your string style)
customize each data point/dot:
+ markeredgecolor, marketwidth -> dot edge width, marketfacecolor -> dot color
plt.xlabel -> label of x axis
`.grid(True)` -> add grid to your chard
`.xticks(rotation=90)` -> rorate x axis label to 90 degree

**Simple plot chart using Seaborn**
-> Can be use along with matplotlib, no worry.
![[Pasted image 20250801205105.png|555]]

**How to see data information on the fly ?**
Use dynamic chart : `import plotly.express as px` -> allow you to each data point info. 
![[Pasted image 20250801205536.png|200]]

+ ? Visual multiple features within ranges
by create subplot for loop each features (column) within the data (df)
![[Pasted image 20250801205651.png]]
**How to Zoom in a sub-area of data** from the main data. -> you can Zoom-in a area of data (Period) 
`.Rectangle([a,b,c,e])` (replace 4 float values by a,b,c,d as coordinates)
![[Pasted image 20250801210417.png]]

`.add_axes` -> create sub-plot within the main plot.

### [[Box Plots]] (Already Explain)
![[Pasted image 20250801210845.png]]
Box Plot visualize Data Distribution and outlier.
+ ! Outlier do convey information -> so in reality, you don't alway remove outlier. 
	để biết cái nào không có correlation đó bác

**How to find an Outlier ?**
![[Pasted image 20250801212012.png|400]]
Acceprable Range to not be a Outlier
![[Pasted image 20250801211954.png|400]]
More in the [[Box Plot]] note.

![[Pasted image 20250801213345.png]]
How should we expand to left & right to fit Gaussian plot
+ ? Choose $\alpha$ so that $Q3 + \alpha . IQR$ < $\mu + 3\sigma$ 

Test with $\alpha = 1,2,1.5$  
![[Pasted image 20250801214013.png]]
Simple Plotly Boxplot code
![[Pasted image 20250801214152.png]]

**In Box pliot, Knowing each feature max value** help to decide when to Normalize Variables to `[-1, 1]` or `[0, 1]`. 
![[Pasted image 20250801214810.png|555]]
`df.plot(stacked=True)` -> stack features within a plot.

**Correlation Chart**
![[Pasted image 20250801215756.png]]
What to advise when using Correlation ? Correlation does not alway show relationship ? 

**Scatter Plot instead of Correlation**
explain
![[Pasted image 20250801220104.png]]

Visualize entire data
![[Pasted image 20250801220524.png]]
Undersand data distribution and if the data is linear -> data correlation and relationship -> give example.

**Piechart**
visual segment of data
![[Pasted image 20250801220706.png]]
>The pie chart showing the distribution of average loads for each load type (High Useful Load - HUFL, High Useless Load - HULL, Middle Useful Load - MUFL, Middle Useless Load - MULL, Low Useful Load - LUFL, Low Useless Load - LULL). Each segment of the pie represents the average proportion of a specific load type relative to the total average load. This visualization helps in understanding the relative contribution of each load type to the overall load in the dataset.


**Group Data use case: Race/Ethnicity Group**
![[Pasted image 20250801221446.png]]

#### Use Case: How to Understand Iris Dataset
Histogram for each features. e.g. see `seqal_width` distribution with histogram. Where bins is sepal width from min to max. 

Scatter Plot -> check linearity.
Bubble Chart -> Visual different distribution base on bubble size -> Allow to see 3D data distribution. Display multiple information like size,width,height in 2D graph instead od just 2.
![[Pasted image 20250801222352.png]]


**KDE Chart (Gaussian related graph)**
![[Pasted image 20250801222658.png]]
Compare different Class's features Distribution. e.g. SepalLength of 3 flower class.

**Displot Chart**
Visualize Distribution with Displot -> data trend.
![[Pasted image 20250801222853.png]]

**Pair plot**
![[Pasted image 20250801223008.png]]
Distribution between mutiple class. 

Even More Type of Charts
![[Pasted image 20250801223939.png|500]]

**Big Case Study: Uber Trips Analysis** 
![[Pasted image 20250801224022.png]]
+ ? How to visualize so that we get the Ideas in yellow.