![[Pasted image 20250227153305.png]]

>Được phát triển giống như cách não ghi nhớ thông tin -> tập trung vào shorterm memory.
![[Pasted image 20241220200750.png]]

+ ? **Recurrent (hồi quy)** means **Feedback loops**
![[Pasted image 20241220201325.png]]
+ ? **Also mean Sharing Weights**. 3 neurons nhưng dùng chung 3 cái weights. 
![[Pasted image 20241220201448.png]]
RNN vd NN: Each RNN nodes only have 2 output (i.e. connected to other 2 nodes) 1 in the hidden state, and 1 in the output. 
![[Pasted image 20241220201553.png]]
+ ? **Each Nodes directly impact the node after it**, unlike MLP where each nodes in the previous layer connected to each nodes in the later layer. 
![[Pasted image 20250227154639.png]]

**Traditional NN vs RNN**
![[Pasted image 20241220201729.png]]
![[Pasted image 20241220201740.png]]
>This features allow NN to remember and predict the future better base on past experiment.

**Neural Network:** Feed forward predictions are only base on the target value in the training data.. 
![[Pasted image 20250227155242.png]]
**Recurrent Neural Network:** Each prediction are **depend on the training data and the previous prediction Weight**.
![[Pasted image 20241220201922.png]]
By this method, weight and bias are Shared across every inputs. No matter how many times we unroll a recurrent NN, we never increase number of weights and bias to train.
![[Pasted image 20241220202004.png]]
**A more intuitive way to look at RNN:** previous layers not responding to making prediction but passing experience.
![[Pasted image 20241220202127.png]]

**Different types of RNNs** (the same method as above but Many)
![[Pasted image 20241220202348.png]]

![[Pasted image 20241220202816.png]]

predict word to word
![[Pasted image 20241220202825.png]]

### Why RNN is not use Often ?
Vì là tham số truyền tới tham số nên sẽ gây ra vấn đề Gradient Exploding.
![[Pasted image 20241220203033.png]]
Or Vanishing Gradient
![[Pasted image 20241220203149.png]]
How to avoid Exploding-Vanishing Gradient: By skipping connection: instead of go through one by one, each layers go directly to the last layers or n layer after it.

## 2. Three Stages in a Single LSTM Unit
>Traditional **RNNs oftern struggle to remember older information** due to vanishing gradient problem. **LSTM's address this by uing a "cell state" that can carry information across many timesteps.**

### 2.1. Key Components of an LSTM
In LSTM there are 3 **gates**, plus an internal memory (**cell state**). Think of it like a valves controlling water flow in a pipeline:
1. **Forget Gate:** decide how much past information to to keep (~ throw away).
2. **Input Gate:** decides how much new information to add
3. **Output Gate** decide how much information the cell to output at the current timestep.

### 2.2. Why Sigmoid and Tanh ?
**Sigmoid** $\sigma$ outputs values from 0 to 1. Perfect for deciding how much infor to be **Remember** (e.g. 0.5 mean remember 50%):
+ **0** mean "remember NO information"
+ **1** mean "remember ALL information"

**Tanh** outputs values between -1 to 1. Completely fit for **Updating** information using add (+) and substract (-):  
+ **Squashing the data into a manageble range** to **avoid exploding values**
+ **Adding or Substracting** from the cell State by **allowing both positive and negative signals**

```ad-summary
 Combinning Sigmoid and Tanh balance what to keep, forget and output (updated value) at each timestep, helping the network to learn both short-term and long-term dependency effectively.
```

### 2.3. Abstract LSTM Architecture Explanation 
#### 2.3.1. LSTM Terms Explanation 
+ ? **Scenario:** there are 2 LSTM cell (like above). Imagine the **1st cell (not show) connected to the 2nd cell above.**  
Note 
+ **State between the first cell/layer to the last cell/layer called hidden state $h_{t}$.** 
+ State passing from the 1st to the last cell called the **cell state $C_{t}$.**


An LSTM cell at time $t$ **taken in:**
+ The current input vector $x$ at timestep $t$ called $x_{t}$ (e.g. normal input like NN)
	
+ The previous hidden state $h$ at previous time step called $h_{t-1}$ represent the prior knowledge learned from the last LSTM cell (i.e. 1st cell).  Hence **short term memory.**
	
+ The preious cell state called $C_{t-1}$  **represent the long term memory (like a conveyor bell) passing through all LSTM cells to transfer all past knowledge**. And like in real life, past memory faded each timestep and replace by fresh memory in the current timestep.  
	
Its **produces**
+ The new **Hidden state** $h_{t}$ (i.e. fresh updated memory)
+ The **updated Cell state** $C_{t}$ (i.e. fresh updated long-term memory)

LSTM's gates:
+ **Input** gate $i_{t}$ (`i` for input)
+ **Forget** gate $f_{t}$ (`f` for forget)
+ **Output** gate $o_{t}$ (`o` for output)
![[Pasted image 20250228093537.png]]

#### 2.3.2. LSTM Fomular Explanation
**NOTE:**
+ What Sigmoid and Tanh doing is compress/squash inputs to a value range (non-linearity) 
	
+ ? Each gate in an LSTM, forget gate `f_t`, input gate `i_t` and output gate `o_t` has its own unique set of weights (e.g. `W_f, W_i, W_o`) and biases (e.g. `b_f, b_i, b_o`) . These weights are learned during training and are distinct for each gate, making the model roburst to changes. 
	(i.e. how much of the long-term memory to forget, how much of the new information to add to long-term memory, how much of the updated information to output)
	
+ **[0, 1] Multiplication indicate:** scale percentage or contribution percent. For example
	+ ? In formula $C_{t}$ multiplication $C_{t} \times f_{t}$ was used to scale the previous cell state $C_{t-1}$ by forget gate $f_{t}$, which range from 0 to 1.
	+ $ The scaling value $f_t$ **depend on weather old information remains relevant given the new input $X_t$ and previous hidden state $h_{t-1}$**
	
+ **[-1, 1] Addition indicate a Direct Update:** updated value. For example:  
	+ ? The cell state $C_{t}$ was updated by adding the retained old information $f_{t} \times C_{t-1}$ with the new information $i_{t} \times \tilde{C}$. 
	+ $ This like when human update their understanding, the LSTM balances what to keep from the past with what to add from the present, like how human forget bad information/irrelevant by replacing them good/relevant information.
	
+ Just like in a standard neural network, each computation in an LSTM includes a bias term. For example:
	- Forget gate: $f_t = σ(W_f [h_{t-1}, X_t] + b_f)$
	- Input gate: $i_t = σ(W_i [h_{t-1}, X_t] + b_i)$
	- Candidate cell state: $\tilde{C}_t = tanh(W_C [h_{t-1}, X_t] + b_C)$
	- Output gate: $o_t = σ(W_o [h_{t-1}, X_t] + b_o)$
	+ $ These biases shift the activation functions (?), increasing the model’s flexibility to fit the data.
	
+ At each timestep $t$, the inputs $[x_{t}, h_{t−1}]$ (which are not learnable parameters) are multiplied by the **learnable** weight matrix $W_f$ (plus a bias bfbf​).
	+ ? If a new word ($X_t$) is positive (e.g. "great") and the past context ($h_{t-1}$) is also positive, the gates might adjust to retain the old positive sentiment (high $f_t$) and add the new positive information (high $i_t$).
	
	
+ $f_{t}\times C_{t-1}$ represent how much of the old information should be kept. 
	In sentiment analysis, if $X_{t}$, $h_{t-1}$ is high, then $f_{t}$ will be high also. Meaning "remember more past information since the curerrent information is relevant"

+ $\tilde{C}$ is candidate cell state computed using the tanh function, value ranging from `[-1, 1]` show how `contradiction (-1)` or `relevant (1)` between the old information and the new information. 
	
+ $i_{t} \times \tilde{C}:$ represent how much of that contradiction/relevant should be updated 
+ $C_{t}$ represent the update between the old and the new information.
	
+ $o_{t}$ represent how the output percentage. .
+ $h_t$ represent how much of the updated information shoud be output in the hidden state prior to the current information (i.e. $h_{t-1}$ and $X_{t}$). 
	
+ ? The act of cell states **passing weight across all LSTM cells without using activated function called Skip Connection** 
![[Pasted image 20250228162227.png]]

+ ? **Long-term memories (Top green line):** contain weight/information past through from the previous layer, this memory contain the knowledge of the previous layer passing through the next.  
![[Pasted image 20241220204125.png]]
+ ? **Short-term memories (bottom red line):** or "working memory" that the network uses at each timestep to make immediate decisions. 
![[Pasted image 20241220204522.png]]
+ @ In summary, the first block take and sum the input `1*1.63` along with the information (weight) from the previous layer `1*2.70` + bias of `1.62` then use the sigmoid 

**LSTM fomula summarize**
![[Pasted image 20250301002817.png]]


## GRU (Gated Recurrent Unit)
![[Pasted image 20250228162604.png]]
GRU architecture simplied LSTM by instead of having both long-term and short-ter, GRU **merges** them into a single separate states (hidden state $h_{t}$ and cell state $c_{t}$). 

+ Like LSTM forget gate, **GRU reset gate $r_{t}$**  **decides how much percent of the previous information to reset** base on how relevant the new information $x_{t}$ and previous information $h_{t-1}$ is. 
+ Reset Gate $r_{t}$ decides how much of the previous hidden state $h_{t-1}$ contributes to the creation of the **new candidate** $\tilde{h}_{t}.$ 
+ $r_{t}\odot h_{t-1}$  tell us how much % of $h_{t-1}$ to retain with 0 mean reset. Represent "how much old state is used when creating the new candidate"   
+ $W_{i\tilde{h}}x_{t} + W_{h\tilde{h}}(r_{t} \odot h_{t-1}) + b_{h\tilde{h}}$ Is the addition of $x_{t}$ and $h_{t-1} \times r_{t}$ with weight and bias. Represent how much % of the hidden state $h_{t-1}$ (information in the previous cell) getting added to the current input state (current information), in other word it is the *updated information*. 
+ $\tilde{h}_{t}$ is the candidate hidden state output, its using tanh to squash *updated information* values to range `[-1, 1]`.
![[Pasted image 20250228163514.png]]
+ Update gate $z_{t}$ decides how much of the candidate $\tilde{h}_{t}$ to integrate into the final hidden state $h_{t}$. Which influence by how relevent the *updated information is, if relevent then $z_{t}$ is bigger else its get smaller. 
+ $z_{t}  \odot  \tilde{h_{t}}$ represent how much of the *updated information* getting updated to the hidden state (i.e. short term memory) 
+ Final Hidden State $h_t$ blend the old with the new updated information.   
	$h_{t}$ take the sum of  $((1-z_{t}) \odot h_{t-1})$ and $(z_{t} \odot \tilde{h}_{t})$ represent the tradeoff between newly added memory and the short-term memory. So the more relevant or important the new information is, the less of the old information retain in the short-term memory (i.e. the more of the old information be forget). 
![[Pasted image 20250228232042.png]]
Fomula Summarize
![[Pasted image 20250301002736.png]]


## Time Series (Basic Knowledg)
![[Pasted image 20250301104143.png]]

![[Pasted image 20250301104200.png]]


### Multi-step vs Iterative Forecasting

#### Single-step Forecasting
![[Pasted image 20250301104545.png]]
>Sử dụng **toàn bộ tập tham số** trước đó để dự đoán time-step tiếp theo. 

**Iterative Multi-step Forecasting:** mô hình câp nhật bộ tham số sử dụng kết quả dự đoán (i.e. predicted value) của nó, để tiếp tục dự đoán T time-step sau đó.
![[Pasted image 20241220215742.png]]
**Multi-step:** sử dụng đúng 1 tập tham số để thực hiện nhiều dự đoán trong T time-step. 
![[Pasted image 20241220215653.png]]

**Full Size:** Sử dụng toàn bộ tập dữ liệu làm tham số để dự đoán những T time-step. 
**Window Size:** Giống như Batch Size, chỉ sử dụng 1 tập dữ liệu thay vì sử dụng hết toàn bộ dữ liệu để dự đoán T time-step.
![[Pasted image 20241220220039.png]]


**Rolling window** (Cross-Validation)
Với 1 tập dự liệu lớn, mình quét từng đoạn qua dataset gọi là subdataset, dùng trong đoạn subdataset đó 1 phần chọn để train, 1 phần đc chọn để test. Theo thời gian (time series), mình sử dụng rolling window để đưa ra dự đoán thực tế dựa theo n tập dự liệu tr'c nó.  
![[Pasted image 20241220220053.png]]

transformer: giúp giải quyết vấn đề phải tính tuần tự trong **Stacked RNN** bằng cách tính song song.
![[Pasted image 20241220223438.png]]

---
### Step-by-Step LSTM

**Forget gate layer**
![[Pasted image 20250214135349.png]]
$f_{t} = 1$  represent "preserve all past information" and $f_{t} = 0$ represent "forget all past information"
Forget gate allow new/updated data preserve it meaning when changes occured through time. (e.g. conversation between human through time)


![[Pasted image 20250214140244.png]]

---



