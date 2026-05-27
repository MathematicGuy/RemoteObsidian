![[Pasted image 20260128134608.png]]

![[Pasted image 20260128134650.png]]

![[Pasted image 20260128134704.png]]

![[Pasted image 20260128134720.png]]

![[Pasted image 20260128134742.png]]
Momentum as memory
L2 regression loss for better memory management


![[Pasted image 20260128134758.png]]
Note: $i \equiv 0 \space (\text{mod(C(l)})$ mean if step $i$ divided by the chunksize $C(l)$, the remainder is 0. then update $\theta(f_{l})_{i+1}$
	because we update by chunk size, with one chunk pass for each step, we could check if the step is divisible then update each memory block.  

![[Pasted image 20260128134817.png]]

![[Pasted image 20260128134845.png]]

![[Pasted image 20260128134911.png]]

