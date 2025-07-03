### What Is Linux? Why Is It Important?

- **Linux** is an open‑source operating system kernel first released by Linus Torvalds in 1991 .
    
- **Key strengths for data science**:
    
    - **Performance at scale:** powers about 90 % of high‑performance computing clusters .
        
    - **Automation:** you can script data pipelines end‑to‑end via simple shell commands.
        
    - **Ecosystem:** native support for big‑data tools (Hadoop, Spark) and integration with Python/R .
        
- **Beginner example:**
    
    ```bash
    # Count how many times each IP appears in all log files
    cat logs/*.log | grep ERROR | awk '{count[$1]++} END{for (ip in count) print ip, count[ip]}'
    ```
    
    This one‑liner reads every log, filters “ERROR” lines, tallies IPs, and prints a summary—no GUI needed!


---

### Common Linux Distributions

Linux comes in many “distributions” (bundles of the kernel plus tools) tailored to different users :

|Distribution|Who It’s For|Why It’s Handy|
|---|---|---|
|**Ubuntu**|Beginners & general use|Friendly setup, long‑term support|
|**Debian**|Stability & reliability|Rock‑solid foundation|
|**CentOS/RHEL**|Enterprises|Enterprise‑grade security|
|**WSL**|Windows users|Run Linux directly on Windows|

> **Tip:** If you follow an online tutorial, it almost certainly uses Ubuntu commands—so you’ll find answers easily.

---

### Unix Philosophy

Unix’s guiding principles make it so powerful for data work :

1. **Small, specialized tools:** each command does one job well (e.g., `grep` to search, `sort` to sort).
    
2. **Everything is a file:** from text data to hardware devices, you can read and write uniformly.
    
3. **Composable via pipes (`|`):** you chain tools by sending one’s output into another’s input.
    

```bash
# Example pipeline: extract “temperature” lines, sort them, count unique entries
cat data.csv \
  | grep "temperature" \
  | sort \
  | uniq -c \
  > temp_report.txt
```

> _Analogy:_ Think of each command as a LEGO block—you snap them together to build complex workflows.

---

### What Is a Shell?

- A **shell** is the program that reads your typed commands and tells the system what to do .
    
- **Terminal vs. Shell:**
    
    - **Terminal:** the window or emulator (e.g., GNOME Terminal) where you type.
        
    - **Shell:** the command interpreter inside (e.g., Bash).
        
- **Popular shells:**
    
    - **Bash:** the default on most systems.
        
    - **Zsh/Fish:** offer nicer autocomplete and suggestions.
        
- **Sample session:**
    
    ```bash
    $ pwd            # show current folder  
    /home/d/projects  
    $ ls -la         # list all files with info  
    -rw-r--r-- 1 d staff 512 Jun 27 09:45 data.csv  
    ```
    

---

### Linux Folder Structure

Linux uses a fixed hierarchy starting at `/` (“root”) with special folders for different purposes :

|Directory|Contains|
|---|---|
|`/bin`|Essential commands (`ls`, `cp`, `grep`)|
|`/etc`|Configuration files (network, users, services)|
|`/home`|Your personal files (e.g., `/home/d`)|
|`/var`|Variable data (logs in `/var/log`, mail spools)|
|`/usr`|Installed applications and libraries|
|`/opt`|Optional third‑party software|

> **Example:** Your data project might live under `/home/d/projects/my-analysis`, while system logs you inspect reside in `/var/log`.

### Part 1 Unix/Linux Overview Summary

```ad-summary
• Linux is the open‑source kernel powering most data‑science backends.  
• Distributions (Ubuntu, Debian, CentOS, WSL) fit different user needs.  
• Unix philosophy: build small, focused tools and chain them with pipes.  
• The shell (e.g., Bash) is your command interpreter inside a terminal.  
• A clear directory tree (/bin, /etc, /home, /var, /usr, /opt) keeps things organized.  
```



## 2. Basic Commands

**Why learn these?** They’re the foundation for managing your data‑science projects: organizing files and folders, inspecting and searching data, editing scripts, controlling who can see what, and keeping an eye on running analyses .

---

### Create & Manage Files / Directories

* **`pwd`**: “Print Working Directory” – shows your current folder.
* **`cd`**: “Change Directory” – move around the filesystem.

  ```bash
  cd ~/projects/data-analysis   # go to your data-analysis folder  
  cd ..                         # go up one level (to the parent folder)
  ```
* **`ls`**: “LiSt” – list files and folders.

  ```bash
  ls -l        # long format: shows permissions, owner, size, date  
  ls -la       # include hidden files (those starting with .)  
  ```
* **`mkdir`**: “MaKe DIRectory” – create new folders.

  ```bash
  mkdir data                   # make a single folder named “data”  
  mkdir -p project/{data,src}  # make project/data and project/src in one go  
  ```

*Example:*

```bash
pwd && mkdir -p project/{data,scripts,results} && cd project  
```

This prints where you are, creates a “project” folder with subfolders “data,” “scripts,” and “results,” and moves you into it .

---

### View File Contents

* **`cat`**: show an entire file (small files only!).

  ```bash
  cat README.md
  ```
* **`less`**: browse large files page by page (use arrows to scroll, `/` to search, `q` to quit).

  ```bash
  less huge_log.txt
  ```
* **`head`/`tail`**: peek at the start or end.

  ```bash
  head -n 10 data.csv    # first 10 lines (e.g., to inspect headers)  
  tail -n 20 data.csv    # last 20 lines (e.g., to see recent entries)  
  ```

*Example:*

```bash
head -n 5 data.csv | less  
```

Shows the first 5 lines, piped into `less` so you can scroll if needed .

---

### Search Files & Data

* **`grep`**: search inside files for text patterns.

  ```bash
  grep "ERROR" logs/*.log       # show only lines containing ERROR  
  grep -r "NullPointer" src/     # search recursively in src/ directory  
  ```
* **`find`**: locate files by name, type, or date.

  ```bash
  find . -name "*.csv"           # all CSV files under the current folder  
  find ~/data -type f -mtime -1  # files modified in the last 24 hours  
  ```

*Example:*

```bash
find project/data -name "*.csv" | grep "2023"  
```

Lists all CSVs under `project/data` whose names include “2023” .

---

### Interact with Basic Text Data

* **`sort`**: order lines alphabetically or numerically.
* **`uniq`**: remove or count duplicate lines (use after `sort`).
* **`wc`**: word/count – counts lines (`-l`), words, or characters.
* **`cut`**: extract columns or character ranges.
* **`sed`**: stream editor—find & replace or print specific lines.
* **`awk`**: mini‑programming language for column‑wise processing.

```bash
# Count how many times each user ID appears in a sorted file
sort user_ids.txt | uniq -c | sort -nr

# Compute average of column 3 in a CSV
awk -F',' '{sum+=$3} END {print "Avg:", sum/NR}' metrics.csv

# Replace all commas with tabs in data.csv
tr ',' '\t' < data.csv > data.tsv
```

*Example:*

```bash
cut -d',' -f1,4 sales.csv | sort | uniq -c | wc -l  
```

Extracts columns 1 and 4, counts unique combos, then totals how many distinct entries you have .

---

### Edit Files with vi/vim

Even if you prefer GUI editors later, knowing vim is invaluable on servers:

1. **Open:** `vim script.sh`
2. **Insert mode:** press `i`, type your changes.
3. **Exit insert:** press `Esc`.
4. **Save & quit:** type `:wq` then `Enter`.
5. **Quit without saving:** `:q!` then `Enter`.

*Tip:* in a pinch, learn just these five steps to tweak scripts on remote machines.

---

### Environment Variables

Settings that configure your tools and libraries:

* **`PATH`**: where to look for commands.
* **`PYTHONPATH`**: where Python finds extra modules.
* **`OPENBLAS_NUM_THREADS`**: number of CPU threads for NumPy/Pandas.
* **Exporting:**

  ```bash
  export VAR_NAME=value      # sets for current session  
  echo $VAR_NAME             # show its value  
  ```

To make permanent, add `export …` lines to `~/.bashrc` or `~/.bash_profile` .

---

### Permissions & Ownership

Linux uses **rwx** flags for **u**ser, **g**roup, and **o**thers:

* **`chmod`**: change permissions.

  ```bash
  chmod u+x train.py        # add execute permission for owner  
  chmod 750 scripts/        # owner rwx, group rx, others none  
  ```
* **`chown`**: change file owner/group.

  ```bash
  chown d:analytics data.csv  # make “d” owner, group “analytics”  
  ```

*Why it matters:* when you share data or run on clusters, correct permissions keep your models and keys safe .

---

### Process Management for Data‑Science Projects

* **`ps aux | grep python`**: list all Python processes (e.g., training jobs).
* **`top -u username`**: real‑time view of your processes’ CPU/RAM use.
* **`kill -9 PID`**: force‑stop a stuck job by its ID.
* **`nohup python train.py &`**: run in background, staying alive after logout; outputs go to `nohup.out`.

*Example:*

```bash
ps aux | grep train.py  
kill -9 12345  
nohup python train.py > train.log 2>&1 &  
```

Keeps your long‑running model training safe from accidental disconnection .

---

## Exercise 1

**Goal:** apply these basics to set up a data‑analysis project.

1. **Create project structure**

   ```bash
   mkdir -p project/{data,scripts,results}
   ```
2. **Secure scripts folder** (owner rwx, group rx, others none):

   ```bash
   chmod -R 750 project/scripts
   ```
3. **Find all CSV files** under `project/`:

   ```bash
   find project -type f -name "*.csv"
   ```
4. **Verify structure & permissions**:

   ```bash
   ls -lR project
   ```

### Part 2 Basic Commands Summary

```ad-summary
• Navigate & organize: cd, pwd, ls, mkdir (with -p for nested folders)  
• Files: touch, cp, mv, rm (use -i or -r safely)  
• Inspect content: cat, less, head, tail  
• Search: grep for text, find for file names/types  
• Text processing: sort, uniq, wc, cut, tr, sed, awk  
• Edit on servers: vim (i, Esc, :wq, :q!)  
• Settings: export and echo environment variables  
• Security: chmod/chown to set permissions and ownership  
• Processes: ps, top, kill, nohup for running and managing jobs  
```

### Part 3

`[^}]*\` mean for every pattern. 
`{[^}]*\}` mean for every pattern inside `{}` 
**Apply Regex:** `\` to `a_pattern` e.g. `\a_pattern`. This work the same for Pattern already have  `\` like `\item`, just do `\\item` -> work like normal. 
**Replace Text Pattern using Regex**. Regex but wrap with `()`, the pattern inside will automatically set as `\1` 
	e.g. `( text pattern to replace )`![[Pasted image 20250701151448.png]]
All Case Study below apply the same logic. Which is `\` to apply Regex Expression, `()` to wrap a regex expression pattern for replacement.  

**Apply Regex and Replace single Pattern**
Replace Item: `( \\item \\texttt\{[^}]*\})` -> can also be call as `\1` 
With: `{\\item \\texttt\{[^}]*\}}` or `{\1}` -> do the same thing
+ ? In VSCode, `\1` is set as  `$1`.  

**Apply Regex and Replace multiple Pattern**
Replace Item: `(\\item) (\\texttt\{[^}]*\})` -> automatically set as `\1\2`
With: `{\\item} [\\texttt\{[^}]*\}]` or `{\1}[\2]` -> do the same thing

**Apply Regex and Replace between Pattern**
Replace Item: `(\\item) (\\texttt\{[^}]*\})` -> automatically set as `\1\2`
With: ``\1  \\colorbox{codehighlight} {\2}`` 
