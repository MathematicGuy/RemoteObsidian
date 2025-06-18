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



## Tài Liệu và Công Cụ Học Git
### 📚 Tài liệu chính thức
- [Pro Git Book](https://git-scm.com/book/en/v2) – Sách chính thống về Git  
- [Git Documentation](https://git-scm.com/doc) – Tài liệu chính thức từ Git  
- [GitHub Docs](https://docs.github.com) – Tài liệu GitHub chính thức  
- [GitHub Guides](https://guides.github.com) – Hướng dẫn GitHub cơ bản  

### 🎓 Khóa học trực tuyến
- [Atlassian Git Tutorials](https://www.atlassian.com/git/tutorials) – Hướng dẫn từ Atlassian  
- [GitHub Learning Lab](https://lab.github.com) – Học Git tương tác  
- [Codecademy: Learn Git](https://www.codecademy.com/learn/learn-git) – Khóa học Git cơ bản  

### ✍️ Blog & Bài viết hữu ích
- [Atlassian Blog về Git](https://www.atlassian.com/blog/git)  
- [Git Tower Blog](https://www.git-tower.com/blog)  
- [GitHub Blog](https://github.blog)  

### 🖥️ Công cụ GUI (Giao diện đồ họa)
- [GitKraken](https://www.gitkraken.com) – UI đẹp, nhiều tính năng  
- [Sourcetree](https://www.sourcetreeapp.com) – Hỗ trợ Git & Mercurial  
- [GitHub Desktop](https://desktop.github.com) – Tích hợp sâu với GitHub  
- **VS Code + Git Extensions** – Dùng Git trực tiếp trong trình soạn thảo  

### 💻 Công cụ dòng lệnh (CLI)
- [GitHub CLI](https://cli.github.com) – Tương tác với GitHub từ terminal  
- [Lazygit](https://github.com/jesseduffield/lazygit) – CLI UI trực quan  
- [tig](https://jonas.github.io/tig) – Trình duyệt repo trong terminal  
- [diff-so-fancy](https://github.com/so-fancy/diff-so-fancy) – Làm đẹp `git diff`  

### 🧩 Tiện ích mở rộng & Công cụ nâng cao
- [Git Flow](https://github.com/petervanderdoes/gitflow-avh) – Mô hình quản lý branch chuyên nghiệp  
- [Git LFS](https://git-lfs.github.com) – Quản lý file lớn trong Git  
- [Husky](https://typicode.github.io/husky) – Tạo Git hooks dễ dàng  
- [Conventional Commits](https://www.conventionalcommits.org) – Chuẩn hóa thông điệp commit  
