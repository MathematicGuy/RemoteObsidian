Set up [SHH Keys](https://youtu.be/RGOj5yH7evk?si=uBO5M8sRXltefoGh&t=1230) (using GitBash Terminal)
SSH - Secured Shell
+ Used for authentication
+ By setting ssh key you can connect to GitLab server without using usemame and password each time

[Connect SSH key to Github](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account?platform=windows&tool=webui)

**Check your connection**
```bash
ssh -T git@github.com
```

**Switching git branch**
HEAD -> my-feature indicate that we currently on my-feature branch.
![[Pasted image 20231114220055.png]]

You must goes into the folder contain the file to commit the file. (Or have at least a file in the current directory)
```bash
git add .
```

Importance git branch operation
```bash
git branch
git status 
git checkout branch_name
```

Delete a branch
```bash
git branch -d my-feature
```

Save working directory & see changes
```bash
git stash push
git stash list
```

```bash
git stash apply
```


