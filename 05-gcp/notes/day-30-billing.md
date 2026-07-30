# Day 30 – Google Cloud: Billing

## Objective

Understand how Google Cloud Billing works, including billing accounts, payment methods, budgets, alerts, quotas, and cost management best practices.

---

# What is Google Cloud Billing?

Google Cloud Billing is the service used to pay for Google Cloud resources.

Every project that uses paid Google Cloud services must be linked to a Billing Account.

Billing helps organizations monitor expenses, control costs, and manage cloud spending efficiently.

---

# Billing Account

A Billing Account stores:

- Payment information
- Payment method
- Transaction history
- Cost reports
- Linked projects

A single Billing Account can be linked to multiple Google Cloud Projects.

---

# Billing Account Structure

```text
Billing Account
        │
        ├── Project A
        ├── Project B
        └── Project C
```

All project charges are billed to the linked Billing Account.

---

# Payment Methods

Google Cloud supports various payment methods such as:

- Credit Card
- Debit Card
- Net Banking (region dependent)
- Bank Transfer (for eligible customers)

The available methods depend on your country and account type.

---

# Free Tier

Google Cloud provides:

- Always Free resources
- Free Trial Credits (for new users)
- Free usage limits on selected services

Examples include:

- Small Compute Engine instances (eligible regions)
- Cloud Storage limits
- Cloud Functions usage limits

Always check the latest free tier limits before deploying resources.

---

# Budgets

A Budget helps you monitor cloud spending.

Example:

```text
Monthly Budget = ₹8,000
```

Google Cloud tracks your spending against this amount.

Budgets do not stop resources automatically—they only help you monitor costs.

---

# Billing Alerts

Billing Alerts notify you when spending reaches a specified percentage of your budget.

Example:

- 50%
- 75%
- 90%
- 100%

Alerts are sent through email or Cloud Monitoring notifications.

---

# Cost Management

Google Cloud provides tools to manage expenses:

- Billing Reports
- Cost Breakdown
- Budgets
- Alerts
- Cost Analysis

These tools help identify expensive resources and optimize spending.

---

# Quotas

A Quota limits how many cloud resources can be created.

Examples:

- Number of Virtual Machines
- CPU Limits
- API Requests
- Storage Capacity

Quotas help prevent accidental overuse of resources.

---

# Best Practices

- Create budgets for every project.
- Configure billing alerts.
- Delete unused resources.
- Shut down idle Virtual Machines.
- Monitor monthly billing reports.
- Use the Free Tier whenever possible during learning.

---

# Real-World Example

A startup creates a monthly cloud budget of ₹15,000.

Billing alerts are configured at 50%, 75%, and 100%. If usage increases unexpectedly, the team receives notifications and investigates before costs become excessive.

---

# What I Learned

- Every paid GCP project must be linked to a Billing Account.
- One Billing Account can manage multiple projects.
- Budgets help monitor spending.
- Billing alerts notify users when costs reach predefined limits.
- Quotas prevent excessive resource usage.
- Cost monitoring is essential for efficient cloud management.
