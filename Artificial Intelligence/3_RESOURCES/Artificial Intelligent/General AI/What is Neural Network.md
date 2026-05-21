![[Pasted image 20230807205708.png]]


How brain can recognize visuals context. (784 total outcome)
-> but which connection layer * layer create the right output?
![[Pasted image 20230807195309.png]]


neuron -> thing that holds a number
represent each pixel (grey scale value)
0 for black  
1 for white (activated)

Last Layer of Neuron-> Represents how much the system thinks that a given image corresponds with a given digit?
![[Pasted image 20230807174958.png]]
for each correct node -> lit up

Why the layers? What are we expecting from its mechanism.
=> **To find the Patterns**
-> seperate a problem to multiple pattern.
If the pattern match -> answer
	Patterns in to Edges. Edges into Pixel 
![[Pasted image 20230807175243.png]]



![[Pasted image 20230807175314.png]]

break down recognition task -> like human -> we don't want to remember everything, but the patern that make everything.
For Example: each vowel in a word.
![[Pasted image 20230807175422.png]]
When break down pattern into many node of a layers. Meaning Calc all the possiblility can happend. For instance, if there're 2 variance of choices which create 2^2 possible outcome. There'll be 2 layer of neuron connecting one by one. 
![[Pasted image 20230807175925.png]]

**Edge detection** works by detecting discontinuities in brightness. Edge detection is mainly used for image segmentation and data extraction in areas.
![[Pasted image 20230807180057.png]]


To take control of Edge, we Assign (Multiply) a **weight** for each neuron connections. 
![[Pasted image 20230807180631.png]]

If we Need to have a Pixel pattern here -> what Parameter we should have?
How can we manipulate the numbers enough to potentially capture this pattern.
Or any pattern.
![[Pasted image 20230807200837.png]]
The solution is to assign a Weights to each one of the connections between neurons.  

However this will make the func to be any number.
- We need to squeeze the sum just between (0;1) -> multiply to a func?
![[Pasted image 20230807180835.png]]

*We Achive this by using a func called* **Sigmoid**
	Basically very negative inputs end up close to zero very positive inputs end up close to 1.
![[Pasted image 20230807180933.png]]


when You just want to take weighted sum that Larger than 10 -> minus bias for it to be inactive, since neg are not active)
=> Add neg 10 to the weighted sum. So only > 10 numbers can be meaningfull.
Then compress all the sum with Sigmoid

![[Pasted image 20230807181050.png]]
**Conclusion:** (func for 1 neuron)
+ **The weight tell you what pixel pattern this neuron in the second layer is picking up on and the bias**
	Imagine their dozen of edges connecting each other. To lead which edges goes with which edges to form the pattern we multiply a weight for each Neuron. 
	-> If the neuron pattern is right. Lit up

 + **The Bias tells you how hight the weighted sum needs to be before the neuron starts getting meaningfully active. (the closer to 1 the active it is)** 
	 Add Bias when you want to only take value larger or smaller than a certain amount. Since the whole func represent an neuron value.

The goal to achieve is Finding the right Weights and Biases.
![[Pasted image 20230807204345.png]]

---

Since this is very cumbersome to write down.
We NEED TO Simplified this down.
	

![[Pasted image 20230807204515.png]]

+ Take all the Activation (Neuron Node) in the Column as a Vectors.
+ Organize all the Weight as a Matrix.
	+ Each layer Corresponds to the connections between one layer and a particular neuron in the next layer.
	+ As each Neuron multiply to all of the adjacent neuron with an according Weight.
+ Bias as column adding to the function.
a^(0)0 -> a layer 0, rank 0
Caution: The function take in all the Neuron output previous it.
Current Neuron = Sigmoid * (1 Activation * Weight at pos n of column n + Bias)
![[Pasted image 20230807204839.png]]
Then we add the Sigmoid Function to the whole function.
![[Pasted image 20230807205536.png]]
**As we simplyfied it, we get** 
![[Pasted image 20230807205708.png]]
![[Pasted image 20230807205831.png]]
In the end, It is sure that Neuron a thing that Hold number. 

**But to be more accurate,**
## Neuron is a Function that take in the output of all the Neuron from the previous layer. 
![[Pasted image 20230807210449.png]]

> **Conclusion:** 
+ Neuron function include all the possible outcome which will be Filter throught a Function in order to get the Potential wanted Result.
**+ 3 Layer of Neuron: Input Layer, Hidden Layer, Output Layer**
	+ Input Layer are just Input number.
	+ Hidden Layer are Neuron by Neuron connected to each other one by one.
	+ Output Layer are the Result of all the process behind it.
(Hidden Layer)
+ Each Neuron can be think as a Number that was Created depend on all the Neuron before it.
	To be more Accurate, Neuron is a Function. that take all the previous function output as an input and  adding it with the bias then multiply with sigmoid for seize the value just between (0 and 1) 
+ **Weight** -> Adjust which value the Bias to be by muliplying with the Activator. (not sure?)
+ **Bias** -> **Like a weight that keep the value** (before mul with signmoid) of the func **under or higher a certain amount.** 
	( Ex:
	+  bias like - 100 Make all the value that under 100 Inactive (bacause value only active when they're > 0)
	+ + 100 -> Boost all the Bias up 100 time)
+ Sigmoid -> Keep all the value between 0 and 1.


