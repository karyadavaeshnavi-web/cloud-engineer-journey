# OSI Model

## Overview

The OSI (Open Systems Interconnection) Model is a framework that explains how data travels between devices over a network. It divides network communication into seven layers, where each layer has a specific responsibility.

The OSI model helps network engineers, cloud engineers, and SREs troubleshoot problems by identifying which layer is causing the issue.

---

## Why the OSI Model is Important

The OSI model provides a structured way to understand network communication.

Benefits:

* Simplifies troubleshooting
* Standardizes network communication
* Helps identify where failures occur
* Forms the foundation of cloud networking concepts

Many cloud technologies such as VPCs, Subnets, Firewalls, Load Balancers, DNS, and Kubernetes networking rely on concepts from the OSI model.

---

## OSI Layers

### Layer 7 - Application

Purpose:
Provides network services directly to end-user applications.

Examples:

* Chrome
* ChatGPT
* YouTube
* DNS
* HTTP
* HTTPS

Function:

* User interacts with applications
* Generates requests and receives responses

Example:

User types:

Hello ChatGPT

---

### Layer 6 - Presentation

Purpose:
Formats, encrypts, and compresses data.

Examples:

* SSL/TLS
* Encryption
* Compression

Function:

* Protects data during transmission
* Ensures data is readable by the receiving system

Example:

Hello ChatGPT

becomes

Encrypted Hello ChatGPT

---

### Layer 5 - Session

Purpose:
Establishes, maintains, and terminates communication sessions.

Examples:

* Login sessions
* Application sessions

Function:

* Tracks active communication between devices

Example:

Maintains a user's login session on a website.

---

### Layer 4 - Transport

Purpose:
Provides end-to-end communication and reliability.

Protocols:

* TCP
* UDP

Function:

* Breaks data into segments
* Ensures delivery (TCP)
* Provides fast communication (UDP)

Examples:

TCP:

* Websites
* Banking applications
* Email

UDP:

* Gaming
* Streaming
* Video calls

---

### Layer 3 - Network

Purpose:
Handles logical addressing and routing.

Examples:

* IPv4
* IPv6
* Routers

Function:

* Determines the path data takes through networks
* Uses IP addresses to identify devices

Example:

Source IP:
192.168.1.10

Destination IP:
142.x.x.x

---

### Layer 2 - Data Link

Purpose:
Handles communication between devices on the same local network.

Examples:

* Ethernet
* Switches
* MAC Addresses

Function:

* Uses MAC addresses for local delivery
* Creates frames

Example:

AA:BB:CC:DD:EE:FF

---

### Layer 1 - Physical

Purpose:
Physically transmits data.

Examples:

* Ethernet Cables
* Fiber Optic Cables
* WiFi Signals

Function:

* Converts data into electrical, optical, or wireless signals

Example:

010101010101

---

## Message Flow Through the OSI Model

When a user sends a message to ChatGPT:

### Sender Side

Application Layer
↓
Creates message

Presentation Layer
↓
Encrypts message

Session Layer
↓
Adds session information

Transport Layer
↓
Adds TCP/UDP information

Network Layer
↓
Adds IP addresses

Data Link Layer
↓
Adds MAC addresses

Physical Layer
↓
Converts data into signals

Internet
↓
Transfers data

### Receiver Side

Physical Layer
↓
Receives signals

Data Link Layer
↓
Reads MAC addresses

Network Layer
↓
Reads IP addresses

Transport Layer
↓
Processes TCP/UDP information

Session Layer
↓
Restores session

Presentation Layer
↓
Decrypts data

Application Layer
↓
Delivers message to application

---

## Layers Most Important for Cloud Engineers

### Layer 3 - Network

Used in:

* VPCs
* Subnets
* Routing
* Firewall Rules

### Layer 4 - Transport

Used in:

* TCP
* UDP
* Ports
* Load Balancers

### Layer 7 - Application

Used in:

* HTTP
* HTTPS
* DNS
* APIs

These are the layers most commonly used in Cloud Engineering, DevOps, and Site Reliability Engineering.

---

## Key Takeaways

* The OSI model contains seven layers.
* Data moves from Layer 7 to Layer 1 when sending.
* Data moves from Layer 1 to Layer 7 when receiving.
* Each layer adds information before transmission.
* Layer 3, Layer 4, and Layer 7 are the most important layers for Cloud Engineers and SREs.
