![[Pasted image 20241008135404.png]]
```python
tf.keras.utils.image_dataset_from_directory
```

**Dataset**
![[Pasted image 20241008135445.png]]
Extract from Dataset
```python
# Instantiate the dataset
train_dataset = tf.keras.utils.image_dataset_from_directory(
    TRAIN_DIR, # load train dir
    image_size=(300, 300), # resize as they're loaded
    batch_size=32, # train in batches -> better performace
    label_mode='binary' # binary classification (hourse 0 or human 1)
)
```
Train with each batches (divide dataset into batches to improve processing speed and get early result report)

Chain of method called **Data Pipeline**
1) Normalize
	Rescale dataset to `[0; 1]` range (by dividing every value to the largest value in the dataset)  
	`.cache():` help retrieval data faster 
	`.shuffle(1000):` picking 1 random value from 1000 value in shuffle dataset. then the buffer filled again by adding 1001st image and moving another random image to shuffle dataset
	`.prefetch(tf.data.AUTOTUNE):` allow parallel execution 

2) Defining ConvNet
 ![[Pasted image 20241008143441.png]]
 > use `sigmoid` for binary classification problem.
 ![[Pasted image 20241008143535.png]]

