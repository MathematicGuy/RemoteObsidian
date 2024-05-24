source: https://www.youtube.com/watch?v=RxHJdapz2p0


![[Pasted image 20240222132710.png]]
Code store using Git called Object Database
```ad-info
**Snapshots, Not Diffs:** Git fundamentally stores snapshots of your entire project at different points in time (commits), rather than just the changes between them. This has performance implications.

**Content-Addressable Storage:** Git generates a unique hash (like a fingerprint) based on the file contents. This makes finding duplicates and detecting changes extremely quick.
```

Get Key of a File
```bash
git hash-object [file_name] -w
```
See Object inside the File
```bash
git cat-file blob [key]
``` 



Git trees
> A tree represents a directory
![[Pasted image 20240222133756.png]]

```ad-info
- **Three Trees:** Each commit keeps track of three "trees" of objects:
    - **The Blob Tree:** Represents the actual file contents (text, code, etc.)
    - **The Directory Tree:** Stores the folder structure and names of files.
    - **The Commit Tree:** Keeps track of the metadata (author, timestamp), and links back to the previous commit, forming the project history chain.
```
>A blob represents file contents without metadata
![[Pasted image 20240222134309.png]]

![[Pasted image 20240222133950.png]]
Commit save each Branche changes into a hashcode key 
![[Pasted image 20240222134001.png]]
A commit is a snapshot of the project
	Each time we make a change the Branches update a new hashcode.
	Each commit have its own hashcode. Every Commit are unique. 
> Imagine Branches like a Drawing Canvas. Each Color Stroke is a Commit. The Canvas changes for every Stroke the artist make. And Each Stroke is different from the rest.
+ ! Commit is immutable (bất biến). Branches is mutable (có thể thay đổi)  


- **git merge:** Here's where it gets more complex:
    1. Git finds the most recent common ancestor commit for the two branches you're merging.
    2. It compares the trees of that ancestor commit to the latest commits on each branch to see what changed.
    3. If changes don't conflict, Git does an automatic merge.
    4. If conflicts exist (same code changed differently), you need to resolve them manually.
```ad-info
**Why This Matters**

- **Speed:** The content-addressable system makes Git very fast at detecting changes and figuring out if files are identical.
- **Backups:** Since it's snapshots, even if you mess up, old versions are still stored, not overwritten.
- **Branching:** Branches are just pointers to commits, which is why they are 'lightweight' and easy to create.
```


+ **git diff**
	Do this when I found out there a bug from one of the feature (new button) on the "main" branch and got it fix another branch: "hotfix". But I cannot just merge 2 Changes together because they are changes to 1 file in 2 different branches. 
-> So I need to merge it with the branch which I orinally pulled this code from (C). 
	![[Pasted image 20240222135621.png]]
	git diff `[commit_key1]` `[commit_key2]` (Check Conflict)
> 	Check Similarity & Differences from 2 Commits
	![[Pasted image 20240222140134.png]]
	`

 (Advance level)
![[Pasted image 20240222140802.png]]
Find a diff branche -> applied the changes into the main branch like everything was written from the main branche sequentially
![[Pasted image 20240222140851.png]]


>applying changes from a single commit on top of another commit
