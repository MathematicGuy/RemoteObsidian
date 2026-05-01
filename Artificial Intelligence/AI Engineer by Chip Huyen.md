Overview - [[AI Engineer Book Overview]]
+ @ *Each chapter have a SUMMARY,* instead of using AI before reading each Chapter, read the summary first.

## 1. Intro to Building A Applications with Foundation Models 
*Market Demand (USA alone)* ![[Pasted image 20260430103426.png]]
**Workflow Automation**
*For End User:* booking restaurants, requesting refunds, planning trips, and filling out forms.
*For Enterprises:* AI to synthesize data -> improve model (Chapter 8)
AI Agent (Chapter 6) - 

**What we should consider before building an AI application ?**
1. If AI poses a *major existential threat to your business*, incorporating AI must have the highest priority (rank by Exposure to AI). 
	often application like financial analysis, insurance and data processing (thing that could be Retrieve and Analyze by Logic/Rules) 
	
2. If you don't do this, u'll miss opotunities to boost profit and productivity (used as a support tools)
3. Unsure where AI will fit -> still better to invest resource into understanding or else you might Fail (like Blackberry, BlockBuster, Nokia). 

**3 Layers of the AI Stack** - Application dev, Model dev and infrastructure (start from Top then Move Down) ![[Pasted image 20260430105239.png]]
1. *Application dev -* use baseline LLM, provide good prompt and context -> Require Rigorous Evaluation. App require good interfaces.

2. *Model dev* - tool for developing models (Langchain) and framework (Unsloth) for modeling, training, finetuning and inference optimization. This layer also include data engineering and rigorous evaluation bc u're finetunning model.

3. *Infrastructure* - includes tooling for model serving, managing data and compute and monitoring. 

### How AI Engineering differ from ML Engineering ?
1. Instead of developing a model from scratch, you *adapt someone else model to your Problem* through fine-tunning or system design.
2. AI Engineer *work with bigger model* unlike ML engineer use small Baseline model for quicker evaluation -> Bigger model use more compute -> Required Engineer to *known how to work with more GPUs and big cluster.* 
3. LLM can produce open-ended output (unexpected output) -> harder to evaluate (bigger problem) -> Making *Evaluation and LLM alignment with human preference more important than ever.* 
-> Less about developing model from scratch but Adapting and Evaluating model. 

Model adaptation split into 2 categories: 
*Prompting* (prompt engineering) & *PEFT using LoRA* -> Adapt/Align model to specific task through LoRA without changing model weight). 
+ ! Not be Enough for Complex task or application with struct performance requirements. 
+ $ Flexibility and better Adaptation to simple task. Require less data and easier to do.

*Finetunning* adapt model by making changes to the model itself 
+ ! more complicated and required more data.
+ $ Improve model's quality, latency and cost significantly.

*Data Engineering (Chapter 8)*
Inference Optimization techniques include quantization, distillation and parallelism *(Chapter 7 through 9)*

*Evaluation (Chapter 3)* to mitigating risks and uncovering improvement opportinities -> needed to select models, benchmark progress to determine wether the model is good enough for deployment. 
	Unlike close-ended model in ML Evaluation, AI Engineer work with open-ended chatbots that have infinite possible responses to each prompt -> impossible to curate the list of ground trith to compare model's response to -> more difficult evaluation. 


**Prompt Engineering (PE) and Context Construction (CC)**
Prompt Engineering (PE) is about grounding model output for it to express the desirable behaviour from the input alone without changing the model weights. e.g. apply PE allow Gemini increase performance on MMLU from 83 to 90%. 

PE is not just prompt but also about giving the right instruction, formatting, model context-window/memory management system so the model can keep track of the conversation history 
	Prompt Engineering *(Chapter 5)*   
	Context Construction *(Chapter 6)*

*AI inference* (through browser extensions, chatbot integrations into chat app, APIs) mean new ways to collect and *extract user feedback* in natural language -> this feedback is harder to extract *(Chapter 10)*

Important of different Categories in app developments for AI engineering and ML engineering.
![[Pasted image 20260430112332.png | 444]]

**AI Engineering vs Full-Stack Engineering**
Like Web Engineering, *AI Engineering is Product Centric.*
![[Pasted image 20260430112452.png]]
 

## 2. Understanding Foundation Models 
Learn how to build foundation model 
### Training 
### Modeling
Spare LLM (7B) has a large `%` of 0 params. 7B parameter model that is `90%` spare only has 700 million non-zero params -> Allow more efficient data storage and computation & Less compute than SMALL but DENSE model.

For example Mixtral 8x7B is a mixture of 8 expert, each with 7B = 56B params. However due to it params being shared, it has only 46.7 billion params. AT each layer, for each token only 2 experts are active. This mean that only 12.9B params are active for each token.
-> 46.7B model have the cost and speed the same as 12.9B params model.

### Post-Training


### Sampling (this is long so read throughly)
Top-K: [[LLM Temperature]]
Top-P: Sample the next-token prediction probability in a descending order, until the probability sum of all sampled token reached a threshold `p`. For example set p=0.7, In "I am + [`next_token`]", the `next_token = ['a':0.4, 'the':0.2, 'happy':0.1]` -> total probability reach 0.7 so stop sampling.  ![[Pasted image 20260430150337.png | 333]]
*Beam-Search:* instead of generating all outputs independently, which might include many less promising candidates, you can use beam search to
*generate a fixed number of most promising candidates (the beam) at each step of sequence generation.* ![[Pasted image 20260430150832.png]]
**Structured Output**
using guidance to generate outputs constrained to a set of options and a regex
![[Pasted image 20260430151033.png | 555]]
You can guide a model to generate structured outputs at different layers of the AI stack: 
+ "bandage *after generation*": prompting, post-processing, test time compute.
+ "intensive treatment (modify *within the model*)": constrained sampling, and finetuning. 
+ [Steering LLM](https://github.com/guidance-ai/guidance)

*Constrained Sampling* - model sample only the logits that meet the constraints. 
![[Pasted image 20260430151500.png | 444]]


## 3. Evaluation Methodology
Learn how to evaluate LLM. Explain how Evaluation for foundation model is harder than ML models. 
### Understand some of their metrics (used for fine-tunning)
Because some of the AI System require both RAG and Fine-tunning to explaining which metric to used is important too. 

**Tokenization Method Comparison**

When train a LLM, your Goal is to learn the distribution of the data. In other word, your goal is to get the model to predict what comes next in the training data. 

**Training Data Entropy** annotated as $H(P)$. 
Cross-Entropy -> use to track model predictability in predicting what come next in this dataset. *CE depend on 2 quality in training data:* 
1. training data's predictability (complexity) -> measured by the training data's Entropy.
2. How close the data distribution captured by the LLM compare to the true training data distribution. 

Note: Divergence (differences) of Q with respect to P can be measured using KL divergence -> represented as $D_{KL}=(P||Q)$
-> As we said above, the 2 quality CE depend on is therefore: $$H(P,Q)=H(P)+D_{KL}(P||Q)$$The 1st term represent training data's Entropy. And the 2nd term represent the divergence between dataset P and dataset Q.  Note that CE isn't symmetric so: 
+ $Q$ with respect to $P$ in H(P, Q)
+ Is DIFFERENT from $P$ with respect to $Q$ to $H(Q, P)$

**Perplexity (PPL)** - like Entropy, PPL measure LLM confidence in predicting the Next-Token. 
+ *High Perplexity (High Diversity/Uncertainty)* mean the next-token probability mass is spread out (e.g. all token is 0.2%), this mean the model is not Confidence in their prediction.
	Clear Example: perplexity is 100 because you have 100 *equally likely outcome.*
+ *Low Perplexity (High Confidence/Dominance)* mean 1 or 2 tokens dominate the probability distirbution -> *PPL will be low approach 1.*  
![[Pasted image 20260430162534.png]]
[Example](https://medium.com/nlplanet/two-minutes-nlp-perplexity-explained-with-simple-probabilities-6cdc46884584) - [Explain](https://medium.com/@mukulranjan/understanding-perplexity-9df50dfa8827)

PPL represent as the Exponential of entropy and cross entropy. Given dataset with *True Distribution $(P)$* defined as: $$PPL(P)=2^{H(P)}$$
The perplexity of a language model with *learned distribution $Q$* on this dataset is defined as 
$$PPL(P, Q)=2^{H(P, Q)}$$



+ ? *PPL of 1 is perfect model*

**Compare Perplexity vs Cross-Entropy**
+ *CE* measre the avg "suprise" (loss) of the model in bits/nats -> Training Objective, *use during training.*
+ *PPL* $e^{CE}$ measure how well a probability model predict a sample -> Interpretability metric. A way to capture 'uncertainty' a model has in predicting. Use for *Evaluating model performance and comparing models (the model is more confused if it has to choose uniformly from 50 token in the next-token list).*

### Exact Evaluation (Differentiate between Exact and Subjective) - Useful in RAG Evaluation Rules design 
*Exact evaluation* produces judgment without ambiguity. Like *0 and 1, True or False.*
*Subjective evaluation* depends on who grades the essay, the same in LLM (different LLM, different score). Even though is you give exact guideline, grading can become more exact with clear grading guidelines. 
-> **AI as a Judge is subjective** base on the LLM model and the prompt. 

There are 2 evaluation approaches that produces exact scores in Open-Ended response scenario:
+ Functional correctness
+ Similarity measurements against reference data. 

**Functional correctness** - like Unit Test in Hackerank -> Test how many Cases your Correct Function could solves, where the *first/previous questions out of N question give more evaluation score then the latter.* 
	For example if there are 10 problems and a model solves 5 with k = 3, then that model’s
	pass@3 score is 50%. The more code samples a model generates, the more chance the model has at solving each problem, hence the greater the final 	score. This means that in expectation, pass@1 score should be lower than 	pass@3, which, in turn, should be lower than pass@10.

**Similarity measurements against reference data.** (257)
If the *task you care about can’t be automatically evaluated using functional correctness*, one common approach is to *evaluate AI’s outputs against reference data.*
+ @ Use in Translation task where Some Sentences or Word could have multiple answer can be correct (not strict answer) 
	Translation **Task contain 1-1 correct answer and 1-M correct answer.**
+ ? In Translate task like English to French, each example in the reference data follows the format **(input, reference responses)**

An *Input can have multiple reference responses* (multi-possible Engish translation of a French sentence) -> *Reference responses are called ground-truth* or canonical responses, metrics that don't are reference-free. 
+ ? Reference data is generated typically by humans and increasingly by AIs.

Generated responses that are more similar to the reference responses are
considered better. There are four ways to measure the similarity between
two open-ended texts:
1. **Asking the Evaluator** AI/Human directly which response are better out of the 2.
	`Usecases:` rate poem by Shakespear standard
	
2. **Exact match** - how similar the whole response to th reference response
	`Usecases:` "fill in the blank", math like "what 2+3" -> specific question. But don't use in Language translation. 
	
3. **Lexical similarity** - how similar based on the distance between shared word form like spelling, pronunciation or roots (e.g BM25 - Best Matching 25) - *FAST but not accurate* 
	fail to detect (buy $\neq$ purchase)
	`Usecases:` *Simple Search like ID*, *Full Text search, Limited Resource*, Long or specific queries. 
+ $ Common metrics for lexical similarity are `BLEU, ROUGE, METEOR++, TER, and CIDEr.`
	Another way is `n-gram`:
		 A 1-gram (unigram) is a token. A 2-gram (bigram) is a set of two tokens. “My cats scare the mice” consists of four bigrams: “my cats”, “cats scare”, “scare the”, and “the mice”. 
		-> Measure what % of n-grams matches the generated response. 
+ ! Fail to detect real meaning the `bank` and river `brank`. Ignoreing word order, just focus on similarity. 
	
4. **Semantic similarity** - how similar by semantic meaning (actual meaning, *slower but accurate*)
	Identifies  (buy $\approx$ purchase)
	`Usecases:` when *Synonyms and Paraphrasing matter*, Handling short or Vague queries, Cross-lingual tasks (multi-language), *recommendation system* (where finding "Similar items" based on user behaviour rather than just metadata) ![[Pasted image 20260430172824.png | 355]]
Another way is Hybrid Search by combining both methods to gain high precision with high recall.
-> **RRF (Reciprocal Rank Fusion):** Use this to merge results from both BM25 and vector searches


### AI as a Judge (human but AI Evaluation for Open-Ended question)
**Why ?** fast, easy and cheaper than human. And Studies have shown that certain AI judges are strongly correlated to human evaluators

**Usecase:**
1. Evaluate the quality of a response by itself, given the original question: ![[Pasted image 20260430173151.png | 444]]

2. Compare a generated response to a reference response to evaluate whether the generated response is the same as the reference response. *Alternative approach to human-designed similarity measurement.* ![[Pasted image 20260430173240.png | 444]]
3. Compare two generated responses and determine which one is better or predict which one users will likely prefer. *preference data for post-training alignment* ![[Pasted image 20260430173344.png | 444]]
**LLM as a Judge Evaluation Tools** ![[Pasted image 20260430173419.png | 444]]

**AI Judge Prompt should explain the following:**
1. The task the model is to perform. "Check the difficulty of the MCQ"
2. The criteria the model should follow to evaluate "set constraint for each difficulty criteria"
3. The scoring system, which can be one of these:
	1. Classificaiton - good/back or relevant/inrrelevant/neutral
	2. Discrete numerical values, such as 1 to 5. Use *if each class has a numerical interpretation instead of a semantic interpretation.*
	3. Continous numerical values - between 0 and 1 (evaluate *Degree of similarity*)
+ @  AI judges work better with classification than with numerical scoring systems. Wider the range for discrete scoring, the worse the model seems to get, because each score represent a criteria.  ![[Pasted image 20260430174053.png]]
+ ! **Limitation:** Unreliable, Inconsistency bc of LLM probabilistic model. Increased costs and latency
	-> can output different score or output format if run twice
	-> hard to reproduce or trust evaluation results. 
	-> Criteria Ambiguity (easy to misintegrer and misuse them) 
+ $ Open-source tools like MLflow, Ragas and LlamaIndex all have built-in criterion *faithfulness* to measure how faithful a generarted output is to the given context.
+ ? However thier instruction and scoring system are all different.
	*MLflow* uses a scoring system *from 1 to 5*.
	*Ragas* uses *0 and 1*.
	*LlamaIndex*’s prompt asks the judge to output *YES and NO*.
+ ! Tips: Do not trust any AI judge if you can’t see the model and the prompt used for the judge.
	Choose a standardize AI Judge for your task. 

Although, traditionally AI Judge would increase the API costs and applicatio latency. What are the tips to reduce cost for AI Judge:
+ SLM for checking small error (spot checking): Evaluating only a subset of responses
+ *use SMALLER (finetuned)model as AI Judge* for bigger model.
	
Finding the right balance between cost and confidence might take trial and error. This process is discussed further in Chapter 4.

All thing consider, AI Judge still cheaper than Human evaluators but Add latency. Making this a non option for app with strict latency requirements.


**Bias of AI as a Judge** - Human evaluators have biases, and so do AI judges
+ *self-bias:* prefer *it own response over other models.* 
+ *first-positional bias:* AI *favor the first answer in a pairwise comparison* or the first in a list of options.
	can be mitigate by multiple testing and shuffle option ordering or carefully crafted prompt. 
+ *recency bias:* AI favor the *answer they see last.*
+ *verbosity bias:* favoring lengthier answer, regardless of their quality (*longer answer > quality answer*).
+ $ however, discovered that GPT-4 is less prone to this bias than GPT-3.5, suggesting that this **bias might go away as models become stronger**

Self-critic might sound cheating, but it a great way to check your sanity. Because *If a model thinks its own response is incorrect*, the model *might not be that reliable (high Perplexity).*  ![[Pasted image 20260430180030.png | 444]]

**3 Specialize AI Judge Example:** Reward models, Reference-based judges, and Preference models.
+ **Reward model** 
	*takes in a (prompt, response) pair and scores how good the response is given the prompt.* Use in *RLHF.* 
	
+ **Reference-based judge** 
	*evaluates the generated response with respect to one or more reference responses.* Output a similarity score or a qualitys core (how good the generated response is compared to the reference responses). e.g in RL.
		BLEURT - compare similarity between generated and preference response. 
		Prometheus take in (prompt, generated response, reference response, scoring rubric) and outputs a quality score between 1 and 5. Higher is better. 
	
+ **Preference model** 
	A preference model *takes in (prompt, response 1, response 2) as input and outputs which of the two responses is better* (preferred by users) for the given prompt. 
	-> AI Judge being to predict human preferenfence open up many possibilities. 
	e.g in RL: JudgeLM & PandaLM. 
		JudgeLM shows an example of how PandaLM works. It not only outputs which response is better but also explains its rationale ![[Pasted image 20260430181339.png | 666]] -> `Usecase:` Twitter Bot, Give opinion about different Comments, or News Preference detection. 
 


### Model Comparison: Ranking Models with Comparative
+ @ rank models using either **pointwise evaluation or comparative evaluation.**

**Pointwise evaluation** you evaluate each model independently -> offering *robust, unbiased scoring* of task compliance. Better for Absolute quality.
	`Usecase:` Factuality, toxicity, grading instruction following, and absolute quality assessment.
**Comparative Evaluation** you evaluate models against each other and compute a ranking from comparison results. 
	Like in Dancing competition: ask all candidates to dance side-by-side and ask the judges which candidate’s dancing they like the most, and pick the dancer preferred by most judges. ![[Pasted image 20260430182005.png | 444]]
	`Usecase:` Ranking model checkpoints, A/B testing user experience, and ranking scenarios. 
-> use *when Quality is subjective* like rate which Song is better by giving it a score and to *Identify minor differences* between models But *more susceptible to bias.*




## 4. Evaluate AI Systems
### Evaluation Criteria
### Model Selection
### Designing your Evaluation Pipeline (Critital Important)


## 5. Prompt Engineering
Give a short take on this as well. Take what I need only

## 6. RAG and AI Agent (Focus on this too)
### RAG 
### A bit of Agent (because RAG is more beneficial for now)
### Memory (give my take on this)

## Fine-Tunning  (read throughly)
### When to finetune

### Memory bottle-neck
### Finetuning Techniques

## Data Engineering (Read throughly)
### Data Curation
### Data Augmentation and Synthesis
### Data Processing 

## Inference Optimization 
quick read bc this part i guess take 1 line in the quiz
### Understanding Inference Optimization
### Inference Optimization

## AI Engineering Architecture and User Feedback
### AI Engineering Architecture
### User Feedback
