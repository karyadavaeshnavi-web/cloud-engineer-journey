# Day 40 – Google Cloud: Load Balancing

## Objective

Understand how Google Cloud Load Balancing distributes incoming traffic across multiple servers, improving application availability, scalability, and performance.

---

# What is Load Balancing?

Load Balancing is the process of distributing incoming user requests across multiple backend servers.

Instead of sending all traffic to one server, a Load Balancer spreads requests evenly to prevent any single server from becoming overloaded.

---

# Why Do We Need Load Balancing?

Without a Load Balancer:

- One server may become overloaded.
- Performance decreases during peak traffic.
- A server failure can make the application unavailable.

A Load Balancer improves reliability by distributing requests across multiple servers.

---

# How Load Balancing Works

1. A user sends a request.
2. The request reaches the Load Balancer.
3. The Load Balancer selects a healthy backend server.
4. The server processes the request and returns the response.

```text
Users
   │
   ▼
Load Balancer
   │
 ┌─┴───────────┐
 │             │
VM 1         VM 2
 │             │
VM 3         VM 4
```

---

# Benefits of Load Balancing

- High Availability
- Automatic traffic distribution
- Better performance
- Fault tolerance
- Scalability
- Improved user experience

---

# Types of Google Cloud Load Balancers

## External Load Balancer

Distributes traffic from internet users to backend services.

Used for:

- Public websites
- APIs
- Web applications

---

## Internal Load Balancer

Distributes traffic within a private VPC.

Used for:

- Internal applications
- Microservices
- Backend communication

---

# Health Checks

A Health Check continuously verifies whether backend servers are operating correctly.

If a server becomes unhealthy, the Load Balancer automatically stops sending traffic to it until it recovers.

---

# Session Affinity

Session Affinity ensures that requests from the same client are directed to the same backend server when required.

This is useful for applications that maintain user session data.

---

# Best Practices

- Deploy backend servers across multiple zones.
- Configure health checks.
- Use autoscaling with Load Balancers.
- Monitor backend performance.
- Avoid single points of failure.

---

# Real-World Example

An online shopping website receives thousands of users during a festival sale.

A Google Cloud Load Balancer distributes requests across several Compute Engine instances deployed in multiple zones. If one instance fails, traffic is automatically redirected to healthy instances, allowing customers to continue shopping without interruption.

---

# What I Learned

- Load Balancing distributes incoming traffic across multiple servers.
- It improves availability, scalability, and reliability.
- Google Cloud provides Internal and External Load Balancers.
- Health Checks ensure traffic reaches only healthy servers.
- Load Balancing is a key component of highly available cloud architectures.
- 
