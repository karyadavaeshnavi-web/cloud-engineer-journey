# Day 17 – Remote Repositories & GitHub

## Objective

Understand how Git connects local repositories to remote repositories using GitHub and learn the commands used for synchronizing projects.

---

# What is GitHub?

GitHub is a cloud-based platform that hosts Git repositories.

It allows developers to:

- Store projects online
- Collaborate with teams
- Track project history
- Review code through Pull Requests
- Backup repositories

---

# Local Repository vs Remote Repository

## Local Repository

A repository stored on your own computer.

- Offline
- Personal working copy
- Created using Git

## Remote Repository

A repository stored online (for example, on GitHub).

- Accessible over the internet
- Used for collaboration
- Acts as the central source of truth

---

# Why Do We Need Remote Repositories?

Without a remote repository:

- Code exists only on one computer.
- Hardware failure can result in data loss.
- Collaboration becomes difficult.

With GitHub:

- Projects are backed up.
- Teams can collaborate.
- Multiple developers can contribute safely.

---

# Git Commands

## View Remote Repository

```bash
git remote -v
```

Displays the configured remote repository.

---

## Clone Repository

```bash
git clone <repository-url>
```

Downloads a copy of an existing GitHub repository to your local machine.

---

## Push

```bash
git push
```

Uploads local commits to GitHub.

---

## Pull

```bash
git pull
```

Downloads new commits from the remote repository and merges them into the local repository.

---

## Fetch

```bash
git fetch
```

Downloads changes from the remote repository without modifying the working directory.

---

# Difference Between Pull and Fetch

## git fetch

- Downloads new commits
- Does not update local files
- Allows you to inspect changes first

## git pull

- Downloads new commits
- Updates the local repository immediately
- Equivalent to fetch + merge

---

# What I Learned

- Git works locally.
- GitHub stores repositories remotely.
- Remote repositories enable collaboration and backup.
- git push uploads changes.
- git pull synchronizes local work.
- git fetch safely checks for updates before merging.

---

# Real Cloud Engineer Use Case

Cloud Engineers regularly push:

- Terraform code
- Kubernetes manifests
- Dockerfiles
- Python automation scripts
- GitHub Actions workflows

to GitHub so teams can review and deploy infrastructure safely.