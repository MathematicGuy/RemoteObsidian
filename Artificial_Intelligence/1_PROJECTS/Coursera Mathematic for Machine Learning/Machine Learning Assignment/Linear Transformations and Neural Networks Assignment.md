# Visual Overview
Purpose for learning this: **Understand Math for Debugging**
![[Pasted image 20240416060714.png]]

Matrix Multiplycation 
![[Pasted image 20240416060912.png]]

 The change of x -> change of the output![[Pasted image 20240416061048.png]]
**Linear Transformation**
row x column

matrix x matrix
![[Pasted image 20240416061723.png]]

> Combine transformation 
![[Pasted image 20240702191758.png]]
Each time the state rotate we'll need to mul to a Matrix (called Transformer)
![[Pasted image 20240416061949.png]]
	Each matrix transform (rotate) the point to a different location and therefor
	**Transformation Multiplication can get the Point Final Coordinates at any given time** so we don't have to re-multiply all the previous step.
- This mean I can get the transformer to the latest potision by multiplying all the previous transformer all together.
![[Pasted image 20240416061923.png]]

+ ! Order matter. Bc row x column, the second one only have 1 column -. the 1st diff from the 2nd matrice.
![[Pasted image 20240416062351.png]]
+ $ To work it out,  we need to **turn row in to corresponding column** using **Matrix Transpose**
	![[Pasted image 20240416062524.png]]
+ ! The example above **transform Matrix Row into Column** **Changing the rows in a matrix into corresponding columns** is called **Transposing** a matrix (the same for Col to Row) - **(Ma Trận Chuyển Đổi)**
	![[Pasted image 20240702192615.png]]
	Transpose mean **turn Matrix Row to Column** 
	![[Pasted image 20240416062714.png]]


> Transpose Matrix will be signal with a T above the variable head.
![[Pasted image 20240416063034.png]]

![[Pasted image 20240416063728.png]]

![[Pasted image 20240416083854.png]]

In this Assignment, we explores the **Foundational concepts of linear transformations and neural networks in two distinct parts**
1) ?  Linear Transformation -> Create func to generate matrices for Stretching, Shearing and Rotation Operations.
2) ? Neural Network -> implementing forward propagation in a simple architecture with two inputs and one perceptron
+ $ **Goal:** By dissecting these fundamental components, this assignment aims to provide a clear understandingw of the **role of linear algebra in both vector transformations and neural network computations.**
+ 𝑇 : ℝ2→ℝ3. Transforming vector 𝑣∈ℝ2 into the vector 𝑤∈ℝ3
+ 𝑇(𝑣) = 𝑤 and read it as "_T of v equals to w_" or "_vector w is an **image** of vector v with the transformation T_".


![[Pasted image 20240702134222.png]]
> -> diff between the original value yi and predicted value y^ are minimum 
![[Pasted image 20240702134427.png]]
![[Pasted image 20240702134444.png]]
```python
def forward_propagation(X, parameters):
    """
    Argument:
    X -- input data of size (n_x, m), where n_x is the dimension input (in our example is 2) and m is the number of training samples
    parameters -- python dictionary containing your parameters (output of initialization function)
    
    Returns:
    Y_hat -- The output of size (1, m)
    """
    # Retrieve each parameter from the dictionary "parameters".
    print("parameters:", parameters)
    W = parameters["W"]
    print("W:", W)
    b = parameters["b"]
    print("b:", b)
        
    # Implement Forward Propagation to calculate Z.
    ### START CODE HERE ### (~ 2 lines of code)
    Z = W@X + b
    Y_hat = Z
#     print(Y_hat)
#     print(f"{Z} = {W}@{X} + {b} = {Y_hat}")
    ### END CODE HERE ###
    

    return Y_hat
```


## Cost function
![[Pasted image 20240702135616.png]]
```python
def compute_cost(Y_hat, Y):
    """
    Computes the cost function as a sum of squares
    
    Arguments:
    Y_hat -- The output of the neural network of shape (n_y, number of examples)
    Y -- "true" labels vector of shape (n_y, number of examples)
    
    Returns:
    cost -- sum of squares scaled by 1/(2*number of examples)
    
    """
    # Number of examples.
    m = Y.shape[1]

    # Compute the cost function.
    cost = np.sum((Y_hat - Y)**2)/(2*m)
    
    return cost
```


## Neural Network Model
```python
def nn_model(X, Y, num_iterations=1000, print_cost=False):
    """
    Arguments:
    X -- dataset of shape (n_x, number of examples)
    Y -- labels of shape (1, number of examples)
    num_iterations -- number of iterations in the loop
    print_cost -- if True, print the cost every iteration
    
    Returns:
    parameters -- parameters learnt by the model. They can then be used to make predictions.
    """
    
    n_x = X.shape[0]
    
    # Initialize parameters
    parameters = utils.initialize_parameters(n_x) 
    
    # Loop
    for i in range(0, num_iterations):
         
        ### START CODE HERE ### (~ 2 lines of code)
        # Forward propagation. Inputs: "X, parameters, n_y". Outputs: "Y_hat".
        Y_hat = forward_propagation(X, parameters)
        print(Y_hat)
        
        # Cost function. Inputs: "Y_hat, Y". Outputs: "cost".
        cost = compute_cost(Y_hat, Y)
        ### END CODE HERE ###
        
        
        # Parameters update.
        parameters = utils.train_nn(parameters, Y_hat, X, Y, learning_rate = 0.001) 
        
        # Print the cost every iteration.
        if print_cost:
            if i%100 == 0:
                print ("Cost after iteration %i: %f" %(i, cost))

    return parameters
```


## Notes 
Third Assignment include 2 distrinct part
+ **Foundational concepts of linear transformations** 
	Delve into linear transformations by creating functions to generate matrices for stretching, shearing, and rotation operations.
+ **Neural network**
	Specifically implementing forward propagation in a simple architecture with two inputs and one perceptron.

1) Transformations
	ℝ2→ℝ3 (R present Dimension)
	 Transform vector from R2 to R3.

(tọa độ theo hàng)
![[Pasted image 20240627165808.png]]

## [[Vector Manipulation]]

