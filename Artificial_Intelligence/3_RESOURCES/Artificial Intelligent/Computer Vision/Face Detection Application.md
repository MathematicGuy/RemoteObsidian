Requirement: a hangout of the result images, the source code, and your explanation file for the below questions in one zip file with the structure: <**Yourname>_FaceDetetectionSVM.zip** 

The goal is to get practical experience with SVM classification and visual object category detection in still images. A simple face detector is presented using the standard “scanning-window” technique. The implementation of the detector will contain the following steps:

• Part 1: Load, format, and normalize positive and negative training images

• Part 2: Learn and evaluate linear SVM classifier; choose the best C value

• Part 3: Use SVM classifier to score image patches and to detect faces in test images

1. Prepare data 

Go through the steps of loading and visualization of training images. Run mean-variance normalization, then format images into SVM-acceptable input by running the provided lines of the code. Ensure you understand the format of variables Xtrain, ytrain, Xval, and yval, as you will need to operate with them in the following steps.

2. SVM Classification 

Train and test a linear SVM classifier. SVM training and evaluation are done with **svmclass** and **svmvalmod** functions, respectively. Next, implement the following steps:

- Compute linear hyper-plane W from SVM support vectors and alpha-coefficients
    
- Re-compute confidence values for training and validation using W and bias b. Make sure your accuracy values correspond to the ones returned by **svmvalmod**
    

Illustrate W as an image using the provided code. Why does it remind a face? How do you explain different values of W? Next, re-train SVM for various values of C. 

- Select the SMV model, maximizing accuracy on the validation set.
    
- - Visualize W as an image at each iteration. Why W looks more like a face for small C-values?
        
    

The best classification hyper-plane W looks like an average face image. Cannot we use such an average image as a classification hyper-plane?

 3.  Face detection

Scanning-window style classification of image patches typically results in multiple responses around the target object. A standard practice to deal with this is to remove any detector responses in the neighborhood of detections with the locally maximal confidence score (non-maxima suppression or NMS). NMS is usually applied to all detections in the image with confidence above a certain threshold. Try NMS face detection for different threshold values and in other images:


