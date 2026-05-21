>Last Declaration Wins (If there 2 CSS style affect 1 element) in other word The Last overwritten the Previous.

**DOM Tree**
> **Inheritance** (sub-element inheritance)
body
	element
		element
		element
	element
	element

**Score for Priority tag** 
	(Tag with higher score can overwrite)
	Even it get specify later.
	e.g. in CSS, tag accessed with id cannot be overwrite by tag accessed with class. 
![[Pasted image 20231030083335.png]]
	Example:
		specify **id after div** can **overwrite class with 2 element after div**
	![[Pasted image 20231030083701.png]]
