[[Numpy Vector Array]]

## Basic Tranformation
> By assigning 2D matrix to 3D matrix
```python
def T(v):
    w = np.zeros((3,1))
    w[0,0] = 3*v[0,0]
    w[2,0] = -2*v[1,0]
    
    return w

v = np.array([[3], [5]])
w = T(v)

print("Original vector:\n", v, "\n\n Result of the transformation:\n", w)
```


![[Pasted image 20240702115527.png]]
```python
u = np.array([[1], [-2]])
v = np.array([[2], [4]])

k = 7
# Linear transformation
print("T(k*v):\n", T(k*v), "\n k*T(v):\n", k*T(v), "\n\n")
print("T(u+v):\n", T(u+v), "\n\n T(u)+T(v):\n", T(u)+T(v))
```

## Matrix Multiplycation/transformation Sign: @
![[Pasted image 20240702115721.png]]
```python
def L(v):
    A = np.array([[3,0], [0,0], [0,-2]]) 
    print("Transformation matrix:\n", A, "\n")
    w = A @ v
    
    return w

v = np.array([[3], [5]]) # v1, v2
w = L(v) # v1 * 1st_value_each_row, v2 * 2nd_value_of_each_row 
# Ex: [3 * 3; 3 * 0; 3 * 3] and the same for 5
print("Original vector:\n", v, "\n\n Result of the transformation:\n", w)
```

## Horizontal Scaling (by a factor of a)
```python
def T_hscaling(v, a):
    A = np.array([[a,0], [0,1]])
    w = A @ v
    
    return w
    
# combine 2 vector into 1 matrix  
def transform_vectors(T, v1, v2, a):
    V = np.hstack((v1, v2))
    # hscaling the matrix
    W = T(V, a)
    
    return W
    
e1 = np.array([[1], [0]])
e2 = np.array([[0], [1]])

# this allow me to choose different matrix transformation function. e.g. instead of T_hscaling I can use T_Shear()
transformation_result_hscaling = transform_vectors(T_hscaling, e1, e2, 2)

print("Original vectors:\n e1= \n", e1, "\n e2=\n", e2, 
      "\n\n Result of the transformation (matrix form) by a factor of 2:\n", transformation_result_hscaling)
```
![[Pasted image 20240702120357.png]]


## Reflection y-axis
```python
def T_reflection_yaxis(v):
    A = np.array([[-1,0], [0,1]])
    w = A @ v
    
    return w
    
e1 = np.array([[1], [0]])
e2 = np.array([[0], [1]])

transformation_result_reflection_yaxis = transform_vectors(T_reflection_yaxis, e1, e2)

print("Original vectors:\n e1= \n", e1,"\n e2=\n", e2, 
      "\n\n Result of the transformation (matrix form):\n", transformation_result_reflection_yaxis)

'''Result
	Original vectors:
	 e1= [[1]
		 [0]] 
	 e2= [[0]
		 [1]] 
	
	 Result of the transformation (matrix form):
	 [[-1  0]
	 [ 0  1]]
'''
```
note: 
+ **Before: Blue**
+ **After: Orange**
![[Pasted image 20240702120620.png]]

## Stretching by a scalar
![[Pasted image 20240702120704.png]]
```python
def T_stretch(a, v):
"""
	Performs a 2D stretching transformation on a vector v using a stretching factor a.

	Args:
		a (float): The stretching factor.
		v (numpy.array): The vector (or vectors) to be stretched.

	Returns:
		numpy.array: The stretched vector.
"""
    # This T_stretch capable of re-scaling the image
    
    print('a ', a)
    print('v ', v)
    
    ### START CODE HERE ###
    # Define the transformation matrix
    A = np.array([[1,0], [0, 1]])
    T = np.array(a * A) # matrix multiplycation 
    print("T:", T) # [[a,0], [0, a]]
    
    # Compute the transformation
    w = T @ v
    ### END CODE HERE ###

    return w
```
![[Pasted image 20240702120847.png]]

## Horizontal Shear Transformation
The horizontal shear transformation with parameter $m$ is a transformation that maps a point $(x,y)$ in the plane to $(x + my, y)$. In other words,

$$T((x,y)) = (x+my, y)$$
```python
def T_hshear(m, v):
    """
    Performs a 2D horizontal shearing transformation on an array v using a shearing factor m.

    Args:
        m (float): The shearing factor.
        v (np.array): The array to be sheared.

    Returns:
        np.array: The sheared array.
    """

    ### START CODE HERE ###
    # Define the transformation matrix
    # e1 = [1, 0]
    # e2 = [0, 1]
    # m*y = m*e2 = m * [0, 1] = [0, m]
    # x + m*y = [1, 0] + [0, m] = [1, m]
    
    T = np.array([[1, m], [0, 1]])
    # Compute the transformation
    w = T @ v
    
    ### END CODE HERE ###
    
    return w
```
![[Pasted image 20240702120946.png]]

## Rotation
To rotate a vector in the plane by an angle of $\theta$ (radians), the matrix related to this transformation is given by:
$$M = \begin{bmatrix} \cos \theta & - \sin \theta \\ \sin \theta & \cos \theta \end{bmatrix} $$
```python
def T_rotation(theta, v):
    """
    Performs a 2D rotation transformation on an array v using a rotation angle theta.

    Args:
        theta (float): The rotation angle in radians.
        v (np.array): The array to be rotated.

    Returns:
        np.array: The rotated array.
    """
    
    ### START CODE HERE ###
    # Define the transformation matrix
    print(np.array([[1, 2], [2, 3]]))
    T = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
    
    # Compute the transformation
    w = T @ v
    
    
    return w
```
![[Pasted image 20240702121144.png]]

## Rotation and Stretch
![[Pasted image 20240702121310.png]]
```python
def T_rotation_and_stretch(theta, a, v):
    """
    Performs a combined 2D rotation and stretching transformation on an array v using a rotation angle theta and a stretching factor a.

    Args:
        theta (float): The rotation angle in radians.
        a (float): The stretching factor.
        v (np.array): The array to be transformed.

    Returns:
        np.array: The transformed array.
    """
    ### START CODE HERE ###

    rotation_T = np.array([[np.cos(theta), -np.sin(theta)],
                           [np.sin(theta), np.cos(theta)]])
    stretch_T = np.array([[a, 0], [0, a]]) # A * a (A: 2D Matrix)
    
    w = rotation_T @ (stretch_T @ v)

    ### END CODE HERE ###

    return w
```
> For Rotation and Shear, do the same like this
![[Pasted image 20240702121401.png]]

