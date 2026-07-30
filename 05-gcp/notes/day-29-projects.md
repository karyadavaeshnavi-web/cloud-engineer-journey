# Day 29 – Google Cloud: Projects

## Objective

Learn what a Google Cloud Project is, why it is the fundamental organizational unit in GCP, and how projects help manage resources, permissions, billing, and services.

---

# What is a Google Cloud Project?

A Google Cloud Project is the basic organizational unit in Google Cloud Platform.

Every resource you create in GCP, such as Virtual Machines, Cloud Storage buckets, databases, or Kubernetes clusters, belongs to a project.

Without a project, you cannot create or manage cloud resources.

---

# Why are Projects Important?

Projects help organizations:

- Organize cloud resources
- Separate development, testing, and production environments
- Manage billing
- Control user access
- Enable or disable Google Cloud services
- Monitor resource usage

Projects act as containers for cloud resources.

---

# Components of a Project

Each project contains:

- Project Name
- Project ID
- Project Number

### Project Name

A human-readable name that can be changed.

Example:

```text
DevOps Learning Project
```

---

### Project ID

A globally unique identifier for the project.

Once created, it cannot be changed.

Example:

```text
devops-learning-123
```

---

### Project Number

A unique number automatically assigned by Google.

Example:

```text
987654321012
```

This is mainly used internally by Google Cloud services.

---

# Project Hierarchy

Google Cloud resources are organized in the following hierarchy:

```text
Organization
    │
    ├── Folder
    │      │
    │      ├── Project
    │      │      │
    │      │      ├── Compute Engine
    │      │      ├── Cloud Storage
    │      │      ├── VPC
    │      │      └── IAM
```

Not every account has an Organization or Folder, but every resource belongs to a Project.

---

# Resources Inside a Project

Examples of resources that belong to a project:

- Virtual Machines
- VPC Networks
- Cloud Storage Buckets
- Cloud SQL Databases
- Kubernetes Clusters
- Cloud Functions
- IAM Policies

All these resources are managed within the project.

---

# Why Use Multiple Projects?

Organizations typically create separate projects for different environments.

Example:

```text
Development Project

Testing Project

Production Project
```

Benefits include:

- Better security
- Easier billing
- Resource isolation
- Independent IAM permissions
- Reduced risk of accidental changes

---

# Enabling APIs

Google Cloud services are accessed through APIs.

Before using a service, its API must be enabled within the project.

Examples:

- Compute Engine API
- Cloud Storage API
- Kubernetes Engine API
- Cloud SQL API

Only enabled APIs can be used within a project.

---

# Best Practices

- Use separate projects for Development, Testing, and Production.
- Give projects meaningful names.
- Follow a consistent naming convention.
- Grant users only the permissions they need.
- Regularly review enabled APIs and resource usage.
- Delete unused projects to avoid unnecessary costs.

---

# Real-World Example

A software company develops an online shopping application.

They create three separate projects:

```text
ecommerce-dev

ecommerce-test

ecommerce-prod
```

Each project has its own resources, IAM permissions, and billing, ensuring that development activities do not affect the production environment.

---

# What I Learned

- A Google Cloud Project is the primary container for cloud resources.
- Every GCP resource belongs to a project.
- Projects help organize resources, billing, and permissions.
- Each project has a unique Project ID and Project Number.
- Using separate projects for different environments improves security and management.
- Google Cloud services must be enabled through APIs before they can be used within a project.
