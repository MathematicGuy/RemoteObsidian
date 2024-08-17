# Text processing

### Pre-processing
+ Tokenization: raw text into words or sentences.
	Different tokenizer tokenize text differently
	![[Pasted image 20240815204656.png]]
	 
+ Cleaning
	+ Remove unescessary data like marks, excess space, special char, etc..
	+ Remove noise: very short and infrequent word, etc..
+ Normalization:
	+ To lowercase
	+ Remove **Stop Word** is **word that represent no value to the context** like a, the, an, etc.. (We can get key word by filter out stop word)
	+ **Streming and Lemmatization**
		+ **Stemming** is a process that stems or removes last few chars from a word (often leed to incorrect meaning and spelling)
		 ![[Pasted image 20240815205601.png]]
		 + **Lemmatization** considers the context and converts word to its meaningful base form. (hence Lemma) - chuyển từ về bản gốc
			 ![[Pasted image 20240815205329.png]]
		 **Stemming** is **faster** but **Lemma is more accurate** bc Lemma involves dictionary lookups and more complex algorithm.
			![[Pasted image 20240815205124.png]]
	+ Expansion of abbreviations
+ Regular expression can be useful

**One-Hot Encoding**
>Tokenize word into integer. Then replace the original text with integer.
![[Pasted image 20240815210906.png]]





# Embeddings and Vector Databases
**Embedding:** turn data like word converted into an array of numbers 
![[Pasted image 20240815212148.png]]
Word with close meaning, stay close to eachother.
![[Pasted image 20240815212244.png]]

Google search engine for image work the same way. Each image section get converted into an array of number allow you to find pattern for similarity for those closely embedding vector.  
![[Pasted image 20240815212346.png]]









# Language Model















