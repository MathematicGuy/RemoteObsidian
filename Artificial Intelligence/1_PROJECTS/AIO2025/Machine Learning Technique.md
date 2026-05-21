### Validation 
Term:
+ Mini-Batchs: just the dataset but get splitted out to many part. (like chopping meat) contain many examples.   
+ Epoch: training iteration 
for Each "Batch and Epoch"
+ ? **Calc Loss and Accuracy Mean** for **Each Batch and Each Epoch** achieve the **same result.** However the plot look better for each batch, since it gather all losses and accuracy from each batch size `batch_size` (e.g. 16, 32, 64, etc...) then calc it mean. This return the average batch's value for each epoch so the plot line got smooth out. 

### Stochastic Gradient Descent vs Gradient Descent
note: **1 example** mean **1 input array.** **GD** mean Gradient Descent

**GD**: calc gradient and update thetas over the entire dataset. (Take in all input array, process it, update thetas) 

**Stochastic GD (SGD)** is just GD but update theta after processing a single training example. (i.e. take in 1 input array, process, update thetas)

**Mini-Batch GD**: like GD but only update after processing a small batch of examples (e.g. 16, 32, 64 examples at a time, process, update thetas) - Mini-Batch GD consider as the hybrid approach compromise between GD and SGD. 
