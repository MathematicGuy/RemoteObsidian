**Definition:** RAG that can understand multiple format of documents. This include Structured, Semi-Structured and Unstructure data. These types of document basically include Image and Number and Text, and CLIP is a model that embed both image and text. 
+ [CLIP explain in 3 levels of details](https://medium.com/one-minute-machine-learning/clip-paper-explained-easily-in-3-levels-of-detail-61959814ad13)
+ [CLIP Fomula + Intuition](https://youtu.be/YOvxh_ma5qE?si=_m3fTdtsPr81VqmX)

## Part 1: CLIP (Constractive Learning-Image Pre-training)
**1 min overview**
in training - maximize the "cosine similarity" between correct and incorrect image-caption pairs, while minimize the similarity scores between all incorrect pairs. 
-> Need a equation to express the distribution of probability between class where the sum of each class is 1 -> Softmax. If the certainty of a class is closer to 1, then all other class will be closer to 0, bc their sum is 1. 

**Constractive Learning**
Is a Learning approach that seeks to represent different views of the same information similarity. 
![[Pasted image 20250820002606.png]]
sim() - e.g. cosine similarity
reference num `[3]` - $e^x$

**Constractive Loss for IMAGE**
![[Pasted image 20250820003452.png]]
$l_{1}$ is the loss for image 1, **between *Image* and *Sentence.***   $$logits_{3,3} = \frac{sim(I_{e}[i], T_{e}[j])}{t}$$Now repeat calculate loss **for each image**, then we take their average.
![[Pasted image 20250820003541.png]]

**Constractive Loss for Text** (the same but for each Text to Images)
![[Pasted image 20250820003646.png| 700]]
repeat **the same for each text (sentence)**
![[Pasted image 20250820003713.png]]

Final Loss is the **logit sum of the Constractive loss for Texts and Images**
![[Pasted image 20250820003949.png | 555]]
This is how we train the weights which translate the raw image and text encodings. 


**Why Softmax ?**


**Training**
dataset: 400 muls of web scraped data of image-caption data pairs. (1 of the 1st model to do this)
![[Pasted image 20250820002102.png]]
	Overview of how CLIP works during training.

**Inference**
**Inputs:** the vector for a single image, and the vectors for a bunch of different possible text captions.
**Output:** the similarity scores of the single image to all the different text captions.
**Goal:** select the text which has the highest similarity with the image.

