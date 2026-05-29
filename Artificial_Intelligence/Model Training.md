**Tips for better model**
1. Average pixel size of each bounding box > 40x40 pixels
    
2. At least 600 labeled examples of each class _before_ dataset augmentation — this rule applies for 1 to 3 total classes in the dataset
    
3. At least 800 labeled examples of each class _before_ dataset augmentation — this rule applies for 4 to 6 total classes in the dataset
    
4. At least 1,500 labeled examples of each class _before_ dataset augmentation — this rule applies for 7-10 total classes in the dataset
    
5. 3-5x dataset augmentation is helpful
    
6. Including null/background images (images without any objects of interest) is helpful. Typically making this 3-5% of your dataset is good, I’ve found.
**Early Stopping Signal**![[Pasted image 20241211162832.png]]




60
![[Pasted image 20241211163427.png]]

100
![[Pasted image 20241211163542.png]]


finaly
![[Pasted image 20241211163605.png]]