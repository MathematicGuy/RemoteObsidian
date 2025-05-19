### Techinical Words
removes the median and scales -> substract the original data to

### Standard Scaler & MinMaxScaler 
- **StandardScaler** (mean = 0, std = 1), and
    $$X_{scaled} = \frac{x - \mu}{\sigma}$$
- **MinMaxScaler** (rescale between 0 and 1)
$$X_{scaled} = \frac{X - X_{min}}{X_{max} - X_{min}}$$
-> sensitive to outliers because they use `Mean and Standard Deviation (which use Mean)` or `Min and Max`.
+ $ RobustScaler solve this issue by using **percentiles** (quantiles in [[Box Plot]], kind of like CART which apply regression independly to each parts instead of all part like Linear Regression), which is statistically robust to outliers.  

### RobustScaler (include 2 form)
+ ? Know as a Scaling method that is **resistant to outliers.**  
$$IQR = Q_{3} - Q_{1}$$
+ $ **IQR** provides a visual representation of the middle 50% of the data. 

**1st form**
$$x_{scaled} = \frac{X - Q_{1}}{IQR}$$
Where:
- Q1 is the **25th percentile** (1st quartile),
	
- Q3 is the **75th percentile** (3rd quartile).

**2nd form** (Most common form, look for intuitive)
$$x_{scaled} = \frac{X - Median}{IQR}$$
+ $ Substract by `Median` gives a central distribution after transformation. While robust to outlier unlike the `Mean`. 


**PCA Application - Indicate Outliers**
+ ? PCA finds the Most Important Component (principal directions), thus also identify weak component which likely Outlier - those that explain the most variance. 
![[Untitled 8.png]]
+ $ In short, PCA can help detect outliers by identifying points that don't follow the dominant patterns in the data. 
![[pca_procedure.png]]



