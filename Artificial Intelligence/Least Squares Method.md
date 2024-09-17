This approach help us to find the best line to all the distributed datas.
![[Pasted image 20240916221858.png]]
First we calc the sum of $X, Y, XY$ and $X^2$
![[Pasted image 20240916222107.png]]
These results can be shorten down to
![[Pasted image 20240916222330.png]]
And we could use these result to calculate m in $y=mx +b$ (m as slope and b as y-intercept)
using this fomula
$$m=\frac{n\sum xy - \sum x\sum y}{n\sum x^{2}- \left( \sum x\right)^2}$$
and 
$$b = \frac{\sum y - m\sum x}{n}$$
and we got 
![[Pasted image 20240916222827.png]]
Put m and b back to y = mx + b, we see that it always stay close to each data point.
![[Pasted image 20240916223058.png]]