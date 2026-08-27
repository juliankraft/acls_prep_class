# Instructions for setting up your Mac computer for the ACLS master program

These are instructions to get your Mac up and running for the ACLS master program.
Please follow the steps below carefully.
Do not hesitate to engage us and ask questions if you have any issues.

## Step 1: Install Homebrew

Since you are installing quite a bit of software in the near future, it is a good idea to install a package manager.
A package manager is a tool that helps you install and manage software on your computer.
Homebrew is a package manager for macOS that makes it easy to install and manage software.

To install Homebrew, follow the instructions on the [Homebrew website](https://brew.sh/).

## Step 2: Install Mamba

Mamba is a package manager for Python that makes it easy to install and manage Python packages and environments.
You might have heard of Conda before or you are going to hear about it in the future.
Mamba is basically the same thing as Conda, but it is faster and more efficient.

To install Mamba, open a terminal and run the following command:
```bash
brew install micromamba
```

After the installation is complete you need to initialize Mamba for your shell.
Run this in your terminal:
```bash
mamba shell init --shell zsh --root-prefix ~/mamba
``` 

To be able to just use `conda` as it will show in most tutorials, you can run this command in your terminal:
```bash
echo 'alias conda="mamba"' >> ~/.zshrc
```

And to finalise this, we need to reload these configurations by running this command in your terminal:
```bash
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

## Step 4: Set up GitHub and SSH

Open [GitHub and SSH tutorial](github_and_ssh.md) and follow the instructions to set up your GitHub account and SSH key.