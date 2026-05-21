**Finetunning for task:** MNLI, NER, SQuAD. 


![[Pasted image 20260414213143.png]]
constant - hằng số dùng để thực hiện quantize
RMSNorm - Root Mean Square Normalization (Pre-normalize): normalize tr'c khi tính thay vì qua 1 lớp Linear rồi mới Normalize.

Masked grouped query attention 
	"group query" - QKV
Quantize -> ít RAM hơn, nhưng train lâu hơn. obviously. 

| **Feature**          | **The "Real-World" Analogy**                               | **Why we use it**                   |
| -------------------- | ---------------------------------------------------------- | ----------------------------------- |
| **NF4**              | A ruler with more marks where the most "action" is.        | Better accuracy for 4-bit weights.  |
| **Double Quant**     | Compressing the list of instructions on how to decompress. | Saves VRAM on metadata (constants). |
| **Paged Optimizers** | Using a backpack (CPU) when your pockets (GPU) are full.   | Prevents "Out of Memory" crashes.   |