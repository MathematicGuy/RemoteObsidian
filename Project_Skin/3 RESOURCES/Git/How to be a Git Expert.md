source: https://youtu.be/hZS96dwKvt0?si=BI9eHXhR-idgQMvc


![[Pasted image 20240222104304.png]]
+ Head as the current pointer pointed to current commit
Each commits related to each other

+ No rename in git, just a different commit

checkout -> move the head pointer to the desire node (commit)

branch -> a name that move along with you as you commit.
	git think - everytime I commit I going to add a node to that branch name
![[Pasted image 20240222104637.png]]

merge
![[Pasted image 20240222104741.png]]
git indentify each part then merge them
Merge open 4 windows (if not u using a crappy merge tool)
	Local, Remote, Base, Final Version

can merge side-branch "feature" with main branch "develop" to get up-to-date development. And continuing building that "feature" 

fetch/pull (sharing code)
fetch - create a local copy 
pull -> fetch & merge


push - fetch (see where the origin is)
	push fail when it not see current commit
	so we must pull

diff/add
	Git diff check the different from 2 branch.

revert (use when the last commit was a mistake)
git see them as a diff. **git create a new diff from that Mistake Commit** 
![[Pasted image 20240222110456.png]] 
usage: accidentally push some bad code -> use revert -> everyone will pull that -> un-does the mistake



use **when you just want to merge the bug-fix part from another branch not the whole branch yet**.
![[Pasted image 20240222110906.png]]
what git does is it, see that commit just a diff and merge it with the develop brance.



![[Pasted image 20240222111108.png]]
 use when I want to base my feature with the lastest development.
 -> git move the feature commit to the main (develop) branch and delete the commit from the feature branch. 
In others word, rebase is a fast-forward merge.
![[Pasted image 20240222111615.png]]

common workflow
+ git status
+ git diff --word-diff
	show only that changing portion not the entire code file.
+ git add -p 
	do you want to make this change? y/n 
	do you want to.... y/n
	- Use to check error
+ git commit
> **Identfying a commit**
![[Pasted image 20240222113018.png]]

```ad-note
X^n parent n
	origin/my-feature^2 -> feature at parent 2
X~n behind n
	X~2 behind 2
	HEAD~3 three commit behind head

2 commit behind parent 4
	X~2^4  
	X~~^4 


```


**diff/apply**
![[Pasted image 20240222114044.png]]
Take all the feature that not head and add it to a new index called "Staged"

> you can change any 2 commits
![[Pasted image 20240222113811.png]]


Understand the concept of Git merge conflicts, offering guidance on how to understand and resolve them. Here's the breakdown:

1) Understand Conflict

+ **What Git Merges Do:** Git merges allow code changes from different branches to be combined into a single branch.

+ ! **Code Conflict**: is when there are 2 portion of code has been modified differently in 2 seperate branches leaving Git unable to automatically determine the intended final version.

- **Visualizing Conflicts:** Git marks conflict sections within the code files, using clear markers (e.g., `<<<<<<`, `=======,` `>>>>>>>`) to distinguish between the different versions).

2) Why Conflicts Happen

- **Independent Work:** Developers **work** on separate branches **without constant synchronization.**
	2 diff persons make 2 diff changes on the same file.

- **Parallel Change:** **The same lines of code are altered on both branches**, perhaps for different reasons. **Git isn't smart enough to guess which** (if any) **automatic merge is correct.**

3) **Resolving Conflicts**

- **Editing is Key:** You must open the file and manually address the marked area.

- **Three Options:**
    1. Keep the incoming change
    2. Keep your current change
    3. Create a new combined solution
    
- **Inform Git:** Once edited, you need to "stage" the change like a regular commit to signal it's resolved.
