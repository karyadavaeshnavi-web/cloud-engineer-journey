# Day 27 – Google Cloud: Cloud Concepts

## Objective

Understand the fundamentals of Cloud Computing, why organizations use cloud platforms, the different cloud service models, deployment models, and the basic concepts of Google Cloud Platform (GCP).

---

# What is Cloud Computing?

Cloud Computing is the delivery of computing resources such as servers, storage, databases, networking, software, and analytics over the internet instead of managing physical infrastructure.

Rather than purchasing hardware, organizations can provision resources whenever needed and pay only for what they use.

---

# Why Cloud Computing?

Cloud computing has become the standard because it offers:

- On-demand resource provisioning
- Scalability
- High Availability
- Cost Optimization
- Global Accessibility
- Faster Deployment
- Improved Reliability
- Better Disaster Recovery

Instead of spending weeks setting up infrastructure, cloud resources can be created in minutes.

---

# Traditional Infrastructure vs Cloud Computing

| Traditional Infrastructure | Cloud Computing |
|----------------------------|----------------|
| Physical Servers | Virtual Resources |
| High Upfront Cost | Pay-as-you-go |
| Manual Scaling | Automatic Scaling |
| Hardware Maintenance | Managed by Cloud Provider |
| Slower Deployment | Rapid Deployment |

---

# Cloud Service Models

## Infrastructure as a Service (IaaS)

Provides virtual infrastructure such as servers, storage, and networking.

The customer manages:

- Operating System
- Applications
- Runtime
- Data

The cloud provider manages:

- Physical Servers
- Storage
- Networking
- Virtualization

Examples:

- Google Compute Engine
- Amazon EC2
- Azure Virtual Machines

---

## Platform as a Service (PaaS)

Provides a complete platform for developing and deploying applications.

The cloud provider manages the infrastructure while developers focus on writing code.

Examples:

- Google App Engine
- Azure App Service

---

## Software as a Service (SaaS)

Provides complete software applications over the internet.

Users simply access the application without worrying about the underlying infrastructure.

Examples:

- Gmail
- Google Docs
- Microsoft 365

---

# Cloud Deployment Models

## Public Cloud

Infrastructure is owned and managed by a cloud provider and shared among multiple customers.

Example:

Google Cloud Platform

---

## Private Cloud

Infrastructure is dedicated to a single organization.

Often used where higher security or compliance is required.

---

## Hybrid Cloud

A combination of public cloud and on-premises infrastructure.

Allows workloads to move between environments as needed.

---

# What is Google Cloud Platform (GCP)?

Google Cloud Platform (GCP) is Google's public cloud platform that provides services for computing, storage, networking, databases, artificial intelligence, security, and application deployment.

It enables organizations to build, deploy, and manage applications on Google's global infrastructure.

---

# Major Service Categories in GCP

## Compute

Provides virtual machines and managed compute services.

Examples:

- Compute Engine
- Google Kubernetes Engine (GKE)
- Cloud Run
- App Engine

---

## Storage

Provides secure and scalable object storage.

Examples:

- Cloud Storage
- Persistent Disks

---

## Networking

Provides secure communication between cloud resources.

Examples:

- Virtual Private Cloud (VPC)
- Cloud Load Balancing
- Cloud DNS

---

## Security

Provides identity management and resource protection.

Examples:

- IAM
- Secret Manager
- Cloud Identity

---

## Monitoring

Provides monitoring, logging, and alerting services.

Examples:

- Cloud Monitoring
- Cloud Logging

---

# Benefits of Google Cloud

- Global Infrastructure
- High Availability
- Built-in Security
- Scalability
- Pay-as-you-go Pricing
- Integration with Kubernetes
- Managed Services
- AI and Machine Learning Services

---

# Shared Responsibility Model

Security in the cloud is shared between Google and the customer.

### Google is responsible for

- Physical data centers
- Networking infrastructure
- Hardware
- Cloud service availability

### Customer is responsible for

- User access management
- Application security
- Data protection
- Firewall configuration
- Operating system management (for IaaS services)

---

# Real-World Example

A startup wants to launch a web application.

Instead of purchasing servers and setting up a physical data center, they can use Google Cloud to provision virtual machines, configure networking, store data, and deploy their application within minutes. As user traffic increases, they can scale resources without purchasing additional hardware.

---

# What I Learned

- Cloud Computing provides computing resources over the internet.
- Cloud platforms reduce infrastructure management and improve scalability.
- IaaS, PaaS, and SaaS serve different purposes.
- Public, Private, and Hybrid Clouds are different deployment models.
- Google Cloud Platform provides services for compute, networking, storage, security, and monitoring.
- Cloud security follows the Shared Responsibility Model.
