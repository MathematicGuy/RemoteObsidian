## Method 1: Single Frame human activities detection using CNN and Classification MLP. 
![[Pasted image 20250119135838.png]]
+ $ This is a simple way to get a final prediction for the video is to **consider the most frequent one** which can work in simple scenarios but is **Falling** in our case and is not correct.

### Approach 2: Late Fusion 
![[Pasted image 20250119141659.png]]
+ $ Performing predictions on each frame independently, the **classification results are passed to a fusion layer that merges all the information and makes the prediction**.


### CNN walk through
>Before dive on to the next Approach, let revision what CNN offer in Activity Recognition ![[Pasted image 20250119142250.png]]
>**Each layer of a ConvNet learns features of increasing complexity** which means, for example, the **first layer** may learn to **detect edges and corners**, while the **last layer** may learn to **recognize humans in different postures**.

## Approach 3: Early Fusion
![[Pasted image 20250119142432.png]]
+ $ This approach merge the pixels of all images to de



## Method 5: Using Pose Detection and LSTM
![[Pasted image 20250119141314.png]]
>**Get landmark coordinates** of the person for **each frame** in the video. The feed the landmarks to an **LSTM Netwrok to predict the activity** of the person. 

---

**Problems with MLP in NLP**
+ fix length inputs 
+ learn information in order (i.e. sequence)
+ can't understand diff meaning of word in diff context. (e.g. the fly vs the fly fly in the sky)


### Recurrent Neural Networks ([RNN](https://nttuan8.com/bai-13-recurrent-neural-network/)) 
>Like MLP but with loop
+ [RNN fool-proof video](https://youtu.be/y9PLF2GsD-c?si=ylGbUg0h48mS77KU)

(Image below show 2 way to represent RNN since input and output in each state have the same size)
![[Pasted image 20250120130658.png]]
+ $ **Each time step** in an RNN **corresponds to a position in the input sequence**. At each time step, the **RNN processes two inputs: the hidden state from the previous time step and the current input from the sequence**. This recurrent mechanism allows RNNs to **capture temporal dependencies and context across the sequence**.

Result of the current Node pass through the next layer as input, hence recurrent:
+ $y_{t}: \text{output to the outside world}$
+ $h_{t}: \text{output to the next hidden layer}$ 
	If $h_{t}$ written as $y_{t}$ it mean output pass to the next time step.  
In Summary, there are 2 case:
+ 1 where you pass result to the `next time-step and outside` 
+ 1 where you pass result to the `next hidden layer and ouside`    
![[Pasted image 20250120130946.png]]

#### Key Terms and Definitions
1. **Input Sequence $(x_1, x_2, \dots, x_T)$:**
    - A sequence of inputs fed to the RNN at each time step $t$.
    - Example: A sequence of words in a sentence or a time series, squence of frames from 1 to 30 in the 30 frames video. 
      
2. **Hidden State ($h_t$):**
    - The RNN's memory or internal representation at time step ttt.
    - It depends on the previous hidden state $h_{t-1}$​ and the current input $x_t$​.
    - $h_t = f(h_{t-1}, x_t)$, where $f$ is typically a non-linear activation function (e.g., tanh or ReLU).
      
3. **Output ($y_t$​):**
    - The output produced by the RNN at each time step.
    - May be emitted at every time step (e.g., sequence-to-sequence tasks) or only at the final time step (e.g., sequence-to-vector tasks).
	
1. **Recurrent Connection:**
    - The mechanism through which the hidden state of one time step ($h_t$​) is passed to the next time step $(h_{t+1})$.
    - This enables the RNN to capture temporal dependencies.
      
5. **Recurrent Weights ($W_h$​):**
    - The weights associated with the hidden-to-hidden connection in the RNN.
    - These weights are shared across all time steps.
      
6. **Input Weights ($W_x$​):**
    - The weights associated with the input-to-hidden connection in the RNN.
    - These weights are also shared across time steps.
      
7. **Bias ($b$):**
    - A learnable parameter added during computation to increase flexibility and improve model fitting.
	
**Types of using RNNs**
![[Pasted image 20250120135153.png]]
1)  **Sequence to sequence (Seq2Seq):** squence of inputs and sequence of outputs. This usually used in predicting stock price where all previous elements (predictions) affect the prediction after its. *(price forecasting, translation)*
	- **Example**: **Language Translation**
	    - Input: A sentence in English: _"How are you?"_
	    - Output: The same sentence in German: _"Wie bist du ?"_
	- **Use Case**:
	    - Machine Translation
	    - Summarization
	    - Speech-to-Text
	      
2)  **Sequence-to-Vector (Seq2Vec):** also called as sequence to single but most RNN have multiple output thus vector is more accurate. This type only output at the last layer while ignoring all its previous outputs making its perfect for predicting result in realtime like word by word where each word make a impact to the final prediction.
	+  **Example: Scam or not**
		+ Input: Sequence of Text.
		+ Output: `Yes/No`
	+ **Use Case**:
		- Document classification
		- Sentiment analysis
		- Emotion detection
		
3) **Vector-to-Sequence (image captioning):** this type only take 1 input from the first layer then passing its output as input of the next layer and repeat. This way, the RNN can predict mulltiple outputs with only 1 input, which is prefect for captioning image where are features vector extractad by a CNN (typically). 
	- **Example**: **Image Captioning**
	    - Input: An image (i.e. a feature vector extracted by a CNN).
	    - Output:  `"A" -> "cat" -> " sitting" -> "on" -> "a" -> "couch"` 
	- **Use Case**:
	    - Image captioning
	    - Music generation from a theme vector
	    - Text generation based on an idea or topic
		
4) **Encoder-Decoder:** 
	**Encoder** be **given input for a couple of time-steps then output vectorized data** to the **Decoder** for **translation**. **Since the context can change if you don't see the whole context** so by Encoding the whole context before decoding can improve accuracy rather than encode then decode word by word.
		  Applied in POS (Part-of-Speech)

#### Backpropagation through time


+ ? Vanishing Gradient problem
	Gating mechanism
	
	
	

### Long Short Term Memory ([LSTM](https://phamdinhkhanh.github.io/2019/04/22/Ly_thuyet_ve_mang_LSTM.html))
[LSTM Parameters](https://www.kaggle.com/code/kmkarakaya/lstm-understanding-the-number-of-parameters)
[[Analyse Layer Effect for Deep Learning Network]]
	Use gate to stabilize the gradient during the training -> avoid Exploding/Vanishing Gradient. 

![[Pasted image 20250218120737.png]]

**i - input**
**c - cell state**
**o - output**
**t - time step**
sigmoid -> điều chỉnh lượng thông tin đi vào. 



---
### CNN + LSTM using TensorFlow
![[Pasted image 20250214101656.png]]
[github code reference](https://github.com/Jaykumaran/Action_Recognition_UCF101_CNN_LSTM.git)


**Bidirectional LSTM**
![[Pasted image 20250224124218.png]]
+ ? Bidirectional LSTMs learn contexts from left to right and right to left then concatinate them.  
+ $ The example above show, because of the influence of the information "left to right" feed through $\hat{y}^{(3)}$ the model know "apple" a fruit or company.

---
[[Body Language Decoder with MediaPipe]]

+ ? **Câu hỏi bảo vệ dự án:**
So sánh phương pháp (giống và khác giữa các phương pháp)
Dataset (so sánh hiệu quả giữa các dataset khác nhau)

Ý nghĩa của các chỉ số Validation

Tham số ? 
Công thức nào đưa vào phải giải thích dc, so sánh vs công thức (mà cùng giải quyết đc 1 vấn đề)

Đồ án tốt nghiệp làm theo hình thức nhóm. 

**Đồ án của mình tốt hơn như thế nào ? khi mình mới làm đồ án**

Thầy Đông - xử lý ngôn ngữ tự nhiên 

