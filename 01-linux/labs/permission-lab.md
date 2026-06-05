# Linux Permissions Lab

## Objective

Understand Linux ownership and permission management.

---

## Environment

Ubuntu on Windows

---

## Lab Setup

Created:

linux-permissions-lab
├── files
└── scripts

Created files:

config.txt

script.sh

---

## Commands Used

mkdir

touch

ls -l

chmod 644

chmod 755

---

## Activities Performed

1. Created files and directories.
2. Viewed permissions using ls -l.
3. Applied chmod 644 to config.txt.
4. Applied chmod 755 to script.sh.
5. Observed permission output.

---

## Observations

Default permissions displayed:

-rw-r--r--

chmod 644 resulted in:

rw-r--r--

chmod 755 resulted in:

rwxr-xr-x


---

## Key Learnings

* Linux uses ownership and permissions for security.
* Every file has an Owner and Group.
* Permissions are Read, Write, and Execute.
* chmod changes permissions.
* chown changes ownership.
* Numeric permissions provide a shorthand way to define access rules.

---

## Outcome

Successfully practiced Linux permission concepts and permission management commands.
