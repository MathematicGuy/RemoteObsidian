
### What is .gitignore
> Git ignore is a way to ignore files and folders that you don't want to push on git. (e.g.  heavy file)

### How to use .gitignore?
1) **Create or Open `.gitignore`:**
	If you don't already have a `.gitignore` file in your repository, create one in the root directory of your project.

2) Add the Folder to `.gitignore`:
	For example, if you want to ignore a folder named `build`, add the following line to `.gitignore`:
```.gitignore
build/
```

3) **Remove the Folder from Git (If Already Tracked):**
+  If the folder has already been committed and is being tracked by Git, you'll need to remove it from the repository history while keeping the local copy. Use the following commands:
```bash
git rm -r --cached folder_name/
```
	
+ Then push the changes
```bash
git push origin your-branch-name
```



### Special Examples

The entry `.idea/*` in a `.gitignore` file is used to ignore all files directly within the `.idea` directory. Here’s what each part means:

- **`.idea/`**: Specifies the `.idea` directory. The trailing slash indicates that it's a directory, not a file.
    
- **`*`**: The asterisk is a wildcard that matches any file or directory name within `.idea`. However, this only applies to files and directories directly inside `.idea`, not subdirectories or their contents.
    
#### How It Works:

- **`.idea/*`**: This pattern will ignore all files (and directories) directly under the `.idea` directory. For example:
    - `.idea/workspace.xml` will be ignored.
    - `.idea/modules.xml` will be ignored.
    - `.idea/someFolder/` will be ignored as a folder, but not the contents of `someFolder`.

#### Important Note:
If you want to ignore everything inside `.idea`, including all subdirectories and their contents, you would use:
```.gitignore
.idea/
```
This would ensure that the entire `.idea` directory, along with all its contents (including nested subdirectories and files), is ignored by Git. 

#### Example Scenarios:

1. **Ignore only files directly inside `.idea`**:
    
    - `.gitignore` entry: `.idea/*`
    - Result: Files like `.idea/workspace.xml` will be ignored, but files in subdirectories like `.idea/codeStyles/style.xml` will not be ignored.
2. **Ignore the entire `.idea` directory and everything inside it**:
    
    - `.gitignore` entry: `.idea/`
    - Result: The `.idea` directory and all its contents, including subdirectories, will be ignored.
