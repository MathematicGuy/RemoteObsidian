![[Pasted image 20260310153612.png]]

![[Pasted image 20260309163747.png]]
Prompt Chain are Deterministic
![[Pasted image 20260309163802.png]]
Agent are less predictable but Adaptive
![[Pasted image 20260309163922.png]]
+ ! Make sure to choose the right Evaluation Metrics like Text comparison when there no exact True/False answer, use human feedback score metrics if human feedback is available. 
	Must have a metrics for track performance across the system. 


![[Pasted image 20260309164355.png]]
![[Pasted image 20260309164417.png]]

### Operational Phrase
**Deployment**
CI/CD - accelerate testing and deployment. 
	**Horizontal Scaling -** *adds more machines* to the system. 
	**Vertical Scaling -** *upgrades current machine* capacity like CPU/RAM.

**Monitoring (monitor from outside) and observability (monitor from inside)**
Data Source to monitor: logs, metrics, traces -> to look for changes, Errors and Malicious content. (learn from the past)
	e.g. checkout for data drift in input data change the data distribution overtime. 
+ $ ->  Help to handle data drift by *monitoring data distribution and periodically udpating the model.*
	other example like tracking Resource, Cost, etc..

*Alert handling (how to setup alert)* - notified when issues arise, have clear procedures. 

*Example monitoring todo list* 
![[Pasted image 20260310150407.png]]

**Strategy to optimize profits**
1. Choose the right model should satisfied:
	- cheapest that able to accomplish the task.
		- or multi-ple cheap model that could work together to accomplish the task
		- cheap model (often small model) allow self-host -> Even cheaper.

2. Optimize prompts
	Use auto prompt compression
	Chat memory management. RAG return fewer results.

3. Optimize the number of calls
	+ batching -> API call is more expensive, Ultilize requests per call can reduce huge in costs.
	+ response caching - another huge reduction so we don't have to go back to old response. 
	+ optimize (and limit) agent call - so u don't run out of moneyyy.
		setup quota and rate limits
	+ Consider tasks don't require LLMs like pdf infor extraction (ie. task that could run local easilly) - save a lot of money.

**Cost metrics and prognosis:**
 Make sure to track (IMPORTANT):
 + *cost per* self-hosted server/machine.
 + cost per cloud-hosted session. 
-> Understand if "*increase in cost is relevant to increase in profit/user-base growth.*"
Note: Monitor explicitly, not overall bc we wan't to achieve control over the current and upcoming cost. 

**Usecase:** both input prompt return the same output but  the shorter on *save more cost since the input have less tokens.*  ![[Pasted image 20260310151804.png]]
**Governance and Security**
*Governance* involves policies, guidelines, and frameworks.
*Security* involves measures to prevent:
	Unauthorized access
	Data breaches
	Adversarial attack like prompt injection
	misuse/manipulation of model's output/capabilities.


**Access control** 
![[Pasted image 20260310152238.png]]
Require *Role based access control* over accessing external information.
	use zero trust based model.

Thread example: *prompt injection*
To Mitigate:
+ always assump instruction *(prompt) can be overwritten* and *content uncovered*.
+ like zero-trust - treat LLM as an untrusted user
+ identify and block known adversarial promps injection. 
![[Pasted image 20260310152407.png | 444]]

Another example: *Output manipulation*
*Execute sensitive actions* on behalf of the user.
To Minigate:
+ DO NOT give app permission/authority over sensitive action.
+ Have another model/system to Censor and block undesired output.
![[Pasted image 20260310152641.png]]

Example 3: *Denial-of-service*
	like DDOS, flood LLM with requests causing substantial cost and performance issues. 
Mitigates:
	Limit request rates per region and IP address.
	Capping resource usage per hours and request.

Example 4: *Data integrity and poisoning*
	 Inject misleading/false/harmful data into training dataset. e.g. personal information 
To Mitigates:
+ use filters (obviously)
+ get *online input from trusted sources* and verify legitimacy.

**Example Usecase:**
![[Pasted image 20260310153510.png]]

