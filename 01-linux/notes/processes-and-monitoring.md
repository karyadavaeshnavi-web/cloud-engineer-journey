# Linux Processes and System Monitoring

## What is a Program?

A program is a set of instructions stored on disk.

Examples:

* Google Chrome
* Visual Studio Code
* Python
* Firefox

A program is inactive until it is executed.

---

## What is a Process?

A process is a running instance of a program.

When a program is executed, Linux creates a process and allocates resources such as CPU time and memory.

Example:

Program:
Python

Command:

python app.py

Result:

Python process starts running.

---

## What is a PID?

PID stands for Process ID.

Every process running in Linux is assigned a unique identification number called a PID.

Example:

PID 1001

PID 2050

PID 3000

PIDs help users and the operating system identify and manage processes.

---

## Parent and Child Processes

Processes can create other processes.

The process that creates another process is called the parent process.

The newly created process is called the child process.

Example:

bash
│
└── ps

In this example, bash is the parent process and ps is the child process.

---

## Process States

### Running (R)

The process is currently executing.

### Sleeping (S)

The process is waiting for an event or resource.

Most Linux processes spend their time in the sleeping state.

---

## Foreground Processes

Foreground processes run directly in the terminal.

Example:

python app.py

The terminal remains occupied until the process finishes.

---

## Background Processes

Background processes run independently of the terminal.

Example:

python app.py &

The terminal remains available for additional commands.

---

## System Monitoring

Linux provides tools for monitoring processes and system performance.

Common tools:

* ps
* ps -ef
* top

These tools help administrators identify running processes, CPU usage, memory usage, and system load.

---

## Why Cloud Engineers Care

Processes are the foundation of applications and services.

Understanding processes helps troubleshoot:

* Slow servers
* Crashed applications
* High CPU usage
* High memory usage
* Service failures

Process monitoring is a critical skill for Cloud Engineers, DevOps Engineers, and Site Reliability Engineers.

---

## Summary

* Programs become processes when executed.
* Every process receives a unique PID.
* Processes can have parent and child relationships.
* Linux provides tools such as ps and top for monitoring processes.
* Processes can be terminated using kill.
