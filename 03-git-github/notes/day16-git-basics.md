# Day 16 - Git Fundamentals

## Objective

Understand why Git exists, how Version Control works, and the basic Git workflow.

---

# What is Git?

Git is a Distributed Version Control System (DVCS) that tracks changes made to files and source code over time.

It allows developers to:

- Track every change
- Restore previous versions
- Work safely without losing code
- Collaborate with other developers

---

# Why was Git created?

Before Git, developers struggled to manage different versions of projects.

Problems included:

- Accidentally overwriting files
- Losing previous versions
- Difficulty collaborating with teams

Git solves these issues by recording every change as a commit.

---

# What is Version Control?

Version Control is a system that records every version of a project.

Benefits include:

- Restore older versions
- Compare changes
- Track who made changes
- Collaborate with teams

---

# Git vs GitHub

Git:
- Local software installed on your computer.
- Tracks changes locally.

GitHub:
- Cloud platform that hosts Git repositories.
- Enables collaboration and remote backups.

---

# Repository

A repository (repo) is a project folder managed by Git.

It stores:

- Source code
- Documentation
- Commit history
- Project files

---

# Git Workflow

Working Directory

↓

Staging Area

↓

Local Repository

---

# Basic Git Commands

## Check Git Version

```bash
git --version
```

Displays the installed Git version.

---

## Initialize Repository

```bash
git init
```

Creates a new Git repository.

---

## Check Status

```bash
git status
```

Shows modified, staged, and untracked files.

---

## Stage Files

```bash
git add .
```

Stages all modified files.

---

## Commit Changes

```bash
git commit -m "Initial commit"
```

Creates a permanent snapshot of the project.

---

## View Commit History

```bash
git log
```

Displays the repository's commit history.

---

# What I Learned

- Git is a Version Control System.
- Git records project history through commits.
- Git works locally while GitHub works remotely.
- Every commit creates a snapshot of the project.
- Version Control prevents accidental loss of work.

---

# Git is used mainly for:
- Terraform Infrastructure as Code
- Kubernetes YAML files
- Dockerfiles
- CI/CD Pipelines
- Monitoring configurations

Every infrastructure change is committed to Git before deployment.