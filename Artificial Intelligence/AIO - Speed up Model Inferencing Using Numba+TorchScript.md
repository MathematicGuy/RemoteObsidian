**What is Inference and Machine Learning Inference?**
**Inference**: sự suy luận
> Machine learning model inference is the process of infer a result from input data (tạo ra dữ liệu mới từ dữ liệu đầu vào)
+ ? **Important part in deploying** ML model.

**Traning vs Inference**
difference from trainning which refer to "a model learning from a data set". Inference model create new data from the "input data". Input data often seperate into smaller datatset called batch.   
![[Pasted image 20241031201041.png]]

Low lantency: processing speed.
High Throughput: amount of data ml model can process. 

---
### Batch Training
```python
for epoch in range(epochs):
    print(f'Epoch {epoch}:')
    # for each epoch run through the whole dataset
    for i in range(0, X_train.shape[0], batch_size): 
        if i < batch_size*8:
            print(f'batch size: {i} to {i+batch_size}')
        # X_i = X_train[i, i+batch_size]
        # Y_i = y_train[i, i+batch_size]
    print()
```
+ ? #? e.g. Extract 16 samples from the dataset. For i iteration divide dataset into batches, with each batch ranging from `[i, i + batch_size]`, For example if 
	+ i = 0, batch contain value from index 0 to 0+16
	+ i = 1, batch contain value from index 1 to 1+16
	+ i = 2, batch contain value from index 2 to 2+16

![[Pasted image 20241101200952.png]]

