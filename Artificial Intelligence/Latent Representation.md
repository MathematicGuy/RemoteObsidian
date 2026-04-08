## What is latent space ? 
![[Pasted image 20260403160525.png]]
To better understand the importance of latent space in deep learning, we should think of the following question: **Why do we have to encode the raw data in a low-dimensional latent space before classification, regression, or reconstruction?**

**The answer is data compression.** Specifically, in cases where our input data are high-dimensional, it is impossible to learn important information directly from the raw data.

For example:
+ *in an image classification task*, the input dimensions could be $512 \times 512 \times 3$ that correspond to $512\times512\times3=786,432$ input pixels. It seems impossible for a system to learn useful patterns for classification by looking at so many values. **The solution is to encode the high-dimensional input space to a low-dimensional latent space using a deep neural network.**
	
+ *in NLP,* word embeddings are numerical representation of words where similar words are close to eachother. And yes, word embedding are a types of compress information lie in a latent space where every word is encoded into a low-dimensional semantic vector.

![[Pasted image 20260403161553.png]]


**Latent Representation in Neural Network:**
1. Latent space is a low dimensional space produced by a NN system that tries to extract the important features from a higher dimensional input space. For example, a NN algorithm will try to reduce /compress a 512x512 images (which has 512x512x3 = 786432 number) to a vector (set of numbers) that have a lot less numbers. The advantage is that after this extraction/reduction/compression, another NN algorithm can then classify or do "other stuff" in a more manageable fashion.
    
2. Vectors in latent space should have the property that objects that are similar in the input space should be closer together (i.e., have a shorter dist between them).
    
3. A new object in the input space can be generated from an existing object by moving from the vector corresponding to the original object to a nearby vector in the latent space, and then somehow decompress/reconstruct that new vector into an object in the input space.

----
## Connect Ideas from Latent Representation with Tokenization
Latent Representation *more than just information suppression;* inherently involve reducing data dimensionality (compression) it *more like "STRUCTURED and intelligent summary" rather than just a smaller version of the original data.* Just like human, we don't remember everything explicitly, but its structure and abstract meaning that could be connect to other information.  

While Autoencoders compress data into lower-dimensional through "bottle neck" the goal is to capture only the enssential, high-level feature while discarding noise. This enable Generation: Latent Spaces organize semantic information rather than just pixels/tokens. (e.g GAN and VAEs)
```ad-seealso
**Compression vs Understanding:** Compare to Traditional Compression (Zip file) aim to reconstruct data perfectly , removing redundancy but not necessarily creating "meaning."
-> Latent representation compresses data to uncover hidden factors (Features) that explain *why* the data look the way it does. 
```

Latent Space is machine-native language/representation.
Two distinct paradigms of language models, i.e., explicit space and latent space

### Explicit Space vs Latent Space
![[Pasted image 20260408150521.png]]
_Explicit Space (words, pixels, symbols):_ represent data in human-readable discrete form while *Latent Space* represents data as high-dimensional continous, machine-native vectors. 

*Data Characterisitcs:* 
+ Explicit Space requires exact matches so they prone to noise. Every state is a sequence of Natural Lanaguage tokens drawn from a finite vocab -> Readable by human. 
+ Latent Space compacts data to its core semantic structure, discarding irrelevant information (noise/spatial, semantic redundancy) 


#### Informtion Processing (how it run in AI model) 
obsivously explicit space data slowers due to its autoregressive generation (sequential) while Latent Space is faster thanks to parallelization.
	Note: *Semantic Steering can be done through PROMPTING.*
	SS in latent space is ==a training-free technique that manipulates AI model outputs by adding, subtracting, or altering specific vectors within the model’s internal, compressed representation (latent space) during inference==

**Linguistric redundancy:** LLM *Generate redundant text and unnessary words or repetitive information* (Giải thích Dài Dòng Văn ). 
+ ? often results from training on massive datasets, causing the model to learn over-informative or repetitive patterns, or from "over-reasoning" in chain-of-thought prompting. 
_Example:_ 
+ "The final result was a major breakthrough in the field." (A breakthrough is already a final result/major).
+ "The output result is..." (Result implies output).
-> Redunance Tokens have *no intrinsic connection* (deep semantic bond between words, phrases or concepts). 

*Intrinsic Connection:* refer to word like *"king" and "queen"* are positioned near each other because their "intrinsic" semantic relationship* is captured in the vector space. 
	*Example:* "Apple" has an _intrinsic_ connection to "Fruit" or "Wheels" has an _intrinsic_ connection to "Car" (part-of)


*Interpretability:*
*Explicit Space - easy to read and verify* (e.g. Chain-of-Though logs). Latent Space in other hand is difficult to intepret directly bc its high-dimensional vector, although it can be using visualization technique through T-SNE.


*When to Used ?* 
+ *Explicit Space* - used when *step-by-step action* are required like *Chain-of-Though tasks*. Good for Debuging cause u can read, Text Generation or Rule-based AI syste.  
+ *Latent Space* - used for Creativity like *Generative Model* (VAE, GAN, etc..), *semantic search* (word hold multiple meaning) and modern LLM. *Cross-model understanding (CV + NLP).* 


#### Inefficient vs Efficient:
For problem like _“Finding the absolute fastest delivery route for a truck given five different stops, varying traffic conditions, and fuel limits.”_. Latent Resonning still analyzes the traffic, distance, and fuel. However, it *processes all of those variables at the exact same time as a complex, abstract math problem, rather than writing a step-by-step* diary entry about each variable before coming to a conclusion

Latent Space Application:
```ad-example
**Latent Reasoning (or Latent CoT)** moving CoT out of the explicit space and into the latent space.
 
-> Allow the model to *think in Abstract instead of step-by-step,* like human, when approached a complex problem, we don't think word by word but with abstract logical senses. This approach remove a lot of redundancy.

e.g. You don't calc the speed of the balls throwing at you in able to catch it, your brain process all those complex, abstract variables in natural then you catch the ball. 
```

**In short:** Latent Representation allow LLM to think in Abstract instead of Sequential/Step-by-step way. 


#### Semantic-lossy vs High-fidelity
Note:  
+ *Externalize* - translate or push sth internal outward. Like *express your complex though or feeling to a friend by speaking out loud*, you are externalizing your though. In NLP, it the model translate mathematical thoughs into human-readable text (token sequence).
+ *Discrete symbols* represent *distinct, separate, or countable values* in mathematics and digital systems. e.g. $\alpha,\beta,\in,0,1,2,3,\dots$

**Why Explicit Space are prone to semantic loss ?** - bc model externalizes its internal continous states as token sequence, this mean "converting/mapping machine *"latent representations into* sequence of *discrete output tokens",* this impose a *quantization constrain* (e.g. 24-bits infor only express in 16-bits): a ==finite vocabulary and the combinatorial constraints of natural language delimit what can be expressed==. 
-> Latent Representation couldn't be fully Express. And other structures that are difficult to render in language may be compressed, distorted or discard. 
+ ? Example: You couldn't express a Abstract Concepts with only a few examples. 1 Khái niệm có thể mô tả theo nhiều cách khác nhau không thể bị ràng buộc bở 1 kí tự và các ràng buộc của nó.

Note: linguistic rendering means the process of translating AI's internal though into human-readable token.  
	+ Linguistic mean sth with himan language, vocabulary, and grammar rules.
	+ Rendering mean converting or processing sth into final, visible format (like in Unreal Engine, you renders code into 3D graphics on the screen)

**Latent Representation preserve infor with higher fidelity,**  By *avoiding discretization and linguistic rendering*, latent variables can carry rich, continuous information between computational steps, including *content that is inexpressible in natural language and representations that naturally support multimodal structure.* 
-> Giá trị Trung Gian để thể hiện ý nghĩa của cả Ảnh và Chữ. 
-> Motivate Research Direction like Continous Thoughts, Latent Memory and Latent visual reasoning, etc.

#### Latent Space Functional Capabilities*
possesses multiple key functional capabilities that distinguish it from the explicit space, including *Operability, Expressiveness, Scalability, Generalization* as well as Evaluability, controllability, and interpretability.

**Operability**  
	Enable *direct calculations* such as concatenation, linear combination, etc.
	Enable *Advance Operation* - like *controllable semantic steering,* active intervention, iterative interleaving, and visual latent thinking.


Scalability - Follows naturally from the compactness and parallelizability of vectorized representations -> Fit for continuos reasoning. 

Generalization -  capture abstract semantic structures rather than superficial linguistic patterns. 



#### Connect to `DCRE` (Descriptive Continual Relation Extraction) paper

uses a Transformer-based model (BERT or LLM2Vec) to translate human sentences into a **latent representation**.
using "Cloze-style" template for masking token
the relation encoded into a vector z as the **latent representation**. 

DCRE’s **Description-Pivots** are essentially a form of latent memory.

Approaches used to solve Few-Shot Continual Relation Extraction problem - [web](https://www.google.com/search?client=firefox-b-d&q=Which+approaches+used+to+solve+Few-Shot+Continual+Relation+Extraction+problem): 
	Memory-based / Replay Methods
	Prompt-based Learning
	Constractive Learning / Distrillation
	Regularization-based 
	Architecture-based 
	Data/Gradient Augmentation

[AI Model](https://www.google.com/search?client=firefox-b-d&q=Which+approaches+used+to+solve+Few-Shot+Continual+Relation+Extraction+problem&fbs=ADc_l-aN0CWEZBOHjofHoaMMDiKpV6Bbbmx4QVaoKkiRQ2jlwspSJmW4ELJ_q6C3Z7ydZ0wIwPTN5bri5tFx3GWosf9sz1pFvdPmUq3bwfNsZThexeIrAzVN-aPbCFfLHnUubZPlfVUhvE8hTQsrIHhafMiDChg2_e6ZG8ZVZ_ib11l-pm6dbtoLPacUND9aN0r6yKeT9jWg2_AR5g6fUSMa0MoqlW9txQ&ved=2ahUKEwj3q6SFhd6TAxX5nK8BHUboJMMQ0NsOegQIAxAB&aep=10&ntc=1&mstk=AUtExfAvtplFk7THsvT-X44dgj-s0x9Hbehnj81OwKQEGXO7irC72HC1eg0mWgxmXyMrI2Att-NJvZCfGYhLYLi5jiGBdLYD1Ub8GvkvkWALehs5PxWOK3oyRDlkSs4RgKQalpW0Jd1gYeRZebayr_iQ2iuSZqGR0ZJSGepHm6U7JPiYFLNVf7hrWm-n3VKVUOevBEzBxdcCm2i3deMUm6WGaUTWtDbnpFlHvz9VwkZwJZNJK4A3Z_7msz8rMZ39CjFQ4499lyg_85vuG84NV9zamT2bfwQN4rwAKbPV5r32KEa2BNmQ6Gsn6A5ZqcEFsQGec0snBpxJrdW7Ug&csuir=1&mtid=hC3WadaGEq65vr0P99S5kQU&udm=50)
List out papers that cites "Few-Shot, No Problem: Descriptive Continual Relation Extraction" and check if they solved ""Few-Shot, No Problem: Descriptive Continual Relation Extraction" paper existing limitation