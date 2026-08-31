# Useful Terminal Commands

A lookup reference based on the terminal crash course.
Use this to refresh your memory on the commands we covered, what they do, and why you'd use them.

## Finding your way around

| Command | What it does |
|---|---|
| `pwd` | **P**rint **w**orking **d**irectory — shows the full path of where you currently are. |
| `ls` | Lists the files and folders in the current directory. |
| `ls -la` | Lists **all** files (including hidden ones, i.e. those starting with `.`) in **l**ong format, showing permissions, size, owner, and modification date. |
| `ls -lah` | Same as above, but with **h**uman-readable file sizes (e.g. `4.0K` instead of `4096`). |
| `cd <folder>` | **C**hange **d**irectory into `<folder>`. |
| `cd ../` or `cd ..` | Go up one level to the parent directory. |
| `cd -` | Go back to the **previous** directory you were in. |
| `cd /` | Go to the root directory of the filesystem. |
| `cd ~` | Go to your **home** directory (`~` is shorthand for it). |

> [!TIP]
> Hidden files (dotfiles like `.gitignore`, `.zshrc`) don't show up with a plain `ls` — you need the `-a` flag to see them. Every directory also contains `.` (itself) and `..` (its parent), which is why `ls -la` always shows at least those two entries.

## Getting help

| Command | What it does |
|---|---|
| `man <command>` | Opens the **man**ual page for `<command>`. Press `q` to quit. |

## Creating and managing files/folders

| Command | What it does |
|---|---|
| `mkdir <name>` | **M**a**k**e a new **dir**ectory called `<name>`. |
| `touch <file>` | Creates an empty file (or updates the timestamp if it already exists). |
| `cat <file>` | Prints the contents of `<file>` to the terminal. Good for quickly checking small files. |
| `rmdir <folder>` | Removes an **empty** directory. Fails if the folder still contains files. |
| `rm <file>` | Removes (deletes) a file. **This is permanent — there is no trash bin.** |

> [!WARNING]
> `rm` does not ask for confirmation and does not send files to a recycle bin. Double-check the path before you hit enter, especially with wildcards (`rm *`) or the recursive flag (`rm -rf`).

To delete a non-empty folder, you generally need to delete its contents first (e.g. `rm tmp/test.txt`) and then `rmdir tmp`, or use `rm -r tmp` to delete recursively in one go.

## Editing files

| Command | What it does |
|---|---|
| `vi <file>` | Opens `<file>` in the `vi`/`vim` text editor (works entirely inside the terminal). |
| `open .` | (macOS) Opens the current directory in the graphical file browser (Finder). |

> [!TIP]
> The one thing you need to learn about `vi` for now is how to get out of it. Press `Esc` to enter command mode, then type `:q` to quit (or `:q!` to quit without saving, or `:wq` to save and quit). 

## Making scripts executable

A script is just a text file with commands in it. To run it directly (rather than passing it to an interpreter), two things need to happen:

1. Add a **shebang** line as the very first line of the file, telling the system which interpreter to use, e.g.:
   ```bash
   #!/bin/zsh
   ```
2. Make the file executable:
   ```bash
   chmod +x test.txt
   ```

| Command | What it does |
|---|---|
| `chmod +x <file>` | **Ch**anges the file's **mod**e to add the e**x**ecutable permission. |
| `./test.txt` | Runs the file directly (the `./` tells the shell to look in the current directory rather than searching the system `PATH`). |
| `zsh test.txt` | Runs the file's contents by explicitly passing it to the `zsh` interpreter — works even without the shebang or executable permission. |

## Command history & shortcuts

| Command / Shortcut | What it does |
|---|---|
| `history` | Lists previously run commands. |
| `↑` (up arrow) | Recalls the previous command, one at a time. |
| `Ctrl + R` | Starts a **reverse search** through your command history — start typing and it will find matching past commands. Press `Ctrl + R` again to cycle through more matches. |
| `clear` | Clears the terminal screen (does not delete history). |

## Remote connections

| Command | What it does |
|---|---|
| `ssh <user>@<host>` | Opens a secure shell connection to a remote machine, e.g. `ssh username@hpc.zhaw.ch` for the HPC cluster. Once connected, the commands above apply to the remote machine you're connected to. |

> [!NOTE]
> You can set up a shortcut for it: e.g., `hpc.zhaw` in the `~/.ssh/config` file.
> This way you can just type `ssh hpc.zhaw` instead of the full command.

## Git

Git is a version control system — it tracks changes to your files over time and lets you sync those changes with a remote repository (e.g. on GitHub).

| Command | What it does |
|---|---|
| `git clone <url>` | Downloads a copy of a remote repository (and its full history) into a new folder on your machine. |
| `git status` | Shows which files have changed, which are staged for commit, and which are untracked. Your go-to command to check the current state. |
| `git add <file>` | Stages `<file>` — marks it to be included in the next commit. Use `git add .` to stage all changed files in the current directory. |
| `git commit -m "<message>"` | Saves the staged changes as a new commit (a snapshot) with a short description of what changed. |
| `git push` | Uploads your local commits to the remote repository. |
| `git pull` | Downloads and merges the latest changes from the remote repository into your local copy. |

> [!TIP]
> A typical local workflow looks like this:
> ```bash
> git status              # see what changed
> git add .                # stage the changes
> git commit -m "..."      # save a snapshot with a message
> git push                 # upload to the remote
> ```

> [!NOTE]
> Always `git pull` before you start working (and before you `push`) to make sure you have everyone else's latest changes and avoid conflicts.