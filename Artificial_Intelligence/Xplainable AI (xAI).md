![[Pasted image 20250525120533.png]]

### Permutation in Computer Vision 
To Find which part of the image is most important for prediction. By compare the model performance before and after that part have been permuted.
![[Pasted image 20250525150058.png]]
+ ? By randomly validate the pot using different color filter, we can identify if the plant classification model actually influenced by the color of the pot.   


Occulasion Maps work by systematically masking out squares of an image. 
![[Pasted image 20250525151313.png# left |600]]
SHAP works by permuting different combinations of subsets of pixels 
![[Pasted image 20250525151411.png# left | 600]]
+ $ Both method above aim to find which region or part of an image is Important. 

PCI (Permutation Channel Important) work by shuffle every pixels in a color channel. We made a prediction with this permutated image if the predicted probability using the original image are significantly different from those using the permutated image -> this tell us that the model was using the red channel to make predictions for this instance. 
![[Pasted image 20250525151535.png]]

### PCI Algorithm 
**Variables and choices:**
![[Pasted image 20250525151922.png# left]]
For a given channel i, we calculate the PCI score by 
**Step 1:** randomly pixel within the image of that channel  
![[Pasted image 20250525152120.png]]

**Step 2:** Use the permuta ted image as input to the trained model to generate predictions.
**Step 3:** Performance we calculate P across the n images using the model's predictions with the permuted channel.
![[Pasted image 20250525152241.png]]

**Step 4:** Important. We compare the permuted performance to the baseline. 
$$PCI_{green} = baseline - p_{\text{permuted}}$$
**Step 5:** Repeat

The average in performance is the PCI score for this channel. 
The precise intepretation of a PCI score will depend on your choice of P, we can use metrics like:
+ for **Classification:** Accuracy or AUC
+ for **Regression:** MSSE or R2
+ Segmentation: average accuracy

The accuracy for each of ours channel decrease show these channel are being used by the model to make prediction. 
![[Pasted image 20250525152914.png# left]]

![[Pasted image 20250525153753.png]]

Using PCI help us to figured out the Model is using the pot not the plant for prediction. In short, PCI can tell us whether color is an important aspect for a model's prediction.   
![[Pasted image 20250525153052.png]]

Beside RGB colours we can see, 