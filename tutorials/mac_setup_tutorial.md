# Instructions for setting up your Mac computer for the ACLS master program

These are instructions to get your Mac up and running for the ACLS master program.
Please follow the steps below carefully.
Do not hesitate to engage us and ask questions if you have any issues.

## Step 1: Install Homebrew

Since you are installing quite a bit of software in the near future, it is a good idea to install a package manager.
A package manager is a tool that helps you install and manage software on your computer.
Homebrew is a package manager for macOS that makes it easy to install and manage software.

To install Homebrew, follow the instructions on the [Homebrew website](https://brew.sh/).

## Step 2: Install Conda

Conda is a package manager for Python that makes it easy to install and manage Python packages and environments.
You might have heard of Conda before or you are going to hear about it in the future.

To install Conda, open a terminal and run the following command:
```bash
brew install miniconda
```

After the installation is complete you need to initialize Conda for your shell.
Run this in your terminal:
```zsh
 conda init "$(basename "${SHELL}")"
```

After the installation is complete, either restart your terminal or run this to load it into your current session:
```zsh
source ~/.zshrc
```

## Step 3: Install R and RStudio

R is a programming language and software environment for statistical computing and graphics - you will be using it for your D modules.
RStudio is an integrated development environment (IDE) for R - it's the easiest way to write and run R code.

To install R, open a terminal and run the following command:
```bash
brew install --cask r
```

To install RStudio, run the following command:
```bash
brew install --cask rstudio
```

Launch RStudio and you will be prompted to select the R version to use.
Select the R version you just installed.
You are all set for your D modules.

## Step 4: Set up GitHub and SSH

Open [GitHub, SSH and IDE tutorial](github_ssh_ide.md) and follow the instructions to set up your GitHub account and SSH key.
And decide on your IDE (Visual Studio Code or PyCharm)