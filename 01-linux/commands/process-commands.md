# Linux Process Commands

## ps

Purpose:

Display currently running processes associated with the current terminal session.

Example:

ps

---

## ps -ef

Purpose:

Display all running processes on the system.

Example:

ps -ef

Important Columns:

UID  → User owning the process

PID  → Process ID

PPID → Parent Process ID

CMD  → Command running

---

## top

Purpose:

Provide real-time monitoring of system activity.

Displays:

* CPU usage
* Memory usage
* Running processes
* Process states
* System load

Example:

top

Press:

q

to exit.

---

## kill

Purpose:

Terminate a process.

Example:

kill 1234

Terminates process with PID 1234.

---

## kill -9

Purpose:

Forcefully terminate a process.

Example:

kill -9 1234

Used when a process does not respond to a normal kill command.

---

## Common Process States

R → Running

S → Sleeping

Z → Zombie
