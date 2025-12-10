## Make sense of Git
>Understand how Git Actually Work - finally understand *commits, branches, reset, rebase & more*. 

+ @ **Git is a database of Snapshot (ie. commit)** (history of your code stage). Sticky Note (HEAD, commit name or message, branch name, etc..) show where you are. 
![[Pasted image 20251208135134.png# left | 244]]

![[Pasted image 20251208135237.png]]
+ $ `git merge` - merge 2 commits into a new commit. New Commit now have 2 parents. Oh and the first commit obviously don't include any commit.    
+ ? HEAD - "You Are Here" pointer. 
+ ? When you checkout to fix an old Commit -> create a seperate branch or Git won't save your changes. 

When you add any file to git, it move to the `staging` area before getting `git commit -m "sth"` push to `changes`.
![[Pasted image 20251208135837.png# left | 433]]

`git checkout a_branch` - *check all of your code* of a Commit from anywhere. Allow you to access any version of your code in the past.
![[Pasted image 20251208140315.png# left | 332]]

`git reset` - move the branch pointer. **(IMPORTANT)**
	 `--soft` : *Re-commit.* If you have 3 commits push to main already git **Remove changes from Tree to Staging area (Stages)**, so you can ready to Commit them (again) or probably trash them.   
	 `--mixed` : **Your changes still exist in your File, just unstaged.**
	 `--hard` : **Delete all changes** (file, fodler, data, etc..) and return to your previous commit. A Fresh Restart. ![[Pasted image 20251208141620.png]]
 
`git revert` - Revert changes by **create a new Commit instead of deleting new changes**. Create a new commit thats *not include any changes that already push and shared.* You can't rewrite history but you can add to it. 
![[Pasted image 20251208142039.png]]
We remeber that `git merge` combine 2 commits into 1 new commit, 

`git rebase` (**most Obnoxious for newbie**) -  **Rewrite History** 
![[Pasted image 20251208143656.png]]

![[Pasted image 20251208143733.png | 444]]

![[Pasted image 20251208143750.png | 444]]

![[Pasted image 20251208143835.png | 355]]

![[Pasted image 20251208143951.png# left | 544]] 
+ ? **Explain:** C is a branch create from Y. This mean C is the same as Y but on a different branch. When rebase, you're basically 

(**RIGHT - New Commit, LEFT - Old Commit**)
The **old B and C still exist briefly** (in relog) - but **they're orphaned and will be garbage collected.** 
![[Pasted image 20251208144030.png]]
+ ? This is why you never rebase Commit that other have seen on REMOTE. 
+ $ While rebase are horrible and chaos in REMOTE, rebase really useful LOCALLY, it help your commit line linear and clean, not  multiple branch branching out.  

+ ? Again, like the above. `git rebase merge new feature into the main branch`
![[Pasted image 20251208153427.png | 233]]


`git reflog` - your safety net. Show history and address (hash) for all your COMMITs. Include all your checkout, all your commit and revert. 
![[Pasted image 20251208144537.png]]
`git branch recovery [address]` (b2c3d4e is a address)
+ @ Reflog can expire so act fast.  ![[Pasted image 20251208144717.png | 322]]

![[Pasted image 20251208145025.png]]
```ad-summary
+ Each time you save your code using git, you create a Commit. A Commit is a Snapshot of all your codes.

+ Git is just a Database of Commit. 

+ Your future commit are connect to your old commit create a commit tree, follow the DAG structure. Direct (one way) - Acrylic (no loop) - Graph (tree-base structure)

+ Each Commit contain a address and a point that point to the next Commit.

+ Sticky note HEAD above show which Commit you currently at. Each branch have a note above to show it name. 

+ Merge connect code from 2 commits into 1 commit.

+ `git add` - move all changes to waiting areas (ie. stages). Like a waiting room, you can pick specificaly which change you want to commit.    

+ `git commit` - move all (file) changes you choose to the `changes` area. File in changes can be push to the repository in github using `git push`.
  
+ `git reset` have 3 types. `--soft` move all changes from commit area (ie. changes) to staging area (ie. stages). `--mixed` remove all changes from the staging area, but preserve all changes in your code folder, basically return back before you even use `git add`. `--hard` reset everything back to the previous Commit by deleting every new changes. 
  
+ `git revert` instead of messing with git stages/changes, it create a new Commit, a replica of the original code before any changes was made.
  
+ `git rebase` - Move the Feature branch as the Head (Lastest Commit) of the Main branch.  
```

![[Pasted image 20251208160821.png]]
`~` mean *move backward*. 
	`git checkout HEAD~` : move backward 1 step
	`git checkout HEAD~2`  : move backward 2 step. 
`^` switch branch
	`git checkout HEAD^2` : Swap HEAD to side branch. (`HEAD^1` move to main Branch) 
+ ? Example: To move to C3 in 1 line, we could do:
	`git checkout HEAD~; git checkout HEAD^2; git checkout HEAD~2`: move backward 1 Commit, move to second branch, move backward 2 Commit.

`git branch -f main o/main` - move main and o/main sticky note from other Commit to HEAD Commit.  
`git branch feature C2` - add feature branch at C2 Commit. 
![[Pasted image 20251208174540.png# left | 141]]


`git fetch` - **JUST Download Commit as a NEW BRANCH from Remote** and Fill 'em up in Local if missing. 
`git pull` - **Download Commit as a NEW BRANCH from Remote  AND MERGE them with LOCAL commit.** Basically `git fetch` + `git merge` in 1 command. 
![[Pasted image 20251208171705.png# left  | 283]]


*Base repo*
![[Pasted image 20251208173010.png# left | 144]]
- Clone your repo `git clone`
- Fake some teamwork (1 commit) `git fakeTeamwork`
- Commit some work yourself (1 commit) `git commit` 
- Publish your work via _rebasing_ `git pull --rebase` + `git push`
	+ ! If you use `git fetch + rebase C2 C3` then you will get this error "That branch name "HEAD" is not allowed !". 
	+ $ Use `git fetch + git rebase C2`
![[Pasted image 20251208172910.png# left | 544]]

### Remote Tracking 
+ @ **Track** mean **Remote branch always follow the Local branch** even though they have different name. Both Local and Remote branch sync through a intermediate call address, the remote addresss in our example is: `o/main`.  Real remote example: `origin/HEAD` `origin/main`

**Create new branch with remote tracking**
`git checkout -b totallyNotMain o/main` - Creates a new branch named `totallyNotMain` and sets it to track `o/main`.
![[Pasted image 20251208182020.png]]

![[Pasted image 20251208182033.png]]

**Add remote tracking to Existed Branch**
`git branch -u o/main foo` - will set the `foo` branch to track `o/main`. If `foo` is currently checked out you can even leave it off: `git branch -u o/main`
![[Pasted image 20251208182130.png]]

+ ? **Example:** You want remote main always follow your new Feature branch name `side`. So you use `git branch -b side o/main` to make the remote branch `o/main` always follow local branch `side` and in reverse. When `git pull --rebase`, `main` from remote will rebase to `side` (not `main`), and changes from `side` will be push to `main`. 
+ @ Intermedia often called "main" or "master" in real world. 
+ $ Just think `o/main` as the connection between Local and Remote. Whichever branch connected to `o/main` sync together   
![[Pasted image 20251208183615.png | 533]]

![[Pasted image 20251208183604.png | 633]]

### Push Local Code straight up to New Remote Branch
`git push origin <source>:<destination>` - This is commonly referred to as a colon refspec. Refspec is just a fancy name for a location that git can figure out (like the branch `foo` or even just `HEAD~1`). 

+ $ Like a pointer, `^` refer to the previous Commit of the Current Commit. `^foo` refer to the Commit previous `foo`. 
+ ? `^` (caret) symbol is used to refer to a **parent commit in the commit history**. It's a way to **navigate the commit graph relative to a specific commit**.
![[Pasted image 20251208184926.png]]

![[Pasted image 20251208184941.png]]


`git push origin main^:foo`
`git push origin foo:main`
![[Pasted image 20251208190421.png]]


### Cherry-pick
`git cherry-pick` - Allow you to cherry-pick specific Commit and connect it to the current Commit. 
+ ? Example: `git checkout C1; cherry-pick main side test` -> now 3 commit `main side test` are connected into a line with C1 as their root/first Commit. 

`git rebase -i HEAD~2`: rebase iteratively 2 COMMIT below. 
`git rebase -i C5`: If before `C5` was `C4 C3 C2` and the HEAD is `C1`, then all of them will be rebase to the `C1` as `C4' C3' C2'` while the original `C4 C3 C2` become Orphan Commit which will be clean up after that.  

**Basic workflow when pulling code from Remote.**
![[Pasted image 20251208174741.png]]

## Git & Github for Version Control
![[Pasted image 20250617094558.png# left]]

### Version Control Systen (VCS)
Use to track and Save changes of a files, system through times.
![[Pasted image 20250617094931.png# left |260]]

#### 2 Types of VCS: Centralize VCS and Distributed VCS
**Centralize VCS:** risky if server broken/failing.   
![[Pasted image 20250617095201.png| 400]]

 
**Distributed VCS:** Everybody have their own version which is a direct copy from the Server. This allow everyone to modified their own version without worrying the original version from the Database (e.g. github is a database for code)
![[Pasted image 20250617095211.png| 400]]

Mỗi khi có sự thay đổi, git chỉ lưu lại đúng sự thay đổi đó giúp tiết kiệm tài nguyên. 
Mọi version đc lưu offline trên local. Chỉ khi cần lưu trên github thì ms online. 

### File Status in Git
![[Pasted image 20250617101105.png]]

![[Pasted image 20250617101117.png]]

**git log for tracking commit history information**
![[Pasted image 20250617101214.png]]
`git log` show commit comment and each git information
![[Pasted image 20250617101803.png|400]]
`git log --stat`
![[Pasted image 20250617101550.png|400]]

`git log --author="Sukmadi"` retrieve commit of a specific author

`git log --oneline --graph --all` view git connection (Only use when you don't have Gitlen)
*or* 
`git log --graph --all`

### Restore Changes at Different Stages (Untracked, Modified, Stages, Commited)
`git restore <file>`  restore file back to their previous commit 
`git restore --staged <file>`  bring file from stages to modified
`git commit --amend`  fix commit message or add file to final commit 
`git revert <commit-hash>` - create a completely new commit to revert changes
+ ! `git restore` will delete all unchanges commit completely, cannot be restore.  

**For safer option:**
`git stash` temporary save changes
`git stash pop` reapply changes save 
`git reset` -> *reset back to previous version* (becaful because this affect commit history)
`git restore --staged file.txt` remove file from staging area but keep them in working directory. 

### Working with Remote Repository
`git remote -v` check fetch (pulll from) push (push to) github directory
![[Pasted image 20250617110333.png]]

Push commit to remote
`git push origin main`

Pull changes from remote to local machine. 
`git pull original main`
`git pull --rebase`

Pull is the combination of `fetch` and `merge`, more detail:
`git fetch` or `git fetch all` # get changes from remtoe
`git merge origin/main` # merge changes from remote to local

**Abort git operation**
`git merge --abort` abort merge operation
`git revert --abort` abort revert operation


**Remote Repository**
The image show from the 1 Version from Remote, each local machine can make a copy of the remote repository 
>by pull the Repository from Online Repository to create their own, called Local Repository.  
+ ? When a Local Machine commit and push a new version to the Online Repositry, every other Version have to pull the new code back to their Version, before pushing their new code to the Online Repository.  
![[Pasted image 20250617110637.png| 600]]

**Tagging** - use tag to annotate important information in repository history. 
+ **Annotated Tag** - tag with user/developer infor, created data and message. **Should be use for a release version.** `git tag -a 1.0 -m "Version 1.0 - official release"` where `-a` mean annotation and `-m` mean message.

**Lightweight tag** - a simple pointer to a specific commit, no save additional information. *Suitable for personal annotation.* `git tag v1.0-beta`

**Push tag to Remote**
+ Push a specific tag: `git push origina v1.0`
+ Push all tag: `git push origina --tags`

**View Tag** `git show <tag_name>` e.g. `git show v1.0`
![[Pasted image 20250617111544.png| 500]]

`git tag -` view all tags

### Resolve Conflict when Merge
**Conflict occur when** 2 branch modified the same part of a file but with different content, now there are 2 versions of a file. Git not sure which version to choose so it ask you to choose which version manually. 
+ ? Modern git allow you to choose between version (before) and (after), so you could debug file conflict quite easily.


### Branch Mangement and History
**Branch is a Pointer** pointed to specific Commit in git changes history of your github project. In Essence:
+ New Commit -> Branch pointed is automatically point to that commit. 
+ A Branch is a small file contain Hash Code SHA-1. That why git create branch so fast. 

(talk more detail about Branch and Commit architecture, pointer and hash code)

**Different Branchs** allow
+ *Developer to develop and testing new features without worrying affecting the orignal code* (on github). Because everyone is editing a copied version of the original code. 
	  
+ *Allow multiple people working/editing together on a codebase without conflict*, if there conflict, its doesn't affect other people who currently working on its. 

**Branch History** can be see as a TREE with multiple branches. Each branch represent a modified version of the original code which then can be merge and rebase (tái cơ sở) to create a complete/unified code. Tree architecture help code versions tracking much easier for developement.   
+ $ `"main"`  and `"master"` is the **default name for original code.** 

**Ví dụ minh họa**
1. Bạn đang làm việc trên nhánh chính main.
2. Tạo nhánh mới để phát triển tính năng đăng nhập:
	`git checkout -b feature/login`
3. Làm việc và commit trên nhánh feature/login mà không ảnh hưởng đến nhánh main.
4. Khi hoàn tất, chuyển về nhánh main và gộp nhánh:
	`git checkout main`
	`git merge feature/login`
	
**In Summary:** different branch allow independent development, testing and debug without affect the original code, this improve teamwork efficiency and avoid conflict. 


+ ? Ví dụ: Tạo và sử dụng nhánh. vs file login trong folder feature  
![[Pasted image 20250617152700.png]]
**Tạo và chuyển nhánh**
	`git checkout -b feature/login`
**hoặc:**
	`git branch feature/login`
	`git checkout feature/login`
**Commit trên nhánh mới**
	`git add .`
	`git commit -m "Thêm tính năng đăng nhập"`
**Gộp nhánh**
	`git checkout main`
	`git merge feature/login`

#### Branch Mangement Code  
![[Pasted image 20250617152842.png]]

In case you want to start a completely new branch that is not related to the original/root branch `git checkout --orphan new_branch_name`

### Rebase
When to use `git rebase` 


## Exercises
![[Pasted image 20250617153914.png]]

![[Pasted image 20250617153921.png]]

![[Pasted image 20250617153934.png]]


