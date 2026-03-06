Bias - Avoid Discrimination
Who responsible - software dev, hospital, docter, company ?
Build Trust - long term benefit

Principle of Transparency:
+ Decision by AI should be explainable and comprehensive. (Algorithm, Validation process)
+ everyone responsible need to understand the system. 

Apply AI ethics:
+ Fairness - continual testing to detect and rectify bias (xác định và sửa chữa thiên kiến)
+ Accountability - clear respon defined for each AI system's outcomes (determined responsibility to each outcome from the start)
+ Transparency - xAI
+ Commiment - build trust and migrate risks

---

**Where's the line ?**
Human create the data -> AI can carry society biases -> AI unintentionally amplify these bias. like early version of ChatGPT that bias about Christian
*Transparency - Complexity traded-off* - complex AI models lack trans but high acc 
*The autonomy-control dilemma* - can be auto but also might operate outside human control. Autonomy or Control ???? For example Tesla's auto pilot system. 
+ $ Nothing perfect even ethics require trade-offs e.g. between auto and manual -> Need diverse stakeholder's involment and continous AI monitoring to *ensure there're always sth responsibble for the AI system.*  

Note: 
+ opt-out mean option out, choosing not to participate in sth.  
+ Independenct AI audits are structured, third-party assessments of AI systems to ensure AI have ethics (follow guidelines, regu, safety measures/standard)

*Openess to AI challanges is the key to Transparency*
1) its can be intimidating but beneditical for business. 
2) Transparency leads to predictable regulations (quy định dễ dự đoán) and public perception


**AI fairness: not just a dream**
By *Omitting (bỏ qua) certain variables as inputs (Fairbess through unawareness)*.
	Variables include race, gender, age, socioeconomic status, sexual orientation, religion.
+ ? You couldn't racist/differentiate if you don't know.

AI unfairness exampl: In medical, human organs and bones structure are uneven between human races -> unintentional bias can still occur -> Need robust strategy to reduce bias. *The first step is acknowledging bias exists.* 
	Understand that the main objective of AI fairness is minimizing bias. And remain *skeptical and vigilant of AI that its never be perfect.*

**Potential fairness issues(s)** 
![[Pasted image 20260304151202.png]]
-> While the system can find the best employees but it will have bias toward employees once word for the company (CEO's alumni) and prefer application who have worked with large construction company. 
	Best employee doesn't mean most economic and suitable. bc there're other criterias.
	
+ ? So how can we make thing right ?  ![[Pasted image 20260304151450.png]]


**Safeguarding AI: Accountability**
+ @ If people know *there's someone responsible* when AI makes a decision, they're more likely to *trust* the system.
	Accountability Mindset: AI is Tool, not the Final decision-maker.  
-> mitigate potential harm. make sure human not running away from responsibility. 

*The paradox of accountability* (paradox mean positive increase could encourage the negative increase)
+ Increasing AI *accountability can improve trust*. *YETTTTT excessive trust in AI can lead to misguided decisions.*
	e.g. Tesla autopilot become reliable make people misunderstanding of the auto-pulot capability. 
+ $ -> If a crash happened, **both the Driver/Consumers and Tesla/AI Company shared responsibility.**  

Accountability is the Bottle-neck, bc *achieving accountability involves transparency* and solving the 'Black Box' problem. 
	Accountability in diff scenarios have diff approach & soution, there no 1 size fit all. 

**Usecase:** Consultant firms have 2 teams, 1 to reflect the User, 1 to reflect the company Accountabilites.  ![[Pasted image 20260304152819.png]]

**Explainable AI**
xAI *central pillars are Tranparency, fairness and Accountability.* 
	AI conclusions should be accessible and logical to humans. 

xAI can work like a wrapper to explain the current ML model. 
![[Pasted image 20260304153047.png | 444]]

*Understand model through a Usecase:* method like LIME (Local Interpretable Model-agnostic Explainations) create a simpler version of the *model's decision process for a specific predict* -> translate the model decision making process.
	e.g. Explains a movie's hit prediction based on factors like director popularity and high budget

Another method is *SHapIey Additive exPIanations (SHAP)*, which reveal which Feature Impact a specific Decision by apply feature masking (hide feature and see if accuracy drop a lot, if yes then that feature is important). 
![[Pasted image 20260304153443.png | 555]]

+ ? xAI can work like a wrapper that you wrap around your model. You doesn't have to restructure the model from the grounup. Use Case: Implement Explainable AI (XAI) techniques in their existing AI models. ![[Pasted image 20260304154015.png]]
  ![[Pasted image 20260304155941.png | 444]]
---

**Summaries Ethical frameworks:** understand what guide model ethical decision-making.
+ *Deontological (predict what wrong to fix) vs Consequentialist (ony fixed if wrong)*

Organization benefits: 
+ having a ethical framework help determine a clear starting point for AI usage (not to fix later) and foresight in AI decision impact. 
+ $ Having Ethical (the bottle-neck) problem alleviate set a clear path for Innovation. 


**The big ones**
Define objectives
Align with stakeholders
Collect and manage data
Design transparently
Evaluate bias
Address concerns
Review and iterate

Next: 
Introduction to Data Ethics by Shalini Kurapati
	Explore the intersection of ethics and data. Learn valuable skills to collect and manage data ethically.