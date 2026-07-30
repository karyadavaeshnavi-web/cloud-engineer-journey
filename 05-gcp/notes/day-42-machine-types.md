# Day 42 – Google Cloud: Machine Types

## Objective

Understand what Machine Types are in Google Compute Engine, how CPU and memory resources are allocated, and how to choose the right machine type for different workloads.

---

# What is a Machine Type?

A Machine Type defines the amount of computing resources assigned to a Virtual Machine.

It specifies:

- Number of Virtual CPUs (vCPUs)
- Memory (RAM)

Every Compute Engine instance must have a machine type.

Choosing the correct machine type ensures good performance while controlling costs.

---

# Why are Machine Types Important?

Different applications have different resource requirements.

For example:

- A small website requires minimal CPU and memory.
- A database server needs more memory.
- Machine learning workloads require powerful CPUs or GPUs.

Selecting the correct machine type improves performance and cost efficiency.

---

# Components of a Machine Type

Every machine type includes:

- vCPUs
- Memory (RAM)
- Optional GPUs
- Local SSD support (for certain machine types)

Example:

```text
Machine Type

2 vCPUs

8 GB RAM
```

---

# Machine Type Families

Google Cloud provides several machine families designed for different workloads.

---

## General Purpose

Suitable for most applications.

Examples:

- E2
- N2
- N2D
- N1

Common uses:

- Web servers
- Application servers
- Development environments

---

## Compute Optimized

Designed for CPU-intensive workloads.

Example:

```text
C2
```

Used for:

- Gaming servers
- Scientific computing
- Video processing
- High-performance applications

---

## Memory Optimized

Designed for applications requiring large amounts of RAM.

Examples:

- M1
- M2

Common uses:

- SAP
- In-memory databases
- Analytics platforms

---

## Accelerator Optimized

Provides GPU support.

Examples:

- A2
- G2

Common uses:

- Artificial Intelligence
- Machine Learning
- Deep Learning
- Graphics Rendering

---

# Custom Machine Types

Google Cloud allows users to create custom machine types.

Example:

Instead of selecting:

```text
4 vCPUs

16 GB RAM
```

You can create:

```text
4 vCPUs

10 GB RAM
```

This helps reduce unnecessary costs.

---

# Choosing the Right Machine Type

Consider:

- Application workload
- CPU usage
- Memory usage
- Budget
- Future scalability

Avoid selecting a machine that is significantly larger than required.

---

# Best Practices

- Start with a small machine type.
- Monitor CPU and memory usage.
- Resize instances if needed.
- Use custom machine types when appropriate.
- Stop unused instances to reduce costs.

---

# Real-World Example

A startup launches a small web application.

Initially, they choose an **E2-standard** machine because traffic is low.

As the application grows, they upgrade to an **N2** machine with additional CPU and memory without rebuilding the server.

---

# What I Learned

- Machine Types determine CPU and memory for Virtual Machines.
- Google Cloud provides General Purpose, Compute Optimized, Memory Optimized, and Accelerator Optimized machine families.
- Custom machine types provide flexibility and cost optimization.
- Selecting the correct machine type improves both performance and cost efficiency.
