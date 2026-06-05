# Linux Process Monitoring Lab

## Objective

Learn how to inspect and monitor running processes in Linux.

---

## Environment

Ubuntu Linux

---

## Commands Executed

ps

ps -ef

top

---

## Observations

### ps

Displayed processes associated with the current terminal session.

Observed:

* bash
* ps

Each process was assigned a unique PID.

---

### ps -ef

Displayed all running processes on the system.

Observed:

* init
* systemd
* rsyslogd
* bash
* ps

Also observed:

* PID
* PPID
* UID
* CMD

---

### top

Displayed real-time process information.

Observed:

* CPU usage
* Memory usage
* Running processes
* Process states
* Load average

System was mostly idle with low CPU utilization.

---

## Key Learnings

* Programs become processes when executed.
* Every process receives a PID.
* Processes can have parent-child relationships.
* Linux provides tools for monitoring processes.
* top acts similarly to Task Manager in Windows.
* kill can terminate processes using their PID.

---

## Outcome

Successfully monitored running processes using ps, ps -ef, and top while understanding process management concepts in Linux.
