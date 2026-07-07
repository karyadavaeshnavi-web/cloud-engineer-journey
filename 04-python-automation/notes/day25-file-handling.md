# Day 25 – File Handling in Python

## Objective

Learn how Python reads from and writes to files. File handling allows automation scripts to store information permanently instead of displaying it only on the terminal.

---

# Why File Handling?

Many automation scripts generate useful information such as:

- Server reports
- CPU usage
- Disk usage
- Memory statistics
- Log files

If this information is only printed to the terminal, it disappears when the program ends.

By writing data to files, automation scripts create permanent records that can be reviewed later.

---

# Opening Files

Python uses the `open()` function to access files.

Example:

```python
file = open("server.txt", "r")
```

---

# File Modes

## Read

```python
"r"
```

Opens an existing file for reading.

---

## Write

```python
"w"
```

Creates a new file or overwrites an existing one.

---

## Append

```python
"a"
```

Adds new data to the end of an existing file without removing previous content.

---

## Create

```python
"x"
```

Creates a new file and raises an error if the file already exists.

---

# Reading Files

Example:

```python
with open("hello.txt", "r") as file:
    print(file.read())
```

---

# Writing Files

Example:

```python
with open("hello.txt", "w") as file:
    file.write("Hello Cloud Engineer")
```

---

# Appending Files

Example:

```python
with open("hello.txt", "a") as file:
    file.write("\nPython Automation")
```

---

# Why use with open()?

Instead of manually opening and closing files:

```python
file = open(...)
file.close()
```

Python provides:

```python
with open(...) as file:
```

Benefits:

- Automatically closes files
- Prevents resource leaks
- Cleaner code
- Safer programming practice

---

# Reading Line by Line

Example:

```python
with open("servers.txt") as file:
    for server in file:
        print(server.strip())
```

The `strip()` function removes extra newline characters.

---

# Write vs Append

Write (`w`)

- Replaces existing content.
- Starts a new file.

Append (`a`)

- Preserves existing content.
- Adds new information at the end.

---

# What I Learned

- Python can read and write files.
- Different file modes serve different purposes.
- `with open()` is the recommended approach.
- File handling is essential for automation and logging.

---

# Real Cloud Engineer Use Case

Cloud Engineers use file handling to:

- Generate monitoring reports
- Store server logs
- Save backup information
- Record deployment status
- Maintain audit logs

Automation scripts rarely rely only on terminal output. They usually save results into log files or reports for future analysis.

---

# Reflection

Today I learned how Python interacts with files by reading, writing, and appending data. I understood why automation scripts save information instead of simply printing it, and why `with open()` is considered the safest and cleanest approach. I also learned that file handling is a fundamental requirement for monitoring systems, reporting tools, and infrastructure automation because it allows engineers to preserve historical records for troubleshooting and analysis.
