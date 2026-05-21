**Bad Generation is expensive more than ever because No-one know exactly what they want.**

+ ! Failure Mode #1 - AI doesn't do what I want.
1. For a MCQ generation system, what are the improvement to align generation preference to the User ? 
	Create a conversation feature where the *LLM askes relentlessly about every aspect of the question deck* until we reach a shared understanding. 
		Deep Fix and Quick Fix Features
	Compare to prompting, this feature guide the user first step, inspire them to make meaningful requirements for the MCQ.
-> Understanding through Adversarial (yeah like GAN)
+ $ Before you gen, reach a shared design concept.


+ ! Failure Mode #2 - AI is way too verbose (dài dòng)
AI using too many word when it communicating.
**Dev vs Domain Expert** 
-> Language Gap problem - *Use term both understand* or Dev would code the wrong features. (communicate with AI like they human) 
-> Have a .md file include a list of terms that you and the AI have in common. Make sure both shared the same understanding of the terms.
+ $ **Sol1:** Domain-Driven Design `UBIQUITOUS_LANGUAGE.md`, LLM scan the documents for terminologies and create the .md file -> for human verify if the AI understand the right thing.
+ $ **Sol2:** Create a Shared Language with the AI.


+ ! Failure Mode #3 - Code/Question that doesn't work/good 
Feedback Loops
- static types
- browser access
- automated tests

+ ! Failure Mode #4 - Doing way to much
	Take small feedback. Never take on a task that's too big
+ $ **Sol3:** `/tdd` *Test Driven Development* - Take small step -> test & verify -> feedback -> loop if fail and continue if success.

**Testing Decisions**
How big a unit ? 
What to mock ? 
What behaviours to test ? 

+ @ Good codebases are Easy to Test - Good Question are easy to verify because it give feedback to the LLM -> Improve/easier to  code. ![[Pasted image 20260428132335.png | 555]]
![[Pasted image 20260428132407.png | 555]]

+ ! **Failure Mode #5** - AI doesn't understand my code 
+ $ Group by question types for verify - Improve question explicitly base on its types. ![[Pasted image 20260428132909.png | 255]]

+ ! **Failure Mode #6** - My Brain Hurts
	Treat Deep Module as Gray boxes - I just design the interface but not gonna review the implementation (code) too much. As long as you have a testable boundary around the modules. 
+ $ **Sol5:** Design the interface, delegate the implementation.

+ @ Conclude, most important thing - Module (question types) Awareness. ![[Pasted image 20260428133141.png | 444]]
	And Code is not cheap, so are most thing.  ![[Pasted image 20260428133217.png | 444]] And Strategic Programming required software fundamental skills. 






