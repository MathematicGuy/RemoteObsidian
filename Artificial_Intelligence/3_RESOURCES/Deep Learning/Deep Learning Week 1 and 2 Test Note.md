broadcast: element-wise calc
example:
```python
a = np.array([[2,1], [1,3]])
a*a 
```
> `array([[4, 1], [1, 9]])` # multiply element-wise 


![[Pasted image 20241106165135.png]]
![[Pasted image 20241106172003.png]]

```python
# GRADED FUNCTION: predict

def predict(w, b, X):
    '''
    Predict whether the label is 0 or 1 using learned logistic regression parameters (w, b)
    
    Arguments:
    w -- weights, a numpy array of size (num_px * num_px * 3, 1)
    b -- bias, a scalar
    X -- data of size (num_px * num_px * 3, number of examples)
    
    Returns:
    Y_prediction -- a numpy array (vector) containing all predictions (0/1) for the examples in X
    '''
    
    m = X.shape[1]
    Y_prediction = np.zeros((1, m))
    w = w.reshape(X.shape[0], 1)
    
    # Compute vector "A" predicting the probabilities of a cat being present in the picture
    #(≈ 1 line of code)
    # A = 
    # YOUR CODE STARTS HERE
    z = np.dot(w.T, X) + b
    A = sigmoid(z)
    
    # YOUR CODE ENDS HERE
    
    for i in range(A.shape[1]):
        
        # Convert probabilities A[0,i] to actual predictions p[0,i]
        #(≈ 4 lines of code)
        if A[0, i] > ____ :
            Y_prediction[0,i] = 1
        else:
            Y_prediction[0,i] = 0
        # YOUR CODE STARTS HERE
        
        
        # YOUR CODE ENDS HERE
    
    return Y_prediction
```

```python
def initialize_with_zeros(dim):
def propagate(w, b, X, Y):
def optimize(w, b, X, Y, num_iterations=100, learning_rate=0.009, print_cost=False):
def predict(w, b, X):
```

