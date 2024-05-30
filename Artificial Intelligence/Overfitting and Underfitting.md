# Overfitting

**Definition**: Overfitting occurs when a model learns not only the underlying patterns in the training data but also the noise and random fluctuations. This means the model fits the training data too closely and fails to generalize to new data.

**Symptoms**:
- **High training accuracy**: The model performs exceptionally well on the training data.
- **Low test accuracy**: The model performs poorly on the validation/test data because it has learned noise from the training data. (noise: the data we not want it to learn)

**Reasons for Overfitting:**
1.  High variance and low bias.
2. The model is too complex.
3. The size of the training data.

**Solutions**:
- **Simplify the model**: Reduce the number of parameters or choose a less complex model.
- **Regularization**: Add a penalty term to the loss function to constrain the model's complexity (e.g., L1 or L2 regularization).
- **More training data**: Increase the amount of training data to help the model generalize better.
- **Cross-validation**: Use techniques like k-fold cross-validation to ensure the model generalizes well.

*example*
![[Pasted image 20240530142855.png]]

![[Pasted image 20240530142939.png]]

# Underfitting
- **Definition**: Underfitting occurs when a model is too simple to capture the underlying patterns in the data. This means the model does not fit the training data well and performs poorly on both the training and test data.
    
- **Symptoms**:
    
    - **Low training accuracy**: The model performs poorly even on the training data.
    - **Low test accuracy**: The model also performs poorly on the validation/test data because it has not captured the underlying patterns in the data.
- **Causes**:
    
    - **Overly simplistic models**: Models with too few parameters or low complexity (e.g., linear regression with few features).
    - **Insufficient training time**: Not allowing the model enough time to learn the patterns in the data.
    - **Poor feature selection**: Not including relevant features that capture the complexity of the data.
- **Solutions**:
    
    - **Increase model complexity**: Use a more complex model or add more parameters to the existing model.
    - **Feature engineering**: Create more relevant features or use techniques like polynomial features to capture non-linear relationships.
    - **Increase training time**: Allow the model to train for more epochs or iterations.
    - **Reduce regularization**: If regularization is too strong, it can prevent the model from learning adequately.

![[Pasted image 20240530142836.png]]

![[Pasted image 20240530142922.png]]


