# IP Addressing Fundamentals

## Overview

IP addresses allow devices to identify and communicate with each other across networks.

Every device connected to a network requires an IP address to send and receive data.

Examples:

* Computers
* Mobile Phones
* Servers
* Routers
* Cloud Virtual Machines

Without IP addresses, network communication would not be possible.

---

## What is an IP Address?

An IP (Internet Protocol) Address is a logical identifier assigned to a device on a network.

Purpose:

* Identify devices
* Enable communication
* Route data between networks

Example:

192.168.1.10

Think of an IP address as a house address used by computers.

---

## IPv4

IPv4 is the most widely used IP addressing format.

Example:

192.168.1.10

Structure:

192 . 168 . 1 . 10

An IPv4 address contains four sections separated by dots.

Each section can have a value from:

0 to 255

---

## Public IP Addresses

A Public IP Address is accessible from the Internet.

Examples:

* Google Servers
* OpenAI Servers
* Cloud Load Balancers

Characteristics:

* Globally unique
* Reachable from the Internet
* Assigned by Internet providers or cloud providers

Example:

34.120.x.x

---

## Private IP Addresses

Private IP Addresses are used inside local networks.

Examples:

* Home Networks
* Office Networks
* Cloud VPC Networks

Characteristics:

* Not directly accessible from the Internet
* Used for internal communication
* Reusable across different networks

### Private IP Ranges

10.0.0.0 - 10.255.255.255

172.16.0.0 - 172.31.255.255

192.168.0.0 - 192.168.255.255

---

## Why Private IP Addresses Exist

Private IP addresses help:

* Reduce public IP consumption
* Provide network isolation
* Improve security
* Enable internal communication

Cloud providers heavily use private IPs inside VPC networks.

---

## Loopback Address

Special IP Address:

127.0.0.1

Also called:

localhost

Purpose:

Allows a computer to communicate with itself.

Traffic sent to 127.0.0.1 never leaves the machine.

---

## Localhost

localhost is a hostname that resolves to:

127.0.0.1

Examples:

http://localhost

http://127.0.0.1

Common Uses:

* Application testing
* Local development
* Troubleshooting

---

## Routing Basics

A route tells the operating system where network traffic should be sent.

Command:

ip route

Example:

default via 192.168.1.1

Meaning:

If the destination is not on the local network, send traffic to the router.

---

## Commands Practiced

### View IP Address

ip addr

### View Loopback Interface

ip addr show lo

### Test Localhost

ping 127.0.0.1 -c 4

### View Routing Table

ip route

---

