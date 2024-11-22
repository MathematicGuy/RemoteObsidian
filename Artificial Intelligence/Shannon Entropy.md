[Shannon Entropy Story](https://www.quora.com/What-is-an-intuitive-explanation-of-the-concept-of-entropy-in-information-theory)

![[Pasted image 20241108121850.png]]
Entropy - Measures disorder.
Shanon Entropy - Measures the uncertaintz of a probability distirbution.

Uncertainty mean sth not very predictable. Like 2024 president election (certain, Donal Trump) and the lottery winning number (uncertain).
![[Pasted image 20241108122015.png]]
+ ? **How did one calc the uncertainty and what the unit of uncertainty** even be
  If we look at uncerstainty from a diff angle and look uncerstainty at a information standpoint, we could rephrase the question to gain better intuition.
+ $ **How much information (bits), on average, would we need to encode an outcome from the distirbution.** (What we want to proved)
note: the more uncertain you are the more information needed to know the outcome.

![[Pasted image 20241108122449.png]]
With n bits as the prob of an event. 
> The example below show only 1 bit required to send information about the event outcomes: tail 0 or head 1
![[Pasted image 20241108122616.png]]

Another event, with 8 diffs outcome so we use 3 bits bc 3 bits is $2^3=8$
![[Pasted image 20241108122727.png]]

For uniform distribution
![[Pasted image 20241108122742.png]]
![[Pasted image 20241108122749.png]]

However we can also show that this formula even holds for **uniform distributions where the number of outcomes is not a power of 2.**

Assume that we have a distribution with 10 equally likely outcomes four bits give 16 unique states so we  could in theory use four bits to encode every possible outcome however this is inefficient as it leaves six states left over. So the average cost to describe a outcome is 4 to 1 (4/1). 
+ ? **Suggestion 1:** To do better we can observe **three separate outcomes and encode the outcomes in groups of three** (e.g. A, A, A) each outcome can be one of ten different states so there are one thousand different possible triples of outcomes ![[Pasted image 20241108123034.png]]
With $2^{10} = 1024$ we can encode all 1000 unique states above. What we're saying is that with 10 bits we can encode three independent outcomes .
The average bits represent an outcome is 10/3 = 3.333 compare to 4/1= 4 when not seperate to triplet, so it is more efficient. 
+ ? Why not use double or more than 3, because using triples allows us to reach an encoding average closer to the theoretical Shannon entropy value, achieving greater efficiency. 
![[Pasted image 20241108143851.png]]

+ ! Though this idea is not completely efficient since we still got 24 unused bits.

**Suggestion 2:** For the most efficient encoding scheme, we're looking for the case where $10^{G}= 2^B$ where $G$ is the possible output can be present using 10 bits. 
![[Pasted image 20241108142856.png]]
+ ? log conversion 
 ![[Pasted image 20241108142916.png]]

Most distribution is not uniform. For M outcome, each outcome is
![[Pasted image 20241108143004.png]]
+ $ This many needed to encoded the outcome. 

>For all M, this is "**the measure of how much information (binary bits) on average is needed to describe outcomes of a distribution**" it is linked tightly with uncertainty. 
![[Pasted image 20241108143100.png]]
> Since **if we're less certain of an outcome we may need more information to describe.**

