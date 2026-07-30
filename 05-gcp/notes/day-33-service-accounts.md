# Day 33 – Google Cloud: Service Accounts

## Objective

Understand what Service Accounts are, how they differ from user accounts, and how they enable applications and services to securely access Google Cloud resources.

---

# What is a Service Account?

A Service Account is a special Google account used by applications or virtual machines instead of human users.

It allows workloads to authenticate securely with Google Cloud services.

---

# Why Service Accounts?

Applications often need to:

- Access Cloud Storage
- Connect to databases
- Read logs
- Deploy resources

Instead of using a user's credentials, they use a Service Account.

---

# User Account vs Service Account

| User Account | Service Account |
|--------------|-----------------|
| Used by people | Used by applications |
| Requires user login | Authenticates automatically |
| Human identity | Machine identity |

---

# Service Account Email

Every Service Account has a unique email.

Example:

```text
web-app@project-id.iam.gserviceaccount.com
```

---

# How Service Accounts Work

1. Create a Service Account.
2. Assign IAM Roles.
3. Attach it to a VM, Cloud Run service, or other resource.
4. The application uses those permissions automatically.

---

# Common Use Cases

- Compute Engine
- Google Kubernetes Engine
- Cloud Run
- Cloud Functions
- CI/CD Pipelines
- Terraform Automation

---

# Best Practices

- Grant only required roles.
- Do not share Service Accounts.
- Rotate keys regularly if using keys.
- Prefer Workload Identity over downloaded keys when possible.
- Monitor Service Account usage.

---

# Real-World Example

A web application stores uploaded files in Cloud Storage.

Instead of storing a developer's credentials, the application uses a Service Account with the **Storage Object Admin** role.

---

# What I Learned

- Service Accounts represent applications, not users.
- They securely access Google Cloud resources.
- IAM Roles determine what a Service Account can do.
- Service Accounts are widely used in automation and DevOps.
