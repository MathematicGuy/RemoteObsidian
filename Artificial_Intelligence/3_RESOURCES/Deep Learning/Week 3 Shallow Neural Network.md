![[Pasted image 20241108151559.png]]

![[Pasted image 20241108151639.png]]
Note: $a^{[2](i)}$ mean layer 2 example $i$.
![[Pasted image 20241108160707.png]]

**Innitialize Paras**
```python
def initialize_parameters(n_x, n_h, n_y):
    parameters = {"W1": W1,
                  "b1": b1,
                  "W2": W2,
                  "b2": b2}
    
    return parameters

def forward_propagation(X, parameters):
    return A2, cache

def compute_cost(A2, Y):
    return cost

def backward_propagation(parameters, cache, X, Y):
    grads = {"dW1": dW1,
             "db1": db1,
             "dW2": dW2,
             "db2": db2}
    
    return grads

def update_parameters(parameters, grads, learning_rate = 1.2):
    parameters = {"W1": W1,
                  "b1": b1,
                  "W2": W2,
                  "b2": b2}
    
    return parameters
```


Simple Chain Rule for 2 Layers ANN
![[Pasted image 20241108154739.png]]

![[Pasted image 20241108155924.png]]

