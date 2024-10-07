## Practice using FashionMNIST

note: ReLU function return x if the x > 0, else return 0.
### Step 1: Loading data and label
![[Pasted image 20241007111758.png]]
use some data to train and some to test trained model. train data use to train the model and test data use to test the model (i.e. unlearned data ).
+ ! **Avoiding Bias:** a product can be present diffently in different languages so we use numeric values to present it (e.g. schoes: 08, jacket: 20, etc..)
	![[Pasted image 20241007112512.png]]

### Step 2: Define Model
+ ? Flatten takes this 28 by 28 square and turns it into a simple linear array.

note: number of output should match the numbers of class.

### Using Callbacks to control training
+ ?  Help us to trainning automatically when a result is meet.
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

note: step training at 0.98 accuracy 

