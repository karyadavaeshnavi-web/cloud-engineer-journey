# Day 24 – Modules & Libraries

## Objective

Learn how Python uses modules and libraries to provide reusable functionality. Modules allow developers to access pre-written code instead of implementing common features from scratch, making automation scripts faster to develop and easier to maintain.

---

# Why Modules?

Instead of writing every algorithm or utility ourselves, Python provides modules containing tested and reusable code.

Example:

Instead of writing your own square root algorithm:

```python
import math

print(math.sqrt(81))
```

Output:

```
9.0
```

Modules reduce development time and improve code reliability.

---

# Module vs Library

## Module

A module is a single Python file containing reusable code such as functions, classes, and variables.

Examples:

- math
- os
- random
- datetime
- subprocess

---

## Library

A library is a collection of related modules.

Example:

Python Standard Library

- math
- os
- datetime
- random
- subprocess
- sys

A library groups modules that provide related functionality.

---

# Importing Modules

Import an entire module:

```python
import math
```

Import a specific function:

```python
from math import sqrt

print(sqrt(64))
```

---

# math Module

Provides mathematical functions.

Example:

```python
import math

print(math.sqrt(81))
print(math.ceil(4.2))
print(math.floor(4.9))
```

---

# random Module

Generates random values.

Example:

```python
import random

servers = ["web01","web02","db01"]

print(random.choice(servers))
```

---

# datetime Module

Provides date and time information.

Example:

```python
from datetime import datetime

print(datetime.now())
```

Useful for timestamps in reports and logs.

---

# os Module

Allows Python to interact with the operating system.

Common functions:

```python
os.getcwd()
```

Current working directory.

```python
os.listdir()
```

Lists files and folders.

```python
os.mkdir()
```

Creates directories.

---

# sys Module

Provides information about the Python runtime.

Example:

```python
import sys

print(sys.version)
```

---

# subprocess Module

Allows Python to execute operating system commands.

Example:

```python
import subprocess

subprocess.run(["pwd"])
```

Linux command executed through Python.

Other examples:

```python
subprocess.run(["ls"])
```

```python
subprocess.run(["uptime"])
```

---

# Why Modules Matter

Modules provide:

- Code reuse
- Faster development
- Better reliability
- Easier maintenance
- Access to powerful built-in functionality

---

# What I Learned

- A module is a reusable Python file.
- A library contains multiple related modules.
- Modules simplify development.
- os interacts with the operating system.
- subprocess executes Linux commands.
- datetime provides timestamps for automation.

---

# Real Cloud Engineer Use Case

Cloud Engineers use modules to automate cloud infrastructure, execute Linux commands, create reports, monitor servers, manage files, and interact with cloud APIs. Instead of manually performing system administration tasks, automation scripts rely heavily on built-in modules to communicate with the operating system and cloud platforms.

---

# Reflection

Today I learned how Python modules and libraries extend the capabilities of a program by providing reusable functionality. I understood the difference between a module and a library, how to import modules, and why modules such as os, subprocess, datetime, and math are essential in Cloud Engineering. I also learned that subprocess forms the bridge between Python and Linux, enabling automation scripts to execute operating system commands.
