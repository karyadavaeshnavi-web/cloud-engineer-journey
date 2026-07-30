# Day 31 – Google Cloud: IAM Users

## Objective

Understand Identity and Access Management (IAM), how users are authenticated, and how access to Google Cloud resources is controlled.

---

# What is IAM?

Identity and Access Management (IAM) is Google's security service that controls who can access cloud resources and what actions they are allowed to perform.

IAM helps organizations securely manage users and permissions.

---

# Why IAM is Important

IAM allows organizations to:

- Secure cloud resources
- Control user permissions
- Follow the Principle of Least Privilege
- Prevent unauthorized access
- Audit user activities

---

# Identity

An Identity represents a person, application, or service that can access Google Cloud.

Examples include:

- Google User Account
- Google Group
- Service Account
- Cloud Identity User

Each identity is authenticated before accessing resources.

---

# IAM Users

An IAM User is typically a Google Account that has been granted access to a Google Cloud Project.

Example:

```text
developer@example.com
```

This user can access only the resources and actions permitted by assigned IAM roles.

---

# Authentication vs Authorization

## Authentication

Authentication answers the question:

**"Who are you?"**

Example:

A user signs in with a Google Account.

---

## Authorization

Authorization answers the question:

**"What are you allowed to do?"**

Example:

A developer can create Virtual Machines but cannot delete projects.

---

# IAM Policy

An IAM Policy defines who has access to which resource.

It contains:

- Members (Users, Groups, Service Accounts)
- Roles
- Permissions

Example:

```text
Member:
developer@example.com

Role:
Compute Viewer
```

---

# Principle of Least Privilege

Users should receive only the permissions necessary to perform their work.

Example:

A developer who only needs to view Virtual Machines should not receive administrator permissions.

This reduces security risks.

---

# Benefits of IAM

- Improved Security
- Controlled Resource Access
- Easier User Management
- Compliance Support
- Activity Auditing

---

# Best Practices

- Grant only required permissions.
- Review user access regularly.
- Remove unused accounts.
- Avoid sharing accounts.
- Use Groups for managing teams.
- Enable Multi-Factor Authentication (MFA).

---

# Real-World Example

A company has separate teams for Developers and Administrators.

Developers receive access to deploy applications, while Administrators manage networking, billing, and security. IAM ensures each team has only the permissions required for its responsibilities.

---

# What I Learned

- IAM manages authentication and authorization in Google Cloud.
- IAM Users are Google Accounts granted access to cloud resources.
- IAM Policies define who can access resources.
- Authentication verifies identity, while authorization determines permissions.
- Following the Principle of Least Privilege improves cloud security.
