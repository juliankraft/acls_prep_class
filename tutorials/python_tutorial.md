# Instructions on how to get started using Python for the ACLS master program

These are instructions to get started using Python in the ACLS master program.
Please follow the steps below carefully.
Do not hesitate to engage us and ask questions if you have any issues.

## Step 1: Install your IDE

If you haven't already done so, please install your IDE (Integrated Development Environment) of choice.
[code.visualstudio.com](https://code.visualstudio.com/) or [jetbrains.com/pycharm](https://www.jetbrains.com/pycharm/)

### If you are using Pycharm:
Apply for the free student license for the professional edition of Pycharm at [jetbrains.com/academy/student-pack/](https://www.jetbrains.com/academy/student-pack/).

### If you use VS Code on Windows:
Install the WSL extension for VS Code and check out, how this works on [marketplace.visualstudio.com](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl)

## Step 2: Create a Python environment

Check out the [Mamba User Guide](https://mamba.readthedocs.io/en/latest/user_guide/mamba.html).
Open a terminal (WSL on Windows) and try to do the following tasks:
1. Create a new environment called `test`
2. List all environments to check if the new environment is there
3. Activate the `test` environment
4. Deactivate the `test` environment
5. Delete the `test` environment

<details>
<summary>Click to reveal the commands (try it yourself first!)</summary>

1. Create a new environment called `test`:
   ```bash
   mamba create -n test
   ```
2. List all environments:
   ```bash
   mamba env list
   ```
3. Activate the `test` environment:
   ```bash
   mamba activate test
   ```
4. Deactivate the `test` environment:
   ```bash
   mamba deactivate
   ```
5. Delete the `test` environment:
   ```bash
   mamba env remove -n test
   ```

</details>

If this all worked out, you are already set to start using Python.

## Step 3: Clone this repository to your local computer

You will be working with quite a few repositories during your studies - so organize them well.
Never use a folder that is synced with a cloud service (e.g. OneDrive, Dropbox, Google Drive) for your development work.
A possible location could be `~/Repos` (create it if it does not exist yet) and keep all your active repos there.
Or find a location that works for you - there are many ways to organize your work.
To clone the repo, open a terminal, navigate to the folder where you want to keep your repos and run the following command:

```bash
git clone git@github.com:juliankraft/acls_prep_class.git
```

## Step 4: Work through the Example Project

### Environment setup

This environment will bring you pretty far in your first term.
You can use it to solve your early assignments and to get started with your first projects.
If you need to add something or create a new environment, conda will help you with that too.


<details>
<summary>Click to reveal the commands (try it yourself first!)</summary>
Run this in your repo root (the folder you cloned the repository to) to create the environment:

```bash
conda env create -f environment.yml
```

and activate it using:

```bash
conda activate acls
```
</details>

### Running a Python script

Your environment is ready and activated - run the `example_script.py` file:

<details>
<summary>Click to reveal the commands (try it yourself first!)</summary>

```bash
python example_script.py
```
</details>

### Jupyter Notebook

Open the Jupyter Notebook in your IDE and try to figure out how this works.
In VS Code, you might have to install the Jupyter extension first.
Select the `acls` environment as the kernel in the top right corner of the notebook to run it.

## Step 5: Create your own GitHub repository

- Use this [guide](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository) to create your own GitHub repository.
- Use this [guide](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository?platform=windows&tool=webui) to clone your new repository to your local computer (use the SSH key option).
- Create a new Python script in your repository that does something.
- Run the script to make sure it works.
- Commit and push your changes to GitHub using your IDE or terminal - figure this one out yourself.