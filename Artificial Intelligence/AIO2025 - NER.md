CNN Output the same for 1D and 2D. ![[Pasted image 20260326145146.png | 444]]
In $Z_{i},$ vector shape (1,4) multiply with vector shape (4,1) become (1,1) vector. 
Flatten Input for FC is (1,1,4) - (batch_size, channel_out, sequence_length_out) 
![[Pasted image 20260326164531.png]]