![[Pasted image 20260208203917.png]]
patch cho cho toàn bộ ảnh = HxW của ảnh / HxW của Patch = 7 x 7 = 49


![[Pasted image 20260208204558.png]]

Catcontinate -> ghép số chiều. e.g. dv = 16, dh = 16 -> FusionLayer F(v, q) = 32 chiều. -> Chỉ có thể Cộng và Nhân vì nó ko làm thay đổi số chiều trong Final Pred
![[Pasted image 20260208204605.png]]




![[Pasted image 20260208230558.png]]
-> Do phép nhân hoạt động như cơ chế chọn lọc thông tin, trong khi phép cộng và phép ghép nối có thể không có khả năng này.


![[Pasted image 20260208231942.png]]

![[Pasted image 20260208231948.png]]

vì 225 / patch 32 = 7. N = WxH. 
Batch = 3, Dim = 768
Visual: [B,N,D]→[3,49,768]
-> Linear (B, L_image=N_image, D) giữ nguyên -> [3, 49, 512]

Text: [B, L_text] = [3, 15]
Linear Proj (B, L, D) -> 3, 15, 768

Cross-Attn Layer 1
- **Áp dụng cho Step 5a (V2T - Visual** to Text):
    - **Query** = Visual [B,N,H]=[3,49,512].
    - **K/V** = Text [B,L,H]=[3,15,512].
    - **→ Output Shape** = Query Shape = **[3,49,512]**.
	
- **Áp dụng cho Step 5b (T2V - Text** to Visual):
    - **Query** = Text [B,L,H]=[3,15,512].
    - **K/V** = Visual [B,N,H]=[3,49,512].
    - **→ Output Shape** = Query Shape = **[3,15,512]**.


Input Visual = **[3,49,512]**.
Input Text  = **[3,15,512]**.
concat theo trục token/sequence 
Visual và Text -> [B, L, H] = [3, 64. 512]
`[REG]` Token: chèn thêm 1 token mới vào đầu hoặc cuối chuỗi hiện có. Token/Sequence_length + 1 đơn vị.
	Add `[REG]` -> [B, L + 1, H] (as I though) -> [3, 65, 512]



![[Pasted image 20260208233823.png]]

![[Pasted image 20260208233832.png]]

N = (Width or Heigh / Patch)^2 
**Visual:** [B, N, H] -> [5, 196, 768] -> Vision Proj (Dv -> H) [B, N, H] = [5, 196, 256]
**Text:**  [B, L, H] ->  [5, 30, 768] ->  [5, 30, 256] 
`[REG]` **embedding** ->  [5, 1, 256]

**Concat:** [REG] + Visual + Text -> [5, 227, 256]
**POS Embedding:** Embedding(227, 227)


![[Pasted image 20260208234713.png]]

Input: [B, S, H] = [5, 227, 256]
Self-Attn + FFN (giữ nguyên): [5, 227, 256]
227 -> [5, 256]


576 => [2, 617, 512]
431.9
[2, 472.9, 512]
n2 = 331.03


618

