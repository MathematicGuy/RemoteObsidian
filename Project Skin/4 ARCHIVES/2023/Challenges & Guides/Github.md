Pull -> Commit -> Push
## **NetBean Push and Clone**
	https://youtu.be/UOIPS-ewFHg?si=i_4yKMdw1Uc8ZRmi


#### [[Github for Beginners]]

#### [[How to be a Git Expert]] (Appending)

#### [[How GIT works under the HOOD]] (Appending)

#### [[Git for Professionals]] (Later)

### Git Explained


##### Git how to push 
+ ! Press 'q' to exit preview stages in terminal
note: repository mean folder, same 
stage-1: **repo- tracks the diff (changes) to your codebase**
```shell
$ git init
```
stage-2:  **. mean add all file to the branch** 
```shell
$ git add .
```
stage-3: **commit all file as a branch** 
```shell
$ git commit -m "message here"
```
stage-4: **set commit branch as main (master) branch** 
```shell
$ git commit -m main
- [ ] ```
stage5: **connect to github repository** 
```shell
$ git remote add orgin http://github.com/user_name/git_name.git
``` 
stage6: **Push all file to the repository**  (-u mean up stream)
+ --set-upstream: 
	**sets up a tracking relationship between the local branch ("main") and the remote branch ("main" on "origin").**
+ -u option is a shorthand for --set-upstream.

**Do this on First push**
```shell
git push --set-upstream origin main
```
or this
```shell
git push -u origin main
```
or if you wan to push your code to other repository
+ ? **upstream** is where you see all the repository you connected to. Like when you fork other people repository, their branch 'main' will show in the **upstream**
```shell
git pull upstream main # pushing code to main branch from upstream
```


or  push your own branch to origin
```shell
git push -u origin side-branch
```

to view all available branch
```shell
git branch -a
```

##### Create an alternative code file to work on without changing the main branch (eg. master branch)
**check current branch** (on progress for editing new-branch)
```shell
git branch
```
![[Pasted image 20231031110609.png]]
**Create an alternative branch (new branch)** 
```shell
$ git branch my-code-version
```
**Move into that branch ( to code )**
```shell
$ git checkout my-code-version
```
> The code edited in this branch doesn't related to the main branch. So you can modify code without changing your original code. (Prevent adding dumb code but can't go back)

or use this code to move into newly created branch 
```shell
git checkout -b new-branch
```

**After finish modifing code, add to branch** 
```shell
git add . 
git commit -m "new save file"
```
Send pull request to get all lasted code update on main branch. 
```shell
git pull origin main 
```


**Merge back to master branch** 
(combine branches into a single codebase)
```shell
$ git merge my-code-version
```
**Get the latest branch update**
```shell
git pull origin main (main is the branch name)
```

**Summary**
? How to merge man branch at once.
! Always want your local computer to synced up to github
! push when you have changed
! when github have changed when you don't have you pull


##### Reponsitory history & Revisit past Code
```shell
$ git log
```
check out the commit token
![[Pasted image 20231031104945.png]]
> Now you back to your old repository
```shell
$ git log 5f54dfa54343c1d7aa36f41dd8f5211345433c24
```

**create new file in windown shell** [(bc can't use touch)]([powershell - touch command not working, what should I use instead? - Stack Overflow](https://stackoverflow.com/questions/67659993/touch-command-not-working-what-should-i-use-instead))
```shell
New-Item new.html
```


### …or push an existing repository from the command line
```shell
git remote add origin git@github.com:MathmatheticGuy/WedJourney-Update-0.1.git
git branch -M main
git push -u origin main
```

### [How to disconnect a local Git repository from remote master](https://stackoverflow.com/questions/29583706/how-to-disconnect-a-local-git-repository-from-remote-master)
```shell
git remote rm origin
```


### Git Config 
```shell
git config --global user.name "Sukmadi"
git config --global user.email "nhatthanhdinh482@gmail.com"
```

### Git Branch
See all Active Branch in a Project, Fetch and Switch Branch 
```bash
git remote show origin
git fetch origin
git switch branch_name
```

Change Last Git Msg (recommit)
```bash
git commit --amend -m "cooler msg!"
```

**Add Files** to last commit
```bash
git commit --amend --no-edit
```

**Overwrite** history on remote 
```bash
git push origin master --force
```

**Undo** a commit with a **New** commit
```bash
git revert better-days
```

