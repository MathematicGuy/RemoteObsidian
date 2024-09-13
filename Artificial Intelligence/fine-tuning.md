
# Example
> Fine-tuning in **unsupervised learning** involves making small adjustments to a pre-trained or previously trained model to better adapt to the current dataset or new patterns. In the context of detecting anomalies in PCBs (Printed Circuit Boards) based on features such as **Missing_holes, Mouse_bite, Open_circuit, Short, Spur,** and **Spurious_copper**, fine-tuning allows the model to be more sensitive to subtle changes in the normal patterns or features while still detecting defects.
> 
> Here’s how fine-tuning works in an unsupervised learning setting for anomaly detection:

### **Steps in Fine-tuning an Unsupervised Model for Anomaly Detection in PCBs**

#### **1. Train an Initial Model on Normal Data**

- **Unsupervised model**: Typically, you train the model on a dataset that mostly contains normal PCBs (without anomalies). For example:
    - **Autoencoders**: Train an autoencoder to reconstruct normal PCB images. The model learns the features that define a normal PCB, such as correct hole placements, circuits, and copper traces.
    - **Isolation Forests or One-Class SVM**: Train these models on normal PCB feature data (e.g., missing holes, mouse bites, etc.) and flag outliers as anomalies.

#### **2. Fine-tuning the Model**

Fine-tuning the model comes into play when the underlying **normal patterns change** slightly, or when the model’s performance degrades (e.g., it starts detecting too many false positives). You might also fine-tune to adjust the model based on subtle new variations in the PCB's features.

#### **When Fine-tuning is Required:**

- **Slight changes in the manufacturing process**: New PCB production methods might slightly alter the appearance of normal boards, making the model flag false positives (e.g., new components or updated designs).
- **Subtle feature changes**: If features like copper traces or holes have minor design changes, the original model trained on past data may need to be fine-tuned to adjust to the new normal.
- **Increased noise in the data**: If the images or feature annotations have noise (e.g., slight blur in images or error-prone annotations), fine-tuning can help the model handle this more effectively.

#### **How Fine-tuning Works in Unsupervised Models**:

1. **Autoencoders (Image-based Features)**:
    
    - **Original Training**: Autoencoders learn to reconstruct normal PCB images. When presented with anomalous data, they struggle to reconstruct it well, leading to higher reconstruction errors, which signal an anomaly.
    - **Fine-tuning**:
        - If the normal PCB design changes (e.g., slight variations in circuit layout), you can **fine-tune** the model by adding a small batch of new normal PCB images (with updated designs) and training the autoencoder for a few more epochs.
        - The goal is to adjust the model just enough so that it can still reconstruct the new normal patterns while maintaining sensitivity to anomalies like missing holes or short circuits.
        - **Avoid overfitting**: Use early stopping or a smaller learning rate during fine-tuning to prevent the model from overfitting on the new patterns and losing its ability to detect anomalies.
2. **Isolation Forest or One-Class SVM (Feature-based Anomalies)**:
    
    - **Original Training**: These models learn to isolate normal data points (PCBs with correct features) from outliers (anomalous PCBs).
    - **Fine-tuning**:
        - If the dataset of normal PCB features changes slightly (e.g., a slight shift in the number of copper traces), you can fine-tune the isolation forest or SVM by retraining with updated normal feature data while keeping the core model intact.
        - Fine-tuning would involve **incremental learning**, where the model adapts to new normal patterns but retains its original anomaly detection capabilities.
        - **Threshold adjustment**: You may also need to adjust the outlier detection threshold to balance false positives (normal PCBs detected as defective) and true positives (correctly identifying defects).

#### **3. Annotation-based Fine-tuning**

- Since your dataset includes both images and annotations in TXT format, fine-tuning could also involve revisiting the annotations:
    - **Annotation improvement**: Ensure that annotations are as accurate as possible. Mislabeling in the annotations (e.g., marking normal features as defects) could lead to incorrect fine-tuning, making the model overly sensitive or too lenient.
    - **Adjust model behavior**: Fine-tune the model using the updated images and correct annotations so it becomes better at detecting specific types of anomalies like **Spur** or **Mouse_bite** without missing other defects.

#### **4. Practical Fine-tuning Process**

- **Collect new normal data**: As PCB designs evolve, continuously gather new normal data (images and features).
- **Use smaller learning rates**: When fine-tuning, use smaller learning rates to make incremental updates to the model without disturbing the pre-learned features.
- **Incremental training**: Instead of full retraining, you can fine-tune the model on new batches of data, allowing it to learn the new patterns without forgetting the old ones (also known as **transfer learning**).
- **Test on previous anomalies**: After fine-tuning, ensure that the model can still detect the original anomalies (e.g., open circuits, spurious copper) by testing it on the original anomaly set.

---

### **Summary: How Fine-tuning Helps**

- **Autoencoders**: Fine-tuning improves the autoencoder’s ability to handle slight changes in PCB images (like copper traces) without losing the ability to detect defects like missing holes or shorts.
- **Isolation Forest or One-Class SVM**: Fine-tuning these models helps the algorithm adapt to new normal patterns in the feature space without requiring complete retraining.
- **Annotation-based models**: Fine-tuning helps models learn better from updated feature annotations, improving their accuracy in detecting complex defects like spur and spurious copper.

Fine-tuning maintains the model’s sensitivity to anomalies while ensuring it adapts to evolving normal conditions, making the system more flexible and robust.