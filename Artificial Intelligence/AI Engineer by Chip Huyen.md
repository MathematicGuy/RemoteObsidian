Overview - [[AI Engineer Book Overview]]
+ @ *Each chapter have a SUMMARY,* instead of using AI before reading each Chapter, read the summary first.

# 0. [[Best Practices in Retrieval-Augmented Generation]]
# 1. Intro to Building A Applications with Foundation Models 
*Market Demand (USA alone)* ![[Pasted image 20260430103426.png]]
**Workflow Automation**
*For End User:* booking restaurants, requesting refunds, planning trips, and filling out forms.
*For Enterprises:* AI to synthesize data -> improve model (Chapter 8)
AI Agent (Chapter 6).

### Setting Expectations
Once you have decide your AI Application. Next step is to figure out what success looks like:
+ how will you measure success ?
+ The most important metric is how this will impact your business.

For example, if it’s a customer support chatbot, the **business metrics** can include the following:
+ What percentage of customer messages do you want the chatbot to automate ?
+ How many more messages should the chatbot allow you to process ?
+ How much quicker can you respond using the chatbot ?
+ How much human labor can the chatbot save you ?
+ ? Although, this is just the base problem, to constantly improve it's necessary to track customer satisfaction and customer feedback in general. 
	"User Feedback" discesses *how to design a feedback system.* 

To ensure ur *product isn't put to the customer before it ready, have clear expectation on its usefulness threshold* like "How good it has to be for it to be useful". Usefulness threshold might include the following metrics group:
+ measure the quality of the chatbot's response (to human reference)
+ latentcy metrics including TTFT (time to first token), TPOT (time per output token) and total latency. 
+ cost metrics - how much it costs per inference request.
+ other metrics such as interpretability and fairness. 

### Milestone Planning
The stronger the model, the less work to do (of course, duh) e.g. Good off-the-shelf model can already automate 30% of the customer support tickets. 

Most likely your goals will change after evaluation. 
```ad-info
In the paper UltraChat, Ding et al. (2023) shared that “the journey from 0 to 60 is easy, whereas progressing from 60 to 100 becomes exceedingly challenging.” LinkedIn (2024) shared the same sentiment. It took them one month to achieve 80% of the experience they wanted. This initial success
made them grossly underestimate how much time it’d take them to improve the product. They found it took them four more months to finally surpass 95%. A lot of time was spent working on the product kinks and dealing with hallucinations. The slow speed of achieving each subsequent 1% gain was
discouraging.
```
In AI Agent System:
-> Small models for routing/retrieval, bigger models for generation

### AI Engineering Stack
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
 

# 2. Understanding Foundation Models 
### Training 
### Modeling
**Spare LLM** (7B) has a large `%` of 0 params. 7B parameter model that is `90%` spare *only has 700 million non-zero params* -> Allow more efficient data storage and computation & **Less compute than SMALL but DENSE model.**

For example Mixtral 8x7B is a mixture of 8 expert, each with 7B = 56B params. However due to it params being shared, it has only 46.7 billion params. AT each layer, for each token only 2 experts are active. This mean that only 12.9B params are active for each token.
-> 46.7B model have the cost and speed the same as 12.9B params model.

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


# 3. Evaluation Methodology
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
+ *CE* measre the avg "suprise" (loss) of the model in bits/nats -> Training Objective, *use during training* due to it directness. 
+ *PPL* $e^{CE}$ measure how well a probability model predict a sample -> Interpretability metric. A way to capture 'uncertainty' a model has in predicting. Use for *Evaluating model performance and comparing models (the model is more confused if it has to choose uniformly from 50 token in the next-token list).*
	-> use during Eval bc it translates that abstract loss into an intuitive, human-readable metric representing "effective" vocabulary size a model is choosing from.

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

**Similarity Measurements against Reference Data.**
If the *task you care about can’t be automatically evaluated using functional correctness*, one common approach is to *evaluate AI’s outputs against reference data.*
+ @ Use in Translation task where Some Sentences or Word could have multiple answer can be correct (not strict answer) 
	Translation **Task contain 1-1 correct answer and 1-M correct answer.**
+ ? In Translate task like English to French, each example in the reference data follows the format **(input, reference responses)**

An *Input can have multiple reference responses* (multi-possible Engish translation of a French sentence) -> *Reference responses are called ground-truth* or canonical responses, metrics that don't are reference-free. 
+ ? Reference data is generated typically by humans and increasingly by AIs.

Generated responses that are more similar to the reference responses are considered better. There are four ways to measure the similarity between two open-ended texts:
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
	`Usecases:` when *Synonyms and Paraphrasing matter.* Handling short or Vague queries, Cross-lingual tasks (multi-language), *recommendation system* (where finding "Similar items" based on user behaviour rather than just metadata) ![[Pasted image 20260430172824.png | 355]]
Another way is **Hybrid Search** by combining both methods to gain high precision with high recall.
**-> RRF (Reciprocal Rank Fusion):** Use this to merge results from both BM25 and vector searches.


### AI as a Judge (human but AI Evaluation for Open-Ended question)
**Why ?** fast, easy and cheaper than human. And Studies have shown that certain AI judges are strongly correlated to human evaluators.

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
	-> can output different score or output format if run twice.
	-> hard to reproduce or trust evaluation results. 
	-> Criteria Ambiguity (easy to misintegrer and misuse them).
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

**Pointwise Evaluation** you evaluate each model independently -> offering *robust, unbiased scoring* of task compliance. Better for Absolute quality.
	`Usecase:` Factuality, toxicity, grading instruction following, and absolute quality assessment.
**Comparative Evaluation** you evaluate models against each other and compute a ranking from comparison results. 
	Like in Dancing competition: ask all candidates to dance side-by-side and ask the judges which candidate’s dancing they like the most, and pick the dancer preferred by most judges. ![[Pasted image 20260430182005.png | 444]]
	`Usecase:` Ranking model checkpoints, A/B testing user experience, and ranking scenarios. 
-> use *when Quality is subjective* like rate which Song is better by giving it a score and to *Identify minor differences* between models But *more susceptible to bias.*


# 4. Evaluate AI Systems
## Evaluation Criteria - Test Driven Development (TDD)
+ ? Which is worse - an application that has never been deployed or an application that is deployed but no one knows whether it’s working ? 
	Before investing time, money, and resources into building an application, it’s important to understand how this application will be evaluated. Huyen call this approach evaluation-driven development.
	or
	*TDD* - writing tests before writing code. Same in AI Engineer, it mean *defining evaluation criteria before building.* 


### EVALUATION-DRIVEN DEVELOPMENT
In general, you can think of criteria in the following buckets: 
	+ domain-specific capability
	+ generation capability, 
	+ instruction-following capability, 
	+ cost and latency.
+ @ Imagine you ask a model to summarize a legal contract. At a high level, *domain-specific capability metrics* tell you how good the model is at understanding legal contracts. *Generation capability metrics* measure how coherent or faithful the summary is. *Instruction-following capability* determines whether the summary is in the requested format, such as meeting your length constraints. *Cost and latency metrics* tell you how much this summary will cost you and how long you will have to wait for it. ![[Pasted image 20260501174633.png | 666]]

### Domain-Specific Capability (use online benchmark)
+ @ how well model understands and reasons about that specific domain e.g. medical, law, finance, coding, teaching, etc.. Usually **achieved through Specialized Training (continued pretraining or fine-tuning on domain data)**  
	**Example**: A model with strong domain-specific capability in medicine can correctly interpret medical literature, understand clinical reasoning, and handle domain terminology, whereas a general model might struggle or hallucinate.
	
	**Key indicator**: Performance on domain-specific benchmarks (e.g., MedQA, LegalBench, GPQA).

Like *Coding-related* capabilities are typically evaluated using *functional correctness* evaluation method. 

*For MCQ:*
Math MCQ - easy -> use mathmodel to check if answer correct or not.
Text MCQ (one and multiple correct answer) - just use *Accuracy* for number of correct.
	If you use Scoring System (1-10) -> Correct Answer plus X score, harder question get more score. 
*Classification* like Tweet Emotion Classification - has output like NEGATIVE, POSITIVE, and NEUTRAL -> use *F1 scores, precision and recall.* 

### Generation Capability
+ @ **Quality of the Generated content (more AI or more Human)**. Model's ability to produce high-quality, coherent, and useful outputs.

**Example**: Two models might both follow an instruction to "write a marketing email," but one generates generic, repetitive text while the other produces persuasive, well-structured, and on-brand copy.

No obsivous way to *measure readability*, so u likely need to use subjective evaluation, such as using *AI judges.*

Metrics used to evaluate the **quality of generated texts** back then included *fluency and coherence* using AI Judge. 
+ *Fluency* measures whether the *text is grammatically correct and natural-sounding* (does this sound like something written by a fluent speaker ?)
+ *Coherence* measures *how well-structured* the whole text is (does it follow a logical structure ?)
+ ? Although, this is might less necessary for Strong Model, this still be useful for weaker models or application involving creattive writing and low-resource languages. 

**Translation Task** metric might use is *faithfulness:* how faithful is the generated translation to the original sentence ?

**Summarization task** might use *relevance*: does the summary focus on the most important aspects of the source document ?

### Factual Consistency
Hallucinations are desirable for creative tasks, not for tasks that depend on factuality.

A metric that many application developers want to measure is *factual consistency (Tính xác thực).* Another metric is *Safety:* *can the generated outputs cause harm to users and society ?* Safety is an umbrella term for all types of toxicity and biases.

**Local factual consistency** - check within a scope of information like a sentence
A task is *factual consistency if it’s supported by the given context:* 
	For example, if the *model outputs “the sky is BLUE”* and the given *context says that the sky is PURPLE*, this output is considered **factually inconsistent**. Conversely, if model output "the sky is purple", it factually consistent.

**Global factual consistency** - output evaluate against open knowledge. 
	For Example: If the model outputs “the sky is blue” and it’s a commonly accepted fact that the sky is blue, this statement is considered factually correct.
	
+ If no context is given, you’ll have to first search for reliable sources, derive facts, and then validate the statement against these facts -> can be hard bc the internet is flood with misinformation. 

When designing metrics to *measure hallucinations, it’s important to analyze the model’s outputs to understand the types of queries that it is more likely to hallucinate on.* ![[Pasted image 20260501191507.png | 666]]
One to to *verify is through Google Search API.* SAFE, Search-Augmented Factuality Evaluator, introduced by
Google DeepMind (Wei et al., 2024) in the paper “Long-Form Factuality in Large Language Models”, works by leveraging search engine results to verify the response 
1. Use an AI model to *decompose the response* into individual statements.
2. Revise each statement to make it self-contained. For example, the “it” in the statement “The Eiffel Tower. It opened in the 20th century” should be changed to the original subject. *e.g. "it" -> "Eiffel Tower" (be specific)*
3. For *each statement, propose fact-checking queries* to send to a Google Search API.
4. Use AI to *determine whether the statement is consistent* with the research results.
![[Pasted image 20260501191836.png]]

*Checking if the Statement is consistent* with the given context can also be framed as *Textual Entailment* (which is a NLP task)
Textual Entailment check the direction (*agree/disagree/neutral*) between 2 statements a premise $T$ and a hypothesis $H$. Basically, asking if the text $T$ *Entails/Constradict/Neutral* to the a hypothesis $H$.
	Like detective, after reading the evidence $T$, he determine if his hypothesis is *Entails or Constradict or Neutral*.
	+ **Entailment** mean the evidence $T$ *support* the hypothesis $H$
	+ **Contradiction** is uh constradic the hypothesis $H$
	+ **Neutral** mean there not enough information to determine if the hypothesis $H$ is Truth base on $T$. 
+ @ **Application:** improve Question Answering (QA by identifying supporting text, Multi-Document Summarization (MDS) to reduce redundancy and Information Extraction -> basically **finding Evidence $T$ for statement $H$**
+ $ Textual Entailment achieved by training a specialized model that take in a pair of (premise, hypothesis) as input and output one of the predefined classes such as entailment, contradiction, or neutral. 
+ ? **Benchmarks for factual consistency include TruthfulQA.** These questions span 38 categories, including health, law, finance, and politics. This benchmark comes with a specialized AI judge, GPT-judge, that was **finetuned to automatically evaluate whether a response is factually consistent with the reference response.** ![[Pasted image 20260501194704.png | 400]]

**For example, given the Premise Context “Mary likes all fruits”:**
	*Entailment $H$:* “Mary likes apples”.
	*Contradiction $H$:* “Mary hates oranges”.
	*Neutral $H$:* “Mary likes chickens”.


### Instruction-Following Capability 
+ @ Model's Capability to *follow Exactly what you Demand.* eg. Gemini-3.5-Instruct.
	Measures how well the model **understands and executes complex or multi-part instructions.**
	+ Includes *handling constraints* (e.g., "only use bullet points," "keep it under 200 words," "respond in JSON").
Instruction-Following is often a result of *instruction tuning* (RLHF, DPO, etc.).

**Example**:
*Weak:*
- User asks for a step-by-step plan with exactly 5 steps → Model gives 7 steps or ignores the format.
+ Unable for Follow Structured JSON format you give out.

*Strong:*
+ Model precisely follows the requested structure, tone, length, and constraints even in complex prompts.
+ Able to follow your JSON format consistently.

### Cost and Latency -> Real World Efficiency
![[Pasted image 20260501175323.png | 666]]
Consideration: quantization to reduce latency, tradeoff between capable models with higher cost and latency, Input and Output optimization because output cost > input cost. 

### Usecase - different type of MCQ
Math MCQ - easy -> use Domain-Specific LLM for evaluate.
Text MCQ (one and multiple correct answer) - just use Accuracy for number of correct.
	If you use Scoring System (1-10) -> Correct Answer plus X score, harder question get more score. 
Classification like Tweet Emotion Classification - has output like NEGATIVE, POSITIVE, and NEUTRAL -> use F1 scores, precision and recall. 

## Designing your Evaluation Pipeline (Critital Important)
TruthfulQA only **moderately correlated** to other benchmarks -> *Improving model's resoning and math capability doesn't always improve it truthfulness.* 

**Benchmark Explain** (ask Which benchmark help me better Understand my problem)
*GSM8K (Math Reasoning)* - Grade school word problems requireing **multi-step reasoning.**  
*MMLU (General Knowledge)* - Multitask accuracy across 57 subjects (science, humanities, etc..)
*HumanEval (Code generation)* - write code from  prompt
*MTEB* - Text Embeddings 
*TruthfulQA (Factuality)* - Tendency of a model to repreduce common misconceptions.  
*HellaSwag* - ability to predict the completion of a sentence or a scene in a story or video -> Test *commonsense* and understanding of *everydays activities* through video. 

Huggingface Open LLM Leaderboard with 8 new benchmark (2024) to *evaluate reasoning and general knowledge* across wide variety of fields.
![[Pasted image 20260504144410.png | 444]]
+ @ **Important aspect of benchmark selection:** you DON'T WANT highly Correlation Benchmark.
+ ? Old benchmark is slowely get Saturated, but even outdated benchmark still can be usefil as example to evaluate and interpret benchmark. 

**Data contamination with public benchmarks** (Benchmarks shared the *same question set*) - Include:
+ Data Leakage (training on testset) or simply cheating.

**Detect Data Contamination** Strategies (detect Anomaly)
1. **N-gram overlapping** - check for *token sequence duplicated ie. Token sequence in training also in testing.*  
	+ ? more *accurate by more time consuming* bc u have to comapre each benchmark example with entire training data. 
2. **Perplexity** - if Score *UNUSUALLY LOW* => model can easily predict the text, maybe the model has seen this data during training.  
	+ ? Less Accurate but **less resource-intensive.**

### Step 1. Evaluate All Components in a System
Even if we have control over training data, we might not want to remove all benchmark data from the training data, because high-quality benchmark data can help improve the overall model performance. Besides, there will always be benchmarks created after models are trained, so there will always be contaminated evaluation samples.

**Evaluation Criteria vs Metrics:** Eval Criterias is the goals we want to achieve, we use Eval Metrics is the Scoring system we use to track how succesful we are in reaching those Criteria. 

**This part we'll focus on evaluating open-ended tasks Evaluation**. Evaluating Close-ended task is easier and its pipeline can be refer from this process.

Real world AI app are complex. Each application might consist of multiple components, and a task might be completed after many turns. 
**-> Evaluation** can happen at *different levels: **per task, per turn and per intermediate output.** 
1. Extract all the text from the PDF.
2. Extract the current employer from the extracted text.

The problem start from here, if the model fails to extract the right current employer, it can be bc of either step
+ if u don't *evalauate each component independentlky* -> don't know exactly where ur system fails. 

**Evaluation at Per Step (run 1 time like forward pass)** - evaluate a Step within the System.
*1st step:* PDF-to-text step can be evaluated *using similarity* between the extracted text and the ground truth text.
	This is the simplist form of evaluation, start with the Text.
*2nd step:* Evaluated using *Accuracy*, given the correctly extracted text, how *often does the application correctly extract the current employer.* 
	Application evaluation per step, you evaluating the **Actual Affect of the text** in step 1 **to the system.** -> how the output response to the changed per step. 

**Evaluation at Per Turn (1 Turn = Many Step)** - evaluate multiple-step within a System.
Useful in chatbot-like app, allow back-n-forth between the user and the application (conversation evaluation) to finish a task. 
e.g. Python code fail -> the Coding AI ask you about your system spec , library and python version -> you provided infor -> Model help u debug.

**Turn-based Evaluation** - evaluate the quality of each output to see whether a system completes a task. 
e.g. Did the application help you fix the bug? How many turns did it take to complete the task ? 
-> Check the *Overall Accuracy of your system.*

### Step 2: Create an Evaluation Guideline
+ ? The hardest part is determine what Good mean.
+ @  Ambiguous guideline is the most important step of the evaluation pipeline. An ambiguous guiline will leads to ambiguous scores. 
-> **Don't be Ambiguous**. Be Specific. **Understand what a bad Response look like.** 

**Define evaluation criteria:** what MADE A GOOD RESPONSE ? 
	**Example Bad Response:** AI Job Assessment application response "You are terrible fit" but What and How Terrible ? 
	**Example Good Response:** Explain the gap between this Job's requirements and the candidate's background -> show how the candidate could improve to close the gap between "good" & "bad". 

A **good response defined by 3 criteria:**
1. Relevance - the response is *relevant to the user's query.* 
2. Factual consistency - the response is *factually consistent with the context.*
3. Safety - the response *isn't toxic.* Is safe,
-> a good response *also need a Ideal User Query.* So you might need to **play around** with test queries, generate multiple response for each queries to determine if they good or bad. 

**How do you score a response ?**  -> create a rubric with examples. 
Ask question like:
+ What does a response with a score of 1 look like and why does it deserve a 1? 
+ Validate your rubric with humans: yourself, coworkers, friends, etc.
+ ?  *If humans find it hard to follow* the rubric, you need to refine it to make *it unambiguous.*
-> might require a lot of back-n-forth, a **reliable evaluation pipeline demand a clear guideline.** 
![[Pasted image 20260504161341.png | 666]]
-> If your test set **score High on multiple Evaliation Benchmark -> It Reliable.**

#### Tie eval metrics to business metrics (Product)
An **app must server a busienss goal.** The app's metric must be considered in the context of the business problem it's built to solve. 
![[Pasted image 20260504163743.png | 455]]
In the context of Customer Service Chatbot, factual consistency allow the chatbot to give product recommendation or general customer feedback so Ideally you want to **map evaluation metrics to business metrics like this:**  
+ *Factual consistency of 80%*: we can *automate 30%* of customer support requests. 
+ Factual consistency of *90%:* we can *automate 50%.*
+ Factual consistency of *98%:* we can *automate 90%*
-> Understand the impact of evaluation metrics on busienss metrics is helpful for planning. If you **know how much you gain** from that Metric, you can have **more confidence to invest** resources into improving that metric.  
Note: also define the threshold must the application achieve for it to be useful ? e.g. > 50% is usable.  

Its crucial to **understand Business metric before developing AI evaluation metrics.** So you know which & how much Business Metric affected by the AI Metrics. Because *business metric relate to engagement metric,* choosing the right metric help to *balance between profits and social responsibility.*
	e.g. Good Metrics -> Good AI -> Increase Social Engagement Metrics but making the app *adictive or extreme content like Character AI*  -> Detrimental to the user. 


+ @ To summarize, base satisfied a Eval Criteria we need to define a good Evaluation Metrics, Good *Evaluation Metrics let us know HOW GOOD is ours RESPONSE ?* that inherently *improve BUSINESS METRIC* it tied to. That in the end *Increase Profit, more confidence in Investing* to increase that metric *while not harming user.*   

### Step 3: Design your Evaluation pipeline (Data)
+ ? This is where you Match/Insert your criteria defined above. 
+ $ Let's define what methods and data we could use to evaluate the metrics above to improve the Application. ![[Pasted image 20260504163743.png | 455]]

#### Select your Evaluation method
You *could Mix and Match evaluation method* for the same criteria. 
e.g. match a expensive AI judge to give high-quality signal on 1% of your data with the cheap classifier that only gives low-quality signals on 100% of your data. 

Use *logprobs to measure model's confidence about a generated token* if available. 

Make sure your *evaluation method also used in production* so you could iterately improve your product. Think about: 
+ what kinds of feedback you want from users ?
+ how user feedback correlates to other evaluation metrics ? 
+ how to use user feedback to improve your application ? (Chapter 10 talk more about How to collect user feedback)

#### Annotate evaluation data
*Curate a set of annotated examples* to evaluate your application. You *need*
*annotated data to evaluate each of your system’s components and each
criterion*, for both turn-based and task-based evaluation.
+ ? The SUCCESS of this phrase *depends on the CLARITY of the Scoring Rubric.* Because the data you collecting at this phrase **could be reuse to create Instruction data for Finetunning later.**   

Slide your data to gain a detail/explicit understanding of your system. Slicing means seperating ur data into subsets and looking at your system's perforamnce on each subset seperately. A fine-grained understanding of ur system could give many benefits:

*Debug* - check the part of data (subset) that causing your app to underperform, could it be some attributes of this subset such as its length, topic and format. 

*Find areas for app improvement:* Check if your app is bad on long inputs or overwhelming/detail context in the subset. Maybe you can try a different processing technique or use new model with better Instruction-Following capability or better embedding/chunking. 
	-> Find-Grained Understanding -> Fine-Grained Debugging & Improvement.

*Avoid* [Simpson's paradox](https://en.wikipedia.org/wiki/Simpson's_paradox) ![[Pasted image 20260504174446.png | 333]]*Literal Mean:* when choosing features where both features provide Correct/True feedback independetly, but give out Misinformation/False when combined - [[simpson's paradox explain]]
*AI Context Mean:* model A outperforms model B on each subgroup but underperforms model B overall.  ![[Pasted image 20260504180955.png | 444]]

Evaluation results can **also be used to Compare system.**
-> say a new Prompt achieves a 10% higher score than the old prompt -> 
+ ? HOW BIG does the evaluation set have to be for us to be certain that the new prompt is indeed better ? 
	Well, u could use theory like **Statistical Significance (compute a lot)** test to compute sample size needed for a certaint level of confidence (e.g. 95% confidence) if you know the score distribution.  ![[Pasted image 20260504162328.png | 333]]

#### Evaluate your evaluation pipeline (evaluate the evaluation)
In a company, real business outcomes is the most important. So Ask:
**Is your evaluation pipeline getting the right signals ?**
	Do better Evaluation Metrics mean better business outcome ? 
	Do better responses actually get higher score ?

**How reliable/consistent is your evaluation pipeline (pl)**
+ **Take Notice of the Variance** in your Evaliation result -> Aim for increase reproducibility and reduce variance in eval pl. 
	e.g. set AI Judget temperature to 0 for consistensy. 
+ **Is your Eval Metrics correleated ?** make sure *each eval metrics give a different Insight* -> save compute and time. 
+ **Be aware of Cost and Latency for each New Evaluation,** some eval integrated within the system -> so be aware of **Accuracy and Latency Tradeoff when Eval** 

#### Iterate (User-Behaviour base Improvement)
*User behaviour change* -> Evaluation Criteria will also evolve -> Need to re-Iterate on your eval pl and *update eval criteria.* But **make sure to keep a certaint level of consistency** from ur evaluation pipeline -> If eval process changes constantly you obviously can't use eval result to guide your app's development.
-> Update your eval criteria as your User bahaviour change while keep a certain level of consistency in your eval pipeline so it won't be Unstable and Useless. 

**LOG/SAVE/TRACK all variables during your Experiments,** including but not limited to the evaluation data, the rubric and the prompt and sampling configuration (ie. LLM output configuration) used for the AI Judges. 
+ @ In Summary, this is one of the hardest but most important part of AI Engineering (application dev). This part explain how to evaluate LLM Domain-Specific capabilities and Generation capabilities, so as LLM factual consistency and safety. How to eval foundation LLM fluency, coherence and faithfulness. Develop a evaluation pipeline starting from define the right Criteria by asking "What Good Mean ?" and how to score them. Base on the Criteria, we learn that Eval Metric must be tied to Business Metric that solve real business problems and return reliable signals to improve the business itself (is my AI Eval Metrics improve my Business Eval Metrics ?) thus creating a business feedback & improvement cycle. Next, we learn how to evaluate each of the system components and criterion using Sliced Curated Data (cured data slided into subset) to have finer-graned understanding of our system to avoid bias, pitfalls and paradox as well as identify bugs and areas for app improvement. Then Evaluate the evaluation pipeline itself as User Behaviour changes by considering "eval metrics to business outcome", reliability, un-correlated metrics, cost and latency. 

+ ? Example of what a **Good MCQs Distractors** look like in AutoConverter Distractors.
![[Pasted image 20260505124450.png]]
Note: If an AI System like RAG MCQs generation don't have Benchmark, you would need first:
Basic AI System (without Internet)
1. Create a Basic RAG pipeline for QAs. 
2. AI Judge to verify the QAs and create Distractor with explaination for each QAs.
Self-Verifying RAG (leverage this to create a Q&A Benchmark)
3. Give AI Judge google search API to extract from reliable source only -> verification and create reliable Benchmark. 
	Identify Reliable Source (limited by the User and Dev) - like NotebookLM
	Curate Data into LLM Readable format -> add Curated data into the Search Space. 
4. Test AI System without the internet access to see how it perform
5. Iterative Improvement

# 5. Prompt Engineering (Quickly Note - this is too boring)
+ @ The goal of Prompt Engineering is to **Reduce the Problem Scope** so the Model could understand your Problem better. Each prompt scope-down the problem by a bit. 
[External Preference - Prompt Engineering Best Practices for Structured AI Outputs](https://levelup.gitconnected.com/prompt-engineering-best-practices-for-structured-ai-outputs-ee44b7a9c293)
System Prompt - Task Description/Context
User Prompt - the task u want them to to
Diff model use Diff chat template.
#### Instruction Clarity and Output Constraints 
-> Write **clear and explicit** instruction
*Ask model to ADAPT a Persona to improve model capabilities in specific task* like grading highschool essay score as a highschool teacher.
*Prompt Position:* by Default *Query at the End > Start*: query at the end of the prompt has more power than query at the front.
*Task Decomposition:* Follow clear and explocit rule. Break complex task into simpler subtasks so model know exactly what it need to do. Don't be ambiguous.
**Specify Output Format:** `.json` or `html` ask it to be concise. Use tools to enforece model output format like [instructor](https://github.com/567-labs/instructor) - [Medium PE best practices](https://levelup.gitconnected.com/prompt-engineering-best-practices-for-structured-ai-outputs-ee44b7a9c293) this tool allow:
	+ Formats the prompt to include JSON schema hints
	+ Parses and validates the model output
	+ Retries auto if the output if malformed or incomplete.

For Example:
+ Define a clear output contract in JSON using pandatic like title, confidence_score and using instructor lib to make sure your LLM follow the extract structure. 
+ Use delimiters like `(```)`  or XML-style tags to clearly *seperate instruction from user input data.*

#### Context and Anchoring 
-> Constrain model Degrees of Freedom -> Increase Consistency.  
**Provide example** with few-shot learning to reduce ambiguity and effective scope-down/anchoring perspective and tone for your model -> better output, less hallucination..
**Provide Sufficient Context (Food for LLM, trash in trash out)** with necessary external information to help the model accuracy and restricts it behaviour to prevent hallucination. 

#### Reasoning and Task Decomposition
-> Improve model reasoning capability ->  *(increase) Accuracy & (increase) Latency Tradeoff*
**Prompt/Task Decomposition:** Apart from improve clarity *breaking down task* also help to chained subtasks to *improve accuracy in multi-step reasoning* workflows.
**Give model time to think,** use *CoT* if the task require problem solving skill. 
**Self-critique** (asking the model to check it own outputs) ensure reliability, accuracy and reduce hallucination.
CoT Variations: ![[Pasted image 20260505164049.png | 555]]

#### Prompt's Optimization Tools
Deepmind's *Promptbreeder* select "breed" of prompts using a mutation process guided by a set of mutator prompts to generate mutations for most promising mutation to sastisfied your criteria. Example how it work at high level: ![[Pasted image 20260506145251.png | 555]]
![[Pasted image 20260506145301.png | 555]]

Many *tools aim to assist parts of prompt engineering.* For example: 
+ Guidance
+ Outlines
+ Instructor guide models toward structured outputs.
Some tools perturb your prompts, such as replacing a word with its
synonym or rewriting a prompt, to see which prompt variation works best

If used correclty, PE tools can *greatly improve your system's* performance **but beware of their downside** like cost and latency to avoid unnessary headache. If 1 API call per prompt variation, 30 evaluation examples and 10 prompt variantions mean 300 API calls.
+ ? if the model is smart, large context windows and could do multiple-task, you could compress multiple generation into 1 otherwise giving tool free rein to devising (auto-plan by themself) prompt chains could result in excessivelky long and expensive chains. 
+ ! Every PE tool can change their format without warning like switch to diff prompt templates or rewrite their default prompts -> *more tools more complexity and maintainance.*  
+ $ Following the **Keep-it-simple** principle, you might want to start by writing your own prompts without any tool to understand of the underlying model and your requirements first. 

#### Prompt Lifecycle and Operation (PromptOps)
-> Testing and Improvement
**Iterate your Prompts:** test your prompt until u satisfied with the result
	*Organize and Version prompts* with versioning, tags or prompt catelogs to improve readability, testing and collaboration.
	*Evaluate Prompt Engineering Tools* (e.g. LangSmith) compare Prompt Evaluation tools. 
+ ? Tips: Pair Prompt Engineering with code-based validation like `json.loads` to catch errors as a post-processing step.
**Parallelization** if possible, generate multiple answers for multiple scenerio to save time. For example, "generate 5 different MCQs each with 3 levels of difficulty" 

#### Security and Guardfails
-> Protect your Output by protect your prompt.
**Defensive Prompting to prevent Prompt Injection**  - Using Instruction Hierarchy to *prioritize System Prompt than User Prompt*
![[Pasted image 20260505170735.png | 666]]

-> prevent prompt extraction, jailbreaking, and indirect prompt injections.
![[Pasted image 20260501160202.png | 666]]
![[Pasted image 20260501160134.png | 666]]

#### Case study: systematic approach to AI-powered attacks "Prompt Automatic Iterative Refinement (PAIR)" uses an AI model to act as an attacker.
1. Generate a prompt. 
2. Send the prompt to the target AI. 
3. Based on the response from the target, revise the prompt until the objective is achieved.
![[Pasted image 20260505170136.png | 666]]

### Risks in Information Extraction
**Data theft -** your competitor steal your data 
**Privacy violation -** Extracting private and sensitive information in both the training data and the context used for the model.
+ ? Example "This suggests the existence of prompt strategies that allow training data extraction without knowing anything about the training data."  ![[Pasted image 20260505170452.png | 555]]
This strategy work the same for image generation model like Stable Diffusion ![[Pasted image 20260505170611.png | 555]]
+ $ When finetuning a model for safety, it’s *important to train the model not only to recognize malicious prompts but also to generate safe responses for borderline requests.*


+ @ To Summary, by learning Prompt engineering best practice you could help model to narrow down the requirements to your problem where each prompt help align your criteria to the modal a little bit. These practice include write "Clear and Explicit instruction prompt" to give model a clear context of your problem, then you use give model Example using Few-Shot Learning and Custom Context to reduce the problem scope even more. After context is sufficient, you want the model to perform well using their resoning capability, while Task-Composition improve Clarity and context for sub-task in multi-step reasoning, combined it with CoT improve reasoning and Self-Critic improve reliability, they all increase Latency, making you to consider the Cost and Latency Tradeoff bc if cost Compute Reduce for that same accuracy, latency will rise. To balance that trade off, you understand that Prompt Lifecycle is crucial to improve prompt and quality check. Finally, a good system need a good security, you realize Prompt Engineering is all for nothing if you get malicious content as input bc Context is King after all, these contents include Prompt Extraction which extract the LLM's system prompt to explot your app, Jailbreaking and prompt injection to make you model to do bad things and Information extraction to get the model to reveal its training data or sensitive information. To encounter these risks you learn about Defensive Prompting from Instruction Hierarchy method to train the LLM to prioritize privileged instruction like system instruction than user instruction. 

# 6. RAG and AI Agent (Focus on this too)
## RAG
### Chunking 

**Chunk Vagueness**
+ ! Customer/User query often vague and lack key detail
+ ? "The revenue grew by 3%") lack the necessary information (e.g., "for Acme Corp in Q2 2023") to be retrieved accurately.
-> The same thing happened with Chunk, some often them might be cutoff from their context in order to preverse chunk consistency e.g. `max_chunk_length`

**Proposed Solution:**
+ *For Customer Input Query:* Re-Writing Query base on the article or user question context -> evaluate query vagueness -> if vaguesness below a threshold -> ask user for more detail. 
+ *For Chunking in RAG:* Anthropic used AI models to generate a short context 50-100 tokens that explains the chunk and its relationship to the original documents ([Anthropic Contextual Retrieval](https://www.anthropic.com/engineering/contextual-retrieval)) to solve the "lost in the middle" or lost context problem. ![[Pasted image 20260506135706.png | 444]]
-> Ensure semantic searchs and keyword matching (BM25) maintain the original meaning. 
![[Pasted image 20260506140338.png]]

#### Evaluating Retrieval Solutions (a RAG component)
+ What *Retrieval Mechanisms* does it support ? Does it *support hybrid search ?* 
+ If it's a vectorDB, what embedding models and vector search algo does it sp ? 
+ *How scalable is it, both in terms of data storage and query traffic* (latency and storage) ? Does it work for your Traffic pattern ? 
+ *How long does it take to index* your data ? How much data can you process (such as delete/add) in bulk at once ? 
+ What's its *query latency for different retrieval algo ?* 
+ *SaaS Retrieval Sol ?*  If it's a managed sol (sol for solution), what's its pricing structure ? Is it based on the docs/vector volumne or the query volume ? 

**External data source:** multimodal and tabular data 
+ ? Multimodal example - search supporting evidence from image base on search query ![[Pasted image 20260506142008.png | 444]]
	If the image have metadata such as titles, tags and captions they can be retrieved using the metadata. e.g. it caption is relevant to the query. And if you want to query images based on their content, you need to have a embed both text and image into a embeddings space, like CLIP as the multimodal embedding model. The retrieval works as follows: 
	1. Generate CLIP embeddings for all your data, both texts and images, and store them in a vector database.
	2. Given a query, generate its CLIP embedding.
	3. Query in the vector database for all images and texts whose embeddings are close to the query embedding.

*Text-to-SQL is the same as Text-to-Image search:*
1. Text-to-SQL: based on the user query and the provided table schemas, determine what SQL query is needed. Text-to-SQL is an example of semantic parsing, as discussed in Chapter 2.
2. SQL execution: execute the SQL query.
3. Generation: generate a response based on the SQL result and the original user query.
![[Pasted image 20260506142801.png | 666]]



### AI Agent
+ ! **Compound Errors effect:** the more steps the AI Agent take, it only need 1 errors to occur for the compound effect to accumulate.e.. 1 steps 95% acc, 10 steps 60% acc and 1 step acc will be only 0.6%. 
+ $ Like human, AI need tools to perform well on given tasks like use Calculator to calc for higher speed and accuracy rather than tell the model to calc 199,999 divided by 292 raw. Be resourceful.

#### Planning in AI Agent
There multiple way to decompose a task, but not all of them will lead to a successful outcome. So the question is, how to tell the model which choice is better overall bc AI have no intuition only data. A simple approach is to list out all the option first then evaluate them by doing it. Consider the query, “How many companies
without revenue have raised at least $1 billion?”, there are 2 options:
1. Find all companies without revenue, then filter them by the amount raised -> a lot fo company without revenue that have not raise 1B dollar -> Enormous search space. 
2. Find all companies that have raised at least $1 billion, then filter them by revenue -> more Efficient bc the search space is smaller. 

Okay, but what if the model comes up with 1000-steps plan that doesn't even accomplish the goal, you cound't just test or evaluate all of them for compute sake.
+ $ This is where *HUMAN STEP IN, YOU'RE THE VALIDATOR*, every plan must be validated before its executed. 
However we still some kind of automation, so you and the AI working together efficiently/
+ simple apprch ? **Heuristic** is model need google search but doesn't have access to gg search API -> Plan is invalid. 
+ bc planning can be subjective, you could use **AI Judge** to validate planning option by asking the model to *evaluate whether the plam seems reasonable or how to improve it.* 
![[Pasted image 20260506144346.png | 666]]
Now you got 1 LLM to gen plan, 1 to validate the plan and another to choose the most promising plan and execute that plan -> you consider each component  an agent because the *Agent communicate to eachother in a loop* -> you got urself a Multi-Agent system. 

*To Speed up the process,* generate several plans in parallel and ask the evaluator to pick the most promising one -> but *add latency/cost tradeoff *

**Planning** requires understanding the intention behind a task like what's the user trying to do with this query ? In other word, it **require an Intent classifiers** is often used to help agent plan. 
+ ? Like a Orchestrator delegate task to his/her subodinates. ie. a managers
+ $ Help agent pick the right tools, e.g. should the agent access payment tool or docs retrieval tool through RAG. 
Note: some queries might be IRRELEVANT (out of agent scope), a good *intent classifier should be able to classify IRRELEVANT queries* too so the Agent could reject politely instead of wasting FLOPs to comming up with a impossible solution or hallucination. 

However, *there still risks* when AI Agent do sensive task like update database or merging a code change. For possible automation, you need to **clearly define the level of automation** an agent can have *for each action.* 
Note that refection in ai agent (e.g. ai agent  verify its output) can significantly boost the agent's performance but aren't madatory cause latency and cost.

+ @ To summerize, an AI Agent system is a LLM with access to tools to accomplish a task. A default Multi-AI Agent system have 3 basic AI Agent, 1 for Planning base on user requirements, 1 for Evaluate those Plans and 1 to execute that most promosing plan and inform the plan's result to the Planner Agent. The workflow is typically involves the following process:
	1. *Plan Generation -* Planner come up with a plan for accomplishing the task in a manageble sequence actions -> Basically **Task Decomposition** by AI. The plan often include Goal for each Main-Task, Sub-Task and prefer Tools for each task.  
	2. *Refletion and Error correction* (Evaluator/AI Judge) - AI Judge evaluate/reason the generated plan if it's a *bad plan then generate a new one.* 
	3. *Execution (e.g. Coding Agent)* - Take actions outlined in the generated plan -> use function calling to *executed outlined tasks*. Upon completion or error Execution Agent will give feedback to the Planner Agent at the next step.
	4. *Reflection and Error correction* - upon receiving the action outcome (success or failure), it evaluate these outcome and determine whether the goal has been accomplished. Basically, *if goal not complate -> identify the problems -> if goal not fullfilled, generate a new plan*. Repeat.



[[AI System Design Rulebook]] 
[[Example AI System Answers]]

# FOCUS on RAG -> AI Agent (that use RAG) first. Everything below this doesn't matter until these 2 complete at MVP level. 

----
# 7. Fine-Tunning  (Read throughly)
### When to finetune

### Memory bottle-neck
### Finetuning Techniques

### RAG + Fine-tunning are complementary techniques in a AI System 
MCQ generation **AI System**, I could use RAG for looking/search/retrieved the right verified information with source and Fine-tunning model to use those retrieved information as input for fine-tunned model
+ ? They solve two distinct problems. If you compare them, that means you have the wrong mental model. e.g. Fine-tuning for consistent MCQ genertion formatting and RAG for retrieval. 
+ ! Complex. Often used in **AI Agent System $\approx$ MCQ + Router + Fine-tunning model for specific task.** 
+ ? Valuable question to ask because some people say, "in a problem if already use RAG, don't use fine-tune and reverse".



# 8. Data Engineering (Read throughly)
## Data Curation
## Data Augmentation and Synthesis
## Data Processing 

# 9. Inference Optimization (Read throughly)
quick read bc this part i guess take 1 line in the quiz
## Understanding Inference Optimization
## Inference Optimization

# 10. AI Engineering Architecture and User Feedback 
> Answer the Question: call API or Host Model.
## AI Engineering Architecture
## User Feedback
