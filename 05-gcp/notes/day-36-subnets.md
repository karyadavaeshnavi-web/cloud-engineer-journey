# Day 36 – Google Cloud: Subnets

## Objective

Understand what Subnets are, why they are used within a VPC, how CIDR ranges define subnet size, and how subnetworks improve organization and security.

---

# What is a Subnet?

A Subnet (Subnetwork) is a smaller network created from a larger VPC network.

Instead of placing every resource in one large network, a VPC is divided into multiple subnets to improve organization, scalability, and security.

---

# Why are Subnets Needed?

Subnets help:

- Organize resources
- Reduce network congestion
- Improve security
- Simplify management
- Separate workloads

Different applications can be placed in different subnetworks.

---

# Example

Suppose a VPC has the network:

```text
10.0.0.0/16
```

It can be divided into smaller subnetworks:

```text
10.0.1.0/24

10.0.2.0/24

10.0.3.0/24
```

Each subnet supports a different group of resources.

---

# Regional Subnets

Unlike the VPC, which is global, each subnet belongs to a specific region.

Example:

```text
asia-south1

↓

Subnet A

Subnet B
```

Virtual Machines deployed in that region use the available subnet.

---

# CIDR Notation

Google Cloud uses CIDR notation to define subnet size.

Examples:

```text
10.0.0.0/24

10.0.1.0/24

192.168.1.0/24
```

A smaller prefix means a larger subnet.

---

# Private IP Addresses

Resources inside a subnet receive private IP addresses.

Example:

```text
VM 1

10.0.1.5

VM 2

10.0.1.6
```

These addresses are used for internal communication.

---

# Public vs Private IP

| Public IP | Private IP |
|------------|------------|
| Internet Accessible | Internal Communication |
| Globally Unique | Used within the VPC |
| Assigned when needed | Assigned automatically within the subnet |

---

# Benefits of Subnets

- Better organization
- Improved security
- Easier network management
- Efficient IP address allocation
- Support for regional deployments

---

# Best Practices

- Separate Web, Application, and Database tiers into different subnets.
- Plan IP ranges before deployment.
- Avoid overlapping CIDR ranges.
- Use meaningful subnet names.
- Allocate sufficient IP addresses for future growth.

---

# Real-World Example

An organization deploys a three-tier application.

```text
VPC

│

├── Web Subnet

├── Application Subnet

└── Database Subnet
```

The web servers receive internet traffic, application servers process business logic, and databases remain isolated in a dedicated subnet, improving both security and organization.

---

# What I Learned

- A subnet is a smaller network inside a VPC.
- Subnets organize cloud resources efficiently.
- Every subnet belongs to a specific Google Cloud region.
- CIDR notation defines subnet size.
- Using separate subnets improves scalability, security, and network management.
