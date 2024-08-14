>  Turn Word into unique number. Like encryption

## **BPE Encoding** (Byte-Pair Encoding)
> Recursively merges the most frequent pairs of consecutive bytes or characters in a corpus.
![[Pasted image 20240813122920.png]]

Then we Initialize the vocab
![[Pasted image 20240813122938.png]]
Rate the word frequency -> if repeat -> turn into a token.


## **Wordpiece**
> Very similar to the BPE encoding tokenizer because it progressively learns a given number of merge rules.
![[Pasted image 20240813123343.png]]
![[Pasted image 20240813123409.png]]


## **Sentencepiece**
Problem: Space is a character.
Try to solve this issuse by making the input text as a steam of character white space included.  
![[Pasted image 20240813123817.png]]
token integrate "whitespace to the word"
![[Pasted image 20240813123909.png]]















---

OOV - Out Of Vocabulary


