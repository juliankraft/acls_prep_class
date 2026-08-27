# Setting up GitHub and SSH for authentication

## Step 1: Create a GitHub account and link it to your student account

GitHub is a platform for hosting and collaborating on software projects.
The tutorials you are currently following are hosted on GitHub and you will be using it quite a bit in the future.
Since you are now a student, you will even get free access to some paid features on GitHub.
To get access to these features follow the instructions (sorry, they are in German) on [zhaw.ch](https://tat.zhaw.ch/github-map/edu.html)

## Step 2: Set up an SSH key and link it to your GitHub account

An SSH key is a way to authenticate yourself when logging into a remote server without having to enter your password every time - it is convenient and secure.
Very basically it works like this: you generate a key pair on your computer, consisting of a public and a private key.
The public key is then uploaded to the server you want to log into (in this case GitHub) and the private key stays on your computer.
When you try to log into the server, the server will check if your private key matches the public key you uploaded and if it does, you are logged in without having to enter your password.

To create an SSH key pair, open a terminal and run the following command (if your key ends up named `your_email@example.com`, I am going to cry - so replace it with your actual email address):

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```
Leave all the options at their defaults by pressing Enter when it asks for a passphrase (you can also set a passphrase if you want, but it is not necessary).

Now you will have two files in your `~/.ssh` directory:
- `id_ed25519` (your private key - never share this with anyone!)
- `id_ed25519.pub` (your public key).

To copy the public key, run the following command:

```bash
cat ~/.ssh/id_ed25519.pub
```
It will show in your terminal something like this:

```bash
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAA
```
Copy the whole line and go to your [GitHub account settings](https://github.com/settings).
In the left sidebar, click on "SSH and GPG keys" and then click on "New SSH key".
Give your key a title (e.g. "My Laptop") and paste the public key you just copied into the "Key" field.
Click on "Add SSH key" and you are done! You can now use SSH to log into GitHub without having to enter your password!