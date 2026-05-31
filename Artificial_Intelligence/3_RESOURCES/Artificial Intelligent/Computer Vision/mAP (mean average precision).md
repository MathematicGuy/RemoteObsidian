![[Pasted image 20241120155816.png]]

>Confidence score appear above
![[Pasted image 20241120160052.png]]

**How to compute precision and recall**
![[Pasted image 20241120160256.png]]
>If confidence score is lower than the threshold (e.g. 0.75) then increase if higher then increase true positive.
![[Pasted image 20241120161132.png]]
![[Pasted image 20241120161151.png]]
>Here we have 3 true positive and 0 false positive
![[Pasted image 20241120161207.png]]

>For 5 true pos and 1 false pos ![[Pasted image 20241120161317.png]]![[Pasted image 20241120161338.png]]

Then **Calc the Area under the Curve**
![[Pasted image 20241120161435.png]]
>$AP@50$ called the "average precision at 50" 
![[Pasted image 20241120161523.png]]

**mAP** (Mean average precision = Sum / No_of_value)
![[Pasted image 20241120161733.png]]

![[Pasted image 20241120162002.png]]

When you analyze these plots, the only thing you do is comparing your training data to your prediction. 
![[Pasted image 20241120162457.png]]