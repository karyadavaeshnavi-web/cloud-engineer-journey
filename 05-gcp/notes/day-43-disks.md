# Day 43 – Google Cloud: Disks

## Objective

Understand the different types of storage disks available in Google Compute Engine, how they are attached to Virtual Machines, and how to choose the appropriate disk for different workloads.

---

# What is a Disk?

A Disk is the storage device attached to a Virtual Machine.

It stores:

- Operating System
- Applications
- User Data
- Configuration Files
- Logs

Every Compute Engine instance requires at least one Boot Disk.

---

# Types of Disks

Google Cloud provides several types of Persistent Disks and Local SSDs.

---

## Standard Persistent Disk (pd-standard)

Uses Hard Disk Drive (HDD) technology.

Best suited for:

- File storage
- Backup
- Low-cost applications

Advantages:

- Lower cost
- Large storage capacity

---

## Balanced Persistent Disk (pd-balanced)

Provides a balance between performance and cost.

Suitable for:

- Web applications
- General-purpose workloads
- Development servers

---

## SSD Persistent Disk (pd-ssd)

Uses Solid State Drive (SSD) technology.

Best suited for:

- Databases
- High-performance applications
- Analytics workloads

Advantages:

- Low latency
- High Input/Output Operations Per Second (IOPS)

---

## Extreme Persistent Disk (pd-extreme)

Designed for applications requiring extremely high performance.

Common uses:

- Enterprise databases
- Financial systems
- Large transactional workloads

---

## Local SSD

Local SSD is physically attached to the host machine.

Advantages:

- Very high performance
- Extremely low latency

Limitations:

- Data is lost if the Virtual Machine is stopped, deleted, or fails.

Suitable for:

- Temporary processing
- Caching
- High-speed analytics

---

# Boot Disk

The Boot Disk contains the operating system required to start a Virtual Machine.

Example:

```text
Ubuntu 24.04 LTS

100 GB SSD
```

Without a boot disk, a VM cannot start.

---

# Additional Persistent Disks

Extra disks can be attached for:

- Databases
- File storage
- Application data
- Backups

These disks can often be detached and attached to another Virtual Machine when needed.

---

# Choosing the Right Disk

Consider:

- Performance requirements
- Budget
- Storage capacity
- Data durability
- Application workload

---

# Best Practices

- Use SSD disks for databases.
- Use Standard Persistent Disks for backups.
- Regularly create snapshots of important disks.
- Monitor storage utilization.
- Delete unused disks to reduce costs.

---

# Real-World Example

An e-commerce company hosts its application on Compute Engine.

- The operating system is installed on an SSD Boot Disk.
- Customer product images are stored on a Balanced Persistent Disk.
- Order records are stored on a high-performance SSD Persistent Disk to ensure fast database access.

This setup balances performance, reliability, and cost.

---

# What I Learned

- Every Compute Engine instance requires a Boot Disk.
- Google Cloud provides Standard, Balanced, SSD, Extreme Persistent Disks, and Local SSDs.
- Different disk types are designed for different workloads.
- SSDs offer higher performance, while Standard Disks provide lower-cost storage.
- Choosing the right disk type improves application performance and cost efficiency.
