**Input Weight of each RNN nodes are shared.** 
Only the **predicted/activated Weight (after ReLU of each Node) are tune differently.** 

`[UNK]` - token for unknow number/word
`[pad]` - padding to make all sentence have the same length. 

![[Pasted image 20251220210806.png]]

![[Pasted image 20251220211639.png]]


![[Pasted image 20251220213423.png]]

RNN trong code có thể lấy cả Weight trong Hidden Layer. 
RNN khi tính số Param ko tính  của Sharing.
![[Pasted image 20251220223302.png]]

![[Pasted image 20251220223723.png]]

