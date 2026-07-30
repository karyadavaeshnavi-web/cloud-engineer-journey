# Day 39 – Google Cloud: Cloud NAT

## Objective

Understand what Cloud NAT (Network Address Translation) is, why it is used, and how it allows private Google Cloud resources to securely access the internet without exposing them to incoming internet traffic.

---

# What is Cloud NAT?

Cloud NAT (Network Address Translation) is a managed Google Cloud service that allows Virtual Machines with only private IP addresses to access the internet.

Unlike assigning public IP addresses to every VM, Cloud NAT provides secure outbound internet connectivity while keeping resources private.

---

# Why Do We Need Cloud NAT?

Many cloud resources need internet access to:

- Download software packages
- Install operating system updates
- Access external APIs
- Retrieve container images
- Connect to cloud services

However, these resources do not need to be directly accessible from the internet.

Cloud NAT solves this problem.

---

# How Cloud NAT Works

When a Virtual Machine with only a private IP sends a request to the internet:

1. The request reaches Cloud NAT.
2. Cloud NAT temporarily translates the private IP into a public IP.
3. The request is sent to the internet.
4. The response returns through Cloud NAT.
5. Cloud NAT forwards the response back to the Virtual Machine.

```text
Private VM
     │
     ▼
 Cloud NAT
     │
     ▼
 Internet
```

---

# Benefits of Cloud NAT

- Secure internet access
- No public IP required on Virtual Machines
- Managed by Google Cloud
- Highly available
- Automatically scales
- Reduces exposure to external attacks

---

# Cloud NAT vs Public IP

| Public IP | Cloud NAT |
|------------|-----------|
| VM is directly reachable from the internet | VM remains private |
| Higher security risk | Better security |
| Public IP on every VM | Shared public IP for outbound traffic |
| Suitable for public services | Suitable for private workloads |

---

# Common Use Cases

Cloud NAT is commonly used for:

- Private Compute Engine instances
- Google Kubernetes Engine (GKE) nodes
- Application servers
- Backend services
- Internal microservices

---

# Best Practices

- Use Cloud NAT for private workloads.
- Avoid assigning public IPs unless necessary.
- Monitor NAT gateway usage.
- Combine Cloud NAT with firewall rules.
- Follow the Principle of Least Privilege.

---

# Real-World Example

A company hosts its application servers in a private subnet.

The servers need internet access to download software updates but should never receive incoming internet traffic.

Cloud NAT enables outbound internet connectivity while keeping the servers private and secure.

---

# What I Learned

- Cloud NAT allows private resources to access the internet.
- Virtual Machines do not require public IP addresses.
- Cloud NAT improves security by limiting internet exposure.
- It is commonly used with Compute Engine and GKE.
- Cloud NAT is a managed and scalable Google Cloud service.
