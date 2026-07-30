# Day 38 – Google Cloud: Firewall Rules

## Objective

Understand how Firewall Rules control network traffic in Google Cloud, the difference between ingress and egress rules, and how firewall configurations improve cloud security.

---

# What are Firewall Rules?

Firewall Rules control which network traffic is allowed to enter or leave resources within a Virtual Private Cloud (VPC).

They act as security filters by evaluating network traffic against defined rules.

Without firewall rules, cloud resources would be vulnerable to unauthorized access.

---

# Why are Firewall Rules Needed?

Firewall Rules help:

- Protect Virtual Machines
- Restrict unauthorized access
- Allow only required traffic
- Improve network security
- Control communication between resources

---

# How Firewall Rules Work

Whenever network traffic reaches a Virtual Machine, Google Cloud checks the configured firewall rules.

If a rule allows the traffic, it is forwarded.

If no rule allows the traffic, it is denied.

```text
Incoming Request
        │
        ▼
Firewall Rules
        │
 ┌──────┴──────┐
 │             │
Allow       Deny
```

---

# Direction of Traffic

## Ingress

Ingress rules control incoming traffic to resources.

Examples:

- SSH
- HTTP
- HTTPS

---

## Egress

Egress rules control outgoing traffic from resources.

Examples:

- Internet access
- Database connections
- External API requests

---

# Firewall Rule Components

Each firewall rule contains:

- Name
- Direction
- Action
- Source or Destination
- Protocol
- Port
- Priority

---

# Action

A firewall rule performs one of two actions:

### Allow

Permits traffic.

### Deny

Blocks traffic.

---

# Protocols

Common protocols include:

- TCP
- UDP
- ICMP

---

# Common Ports

| Port | Service |
|------|---------|
| 22 | SSH |
| 80 | HTTP |
| 443 | HTTPS |
| 3389 | Remote Desktop (RDP) |

---

# Priority

Firewall Rules have priorities.

If multiple rules match the same traffic, the rule with the lowest numerical priority is evaluated first.

---

# Firewall Targets

Rules can be applied to:

- All instances
- Specific instances
- Network Tags
- Service Accounts

This provides fine-grained control over network access.

---

# Best Practices

- Allow only required ports.
- Block unused services.
- Use network tags to organize firewall rules.
- Avoid overly permissive rules.
- Review firewall configurations regularly.

---

# Real-World Example

A company deploys a web application on Compute Engine.

The firewall configuration allows:

- Port 80 (HTTP)
- Port 443 (HTTPS)
- Port 22 (SSH) only for administrators

All other incoming traffic is blocked, reducing the attack surface while allowing legitimate access.

---

# What I Learned

- Firewall Rules secure resources inside a VPC.
- Ingress rules control incoming traffic.
- Egress rules control outgoing traffic.
- Rules evaluate traffic based on protocol, port, direction, and priority.
- Proper firewall configuration is essential for securing cloud infrastructure.
