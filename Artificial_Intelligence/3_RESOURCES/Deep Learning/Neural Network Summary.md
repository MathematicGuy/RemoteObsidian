**Goals:** Fit a non-linear line to all point of data (hence `.fit()`)
**Input:** number of drug dosage. 
**Hidden Layer**: contain 2 activations function
	Activation Function:  
Loss Function:

![[Pasted image 20250110141300.png]]

## Step-by-Step
**Step 1: Activation function input value**
>note: softplus was used as the activation function
![[Pasted image 20250110141635.png]]
  **x-axis coordinate = -15.06**
  Because **Dosage only in range 0 to 1.** If we plot **each points in x-axis we only get the corresponding y-axis values** in the **red box** are used to make this **new blue curve.**
![[Pasted image 20250110145519.png]]

**Step 2: Calc Activation Function Value**
![[Pasted image 20250110141902.png]]
>with x-axis = -15.6, activation function f(x) is 2.25 (on the y-axis).
+ Calc each Dosage value from 0 to 1, and plot them to the activation function f(x), we got the blue line. This mean each y value corresponding to x (x in range 0 to 1) mapped to f(x) create the blue line above.
   
**Step 3: Scale y-axis coordinate on the blue curve** by -1.30. 
note: 1.3 come from fitting the NN
![[Pasted image 20250110145717.png]]
![[Pasted image 20250110152654.png]]

**Repeat for all Activation functions** (i.e. orange in ours case)
![[Pasted image 20250110144344.png]]
![[Pasted image 20250110142032.png]]
>With orange activation function, when we plug a Dosage value to the activation function plot we only retrieve value in the orange activation function y values range. 
![[Pasted image 20250110144941.png]]
  Then we scale the y-axis on the orange curve by a posititve number: 2.28.

**Step 5: Combine 2 activation functions Curve Coordinate axis to get the fitted line**
>Now we Add (cộng) the y-axis coordinates of the blue curve to the orange curve, this give us the green squiggle.
> ![[Pasted image 20250110153825.png]]
> Now we can find the cooresponding y-axis coordinate on the green squiggle to see if the Dossage is effective. Or we can do the math.       
![[Pasted image 20250110142216.png]]
>**Summary:** X value mapped to the activation function and  get scale to get the new shape, to create 

Note: 
+ value we multiply are called Weights and value we add called Biases.
+ The NN starts with 2 identical activation functions. But by multiplying the weights and adding biases, we have flip them and stretch them into new shapes. Which are then added together to create a entire new squiggle. With more layers, we surely can create a much more complex squiggles.

