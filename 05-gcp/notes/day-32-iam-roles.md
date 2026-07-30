# Day 32 – Google Cloud: IAM Roles

## Objective

Learn what IAM Roles are, how they control permissions in Google Cloud, and understand the different types of IAM roles.

---

# What are IAM Roles?

An IAM Role is a collection of permissions that determines what actions a user, group, or service account can perform on Google Cloud resources.

Instead of assigning permissions individually, Google groups them into roles.

---

# Why IAM Roles?

IAM Roles help:

- Control access to resources
- Simplify permission management
- Improve security
- Implement the Principle of Least Privilege

---

# Permissions

Permissions define specific actions that can be performed on resources.

Examples:

- Create a Virtual Machine
- Delete a Storage Bucket
- View Billing Information
- Start or Stop an Instance

A role contains multiple permissions.

---

# Types of IAM Roles

## Basic Roles

Available in every project.

- Owner
- Editor
- Viewer

### Owner

Has full control over the project, including billing and IAM.

### Editor

Can create and modify most resources but cannot manage IAM permissions.

### Viewer

Can view resources but cannot make changes.

---

## Predefined Roles

Created and managed by Google.

Examples:

- Compute Admin
- Storage Admin
- Network Admin
- Kubernetes Engine Admin

These roles provide permissions for specific services.

---

## Custom Roles

Organizations can create their own roles by selecting only the required permissions.

Useful when predefined roles provide too many permissions.

---

# Role Assignment

Roles are assigned to:

- Users
- Groups
- Service Accounts

Example:

```text
User:
developer@example.com

Role:
Compute Admin
```

---

# Best Practices

- Use predefined roles whenever possible.
- Assign the minimum permissions required.
- Avoid giving Owner access unless necessary.
- Regularly review assigned roles.

---

# Real-World Example

A Cloud Administrator assigns:

- Developers → Compute Admin
- Security Team → Security Admin
- Finance Team → Billing Viewer

Each team receives only the permissions required for its responsibilities.

---

# What I Learned

- IAM Roles are collections of permissions.
- Google provides Basic, Predefined, and Custom Roles.
- Roles simplify permission management.
- Following the Principle of Least Privilege improves cloud security.
