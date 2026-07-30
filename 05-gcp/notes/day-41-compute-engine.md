# Day 41 – Google Cloud: Compute Engine

## Objective

Understand what Compute Engine is, how Virtual Machines (VMs) work in Google Cloud, and learn the key components involved in creating and managing VM instances.

---

# What is Compute Engine?

Compute Engine is Google's Infrastructure as a Service (IaaS) offering that allows users to create and manage Virtual Machines (VMs) on Google Cloud.

Instead of purchasing physical servers, users can create virtual servers in minutes and pay only for the resources they use.

Compute Engine provides complete control over the operating system, installed software, networking, storage, and security.

---

# Why Compute Engine?

Organizations use Compute Engine because it provides:

- On-demand Virtual Machines
- High performance
- Scalability
- Flexible machine configurations
- Pay-as-you-go pricing
- Integration with other Google Cloud services

It is suitable for hosting web applications, databases, development environments, and enterprise workloads.

---

# What is a Virtual Machine (VM)?

A Virtual Machine is a software-based computer that runs on physical hardware.

Each VM has its own:

- Operating System
- CPU
- Memory (RAM)
- Storage
- Network Interface

A VM behaves like a physical computer but shares hardware resources with other virtual machines.

---

# Components of a Compute Engine Instance

Every Compute Engine instance consists of:

- Machine Type
- Boot Disk
- Operating System
- Network Interface
- Firewall Rules
- Service Account
- Metadata

These components determine how the VM operates.

---

# Creating a VM

The general steps are:

1. Create or select a Project.
2. Choose a Region and Zone.
3. Select a Machine Type.
4. Choose an Operating System image.
5. Configure the Boot Disk.
6. Configure Networking.
7. Set Firewall Rules.
8. Create the Instance.

Once created, the VM becomes available within a few minutes.

---

# Common Operating Systems

Google Cloud provides many operating system images.

Examples include:

- Ubuntu
- Debian
- CentOS
- Rocky Linux
- Windows Server
- Red Hat Enterprise Linux

Custom images can also be used.

---

# VM Lifecycle

A Virtual Machine can exist in different states.

```text
Create
   │
Running
   │
Stopped
   │
Restarted
   │
Deleted
```

Administrators can start, stop, restart, suspend, or delete instances whenever required.

---

# Common Use Cases

Compute Engine is commonly used for:

- Hosting web applications
- Running databases
- Development and testing
- CI/CD build servers
- Container hosts
- Data processing
- Enterprise applications

---

# Advantages of Compute Engine

- High flexibility
- Complete operating system control
- Fast deployment
- Automatic scaling support
- Integration with Cloud Storage, VPC, IAM, and Load Balancing

---

# Best Practices

- Choose the correct machine type.
- Use private IP addresses whenever possible.
- Enable automatic backups.
- Apply least privilege using IAM.
- Regularly update the operating system.
- Stop unused Virtual Machines to reduce costs.

---

# Real-World Example

A software company hosts its customer-facing website on multiple Ubuntu Virtual Machines using Compute Engine.

These VMs are placed behind a Google Cloud Load Balancer. If traffic increases, additional VM instances can be added without changing the application architecture.

---

# What I Learned

- Compute Engine provides Virtual Machines in Google Cloud.
- Virtual Machines offer complete control over the operating system and software.
- Every VM includes compute, storage, networking, and security components.
- Compute Engine is Google's Infrastructure as a Service (IaaS) platform.
- It is widely used for hosting applications, development environments, and enterprise workloads.
