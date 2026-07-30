# Day 37 – Google Cloud: Routes

## Objective

Understand what Routes are in Google Cloud, how they control network traffic, the different types of routes, and how routing enables communication between cloud resources and external networks.

---

# What is a Route?

A Route is a networking rule that tells Google Cloud where network traffic should be sent.

Whenever a Virtual Machine sends data, Google Cloud checks the routing table to determine the correct destination.

Without routes, resources would not know how to communicate with each other or with external networks.

---

# Why are Routes Important?

Routes help:

- Direct network traffic
- Connect Virtual Machines
- Access the internet
- Connect different subnetworks
- Enable communication with on-premises environments

Every VPC contains a routing table that determines how packets travel through the network.

---

# How Routing Works

When a packet is sent:

1. The source VM sends the packet.
2. Google Cloud checks the routing table.
3. The best matching route is selected.
4. The packet is forwarded to its destination.

Example:

```text
VM
 │
 ▼
Routing Table
 │
 ▼
Destination
```

---

# Route Components

Every route contains:

- Destination Range
- Next Hop
- Priority

---

## Destination Range

Defines where the traffic should go.

Example:

```text
10.0.1.0/24
```

---

## Next Hop

Specifies where the packet should be forwarded.

Examples:

- Default Internet Gateway
- Virtual Machine
- VPN Tunnel
- Load Balancer

---

## Priority

If multiple routes match a destination, Google Cloud selects the route with the highest priority (lowest numerical value).

---

# Types of Routes

## System-Generated Routes

Automatically created when subnets are added.

These routes enable communication between subnetworks within the VPC.

---

## Custom Routes

Created manually by administrators.

Useful for:

- VPN connections
- Hybrid cloud
- Custom networking requirements

---

## Default Route

Every VPC contains a default route.

Example:

```text
0.0.0.0/0
```

This route sends internet-bound traffic through Google's Default Internet Gateway.

---

# Routing Table

Google Cloud maintains a routing table for every VPC.

Example:

| Destination | Next Hop |
|-------------|----------|
| 10.0.1.0/24 | Local Subnet |
| 10.0.2.0/24 | Local Subnet |
| 0.0.0.0/0 | Internet Gateway |

---

# Best Practices

- Remove unnecessary custom routes.
- Use descriptive names.
- Review routing tables regularly.
- Plan network architecture before deployment.
- Monitor routing changes in production.

---

# Real-World Example

A company hosts a web application in Google Cloud.

Internal traffic between web servers and databases follows local subnet routes, while user requests coming from the internet use the default internet route.

Custom routes are also configured to connect the company's on-premises data center through a VPN.

---

# What I Learned

- Routes determine where network traffic is sent.
- Every VPC contains a routing table.
- Google automatically creates system routes.
- Custom routes support advanced networking.
- The default route enables internet connectivity.
