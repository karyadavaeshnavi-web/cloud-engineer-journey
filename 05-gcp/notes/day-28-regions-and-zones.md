# Day 28 – Google Cloud: Regions & Zones

## Objective

Understand how Google Cloud's global infrastructure is organized using Regions and Zones, why this architecture improves reliability and availability, and how it helps design highly available cloud applications.

---

# Google Cloud Global Infrastructure

Google Cloud Platform operates on one of the world's largest private networks.

Its infrastructure consists of:

- Regions
- Zones
- Data Centers
- Edge Locations
- Global Network

These components work together to provide reliable, scalable, and highly available cloud services.

---

# What is a Region?

A Region is a specific geographical location where Google operates cloud resources.

Each region contains multiple independent zones.

Examples:

- us-central1 (Iowa)
- us-east1 (South Carolina)
- europe-west1 (Belgium)
- asia-south1 (Mumbai)
- asia-southeast1 (Singapore)

Organizations choose regions based on:

- User location
- Compliance requirements
- Latency
- Disaster Recovery

---

# What is a Zone?

A Zone is an isolated location within a region.

Each zone contains its own:

- Power
- Cooling
- Networking
- Physical Infrastructure

Zones are designed to operate independently from one another.

Example:

Region:

```text
asia-south1
```

Zones:

```text
asia-south1-a
asia-south1-b
asia-south1-c
```

If one zone experiences an outage, applications running in another zone within the same region can continue operating.

---

# Region vs Zone

| Region | Zone |
|---------|------|
| Geographic location | Individual data center location within a region |
| Contains multiple zones | Belongs to one region |
| Used for disaster recovery | Used for application deployment |
| Examples: asia-south1, us-central1 | Examples: asia-south1-a, asia-south1-b |

---

# Why Multiple Zones?

Using multiple zones improves:

- High Availability
- Fault Tolerance
- Reliability
- Business Continuity

If one zone becomes unavailable due to maintenance or failure, workloads running in another zone remain accessible.

---

# High Availability

High Availability (HA) means applications remain available even if part of the infrastructure fails.

Instead of deploying everything in a single zone:

```text
Region
└── Zone A
```

A better architecture is:

```text
Region
├── Zone A
└── Zone B
```

This minimizes downtime and improves reliability.

---

# Low Latency

Latency is the time taken for data to travel between a user and a server.

Choosing a region close to users reduces latency and improves application performance.

Example:

Users in India should typically use:

```text
asia-south1 (Mumbai)
```

instead of a region located in North America.

---

# Disaster Recovery

Disaster Recovery (DR) ensures applications can recover from unexpected failures.

A common strategy is to replicate data across multiple regions.

Example:

Primary Region:

```text
asia-south1 (Mumbai)
```

Backup Region:

```text
asia-southeast1 (Singapore)
```

If the primary region becomes unavailable, services can be restored from the backup region.

---

# Best Practices

- Choose the region closest to your users.
- Deploy workloads across multiple zones for high availability.
- Use multiple regions for disaster recovery.
- Consider data residency and compliance requirements before selecting a region.
- Design applications to tolerate zone failures.

---

# Real-World Example

An e-commerce company serves customers across India.

Instead of deploying all resources in a single zone, they deploy web servers across:

```text
asia-south1-a
asia-south1-b
```

If one zone experiences an outage, customer requests are automatically handled by resources in the other zone, ensuring uninterrupted service.

---

# What I Learned

- Google Cloud's infrastructure is organized into Regions and Zones.
- A Region contains multiple independent Zones.
- Zones provide isolation and fault tolerance.
- Deploying across multiple zones improves High Availability.
- Choosing the correct region reduces latency and improves performance.
- Multi-region deployments support disaster recovery and business continuity.
