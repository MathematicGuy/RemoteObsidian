+ ? Dense Layer: A layer of neurons fully connected to its adjacent layers (i.e. Hidden Layers)
```python
# Build a simple Sequential model
model = tf.keras.Sequential([

    # Define the input shape
    tf.keras.Input(shape=(1,)),

    # Add a Dense layer
    tf.keras.layers.Dense(units=1)
    ])
```


+ ? Trains the neural network to fit the inputs to the expected outputs. 
```python
model.fit()
```


