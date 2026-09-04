# Instructions on how to get started using Python for the ACLS master program

These are instructions to get started using Python in the ACLS master program.
Please follow the steps below carefully.
Do not hesitate to engage us and ask questions if you have any issues.

## Step 1: Create a Python environment

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
   conda create -n test
   ```
2. List all environments:
   ```bash
   conda env list
   ```
3. Activate the `test` environment:
   ```bash
   conda activate test
   ```
4. Deactivate the `test` environment:
   ```bash
   conda deactivate
   ```
5. Delete the `test` environment:
   ```bash
   conda env remove -n test
   ```

</details>

If this all worked out, you are already set to start using Python.

## Step 2: Clone this repository to your local computer

You will be working with quite a few repositories during your studies - so organize them well.
Never use a folder that is synced with a cloud service (e.g. OneDrive, Dropbox, Google Drive) for your development work.
A possible location could be `~/Repositories/` (create it if it does not exist yet) and keep all your active repos there.
Or find a location that works for you - there are many ways to organize your work.
To clone the repo, open a terminal, navigate to the folder where you want to keep your repos and run the following command:

```bash
git clone git@github.com:juliankraft/acls_prep_class.git
```

## Step 3: Environment setup

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

## Step 4: Connecting your IDE with Python

**Important:** You need to understand the difference between opening a file and opening a project - so we send this ahead of any other instructions.
If you open a file - you will have limited access to settings and to configuring your interpreter.
If you open a project - by opening a folder - you will have access to all settings and can configure your interpreter for the project.

### Install your IDE

This part depends on your OS and choice of IDE. Do the section corresponding to your setup.

If you haven't already done so, please install your IDE (Integrated Development Environment) of choice.
[code.visualstudio.com](https://code.visualstudio.com/) or [jetbrains.com/pycharm](https://www.jetbrains.com/pycharm/)

### PyCharm
Apply for the free student license for the professional edition of PyCharm at [jetbrains.com/academy/student-pack/](https://www.jetbrains.com/academy/student-pack/).

#### OSX:
You are lucky, this should not be a problem - just select conda as your interpreter in your IDE.
Should you need more instructions check out [jetbrains.com](https://www.jetbrains.com/help/pycharm/conda-support-creating-conda-virtual-environment.html#conda-requirements)

#### Windows:
This will be a bit more involved, since you need to configure your interpreter within WSL.
Give it a go using the instructions on [jetbrains.com](https://www.jetbrains.com/help/pycharm/using-wsl-as-a-remote-interpreter.html#configure-wsl)

### VS Code

#### OSX:
You should be able to select your Python interpreter in your IDE and you should be good to go.
For additional instructions check out [code.visualstudio.com](https://code.visualstudio.com/docs/python/environments)
Install all the official Python and Jupyter extensions for VS Code.

#### Windows:
Connect your VS Code to WSL. You will find instructions on this on [code.visualstudio.com](https://code.visualstudio.com/docs/remote/wsl).

Once connected:
- Open your project folder in the WSL window (e.g. run `code .` from a WSL terminal inside the cloned repo).
- Install the Python and Jupyter extensions again inside the WSL window if prompted - extensions that run remotely need to be installed separately for WSL, even if you already installed them locally.
- Select the `acls` conda environment as your Python interpreter (`Ctrl+Shift+P` -> "Python: Select Interpreter").


## Step 5: Running Code

## Running a Python script

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

## Step 7: Create your own GitHub repository

- Use this [guide](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository) to create your own GitHub repository.
- Use this [guide](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository?platform=windows&tool=webui) to clone your new repository to your local computer (use the SSH key option).
- Create a new Python script in your repository that does something.
- Run the script to make sure it works.
- Commit and push your changes to GitHub using your IDE or terminal - figure this one out yourself.

# Stuff you can do to get even more ready:

- Set up Cisco VPN connection: [ServiceDesk - VPN](https://servicedesk.zhaw.ch/tas/public/ssp/content/detail/service?unid=a07ed1318fe646008b9bba5df2f7b15d)
- sign up for a hpc account: [HPC-Wiki](https://docs.hpc.zhaw.ch/getting-started/)
- if you care for it - sign in to office 365 with your student account and get it for free
- install the ZHAW LSFM app on Google Play or Apple App Store to learn what's for lunch
- apply for the student discount on Spotify: [Spotify Student Discount](https://www.spotify.com/ch-de/student/)
- check if you pay for other subscription where you can get a student discount - hopefully you will find some more
