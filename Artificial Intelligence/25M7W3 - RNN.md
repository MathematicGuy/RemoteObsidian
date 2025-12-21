**Input Weight of each RNN nodes are shared.** 
Only the **predicted/activated Weight (after ReLU of each Node) are tune differently.** 

`[UNK]` - token for unknow number/word
`[pad]` - padding to make all sentence have the same length. 

![[Pasted image 20251220210806.png]]

![[Pasted image 20251220211639.png]]

![[Pasted image 20251220213423.png]]
RNN trong code có thể lấy cả Weight trong Hidden Layer.    
RNN khi tính số Param ko tính của Sharing.  
![[Pasted image 20251220223302.png]]

![[Pasted image 20251220223723.png | 433]]


```text
filename: rnn_backprop_visualization.txt

================================================================================
 VISUALIZATION: Backpropagation Through Time (BPTT)
 ARCHITECTURE:  Input (X) -> Hidden1 (H1) -> Hidden2 (H2) -> Output (O)
 CONTEXT:       Unrolled over 3 Time Steps (t-1, t, t+1)
================================================================================

LEGEND:
 [ ... ]    : Nodes (Neurons/States)
 W_xx       : Weight Matrices (The parameters we want to update)
 --->       : Forward Pass (Data Flow)
 <===       : Backward Pass (Gradient/Error Flow)
 (+)        : Summation of gradients (from future time + current layer)
 L_t        : Loss function at time t

================================================================================
 1. THE FORWARD PASS (Data flows Right and Up)
================================================================================

              (Time t-1)              (Time t)              (Time t+1)

OUTPUT LAYER:
              [  O_t-1 ]              [  O_t   ]              [  O_t+1 ]
                  ^                        ^                        ^
                  | W_h2o                  | W_h2o                  | W_h2o
                  |                        |                        |
HIDDEN 2:     [ H2_t-1 ] --W_h2h2---> [  H2_t  ] --W_h2h2---> [ H2_t+1 ] ...
                  ^                        ^                        ^
                  | W_h1h2                 | W_h1h2                 | W_h1h2
                  |                        |                        |
HIDDEN 1:     [ H1_t-1 ] --W_h1h1---> [  H1_t  ] --W_h1h1---> [ H1_t+1 ] ...
                  ^                        ^                        ^
                  | W_xh1                  | W_xh1                  | W_xh1
                  |                        |                        |
INPUT:        [  X_t-1 ]              [  X_t   ]              [  X_t+1 ]


================================================================================
 2. THE BACKWARD PASS (Error flows Left and Down)
    *Focus on Time Step t*
================================================================================

Assume we calculated Loss (L_t) at time t. We need to send this error back.

STEP 1: Calculate Gradient at Output
   L_t <=== (Start Here)
    |
    v
 dL/dO_t
    ||
    \/
  [ O_t ]  <== Computes error relative to target Y_t
    ||
    || (Crosses W_h2o) -> Updates W_h2o
    \/

STEP 2: Backprop into Hidden Layer 2 (The Split)
    ||
    \/
  [ H2_t ] <==== (Gradient from Future H2_t+1 comes here too!)
    ||
    ||===== SPLIT FLOW ===================================================\
    ||                                                                    ||
    || PATH A: SPATIAL (Down)                                             || PATH B: TEMPORAL (Back)
    || (Going to lower layer)                                             || (Going to previous time)
    ||                                                                    ||
    \/                                                                    \/
 (Crosses W_h1h2)                                                      (Crosses W_h2h2)
 -> Updates W_h1h2                                                     -> Updates W_h2h2
    ||                                                                    ||
    \/                                                                    \/
  [ H1_t ]                                                             [ H2_t-1 ]
    ||                                                                    ||
    ||                                                                    ||
    ||===== SPLIT FLOW ===============\                                   (Recurses back to t-2...)
    ||                                ||
    || PATH C: SPATIAL (Down)         || PATH D: TEMPORAL (Back)
    ||                                ||
    \/                                \/
 (Crosses W_xh1)                   (Crosses W_h1h1)
 -> Updates W_xh1                  -> Updates W_h1h1
    ||                                ||
    \/                                \/
  [ X_t ]                          [ H1_t-1 ]
 (End of chain for X)                 ||
                                      (Recurses back to t-2...)


================================================================================
 3. PSEUDO-CODE TRACE (CS Logic)
================================================================================

function BackwardPass(t):
    // 1. Output Layer Gradient
    grad_O_t = deriv_loss(O_t, Target_t)
    
    // 2. Hidden Layer 2 Gradient (Accumulate from Output + Future H2)
    //    Note: grad_H2_future comes from the previous recursive call (at t+1)
    grad_H2_t = (grad_O_t * W_h2o) + (grad_H2_future * W_h2h2)
    
    //    Store gradients for weights
    dW_h2o += grad_O_t * H2_t
    dW_h2h2 += grad_H2_t * H2_prev
    
    // 3. Hidden Layer 1 Gradient (Accumulate from Above H2 + Future H1)
    grad_H1_t = (grad_H2_t * W_h1h2) + (grad_H1_future * W_h1h1)
    
    //    Store gradients for weights
    dW_h1h2 += grad_H2_t * H1_t
    dW_h1h1 += grad_H1_t * H1_prev
    dW_xh1  += grad_H1_t * X_t
    
    // 4. Recurse Backward in time
    return BackwardPass(t-1) with (grad_H2_t, grad_H1_t)
```


### How RNN Work 
RNN born to solve the problem of dependency and capture the relation between sequence data (time-series, predict the next word using the previous word). 

**Recurrent** in RNN mean **repeat itself for each timestep** represent á RNN cell. (1 RNN cell == 1 timestep). In other word, RNN create a Feedback loop to gain experience for each piece of information. 
![[Pasted image 20251221150806.png]]
At each Timestep, the previous cell will pass its experience to the next cell create a Feedback loops, thus connecting all cell together making weight become Shared Weight.   
![[Pasted image 20251221151244.png]]

+ $ This can be **very useful for predicting Sequence Information, this mean the previous piece of information give information to predict the next information.**  For example, predicting Next Word using the Previous Word or predicting stock, 

### Constructing RNN using MLP
Another way to see RNN is throug practical practice. For the predicting "Next Word" problem.  

In NLP, we token each word for identification purpose (unique) then convert each of them into vector format so machine can understand easier by embedding them. 
![[Pasted image 20251221151917.png]]

Before using RNN ideas, people often asked: "Why don't use MLP and Stuff", okay let start from MLP shall we. Started from the simplist ideas is passing all word into a Neural Network with each input passing through a Non-Linear layer of activation function z, then concatinate them into 1 vector.  
![[Pasted image 20251221152305.png]]
+ ! But here the problem, 
	1. **Fixed-Length inputs:** Standard MLP must have *fixed number of input and outputs* -> Unsuitable for variable-length sequene like problem. (e.g., text, time-series, user interaction histories). **Limited to Long Context information like predicting word in a sentence probelm**
	   
	2. **Inability to learn Temporal dependency:** This mean MLP ***learn the relationship between word** in a sentence but **not their dependency and sequential order*** (if this word come first then what likely to come after) because all inputs are flattened. 
	+ $ Learn which word more likely to happend but not really understanding 
		e.g. word position. 

After Non-Linear layer (z), we know that MLP have learn relationships between word but not the dependency/sequential information. 
+ ? How can we teach the model to predict the next infor using the previous infor.
+ $ Simple, just passing them through eachother. So the next activation func, also use the information from the previous layer. 
![[Pasted image 20251221155115.png]]
+ ! However, just connect Non-Linear with Non-Linear will ignore the normalization step at the activation function (Squash value to -1 and 1 using Tanh)
+ $ So we would need to add previous output value with the current next value before pass them through the Activation.
![[Pasted image 20251221155801.png]]
To make all step similar, we could add h_0 and b_hh as 0 to the first cell activation layer.
![[Pasted image 20251221155922.png]]
+ @ There you go, that **RNN** or should I say **MLP to RNN**.

Simplified everything, this is our MLP to RNN neural network. With the first layer as input, second layer as RNN cells with the curvy arrow mean Recurrent, and the given RNN cell represent the last layer give out it prediction.  
+ ? Example for 1 RNN cell.
![[Pasted image 20251221160237.png | 333]]

![[Pasted image 20251221161219.png]]

+ ? Stack of RNNs example. With 2 RNN stacked together, we just repeat those 2 RNN cell for each word with only the last cell $k_{2}$ predict the next word. 
![[Pasted image 20251221161303.png]]

### Backpropagation Through Time (BPTT)
**Example for RNN forward propagation:**
Let start from abstract. Here a 1 RNN network through multiple timestep with multiple cell. With V as the output Weight, U as the input Weight come with each input word, and W is the shared weight of 1 RNN network. All of these are Weight the model need to udpate. In this step, just apply Backpropagation for all Weight.   
![[Pasted image 20251221162741.png# left  | 433]]
If there are multiple Stack of RNN, then that just more Derivative through the Derivative Chain.   

### A Deeper Look at 1 RNN cell
Example for the last RNN Cell. Every **other cell look the same without the softmax step.**  
![[RNN_BPTT_origin.png]]
First, let look at our derivative target of this cell. (other cell repeat the same, just different input/output value)
**Purple Node as the Update Node.** 
 
**V ($W_{hy}$) - The Top purple node** at top right $W_{hy} h_{t}$ have 2 arrows whereas. **(Output Layer Connection** for **1 stack RNN**, **Hidden-to-Hidden Layer** for **multiple stack RNN)**
+ Input arrow $y_{t}$ is the Weight *FROM* the previous Hidden layer. 
+ Left output arrow $W_{hy}$ is the Weight pass *TO* the next Hidden Layer.

**U ($W_{xh}$) - The Lower purple node** at bottom: input $x_{t}$ with its Weight $W_{xh}$ **(Input Weights - X.W + b)**

**W_out ($h_{t-1}$) - The Middle purple node** at the left **(pass Shared Weight to the Past/Previous RNN cell)**
+ $W_{hh}$ - Shared Weight from the previous timestep.
+ $h_{t-1}$ - Output (activation function value) from the previous timestep.

**W_in ($\partial h_{next}$) - The Middle Green node** at the right basically **copy then sum the Future Prediction Error with the Current Prediction Error** and pass to activation func `tanh` to calc derivative.

![[Pasted image 20251221172644.png]]

