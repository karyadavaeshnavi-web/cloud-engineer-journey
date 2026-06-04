# Linux Permissions and Ownership

## Why Permissions Matter

Linux is a multi-user operating system. Permissions are used to control who can read, modify, or execute files and directories. They help protect system files, user data, and applications from unauthorized access.

## Users

A user is an account that can access the Linux system.

Examples:

* root
* vaeshnavi
* john

### Root User

The root user is the administrator of the system and has unrestricted access to all files and resources.

---

## Groups

A group is a collection of users.

Groups simplify permission management because permissions can be assigned to a group instead of individual users.

Example:

developers
├── Alice
├── Bob
└── Charlie

---

## Ownership

Every file and directory has:

* Owner
* Group

Example:

Owner: vaeshnavi

Group: developers

Ownership determines who controls the file and which group permissions apply.

---

## Permission Types

### Read (r)

Allows viewing the contents of a file.

### Write (w)

Allows modifying the contents of a file.

### Execute (x)

Allows running a file as a program or script.

---

## Permission Categories

Permissions are applied to:

### Owner

The user who owns the file.

### Group

Members of the file's assigned group.

### Others

Everyone else on the system.

---

## Understanding ls -l Output

Example:

-rwxr-xr--

Breakdown:

Owner  → rwx

Group  → r-x

Others → r--

Meaning:

Owner can read, write, and execute.

Group can read and execute.

Others can only read.

---

## Numeric Permissions

Linux represents permissions using numbers.

Read = 4

Write = 2

Execute = 1

### 755

Owner → 7 = rwx

Group → 5 = r-x

Others → 5 = r-x

Result:

rwxr-xr-x

### 644

Owner → 6 = rw-

Group → 4 = r--

Others → 4 = r--

Result:

rw-r--r--

---

## chmod

The chmod command changes file permissions.

Examples:

chmod 755 script.sh

chmod 644 config.txt

---

## chown

The chown command changes file ownership.

Example:

chown vaeshnavi file.txt

---

## Why Cloud Engineers Care

Incorrect permissions can cause:

* Application failures
* Docker container issues
* Kubernetes volume access problems
* SSH authentication failures

Understanding permissions is essential for managing Linux servers and cloud infrastructure.

---

## Summary

* Every file has an Owner and Group.
* Permissions are Read, Write, and Execute.
* Permissions apply to Owner, Group, and Others.
* chmod changes permissions.
* chown changes ownership.
