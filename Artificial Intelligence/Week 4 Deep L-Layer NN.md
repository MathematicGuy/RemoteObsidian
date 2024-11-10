![[Pasted image 20241109161739.png]]

### Matrix Dimension in NN
![[Pasted image 20241109162307.png]]
For $W^{[l]}$ it basic matrix dimension can be use to represent input and output data. For instance `(outputs, inputs)` for $W^{[1]} = (3, 2)$ so the general fomular for each layer dimension is:
$$W^{[l]} = (n^{[l]}, n^{[l-1]})$$
note that dimension of $b^{[l]}$ must be equal to $W^{[l]}$ for matrix addition (or broadcasting in code). Since b is a array, b dimension should be $$b^{[l]} = ()$$

