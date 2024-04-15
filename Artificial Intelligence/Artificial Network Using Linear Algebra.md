wA as Matrix A 
(don't pay attention to the value, focus on how it work)
 A.T -> Matrix transpose
 ![[Pasted image 20240413092221.png]]

A.T.shape -> shape the matrix
(4, 2) -> 4 columns and 2 rows

A.reshape(6 ,1) -> reshape the matrix into 6 cols and 1 rows
![[Pasted image 20240413092504.png]]
A1.X + B1.Y + phi -> (Turn into Y of the next layers)
![[Pasted image 20240413093315.png]]

![[Pasted image 20240413094545.png]]

![[Pasted image 20240413094522.png]]
Each layer has n neuron. Layer 2 has 2 neuron.
The first layer is the Activations (in other word it the input value)

W21
+ Weight of the **2nd neuron**
+ Multiplying the activation of the **1st neuron** (of the previous layer)
+ ! but it don't tell us which layer this weight belong
![[Pasted image 20240413095006.png]]

![[Pasted image 20240413095800.png]]

![[Pasted image 20240413101217.png]]

![[Pasted image 20240413103941.png]]
This mean we **compute activations of the layer 2** as 
Sigmoid(Weight of th layer 2 * Activation input of the layer 1 + Bias of the layer 2)

This is the same for layer 3
Sigmoid(Weight of th layer 3 * Activation input of the layer 2 + Bias of the layer 3) 
![[Pasted image 20240413104116.png]]
