# Day 18 – Branching, Merging & Pull Requests

## Objective

Learn how professional software teams develop new features safely using Git branches, Pull Requests, and merges.

---

# Why Branches Exist

The main branch usually contains stable, production-ready code.

Developers avoid working directly on the main branch because unfinished or faulty code could affect the entire project.

Instead, they create separate branches for new features or bug fixes.

---

# What is a Branch?

A branch is an independent line of development created from another branch (commonly `main`).

It allows developers to work on new features without affecting the stable version of the project.

---

# Why Use Branches?

Branches provide:

- Safe development
- Parallel work by multiple developers
- Easier testing
- Better collaboration
- Protection of the production code

---

# Common Branch Naming

Feature branch

```text
feature/login
```

Bug fix

```text
bugfix/database-error
```

Hotfix

```text
hotfix/security-patch
```

---

# Create a Branch

```bash
git branch feature/readme-update
```

Creates a new branch.

---

# View Branches

```bash
git branch
```

Lists all local branches.

---

# Switch Branches

```bash
git switch feature/readme-update
```

or

```bash
git checkout feature/readme-update
```

Moves to another branch.

---

# Create and Switch

```bash
git switch -c feature/readme-update
```

or

```bash
git checkout -b feature/readme-update
```

Creates and immediately switches to the new branch.

---

# Merge

Return to main.

```bash
git switch main
```

Merge.

```bash
git merge feature/readme-update
```

The changes from the feature branch become part of the main branch.

---

# Pull Requests

A Pull Request (PR) is a request to merge one branch into another after review.

It allows teammates to:

- Review code
- Suggest improvements
- Run automated tests
- Approve changes before merging

---

# Merge Conflicts

Merge conflicts occur when two branches modify the same part of a file and Git cannot automatically determine which version should be kept.

The developer must manually resolve the conflict before completing the merge.

---

# Branch Workflow

main

↓

Create Feature Branch

↓

Develop Feature

↓

Commit Changes

↓

Push Branch

↓

Open Pull Request

↓

Code Review

↓

Merge into main

---

# What I Learned

- Branches isolate development work.
- Pull Requests enable code review.
- Merge combines completed work into another branch.
- Merge conflicts require manual resolution.
- Professional teams rarely develop directly on the main branch.

---

# Real Cloud Engineer Use Case

Cloud Engineers use feature branches when:

- Developing Terraform modules
- Updating Kubernetes manifests
- Creating CI/CD pipelines
- Modifying Dockerfiles
- Improving monitoring scripts

This ensures infrastructure changes are reviewed before deployment.
# Reflection

Today I learned how professional software teams collaborate using Git branches and Pull Requests. I understood why developers avoid working directly on the main branch and how feature branches provide a safe environment for developing and testing changes. I also learned that Pull Requests enable code review before changes are merged into the production branch, reducing the risk of introducing errors.

