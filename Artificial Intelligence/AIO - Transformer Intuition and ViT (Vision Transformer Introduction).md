```ad-important
**Objective**
+ From Attention mechanism to Transformer (Encoder-only)
+ From Transformer to Vision Transformer
+ How Vision Transformer work in a forward pass
```
## [Key ideas of ViT Summarization](https://www.pinecone.io/learn/series/image-search/vision-transformers/) 

## Seq2Seq: Encoder and Decoder in LSTM
+ $ Seq2Seq mean (input) Sequence to (output) Sequence (array of text), it like google translate vietnamese to english.
+ ? Seq2Seq Architecture include: 
	+ **Input:** often numeric time series data
	+ **Decoder:** Numerize input data, convert sentence (input) into vector/matrix (State)
	+ **State** (Though vector, capture all information of input sequence)
	+ **Encoder:** Convert encoding into a sequence in target language (output)
![[Pasted image 20250308171048.png]]
 Trong TH mà inference chỉ có câu đầu vào mà không có câu đích (vì đang dự đoán) thì từ đầu tiên sẽ có t=0 (i.e. time-step) ký hiệu bằng thẻ `<START>`.

+ ? **Training vs Inference:** khi train input có label, infer ko có label. Khi Training, model sẽ cho bik tr'c từ tiếp theo luon thay vì dự đoán (phương pháp này gọi là Teacher Forcing). Còn khi inference, model lấy dự đoán (hiện tại) tại t=0 làm label để dự đoán cho từ tiếp theo thoi. 

## Attention Mechanism
**Step 1: Scaled Dot-Product Attention**
Calculate **Attention Score** for each token (word) in the current time-step, then put them input $e^t$ list. $$\frac{q_{n}k_{1}^T}{\sqrt{d_{k}}}$$ Where:
+ $q_n$ (Query vector) represent the query for the n-th token in the sequence. (từ mà mìh muốn dự đoán)
+ $k_{1}^T$ (Key vector Tranpose) represent the **key** for the **first** token (word) in the sequence.
 + $d_{k}$ (Dimension of the key/query vector) is The **size of each key/query vectors** vector size in self-attention) - embedding depth
	 -> vector q . vector k divided by its vector size / magnitude -> that like Cosine Similarity. [[Why Attention Score don't use Cosine Similarity]]
	
+ $q_{n}k_{1}^T$ computes a **similarity score** between the query of the current token and the key of the first token. (reference: [Dot Product](https://en.wikipedia.org/wiki/Dot_product))
+ The **division by** $\sqrt{d_{k}}$ is a **scaling factor** to prevent large values that might lead to unstable gradient when applying softmax. 
![[Pasted image 20250308174003.png]]

Then **Convert $e^t$ to Softmax Distribution/Attention Distribution** for **Attention Evaluation** (i.e. which word is the most important for $q_{1}$) with **each value** called **Attention Weight**.
+ $ **Softmax to Attention Score:** The softmax function converts **raw attention scores into probability distribution**, determind **how much focus the query $q$ should give to each key $k$.** The dot product **$q.k$ measure similarity**, and softmax ensure all keys contribute proportionally instead of attending to just 1 or 2. This **allow model to consider all possible keys while focusing more on the most relevant one.**
	+ ? Softmax help find **which key $k$ is most relavent** to a given **query** $q$ **(i.e. give the most context)**. With **key** $k$ represents the available information (e.g. words that provide context) and query q represent what we are looking for (e.g. word needing context).
![[Pasted image 20250308175331.png]]
+ $ Finally, repeat calculating Attention Score for each $q$

V value of Key K for query $Q_{n}$. 
![[Pasted image 20250309143108.png]]
+ ? Attention(Q, K, V) for $q_{1}$  ![[Pasted image 20250309143724.png]]

VD: khi dự đoán, token đầu sẽ luon luon là `<Start>` và cuối là `<End>`, nếu thừa slot thì sẽ thêm `<PAD>` vào, nhưng do softmax nhiều khi `<PAD>` có thể là 1 từ nào đó.
![[Pasted image 20250309144623.png]]

## Transformer Encoder
+ ? Transformer is base on **Seq2Seq + Attention Mechanism**
Architecture:
	N Encoder layer
	N Decoder Layer
Core technique: Attention
Loss function: Cross-Entropy

### Transformer Encoder
-> ViT mainly use Encoder (don't use Decoder)
**Inputs:** token
**Inputs Embedding:** token to vectors (tensors)

#### Multi-Head attention
![[Pasted image 20250309145748.png]]
Take (Q, K, V) as inputs for each token $x_{1},x_{2}, x_{3}, x_{4}$

**Self-attention**
+ ? Calculate Attention Score of each q for all k, then apply Softmax to get Attention Output $\alpha$. For instance, with $q_{1}$ we got $\alpha_{1}$.  ![[Pasted image 20250309150029.png]]
+ Finally multiplying by V (v of each token) then you got $Attention(Q, K, V)$ ![[Pasted image 20250309150600.png]]
**note:** rows by columns
$$
[0.7, 0.2, 0.1] \times 
\begin{bmatrix}
1 & 1 & 1  \\
0 & 1 & 0 \\ 
0 & 0 & 0 
\end{bmatrix} = [0.7, 0.9, 0.7]$$

Repeat for each token, This Self-Attentionstep allow model to learn the relationship between word in the sentence.  
![[Pasted image 20250309151309.png]]
+ ? Self ám chỉ việc lấy chính những câu nguồn (input) để tính toán Attention for từng câu của câu nguồn luon. -> Để tìm mqh của Q vs từng K. 

**Ignore the order of words in the sequence ?**
in LSTM/RNN/GRU, understand information seq by seq, with only Self-Attention, the model might fail to recognize context of the data. (Ex: in english, after verb is adj -> recognize by reading seq by seq)   
+ ? Need method allow model to understand the position of sentence and word, so its can fully comprehence the context.


+ $ **Positional Encoding (vector P):** The position of a token in a sentence as unique representation - **each position is mapped to a vector.** 
+ ? Cộng vector P vs vector I (input) -> I embedding with positional information.
![[Pasted image 20250309210001.png]]
>Cộng thêm Positional embedding để cho Inputs Embedding nó có thông tin về tính thứ tự bên trong nó.


**Multi-Head Self Attention**
+ ? Split into the mutiple attention head (process independently) -> self-attention -> concat.
 ![[Pasted image 20250309210955.png]]
 + ? 1 Weight cho cả Q, K, V thì model có thể học ko tốt, nên mình tách nhỏ Q, K, V thành các ma trận nhỏ hơn với các weight lần lượt là $W_{Q}, W_{K}, W_{V}$ để mô hình có thể tự học các thông tin khác nhau 1 cách độc lập.  
 + ? Ma trận con đc chia ra khỏi ma trận lớn Q, K, V gọi là các Head. Số Head = 5 nghĩa là chia ma trận Q, K, V ra làm 5 phần.
 + $ Với input đầu vào là 3 ma trận (Q, K, V) shape SxD, t chia mỗi ma trận thành các Head (H) để tính Attention Score độc lập cho từng Query Q gọi là O có kích thước $H \times S \times (D/H)$, rồi gộp lại (concat) thành 1 ma trận kích thước $S \times D$ 

#### Add & Norm
##### Layer Normalization
+ ? Layer-Norm mà ko phải Batch-Norm là do dữ liệu text. 
+ ? Phần skip-connection sau Positional Encoding được Cộng với phần Norm. 
![[Pasted image 20250309212821.png]]
#### Feed Forward
+ ? Dữ liệu Attention Score Feed Forward Network để học đặc trưng phi tuyến (non-linear) của input đầu vào (dim nhỏ -> dim lớn). Sau khi học được nhiều thông tin hơn từ dim lớn, mình nén nhữg thôg tin học đc về chiều không gian nhỏ (dim nhỏ) và tiện lợi cho việc truyền thông tin sang lớp Transformer Block tiếp theo. 
note: `N x` bên phải khung hình chứa Multi-Head Attention đến `Add & Norm` được gọi là 1 Transformer Encoder Block.
![[Pasted image 20250309213847.png]]
+ ? Lý do có nhiều Encoder là để xử lý các dữ liệu quá phức tạp -> nhiều lớp Encoder, Embedding dim, Transformer Block hơn.

### Text Classification
> Bài Text Classification cần có 1 cái vector 1D để đẩy vào Classifier để dự đoán. 
![[Pasted image 20250309220758.png]]

### Vision Transformer
>Image contain spatial information. Can we tokenize an image ?
>![[Pasted image 20250310152658.png]]

![[Pasted image 20250310152356.png]]

#### Linear Projection
+ ? Project mean **Encode higher dimension vector to lower dimension vector**. (e.g. 3D -> 1D) 
![[Pasted image 20250310152717.png]]
Image divide into Patchs -> Flattened -> 1D vector 
![[Pasted image 20250310153026.png]]
To encode 3D channel into 1D channel, we simply apply a Convolution layer to extract feature that the same size patch size.   
![[Pasted image 20250310153205.png]]

+ ? `[cls] Token` or class token acts as a special token that aggregates information from all patches during the forward pass.  Traditional ViT only have 1 `[cls] token` and can only produce 1 prediction, single-label classification.
+ ? MSA mean **Multi-head Self Attention**, MLP mean **Multi Layer Perceptron**, LN mean **Layer Norm**.
![[Pasted image 20250310161200.png]]

