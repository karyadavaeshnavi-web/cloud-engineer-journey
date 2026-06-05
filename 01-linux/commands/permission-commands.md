# Linux Permission Commands

## ls -l

Purpose:

Display file permissions, ownership, and additional file information.

Example:

ls -l

---

## chmod

Purpose:

Change file permissions.

Examples:

chmod 755 script.sh

chmod 644 config.txt

Common Values:

755 → rwxr-xr-x

644 → rw-r--r--

---

## chown

Purpose:

Change file ownership.

Example:

chown username file.txt

---

## Permission Values

Read = 4

Write = 2

Execute = 1

Examples:

7 = rwx

6 = rw-

5 = r-x

4 = r--
