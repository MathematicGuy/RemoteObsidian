+ ! Normalize your data so your Model converge faster (bc gradient descent) (i.e. minimize loss using Loss Function)

### Step 1: Define data
### Step 2: Define and compile model using Keras
**Define**
```python
def define_and_compile_model():
    """Returns the compiled (but untrained) model.

    Returns:
        tf.keras.Model: The model that will be trained to predict house prices.
    """
    
    ### START CODE HERE ###

    # Define your model
    model = tf.keras.Sequential([ 
		# Define the Input with the appropriate shape
		tf.keras.Input(shape=(1, )),
		# Define the Dense layer
		tf.keras.layers.Dense(units=1)
	])
```
**Compile**
```python
    
    # Compile your model
    model.compile(optimizer='sgd', loss='mean_squared_error')

    ### END CODE HERE ###

    return model
```
note: `.summary()` to see model detail
```python
untrained_model = define_and_compile_model()
untrained_model.summary()
```

### Step 3: Train Model
this part consist of getting input values, process input value using a model then train the model using `.fit()` 
```python

def train_model():
    """Returns the trained model.

    Returns:
        tf.keras.Model: The trained model that will predict house prices.
    """


    # Define feature and target tensors with the values for houses with 1 up to 6 bedrooms
    n_bedrooms, price_in_hundreds_of_thousands = create_training_data()
    
    # Define a compiled (but untrained) model
    model = untrained_model
    
    # Train your model for 500 epochs by feeding the training data
    model.fit(n_bedrooms, price_in_hundreds_of_thousands, epochs=500)

    return model
```

### Step 4: Test your Model
note: tensorflow function don't need initialize inputs. just call `.predict()` on the model to test it.  
```python
new_n_bedrooms = np.array([7.0])
predicted_price = trained_model.predict(new_n_bedrooms, verbose=False).item()

print(f"Your model predicted a price of {predicted_price:.2f} hundreds of thousands of dollars for a {int(new_n_bedrooms.item())} bedrooms house")
```