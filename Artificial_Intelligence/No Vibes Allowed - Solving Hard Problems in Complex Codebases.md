+ @ **[12-Factor Agent:](https://github.com/humanlayer/12-factor-agents)** engineering techniques that make LLM-powered software more reliable, more scalable, and easier to maintain.
	Context Engineer -> get the most out of today model.

#### How to vibe code more efficiently ? 
Naive Approach - prompt until it work
Smarter Apprach - Intentional Compaction 
Compact the previous work into a Context file -> Use New Model to continoue the work.  ![[Pasted image 20260428154844.png]]*What are we compacting ?* 
	Looking for Files
	Understanding code flow
	Edits to files
	Test/ Build output
	JSON Tool Responses
	
+ ? The Exact files and lines of problem we're currently solving ![[Pasted image 20260428155021.png | 666]]

**Optimize Context Windows For:**
	Correctness
	Completeness
	Size
	Trajectory

#### Why obsess over context ?
**Context Problems Ranked**
	Incorrect Information
	Missing Information
	Too Much Noise
![[Pasted image 20260428155249.png | 444]]
![[Pasted image 20260428155316.png | 444]]
+ @ LLMs are stateless functions. Because the *only thing that affects the quality of your output* (without training/tuning models themselves) *is the quality of the inputs.*

*The 1st 40% of the Context is the Smart Zone* - where the Model accurate most of the time. After that is the Dumb zone wher its dumb. ![[Pasted image 20260428155517.png | 666]]
If you have *Too many MCPs*, you are all *leaving your work in the DUMB zone.* 
![[Pasted image 20260428155556.png | 444]]
(how many `%` actually depend on task's complexity, but 40% is the guideline)

#### How to avoid the Dumb Zone ? well u could use sub-agent
+ $ GOALS: *STAY IN THE SMART ZONE*
Sub-Agent for not playing house (testing -> fail ->Repeat until find the answer), **sub-Agent is for Enhance/Providing Context** *for the Main Agent.* 
+ @ *Sub-Agent can provided context really well.* Because instead of making 1 Agent eating up all the tokens (and get FULL) just delegate a sub-agent for smaller task (so Input Prompt stayed in the *SMART ZONE most of the time*)  
![[Pasted image 20260428160209.png | 888]]

#### What works even better: Frequent Intentional Compaction - [live coding section & docs](https://github.com/ai-that-works/ai-that-works)
+ @ Essentially, this means **designing your ENTIRE WORKFLOW around context management, and keeping utilization in the 40%-60% range** (depends on complexity of the problem)

**This method split into 3-ish step:** (about 3 step bc sometime u skip the research step) 
	Building your work around context management
	Research - Plan - Implement -> Goals: stay in the smart ZONE. 
**Plan**
	Outline the Exact Implementation Steps
	Include Filenames, Lines and Snippets
	Explicit about testing steps

The Farther you go, the more lies you have (y-axis for "Amount of Lies")
![[Pasted image 20260428163935.png |344]]
+ ! For a Large Code base, the problem of compressing code file into context.md is simply TOO MUCH to handle -> take up the 40% SMART ZONE 
+ $ You should only Compress just the SNAP SHOT of the Code base itself, part of the codebase are that matters -> compressing Truth. 
![[Pasted image 20260428163829.png]]
**Compress Context on a Large Code Base** - have subagent to analyze and compress related codebases. 
![[Pasted image 20260428163638.png]]

**Keep things Objective**
	Discourage opinions
	Avoid implementation planning 
	Research == Compression of Truth
![[Pasted image 20260428164304.png | 444]]

### What is code review for and how -> FOR MENTAL ALIGNMENT 
+ @ The most important thing is the Whole Team are always on the same page.
	[Blake Smith's framing in Code Review Essentials for Software Teams](https://blakesmith.me/2015/02/09/code-review-essentials-for-software-teams.html), where he says the most important part of code review is mental alignment - keeping members of the team on the page as to how the code is changing and why. ![[Pasted image 20260428162721.png | 444]]
But you **ABSOLUTELY** need an engineering process that
1. **keeps team members on the same page**
2. enables team members to quickly learn about unfamiliar parts of the codebase

#### On Human Leverage
+ @ You still need to read the Plan and Review Code. Of Course
![[Pasted image 20260428162314.png]]

![[Pasted image 20260428164523.png | 355]]

+ @ A bad line of code is… a bad line of code. But a bad line of a **plan** could lead to hundreds of bad lines of code. And a bad line of **research**, a misunderstanding of how the codebase works or where certain functionality is located, could land you with thousands of bad lines of code.
So you want to **focus human effort and attention** on the HIGHEST LEVERAGE parts of the pipeline.![[Pasted image 20260428162558.png | 666]]
![[Pasted image 20260428162506.png | 555]]

![[Pasted image 20260428164752.png]]

**Improve Intuition about Context Engineering ?** 
![[Pasted image 20260428164857.png | 666]]

![[Pasted image 20260428164932.png]]
