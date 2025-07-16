Start Abstract and Simple -> then go into detail for each component gradually.

---

**Terms & Definitions**
+ protocol is set of rules that ensures how data transmitted within the network or system.
+ In Langchain `Runnable` is a building blocks represent a single task or operation where *a Runnable is a Python Object.*  

**Key concepts of langchain** `Runnables`:
+ **Modularity** (tính chất của 1 Runnable đơn lẻ)
	+ A `Runnable` is a building blocks represent a single task or operation.
	+ These task include running a LLM, processing data or chaining multiple operation together. 
	
+ **Composability** 
	+ Multiple Runnables can be linked to gether to form a pipeline. 
	+ This allow building complex workflows from smaller, reusable component 
	
+ **Reusability:** Runnables can be reused in different workflows.
	
+ **Asynchoronous Execution:** Runnables can execute task in parallel. 

**Core API Components**
1. **Runnable: Base Class** (Object)
```python
from langchain.schema.runnable import Runnable

class MyRunnable(Runnable):
    def invoke(self, input):
        return input.upper()

# Create an instance of MyRunnable
runnable = MyRunnable()

# Test with a sample input
result = runnable.invoke("hello world")
print(result)  # Output: HELLO WORLD

# Try another example
result = runnable.invoke("LangChain is awesome")
print(result)  # Output: LANGCHAIN IS AWESOME
```

2. **RunnableMap:** like python `map()` its execute multiple Runnables inside RunnableMap in parallel and aggeragate (tổng hợp) their result. *(Áp dụng nhiều hàm độc lập cho input string, mỗi hàm có 1 output)*
	Output explicit/different result for 1 input string.  
```python
from langchain.schema.runnable import RunnableMap  
  
runnable_map = RunnableMap({  
    "uppercase": lambda x: x.upper(),  
    "reverse": lambda x: x[::-1],  
})  
  
result = runnable_map.invoke("langchain")  
# Output: {'uppercase': 'LANGCHAIN', 'reverse': 'niahcnagL'}
```

3. **RunnableSequence:** apply each Runnable Sequentially to the input. *(Áp dụng từng hàm cho input string 1 cách tuần tự)* 
	Simpler than RunnableMap, the input get processes linearly to each Runnable. 
```python
from langchain.schema.runnable import RunnableSequence

runnable_sequence = RunnableSequence([
    lambda x: x.lower(),
    lambda x: x[::-1],
])

result = runnable_sequence.invoke("LangChain")
# Output: 'niahcnag'
```

4. **RunnableLambda:** the simplist Runnable, basically define a lambda function as Runnable. *(Áp dụng 1 hàm cho input string)*  
```python
from langchain.schema.runnable import RunnableLambda

uppercase_runnable = RunnableLambda(lambda x: x.upper())
result = uppercase_runnable.invoke("langchain")
# Output: 'LANGCHAIN'
```


+ $  In esseince, `Runnables` is like a wrapper that optimize your function using Paralellism
### Example: End-to-End Workflow
**Problem Statement:** process customer feedback, classify its sentiment, and summarize it.
1) create a runnable that classified sentiment, if 'good' then Positive, else Negative using lambda ofcourse -> sound like a function -> RunnableLambda. 
2) The next step is to retrieve the context then give the LLM instruction and context using PromptTemplate -> Sound Sequentially, because that it is -> RunnableSequence
3) Now we want to combine both step 1 and 2 together to get seperate output, 1 for sentiment, 1 for model summary -> RunnableMap  

```python
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.schema.runnable import Runnable, RunnableSequence, RunnableMap,RunnableLambda

# Define individual Runnables
sentiment_analysis_runnable = RunnableLambda(lambda text: "Positive" if "good" in text.lower() else "Negative")

summarization_runnable = PromptTemplate(input_variables=["text"], template="Summarize this: {text}") | llm # | represent RunnableSequence


# Combine Runnables into a pipeline
pipeline = RunnableMap({
    "sentiment": sentiment_analysis_runnable,
    "summary": summarization_runnable
})

# Invoke the pipeline
feedback = "The product quality is really nice and exceeded expectations."
result = pipeline.invoke(feedback)

print(result)
# Output:
# {
#   "sentiment": "Positive",
#   "summary": "The product quality is excellent."
# }
```

**LangChain Expression Language (LCEL)**
+ $ Syntax create to help run **execution of chains in an optimized way, either synchronous (parallel) or asynchronous (not parallel)** by composing `Runnables` together.   
+ ? LCEL good for simple chain (e.g. prompt + llm + parser), but LangGraph is recommend for further expantion when you're building complex chain (e.g. with branching, cycles, multiple agents, etc). Note that *LCEL can be use within LangGraph*. 

Modularity, Composability, Reusability, Asynchronous Execution


----
### LangChain vs LlamaIndex
**LlamaIndex** **focus in building Retrieval Augmented Generation (RAG) pipelines** with more tools and efficient. Its excels at data indexing (unstructured datasets) and connecting LLMs to external knowledge sources. 
	e.g. Strong in data-intensive appllication like search enginges and knowledge bases.    

**Whereas LangChain is a general-purpose framework**, offers a wider range of components and integrations beyond just RAG. Allowing for more complex workflows and customization for building LLM's application. 
	e.g. generate financial industry in-depth market analysis reports from real-time data.

#### Core Functionalities 
As we know, **LlamaIndex is for data-intensive search tasks while LangChain is for broader, customizable NLP solutions..** 

**LlamaIndex** excels at transforming diverse data format into searchable index -> **allowing for rapid and accurate retrieval of relevant content**.
	**Perfect for:** management systems, internal search engines and QA systems. 

**LangChain** provided a **more comprehensive framework beyond NLP applications,** with "chains" describe sequences of tasks or operations to build complex workflow. 
	**Ideal for** chatbots, content generatin, multi-step workflows. 

Although, **Langchain has stronger contexts retention while LlamaIndex has basic memory features.**
