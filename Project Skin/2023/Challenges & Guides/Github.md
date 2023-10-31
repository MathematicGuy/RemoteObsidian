Pull -> Commit -> Push
## **NetBean Push and Clone**
	https://youtu.be/UOIPS-ewFHg?si=i_4yKMdw1Uc8ZRmi


### **Git Explained**
note: 

##### Git how to push 
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
$ git commit -M main
```
stage5: **connect to github repository** 
```shell
$ git remote add orgin http://github.com/user_name/git_name.git
```
stage6: **Push all file to the repository** 
```shell
$ git push -u origin main
```


##### Create an alternative code file to work on without changing the main code (on master branch)
**check current branch** (on progress for editing new-branch)
```shell
git branch
```
![[Pasted image 20231031110609.png]]
**Create an alternative branch**
```shell
$ git branch my-code-version
```
**Move into that branch to code**
```shell
$ git checkout my-code-version
```
or use this code to move into newly created branch 
```shell
git checkout -b new-branch
```


**Merge back to master branch** 
(combine branches into a single codebase)
```shell
$ git merge my-code-version
```
**Summary**
? How to merge man branch at once.
! Always want your local computer to synced up to github
! push when you have changed
! when github have changed when you don't have you pull




git pull origin main (main is the branch name )



##### re-visit old code reponsitory
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
	