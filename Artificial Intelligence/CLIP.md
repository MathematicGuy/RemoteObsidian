**Keypoints - [source](https://www.youtube.com/watch?v=dh8Rxhf7cLU&t=532s)**
+ Train on Constractive Learning. Simply helping the model learn what is True by also learning what is False. Mapping Text and Image pair by pair using Softmax to calculate loss. In simple term Constractive Learning ask: How many token from the text match with each token of the image.    
+ CLIP trained on 400 millions text-image pairs -> generalize well but fail to understand handwritten character from MNIST because data imbalance for handwritten dataset. 
+ Zero-shot understanding: Can understand Image directly. 
+ Computational Efficiency: Transformer doesn't have inductive biases that help during learning from little data, they need more data to learn well. -> Not do data efficient.
+ V&L representations: CLIP present better with more description, not a single word. e.g. `a photo of a {object}` 
+ **Limitations:** with Resnet-50 as baseline for Evaluation.
	+ x1000 increase in computational resource/cost to reach overall SoTA performance. 
	+ Low compute and data efficience. 
	+ struuggle for fine-granined classification such as differentiate between cars, plans, species of flowers + abstract and systematic task such as counting the number of object. 
	+ Unable to understand temporal information. 
	+ Not a Caption generation model, can only match and understand text to image. More like a text-imag translation model hence embedding.
	+ Does not address poor data efficiency of DL. Instead CLIP compensates with hundred of millions of supervised data. 
	
+ **Application:** use to filter image, search image, etc...any thing text to image related. 

![[Pasted image 20251029105823.png]]