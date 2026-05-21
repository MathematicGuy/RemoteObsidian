![[Pasted image 20251225213655.png | 455]]

**For LSTM:**
+ **Translation Task:** Input Length $\neq$ Output Length.
	![[Pasted image 20251225215015.png | 424]]

+ ? At $\hat{y}$ and before $J_{n}$ is a Fully Connected Layers for pred word. 
![[Pasted image 20251225215339.png]]
Teacher Forcing - upadate gradient in small region to help model convergence better, f

Regular Attention Score - you calculate Attn Score for each previous token at previous timestep -> multiply the Attention score between q_1 to $k_{i}$.  
![[Pasted image 20251225220507.png]]

**Self-Attention:** so each words can learn the relationship between itself to itself and itself to every others word in the sentence. 
	Query = Key = Value = Embedded
![[Pasted image 20251225224319.png]]
+ $ **Head is the combination of Q, K, V -> Head(Q, K, V), that why its call Attention Head** where **Each Head try to capture a different Meaning of the sentence.** 
+ ? e.g. Q_1, K_1, V_1 combine is a Head of Output 1. Q_2, K_2, V_2 is another Head of Output 2. 
	- **Head 1 (Grammar):** Might focus on **syntax**. For example, it tracks which verb belongs to which subject (linking "run" to "athletes").
	- **Head 2 (Pronouns):** Might focus on **reference**. It looks for what "it" or "he" refers to (linking "it" to "the ball").
	- **Head 3 (Position):** Might focus on **neighbors**. It pays attention only to the words immediately next to the current word.
	- **Head 4 (Semantics):** Might focus on **meaning**. It links "King" to "Queen" or "Man" to "Woman".

If the number of head is 8, EACH Head calc Attn output a matrix size $(Seq\_{len \times d_{k}})$ where $Seq\_len = 100$ and $d_{k}=64$.
	
-> This mean each head have $d_{k}=64$ -> $64 \times 8 = 512$ total dimension after concat. Note that *concat is like add another matrix ontop of the original*, so its lengh or sequence length don't change, only its Dimension. 

![[Pasted image 20251225231417.png]]

![[Pasted image 20251225231231.png]]
For the matrix to pass through FFN layer, we must expand its embed dim to 1024. That mean matrix size when pass through the first Linear layer is 32 x 50 x 1024. That it. 

# Transformer for Text Classification
Note: `pretokenizer = Whitespace()` - looks for spaces (tab, whitelines, etc.) and break the sentence into individual chunks (tokens).  
	For example, it turns `"We are learning AI"` into `["We", "are", "learning", "AI"]`

Not use Attention bc its use Tokenzie by appear frequency