Regularization reduces the chance of overfitting. 
![[Pasted image 20260128153655.png# left  | 233]]
Note: 
+ if the regularization term is large then the weight is force to be small when trainning to stabalize/minimalize the Loss function. 
+ When apply $\lambda$, model forced to adjust every weight as a group, this help model to generalize instead of focusing on adjusting each variables to minimalize loss. 
	in short, $\lambda$ help adjust weight as a group so the model not adjusting each node to minimalize loss and get overfitting.  ![[Pasted image 20241118090525.png]] 
-> In short, L2 regularization amplified for having *large weights* using the square. If weight doubles then the penelty is quadrupples -> Force the model to keep weights small.  
![[Pasted image 20260128154115.png]]
In politic term, Overfitting is like corruption where 1 person have too much power making the government unstable. 
**L1 - Lasso Regularization:** when the model update, we calc DERIVATIVE w.r.t each weight, so only 1 weight get regularization for L1. 
**L2 - Ridge Regularization:** when the model update, the DERIVATIVE for each weight $w^2$ is $2w$, therefor every weight is ultilze, not result in 0. 

![[Pasted image 20260128154255.png]]
+ @ Think of applying regularization as moving or chaing the Loss function landscape. Where L1 diamond and L2 circle shape are the Constraint when the model reach a optimal point. 

Below: Visualization for L1 Regularization. 
![[Pasted image 20260128165207.png]]
Note: when $\lambda = 40$, we ignore Weight as a variable when predicting Height.   


### L1 vs L2 Regression Loss (not Regularization)
**L1 Loss:** reduce the weight to zero making only the imporatance weight hold decision. Like pure communism.
	Robust to outliers. Effectively learn the median. 
	
**L2 Loss:** instead of killing the weight, its reduce the unimportant weight influence close to zero, leading to evently distributed solution where every weight contribute a little. 
	Sensitive to outlier. Effectivly learn the mean.
 
#### Mean Absolute Error (MAE) -> magnitude of the errors, ignore error direction neg/pos
+ $ Solve neg and pos cancelling out eachother problem. 
![[Pasted image 20241109202203.png | 555]]
>*Solve Value Cancellation problem in ME* 
- @ **Intuitive Definition:** Calculates the average magnitude of errors without considering direction (over/underestimation).
- ? **Example Intuition:** MAE = 10 means the model is off by 10 units on average.
+ & **Use Case:** Assessing average error magnitude (e.g., predicting house prices).
> Bc the predicted and actual value cancell eachother but not negative. So the closer to 0 MAE is, the better our prediction is. 

#### Mean Square Error (MSE) -> penalize errors heavily
![[Pasted image 20241121094140.png | 555]]
- @ **Intuitive Definition:** Averages the square of each error, penalizing larger errors more heavily.
- ? **Example Intuition:** MSE = 25 means the average squared error is 25, emphasizing that big errors are significant.
+ & Comparing model fits (e.g., energy consumption prediction).
+ $ **Advantage** is MSE penalize large errors **bc errors are squared.** However, this is a 2 edge sword when there're outliers. 
+ ! **Disadvantage** is MSE also magnified the outlier. Hence sensitive to outliers and lead to unstable loss function. e.g. 1 value larger x10 the rest can can break the loss function. 
Also it **Scale dependent errors:** this mean it *prone to error if data are not re-scale using normalized and standardized technique.*

