# Day 35 – Google Cloud: Virtual Private Cloud (VPC)

## Objective

Understand what a Virtual Private Cloud (VPC) is, why it is required, how it enables secure communication between cloud resources, and how networking works within Google Cloud.

---

# What is a VPC?

A Virtual Private Cloud (VPC) is a private virtual network within Google Cloud where you can deploy and manage cloud resources securely.

It allows resources such as Virtual Machines, Kubernetes clusters, databases, and load balancers to communicate with each other while remaining isolated from other users.

Think of a VPC as your own private network inside Google's global infrastructure.

---

# Why Do We Need a VPC?

Without a VPC:

- Resources would communicate over the public internet.
- There would be limited network isolation.
- Security would be harder to manage.

A VPC provides:

- Private communication
- Network isolation
- Traffic control
- Secure resource management

---

# Characteristics of a VPC

A Google Cloud VPC is:

- Global
- Software-defined
- Highly available
- Scalable
- Private

Unlike many cloud providers, a single VPC can span multiple regions.

---

# Components of a VPC

A VPC contains:

- Subnets
- Routes
- Firewall Rules
- IP Address Ranges

These components work together to manage communication between cloud resources.

---

# IP Address Range

Every VPC uses a CIDR block to define the range of available IP addresses.

Example:

```text
10.0.0.0/16
```

This network can be divided into smaller subnetworks.

---

# Default VPC

When a new Google Cloud project is created, Google automatically creates a Default VPC.

It includes:

- Preconfigured subnets
- Default firewall rules
- Automatic routing

Although useful for learning, production environments usually create custom VPCs for better control.

---

# Custom VPC

A Custom VPC allows complete control over:

- IP ranges
- Subnets
- Firewall rules
- Routing

Organizations typically use custom VPCs to meet security and networking requirements.

---

# Communication Inside a VPC

Resources within the same VPC can communicate using their internal IP addresses.

Example:

```text
VM 1
10.0.1.5

↓

VM 2
10.0.2.8
```

Traffic remains within Google's private network.

---

# Advantages of VPC

- Secure communication
- Private networking
- High scalability
- Better network management
- Integration with Google Cloud services
- Global connectivity

---

# Best Practices

- Create custom VPCs for production workloads.
- Plan IP address ranges before deployment.
- Separate environments using different VPCs.
- Use firewall rules to restrict unnecessary traffic.
- Monitor network traffic regularly.

---

# Real-World Example

An organization hosts a web application in Google Cloud.

The web server, application server, and database are deployed inside the same VPC.

The web server communicates with the application server, and the application server communicates with the database using private IP addresses. External users can access only the web server, while the database remains protected inside the private network.

---

# What I Learned

- A VPC is a private virtual network in Google Cloud.
- It provides secure communication between cloud resources.
- A VPC contains subnets, routes, firewall rules, and IP ranges.
- Google provides both Default and Custom VPCs.
- Production environments generally use Custom VPCs for greater control.
- 
