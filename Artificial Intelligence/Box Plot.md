
 
![[box-plot-explained.gif]]

**Râu Đỉnh (Upper Whisker)** - largest value that is **not outlier.**
**Râu Đáy (Lower Whisker)** -  smallest value that is **not outlier.**

**Upper Part - Q3** -> 25% of data is > than this value 
**Median - Q2** -> Middle value.
**Lower Part - Q1** mean 25% of data < than this value 
**Outlier** - mean they're less than 3/2 value of the upper-lower quartile 

For example given `[5, 7, 8, 12, 14, 18, 21, 23, 24, 26, 30]`, 
+ **Median** (middle value) is 18
+ **Lower half** (before median): `[5, 7, 8, 12, 14]` -> Q1 is 8 (middle)
+ **Upper half** (after median): `[21, 23, 24, 26, 30]`  -> Q3 is 24. 

**IQR (Interquarile range)** - Between Upper Quartile Q3 and Lower Quartile Q1 calculated by Q3 - Q1 = 16. 
+ $ **Purpose:** provides a visual representation of the middle 50% of the data. 
$$IQR = Q_{3} - Q_{1}$$


**Outlier have 2 Bound**, upper outlier and lower bound **define a values become a outlier**.
$$x < Q_{1} - 1.5 \times IQR \space \space \text{or} \space \space x > Q3 + 1.5 \times IQR$$

+ The **Upper bound** define as $Q_{3} + 1.5 \times IQR$. This mean value larger than the `max upper quartile + 1.5 * interquartile range`   are Upper Bound Outlier.  
+ The **Lower Bound** define as $Q_{1} - 1.5 \times IQR$, this mean values less than the Lower Bound are Lower Bound Outlier.  


