# Day 22 – Loops in Python

## Objective

Learn how Python automates repetitive tasks using loops. Loops are one of the most important concepts in automation because they allow the same task to be performed repeatedly without writing duplicate code.

---

# Why Loops?

Imagine checking the health of 1,000 servers.

Without loops:

```python
check("web01")
check("web02")
check("web03")
...
```

This approach is inefficient and difficult to maintain.

With loops:

```python
for server in servers:
    check(server)
```

The same logic works for any number of servers.

---

# Types of Loops

## for Loop

A `for` loop is used when iterating through a collection or when the number of iterations is known.

Example:

```python
servers = ["web01", "web02", "db01"]

for server in servers:
    print(server)
```

---

## while Loop

A `while` loop repeats as long as a condition remains True.

Example:

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

---

# range()

The `range()` function generates a sequence of numbers.

Example:

```python
for i in range(1,6):
    print(i)
```

Output:

```
1
2
3
4
5
```

---

# break

Stops the loop immediately.

```python
if cpu > 95:
    break
```

Useful when continuing the loop is unnecessary.

---

# continue

Skips the current iteration and moves to the next one.

```python
if server == "maintenance":
    continue
```

Useful when certain items should not be processed.

---

# Nested Loops

A loop inside another loop.

Example:

```python
for server in servers:
    for check in checks:
        print(server, check)
```

---

# What I Learned

- Loops automate repetitive work.
- for loops iterate through collections.
- while loops repeat until a condition becomes False.
- break exits a loop.
- continue skips one iteration.
- range() controls the number of iterations.

---

# Real Cloud Engineer Use Case

Cloud Engineers use loops to:

- Monitor hundreds of servers.
- Check virtual machines.
- Deploy infrastructure.
- Process log files.
- Perform health checks on multiple cloud resources.

Loops make automation scalable and efficient.
# Reflection

Today I learned how loops automate repetitive tasks in Python. I understood the difference between `for` and `while` loops, when to use each one, and how `break` and `continue` control loop execution. I also learned how loops are essential for Cloud Engineering because they allow automation scripts to perform the same operation across multiple servers, virtual machines, and cloud resources without duplicating code.





