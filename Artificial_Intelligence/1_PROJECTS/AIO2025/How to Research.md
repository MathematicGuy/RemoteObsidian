*Run Experiement Tonight*: https://github.com/PiDinosauR2804/WAVE-CRE-PLUS-PLUS
+ ? Research focus on finding the Why (Why the result is not improving). Engineer focus on finding the How (How to make this work).

**Understand Research Context -> Research Gap** 
0. ~~Little bit about CL History and current Trend to show why CRE.~~
	~~e.g. Trend move from Prevent Forgetting to Balance Stability and Plasticity~~ 
	~~1. Understand Continual Relation Extraction Context (2 check)~~
1. Understand author's *papers Context* "FCRE, Adaptive Prompting (WAVE-CRE and WAVE++)"
2. [CRE - Slide Representation](https://www.canva.com/design/DAHFffvAjWg/zK4O_f21sW6nIu3jaIraIQ/edit?ui=eyJBIjp7fX0&referrer=https%3A%2F%2Fwww.canva.com%2Fs%2Ftemplates%3Fquery%3Dresearch) - [Paper Survey Google Sheet](https://docs.google.com/spreadsheets/d/18DhvDwnHKNR4n7E1EgZ2EppEksPNjr6y81cS8WoXOks/edit?usp=sharing) 
	~~4.1. Understand why the author know the Problem is in Spatial and Semantic Alignment. Is it started from How to made the Detailed Desciption work ?~~ 
	
	4.3. What *problem did the current paper solved* based on the previos paper (FCRE -> WAVE -> WAVE++)
	4.4. What is the *Existed/Remaining Problem* in each paper (FCRE, WAVE-CRE, WAVE++). 
	-> How to Narrow Down Research GAPs - Visualize learned Latent Feature in Latent Space ? (T-SNE, UMAP) 
		Is there much Noise in the Learning Process 
	
3. **Compare** Limitation, Pros & Cons of paper in CRE.
4. How much *problem listed in TACRED_Errors_Analysist paper get solved in these 3 papers (FCRE, WAVE-CRE, WAVE++)*
5. Advise from Mentor and the Author - Finding the Research Gap

**Social & Reference**
1. [[AI Conference Deadline]]

---
### General Concepts
[Adaptive Prompting : Teaching Agents to Evolve with Context and Feedback](https://medium.com/@jeevitha.m/adaptive-prompting-teaching-agents-to-evolve-with-context-and-feedback-03e7e6995308)
**Prompt** = Your starting instruction.
**Context** = Information you give alongside the prompt.
**Adaptive Prompting** = Letting the AI _change its own instructions_ based on feedback or environment.
Continual Relation Extraction (CRE) is primarily a type of Class-Incremental Learning (CIL). Utilizes techniques from Task-Incremental Learning (TIL) to manage the learning process
[Continual Learning for Begineer](https://pengxiang-wang.com/posts/continual-learning-beginners-guide.html#sec-optimisation-based-approaches)

## CRE Paper Comparison (DRI, WAVE-CRE, WAVE++)
### DCRE (Few-Shot CRE, Improve Feature Representation)
#### Addressed Limitation:
1. *Address severely limited training data scenario* in FewShot learning (N-way-K-shot setting) 
	+ $ Using *LLM-generated descriptions* as stable anchors for  to solve *CRE in data scarcity scenario.*
	
2. *Poor Quality of Raw `relation` Description* - In RE, 1 class have Multiple Label Description, previous method mapping input embeddings to a single "raw label description" causing Noise and lack Diversity (ie. 1 relation like `education_at` can be express in multiple way) ![[Pasted image 20260325184538.png | 444]]
+ $ Prompts Gemini 1.5 to generate multiple diverse, detailed descriptions and examples for each relation . Acting as a Stable Semantic Representation "pivots" for each relation.

#### Existing/Remaining Problems:
Still *reliance on Memory Buffer*, does not solve privacy concerns and storage overhead with rehearsal-based CL methods. 


### WAVE-CRE (CRE, Generative Replay) 
#### Addressed Limitation:
1. *Privacy and Memory issues in Rehearsal-based* methods require storing old data 
	-> Solved with Rehersal-Free Prompt-based method using a *Generative (replay) method so synthesize latent representations of past data.*
	
2. However, prompt method cause *Inaccurate Prompt Selectione & Shared Parameter Forgetting* - method like L2P or DualPrompt suffer from performance degradation bc they share prompts across tasks or use a shared classifier head that forgets.    
	-> Allocates a dedicated, task-specific prompt pool for each task to capture within-task variations and maximize cross-task divergence.
	
3. *Suboptimal Task Prediction* (READ MORE) Previous methods group all relations within a task as a single class to predict the task ID, which lacks semantic meaning.
	-> Introduces an MLP-based task predictor that predicts the specific relation, allowing for more accurate prompt pool selection

#### Existing/Remaining Problems:
+ *Inference-Time Forgetfulness:* If the model selects the wrong prompt pool during testing, forgetfulness still occurs. 
+ *Simplistic Experts:* prefix-tunning experts used in prompt pools are relatively simple math func *(acting as constant offset vectors)*

### WAVE++ (CRE, Generative Replay & Representation) 
focus on standard CRE, evaluating on broader dataset. Aims to eliminate the need for a memory buffer entirely because storing real data can raise privacy and storage concerns. -> *Address Limitation in WAVE-CRE*
#### Addressed Limitation: 
1. *Suboptimal Task Predictor (MLP head):* used in WAVE-CRE required explicit training and is prone to misclassification errors when distribution shifts occur. 
	+ $ *Cascade Voting:* training-free inference mechanism where prompt pools evaluate Mahalanobis distance to vote on task identity.
	
2. *Lack of Global Relation Context in Prompts:*  task-specific prompt pools might still overfit or fail to generalize for (reference from **DCRE**).
	+ $ Integrates *LLM-generated label Descriptions and a Contrastive loss to pull representations closer to the true meaning* of the relation, making the prompt pools highly robust (borrowing the core idea from DCRE)

#### Existing/Remaining Problems:
+ **Increased Storage for Distributions:** While Cascade Voting removes training overhead, it requires storing relation distributions specialized by _each_ prompt pool.
	-> larger overall number of stored distributions compared to the MLP-based approach.

+ **Dependence on Prompt Pool Design:** The model's success heavily depends on the design of the prompt pools and experts.

+ **Simplistic Prefix Experts:** Like WAVE-CRE, WAVE++ still uses relatively simplistic prefix-tuning experts. The authors explicitly state that future work needs to explore more complex expert architectures to strengthen the model.

+ **Testing-Phase Forgetfulness:** Retaining knowledge is still challenging if prompt pools are incorrectly applied during the testing phase.

### Task Prediction and Inference Mechanism
*DCRE use Descriptive Retrieval Inference (DRI) strategy* for prediction by *calc a reciprocal rank fusion score* that combines the *Euclidean distance to saved class prototypes* (from the memory buffer) *with the cosine similarity to the LLM-generated relation description.* 
+ @ Basically rank possible *relations (labels)* to figure out which label best fits that sample. 
+ ? A *Sample* is defined as data pair (x, y) that consists of a *text sentence containing two specific entities (a head entity and a tail entity)*, along *with the specific relation label* that describes how those two entities are connected. 
**Example:**
- **Sentence (x):** "`[John]` is a professor at `[Z university]`."
- **Entities:** "John" is the `(head entity)` and "Z university" is the `(tail entity)`.
- **Relation Label (y):** "`professor at`" (or "employed by")

+ ? *Class Prototype (the average representation of old samples stored in memory)* for each possible relation (ie. relation sample/label). 

+ ? Reciprocal Rank Fusion combine 2 distance into 1 single score ie. the distant between the  *sample and "the Prototypes* & *the sample and LLM-generated description"*   .  Then choose the best score as the final relations. ![[Pasted image 20260331121900.png | 555]] Detail DRI explaination: [[Few-Shot, No Problem - Descriptive Continual Relation Extraction]]
	Why use 2 terms Spatial and Semantic if both are data points in the embedding space, 

*WAVE-CRE - MLP-based task predictor:* Trains a dedicated Feedforward network on Gen-Query representation to explicitly the task identity before selecting the approproate prompt pool. 

*WAVE++ discard the MLP head approach* from WAVE-CRE. Replaced by a training-free **Cascade Voting machanism** where the expert prompts pools independently calculate distance-based scores (Mahalanobis distance) and "vote" on the most appropriate task identity, reducing training overhead and improving stability.

Note from author: Treating each task as a distinct class can be suboptimal because tasks are defined by their order of appearance rather than by meaningful semantic differences.

#### Comparison
DCRI - improve label quality by adding Description to each `relation` label.


What **WAVE++** takes from **WAVE-CRE:**
+ & WAVE++ improved from WAVE-CRE. WAVE++ relies entirely on the same **task-specific prompt pool** architecture and *generative latent replay to achieve continuous learning without needing a memory buffer.* 

What **WAVE++** shares with **DCRE:**
+ & To sovles prompts overfitting to specific tasks, WAVE++ *adopts Description Generation* using LLM (Gemini 1.5) *from DCRE* to generate diverse detail description for each relation -> Provide stable anchor & global context for relation.

