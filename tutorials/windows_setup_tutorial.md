# Instructions for setting up your Windows computer for the ACLS master program

These are instructions to get your Windows PC up and running for the ACLS master program.
Please follow the steps below carefully.
Do not hesitate to engage us and ask questions if you have any issues.

## Step 1: Install WSL (Windows Subsystem for Linux)

Since programming is a pain in the ass on Windows, our recommendation is to install WSL (Windows Subsystem for Linux) and use Ubuntu as your operating system.
This will allow you to run Linux commands and software on your Windows machine.
It is scary right now, but it is worth it in the long run.

To install WSL, follow the instructions on the [Microsoft website](https://learn.microsoft.com/en-us/windows/wsl/setup/environment).

Once it's installed (and you've rebooted if prompted), you need a terminal running inside your new Ubuntu system - this is where you'll run every command in the rest of these tutorials. Open the Start menu, type "Ubuntu" and launch the app that shows up (the first time you do this it will ask you to create a username and password for your Linux user - this is separate from your Windows login). From now on, whenever these tutorials say "open a terminal", this is the terminal to use.

## Step 2: Install Mamba

Mamba is a package manager for Python that makes it easy to install and manage Python packages and environments.
You might have heard of Conda before or you are going to hear about it in the future.
Mamba is basically the same thing as Conda, but it is faster and more efficient.

We'll install a slimmed-down version of it called Micromamba. First, make sure `curl` is available:
```bash
sudo apt update && sudo apt install -y curl
```

Then open your WSL (Ubuntu) terminal and run the following command:
```bash
"${SHELL}" <(curl -L micro.mamba.pm/install.sh)
```
When prompted, accept the default install location, use `~/mamba` as the root prefix, and let it initialize itself for your shell (it will auto-detect `bash`, WSL's default shell).

After the installation is complete, either restart your terminal or run this to load it into your current session:
```bash
source ~/.bashrc
```

This installs a command called `micromamba` (not `mamba`). To be able to just use `conda` as it will show in most tutorials, you can run this command in your terminal:
```bash
echo 'alias conda="micromamba"' >> ~/.bashrc
```

And to finalise this, we need to reload these configurations by running this command in your terminal:
```bash
source ~/.bashrc
```

## Step 3: Install R and RStudio

R is a programming language and software environment for statistical computing and graphics - you will be using it for your D modules.
RStudio is an integrated development environment (IDE) for R - it's the easiest way to write and run R code.

Download and install R from the [R-project website](https://cran.r-project.org/bin/windows/base/).

Download and install RStudio from the [RStudio website](https://docs.posit.co/ide/user/#rstudio-ide-oss-downloads)

Launch RStudio and you will be prompted to select the R version to use.
Select the R version you just installed.
You are all set for your D modules.

## Step 4: Set up GitHub and SSH

Open [GitHub, SSH and IDE tutorial](github_ssh_ide.md) and follow the instructions to set up your GitHub account and SSH key.
And decide on your IDE (Visual Studio Code or PyCharm)