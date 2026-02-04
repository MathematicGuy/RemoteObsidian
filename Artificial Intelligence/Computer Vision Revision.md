### Important Image Characteristic
Every Image have a pattern and every Image can have similar patterns.
If we zoom in close enough, we will see these pattern are defined by multiple local features (ie. group of pixels) represent edges with color and direction like red straight, red bending or orange orthogonal line. To imagine eventhough a fur ball have uneven surfaces upclose (local feature), compare to a football, they both have round edges when zooming out (global feature). 

Thus Image have 2 property: 
*Feature Localization:* each pixels or features often have strong relationship with its neighbour pixels. 
-> This mean, local feature or small area of pixels contain important information. 
*Feature Independent of Location* similar pattern (like straight, orthogonal, curvy edge) have similar meaning in every image.  
-> We don't care *where* the feature is, we only care it those fetures were there or not. 

### CNN
CNN was designed to inherit these 2 image property. _but first let think why MLP don't work well with image_, overall MLP is designed to learn anyway. 

So imagine, you want to classified 100, 1024x1024 images with MLP, you're putting 1 million pixels as parameters for each image then somehow tweak the params to find the relationship between all these images to classifies them. Sound kinda brute force and inefficient doesn't it. Well, It is, the training was unstable and MLP started to overfitting thus the accuracy doesn't improve over epochs. 

![[Pasted image 20260203175230.png | 322]]

Instead of taking every pixels as granted, CNN use a NxN sliding windows to detect local features then extract noticeble features from the NxN local fetures using convolution, those noticeble then be downsampling into a single pixel using max pooling to extract the "most" noticeble feature. 

This mean every NxN local features reduced down to a single pixel, this is important because *pixels that are close to eachother are more heavily related than pixels far away from eachother.*  
-> Compare to MLP, CNN take in a Group of Pixels then compress them. This way, not only CNN preserve the spatial features (relationship between close pixels that convey more information) but all save a lot of computation after each layer of CNN. 
	Simply, instead of matching every pixels as features to find the pattern, CNN matching a group of pixels as features to find the pattern.    

For visualization, this is how Image transformed after each layer of CNN. 

![[Pasted image 20260203180836.png]]

