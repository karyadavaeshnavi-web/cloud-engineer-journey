# Day 34 – Google Cloud: IAM Policies

## Objective

Understand how IAM Policies connect identities with roles to control access to Google Cloud resources.

---

# What is an IAM Policy?

An IAM Policy is a document that specifies who can access a resource and what actions they are allowed to perform.

Every Google Cloud resource can have an IAM Policy.

---

# Components of an IAM Policy

An IAM Policy consists of:

- Members
- Roles
- Bindings

---

# Members

Members are identities that receive access.

Examples:

- User
- Group
- Service Account
- Domain

Example:

```text
developer@example.com
```

---

# Roles

Roles define the permissions granted to a member.

Examples:

- Viewer
- Editor
- Compute Admin
- Storage Admin

---

# Bindings

A Binding connects a Member to a Role.

Example:

```text
Member:
developer@example.com

Role:
Compute Admin
```

---

# Policy Structure

```text
IAM Policy
│
├── Member
│
├── Role
│
└── Permissions
```

---

# Resource Hierarchy

Policies can be applied at different levels.

```text
Organization
    │
    ├── Folder
    │
    ├── Project
    │
    └── Resource
```

Permissions inherited from higher levels are available to lower levels unless restricted.

---

# Policy Inheritance

Example:

If a user has the Viewer role at the Project level, they can view resources inside that project unless more restrictive controls apply.

---

# Best Practices

- Grant access using Groups whenever possible.
- Review IAM Policies regularly.
- Remove unused members.
- Follow the Principle of Least Privilege.
- Audit IAM permissions frequently.

---

# Real-World Example

A company grants the **Compute Admin** role to its DevOps team at the project level. Every VM within that project inherits the permissions, eliminating the need to configure each resource individually.

---

# What I Learned

- IAM Policies define access to Google Cloud resources.
- Policies contain Members, Roles, and Bindings.
- Policies can be applied at Organization, Folder, Project, or Resource levels.
- Permissions are inherited through the resource hierarchy.
- Well-designed IAM Policies improve security and simplify access management.
