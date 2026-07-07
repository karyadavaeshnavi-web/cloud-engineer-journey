# Day 23 – Functions in Python

## Objective

Learn how functions organize Python code into reusable blocks. Functions improve readability, reduce code duplication, and make automation scripts easier to maintain.

---

# Why Functions?

Without functions, the same block of code must be written repeatedly.

Instead of writing identical logic multiple times, we write it once inside a function and call it whenever needed.

Functions help build larger applications in a structured and modular way.

---

# What is a Function?

A function is a reusable block of code designed to perform a specific task.

General Syntax:

```python
def function_name():
    # code
```

---

# Defining a Function

A function is created using the `def` keyword.

Example:

```python
def greet():
    print("Welcome Cloud Engineer")
```

Defining a function only stores it in memory.

It does not execute.

---

# Calling a Function

To execute a function:

```python
greet()
```

Output:

```
Welcome Cloud Engineer
```

---

# Parameters

Parameters are variables defined inside the function declaration.

Example:

```python
def greet(name):
    print("Hello", name)
```

Here,

`name`

is the parameter.

---

# Arguments

Arguments are the actual values passed to a function.

Example:

```python
greet("Vaeshnavi")
```

"Vaeshnavi"

is the argument.

---

# Multiple Parameters

Example:

```python
def server_status(server, cpu):
    print(server)
    print(cpu)
```

Call:

```python
server_status("web01", 82)
```

---

# Return Statement

Functions can return values.

Example:

```python
def add(a, b):
    return a + b
```

Usage:

```python
result = add(10,20)
print(result)
```

Output:

```
30
```

Unlike `print()`, `return` sends the value back to the calling code so it can be stored, reused, compared, or passed to another function.

---

# Local Variables

Variables declared inside a function only exist within that function.

Example:

```python
def test():
    cpu = 80
```

The variable `cpu` cannot be accessed outside this function.

---

# Global Variables

Variables declared outside a function can be accessed by functions.

Example:

```python
server = "web01"

def show():
    print(server)
```

---

# Why Functions Matter

Functions provide:

- Code Reusability
- Better Organization
- Easier Debugging
- Simpler Maintenance
- Modular Programming

---

# What I Learned

- Functions organize code into reusable blocks.
- Functions reduce duplicate code.
- Parameters receive values.
- Arguments provide actual data.
- Return sends values back to the caller.
- Local variables exist only inside functions.

---

# Real Cloud Engineer Use Case

Cloud Engineers create reusable functions for:

- Checking CPU usage
- Monitoring memory
- Collecting disk information
- Deploying cloud resources
- Creating virtual machines
- Running health checks

Instead of rewriting the same automation logic repeatedly, one function can be called for hundreds of servers.

---

# Reflection

Today I learned how functions improve code organization and make programs easier to maintain. I understood the difference between defining and calling a function, parameters and arguments, and how the `return` statement differs from `print()`. I also learned why Cloud Engineers use functions extensively to build reusable automation scripts that can perform the same task across many servers without duplicating code.
