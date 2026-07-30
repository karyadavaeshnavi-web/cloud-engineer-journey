# Day 45 – Google Cloud: Startup Scripts

## Objective

Understand what Startup Scripts are, how they automate Virtual Machine configuration, and why they are widely used in cloud automation and DevOps.

---

# What are Startup Scripts?

A Startup Script is a script that automatically runs when a Virtual Machine starts.

Instead of manually configuring a server after creation, administrators can automate software installation, configuration, and system setup.

Startup Scripts are commonly written in Bash for Linux or PowerShell for Windows.

---

# Why Use Startup Scripts?

Without Startup Scripts:

- Every VM must be configured manually.
- Configuration takes more time.
- Human errors become more likely.

Startup Scripts automate repetitive setup tasks and ensure every VM is configured consistently.

---

# How Startup Scripts Work

When a VM starts:

1. The operating system boots.
2. Google Cloud checks for a Startup Script.
3. The script executes automatically.
4. The VM becomes ready for use.

```text
Create VM
     │
     ▼
VM Boots
     │
     ▼
Startup Script Executes
     │
     ▼
Application Ready
```

---

# Common Tasks Performed

Startup Scripts can:

- Install software
- Update packages
- Configure web servers
- Create users
- Set environment variables
- Download application files
- Start services

---

# Example Startup Script

```bash
#!/bin/bash

sudo apt update
sudo apt install -y nginx
sudo systemctl enable nginx
sudo systemctl start nginx
```

This script:

- Updates package information
- Installs Nginx
- Enables the service
- Starts the web server automatically

---

# Benefits

- Automation
- Consistent server configuration
- Faster deployments
- Reduced manual effort
- Better scalability

---

# Common Use Cases

Startup Scripts are widely used for:

- Web server deployment
- CI/CD environments
- Kubernetes nodes
- Development environments
- Automated testing
- Cloud infrastructure provisioning

---

# Best Practices

- Keep scripts simple and modular.
- Test scripts before production deployment.
- Store reusable scripts in version control.
- Avoid hardcoding sensitive information.
- Use logging to troubleshoot startup failures.

---

# Real-World Example

A company launches dozens of Compute Engine instances during periods of high demand.

Each VM runs a Startup Script that installs application dependencies, downloads the latest application version, and starts required services automatically. This allows new servers to become operational within minutes without manual intervention.

---

# What I Learned

- Startup Scripts automate Virtual Machine configuration.
- Scripts run automatically whenever a VM starts.
- They improve consistency, scalability, and deployment speed.
- Startup Scripts are an important DevOps automation technique.
- Bash and PowerShell are commonly used to write Startup Scripts.
