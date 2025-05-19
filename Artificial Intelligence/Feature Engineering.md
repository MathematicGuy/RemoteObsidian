### Techinical Words
removes the median and scales -> substract the original data to

### Standard Scaler & MinMaxScaler 
- **StandardScaler** (mean = 0, std = 1), and
    
- **MinMaxScaler** (rescale between 0 and 1)
-> sensitive to outliers because they use `Mean and Standard Deviation (which use Mean)` or `Min and Max`.
+ $ RobustScaler solve this issue by using **percentiles** (quantiles, kind of like CART which apply regression independly to each parts instead of all part like Linear Regression), which is statistically robust to outliers.  

### RobustScaler
+ ? Know as a Scaling method that is **resistant to outliers.**  
+ 