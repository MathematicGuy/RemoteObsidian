#### Simple Sequential model
```python
# Build a simple Sequential model
model = tf.keras.Sequential([

    # Define the input shape
    tf.keras.Input(shape=(1,)),

    # Add a Dense layer
    tf.keras.layers.Dense(units=1)
    ])
```
+ **Input Layers**: receive input data shape
+ **Dense Layer:** A layer of neurons fully connected to its adjacent layers (i.e. Fully Connected Layers)

+ ? Trains the neural network to fit the inputs to the expected outputs. 
```python
model.fit()
```

### Normalization
>**keras.layers.Rescaling()**
```python
rescale_layer = tf.keras.layers.Rescaling(1./255)
```

### Convolution Layers
![[Pasted image 20241008105513.png]]


### Callback for Control Trainining
+ ?  Help to stop trainning automatically when a result is meet.
+ ? tensorflow [CallBack](https://www.tensorflow.org/guide/keras/writing_your_own_callbacks) class allow us to return logs of each epoch. Logs can either be return at the start or end of the training or test  base on your preference. 
	You can create a callback by **defining a class that inherits** the [tf.keras.callbacks.Callback](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/Callback) **base class**. **From there, you can define available methods** to set where the callback will be executed.

**Example of stop if loss < 0.4**
```python
class myCallback(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs=None):
        '''
        Halts the training when the loss falls below 0.4

        Args:
            epoch (integer) - index of epoch (required but unused in the function definition below)
            logs (dict) - metric results from the training epoch
        '''

        # Check the loss
        if logs['loss'] < 0.4:

            # Stop if threshold is met
            print("\nLoss is lower than 0.4 so cancelling training!")
            self.model.stop_training = True
```

**Example of accuracy > 98%**
```python
class StoppingCallBack(tf.keras.callbacks.Callback):
	# Define function on_epoch_end method
	def on_epoch_end(self, epoch, logs=None):
		if (log.get('accuracy')) > 0.98:
			self.model.stop_training = True
			print('\nModel have stop trainng at 98% accuracy')
```

Then train the Model with `callback` parameters 
```python
model.fit(x_train, y_train, epochs=10, callbacks=[myCallback()])
```

