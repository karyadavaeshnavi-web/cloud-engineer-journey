# Linux Services and Logs

## What is a Service?

A service is a program that runs in the background and provides functionality to the system or other applications.

Unlike normal programs, services are designed to run continuously and automatically.

Examples:

- SSH Service
- Cron Service
- Docker Service
- Nginx Service
- MySQL Service

---

## Why Services Matter

Most applications running on Linux servers depend on services.

Services allow systems to:

- Run applications continuously
- Automate tasks
- Handle network requests
- Manage databases
- Support cloud infrastructure

---

## Common Linux Services

### SSH

Provides remote access to Linux systems.

### Cron

Runs scheduled tasks automatically.

### Docker

Manages container workloads.

### Nginx

Provides web server functionality.

---

## What is systemd?

systemd is the service manager used by modern Linux distributions.

It is responsible for:

- Starting services
- Stopping services
- Restarting services
- Monitoring services
- Managing service dependencies

systemd is one of the first processes started during system boot.

---

## What is systemctl?

systemctl is the command-line tool used to interact with systemd.

It allows users to:

- View service status
- Start services
- Stop services
- Restart services
- Enable services at boot

---

## Service States

### Active (Running)

The service is currently running and functioning normally.

### Inactive

The service exists but is not currently running.

### Failed

The service encountered an error and stopped working.

---

## Starting Services

Example:

sudo systemctl start cron

Starts the service immediately.

---

## Stopping Services

Example:

sudo systemctl stop cron

Stops the service.

---

## Restarting Services

Example:

sudo systemctl restart cron

Stops and starts the service again.

Often used after configuration changes.

---

## Enable vs Start

### Start

Starts a service immediately.

Example:

sudo systemctl start cron

### Enable

Configures a service to automatically start during system boot.

Example:

sudo systemctl enable cron

Think:

Start = Current Session

Enable = Every Boot

---

## Linux Logs

Logs record events that occur on the system.

Logs help administrators:

- Troubleshoot issues
- Investigate failures
- Monitor activity
- Track system behavior

---

## The /var/log Directory

Most Linux log files are stored in:

/var/log

Common files include:

- syslog
- auth.log
- kern.log
- dpkg.log

---

## journalctl

journalctl is used to view logs collected by systemd.

Examples:

journalctl

journalctl -n 20

journalctl -u cron

---


Services power nearly everything in cloud environments.

Examples:

- Docker Service
- Kubernetes Components
- Web Servers
- Monitoring Agents

Understanding services and logs is essential for troubleshooting and maintaining cloud infrastructure.

---

## Summary

- Services run in the background.
- systemd manages services.
- systemctl controls services.
- Logs help troubleshoot issues.
- journalctl displays service and system logs.
- /var/log stores important log files.
