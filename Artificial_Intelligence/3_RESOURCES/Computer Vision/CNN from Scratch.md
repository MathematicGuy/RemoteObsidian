## How Convolutional Network work from Scratch
Trick that **CNN** use for machine to **understand image**. Understand a image mean knowing **which Features make that image unique** and **able to Classify them.**
Note: [Deeper understanding about CNN Kernel - But what does a trained Convolution Neural Network actually learn ? VISUALIZED!](https://www.youtube.com/watch?v=kebSR2Ph7zg)


Feature match pieces of the images
![[Pasted image 20251218140319.png | 344]]
-> Call **Filtering: the math behind the pattern matching** 
1. Line up the feature and the image patch.
2. Multiply each image pixel by the corresponding feature pixel.
3. Add them up.
4. Divide by the total number of pixels in the feature.

**Apply Filtering**
If match then equal 1 - this mean the matched percentage is 100%. 
![[Pasted image 20251218140523.png]]
How about this pattern, this said 55% matched. 
![[Pasted image 20251218140604.png]]

+ ? **Convolution basically just mean move a Filter across the image to find Features that it might Match** 
	Its answer the question: **is this pattern existed within this image, if so how can I emphasize/activate it.**
![[Pasted image 20251218140730.png]]

Another example of apply diff Filter, we could extract or at least activate a similar pattern within the filted image.  
![[Pasted image 20251218141032.png]]
Simplified version of the image above.
![[Pasted image 20251218141431.png# left | 333]]

**Pooling: Shrinking the image stack to smaller image.**
1. Pick a window size (usually 2 or 3)
2. Pick a stride (usually 2)
3. Walk your window across your filtered images.
4. From each window, take the maximum value.

**Max Pooling:** picked out the max value from the filtered image/feature map. ie. *Out of all Features, only retrieve the most noticeble features.* 
![[Pasted image 20260105000748.png]]

![[Pasted image 20251218141711.png]]

**Normalization**: keep the math from breaking by tweaking each of the values just a bit. **Change everything negative to zero using ReLU.**
![[Pasted image 20251218141939.png]]

**Layers get stacked** 
The output of one becomes the input of the next. 
![[Pasted image 20251218142010.png]]
 
**Deep stacking**
Layers can be repeated several (or many) times. 
![[Pasted image 20251218142117.png]]
 
**Fully connected layer - How Deep Neural Networks Work**
+ ? [[What do Neural Network Learn]]
Every value gets a vote. Allow the Neural Network to learn Which 
![[Pasted image 20251218144124.png# left  | 544]]
This is how a simple NN classified a Class/Option.
![[Pasted image 20251218144414.png | 333]]

Next level of detail, if we just **depend on total value** we **can't really clasified base on their position** (both horizontal but 1 top & 1 bottom). 
![[Pasted image 20251218144542.png]]

Now we gonna **build Neuron, first we take all the input then add 'em up.** 
Give each NN Nodes a receptive fields to extract a specific feature. 
Postivei in white, negative in black, Zero -> zero line/value.
![[Pasted image 20251218145123.png | 455]]

**Activation Function:** map input value to another value Domain while still preserve its meaning. By using sigmoid we basically squashing all value larger then 1 back to 1 and smallar then -1 to -1.  
![[Pasted image 20251218145208.png | 444]]
**Squash the result**
![[Pasted image 20251218145354.png | 233]]
 
![[Pasted image 20251218145918.png]]

Note: Why Hidden layer use Sigmoid but not ReLU. 
+ $ With **ReLU**, we not only **reduce Gradient Vanishing problem** but also **Flip the value backward so the MLP can learn every pattern in reverse.** ![[Pasted image 20251218150203.png]]
	The 2nd layer upper nodes take the **sum of the black and white** node and getting **value of Zero (Grey)**.

+ ? Intuition Example of how MLP classified a image is horizontal.
![[Pasted image 20251218151105.png]]


#### How Optimization for ML Works
**Problem:** Tea drinking temperature to personal enjoyment. Right temperature -> High Enjoyment.  ![[Pasted image 20251218151417.png | 333]]To use these information as a Optimization problem, we flip all values downward, bc we're minimizing value in a value domain.
![[Pasted image 20251218151305.png | 333]]
+ ? Explain Gradient Descent using user feedback terminology. Have a lot of people drinking tea -> feedback -> update value to lower/increase the temperature.  ![[Pasted image 20251218151852.png | 233]]
A more advance method is to use curvative, by **calc the curvature in both size** you compare which side is steeper to go. ![[Pasted image 20251218152007.png# left | 133]]
**Global and Local Minima**
+ ? What if the value Domain have multiple Minima (ie. best temperature for tea enjoyment) 
![[Pasted image 20251218152150.png | 333]]
![[Pasted image 20251218152239.png | 333]]

+ ! What about have more feedback -> more Accurate but waste Too much resource. But using Gradient Descent is like guessing/assume this or that value is optimal. 
+ ? Is there a Middle ground to find the optimal value and avoid local minimal ? 
![[Pasted image 20251218152502.png]]

+ $ **Instead of trying to answer right, we try to be (answer) LESS Wrong** -> need define  **specific how wrong is my answer** (ie. in **What range of value make my guess RIGHT, $d_i$ for deviation -> Duh, that basically the Loss Function**) ![[Pasted image 20251218153221.png | 444]]

![[Pasted image 20251218153324.png | 433]]

+ ? **The Cost function** allow us to **estimate how wrong is my Guess**. As the example below show the total Cost of ours guesses. (Thats a simple example of numerical optimization)  ![[Pasted image 20251218153440.png]]

![[Pasted image 20251218153839.png | 444]]

![[Pasted image 20251218153905.png | 233]]

**However, there another Analycal shortcut to find what the best guess is.** 
![[Pasted image 20251218155318.png]]

**Backpropagation: calc change in Error given the change in Weight** (ie. calc derivative for a Weight)
+ $ This **doesn't tell us where the Local minimum** is but it does tell us **Which way is better to go.**
![[Pasted image 20251218155538.png]]
**Simplified and Visualize**
![[Pasted image 20251218155821.png]]
This Chain answer the Question, for the total error to decrease what need to change in weight z, in weight y and so on to weight a -> Help increase value to classified a specific image.
![[Pasted image 20251218155839.png]]
	Apply this information to the classified the horizontal edge image, its would mean changing all weights so that horizontal edge get emphasize when the horizontal image pass through the network.   

**This can also be stacked**
![[Pasted image 20251218160527.png]]

**Putting it all together:** A set of pixels becomes a set of votes. 
![[Pasted image 20251218160604.png]]

+ ? Remaining topic to explain -> Too much to Test, so there actually a fomula to choose. ![[Pasted image 20251218160746.png | 344]]
  Note: visualize and explain what Abstract feature look like. 
+ ! **Limitations:** ConvNets only capture local "spatial" patterns in data. If the data can't be made to look like an image, ConvNets are less useful. 

**Rule of thumb:**
If your data is just as useful after swapping any of your columns with each other, then you can't use Convolutional Neural Networks.
+ $ **ConvNets** are good at finding pattern and classifing image. 

# [[Step by Step CNN]]
