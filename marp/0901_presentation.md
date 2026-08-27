---
marp: true
theme: zhaw
paginate: true
footer: 'pece@zhaw.ch, krft@zhaw.ch'
lang: de
size: 16:9
---

<!-- _class: title -->
<!-- _paginate: false -->
<!-- _footer: '' -->

# Prep Class ACLS
Part I - setting up your development environment
01 September 2026

Jūlija Pečerska, Julian Kraft

---

# Jūlija
## Education/Research

- **'08 – '12:** BSc, CS @ LU (software engineering)
- **'12 – '14:** MSc, CS @ ETHZ (general CS)
- **'14 – '19:** PhD, Computational Evolution w/ Tanja Stadler @ ETHZ
- **'20 – ...:** Postdoc/Researcher, Computational genomics w/ Maria Anisimova & Manuel Gil @ ZHAW

---

# Jūlija
## Experience

- **'10 – '12:** Software engineer @ Accenture
- **'12 – '14:** Research assistant @ ETHZ
- **'16 – '24:** TA/instructor @ Taming the BEAST course
- **'22 – ...:** TA/instructor @ CoME summer school
- **'23 – ...:** Lead developer of the `phyne` library in Rust

---

# Julian
- BSc as Environmental Engineer at ZHAW in 2024
- currently pursuing MSc Applied Computational Life Sciences at ZHAW ICLS
- working as Research Assistant at ZHAW ICLS in the field of Computer Vision and Machine Learning

---

# Roadmap for today
- insalling some things
- beeing confused a little
- installing more things
- beeing confused more
- installing even more things
- beeing okay with beeing confused

---

# How we do things today

- short presentations about the tools
- a terminal crash course
- hands-on using tutorials and links
- we are here to help
- you find all materials under: <br>
  [https://github.com/juliankraft/acls_prep_class](https://github.com/juliankraft/acls_prep_class)

---

# WSL (Windows Subsystem for Linux)

- a real Linux system running inside your Windows machine
- **why:** almost all programming/data-science tools are built for Linux (or macOS) first - Windows is often the odd one out
- gives you a proper terminal and all the tools you need
- macOS and Linux users already have this out of the box - lucky you

---

# Homebrew (macOS)

- a **package manager**: installs and updates software from the terminal instead of clicking through installers
- **why:** fast, repeatable, easy to see what's installed - and you simply copy-paste "brew install ..."

---

# Mamba (Python environment manager)

- installs Python itself, plus isolated **environments** for each project
- **why:** different projects need different (and sometimes conflicting) package versions - environments keep them from stepping on each other
- you'll hear "conda" everywhere - mamba does the same job, just faster

---

# R and RStudio

- **R:** a programming language for statistics; **RStudio:** the IDE you write and run it in
- **why:** used throughout the D modules of the program
- a separate toolchain from Python - different job, different tool

---

# GitHub

- a platform for hosting code and collaborating on it, built around **git** (a version control tool that tracks changes to your files)
- **why:** you'll use it to submit assignments, work in teams, and track your own progress - and it's the industry standard
- git = the tool, GitHub = the website/platform built around it

---

# SSH keys

- a pair of cryptographic keys that let you log in securely - without typing a password every time
- **why:** this is how you authenticate with GitHub from your terminal
- the public key goes to GitHub, the private key stays on your machine and is never shared

---

# IDE (Integrated Development Environment)

- a program for writing, running and debugging code - with autocomplete, error highlighting, and more
- **why:** technically you could write code in any texteditor, but an IDE makes you dramatically faster and catches mistakes early
- we recommend VS Code or PyCharm - either is fine, details in the tutorial

---

# Terminal

A little crash course

- a text-based way to talk to your computer: you type commands instead of clicking
- **why:** most of the tools from today (mamba, git, ssh) only exist as command-line tools - this is a core skill, not an optional one
- looks intimidating now, will feel normal within a couple of weeks



