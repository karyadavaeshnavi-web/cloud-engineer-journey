# Day 21 – Decision Making in Python

## Objective

Learn how Python programs make decisions using conditional statements. These concepts form the basis of monitoring systems, automation scripts, and infrastructure health checks used by Cloud Engineers.

---

# Why Decision Making?

Automation scripts should not always perform the same action.

Instead, they should react based on system conditions.

Example:

- CPU usage above 80% → Generate an alert.
- Disk usage below 80% → Continue monitoring.

Conditional statements make this possible.

---

# Boolean Values

Every condition in Python evaluates to either:

- True
- False

Example:

```python
5 > 2
```

Result:

```
True
```

---

# Comparison Operators

| Operator | Meaning |
|----------|---------|
| == | Equal to |
| != | Not Equal |
| > | Greater Than |
| < | Less Than |
| >= | Greater Than or Equal |
| <= | Less Than or Equal |

---

# Assignment vs Comparison

Assignment:

```python
cpu = 80
```

Comparison:

```python
cpu == 80
```

Assignment stores data.

Comparison checks a condition.

---

# if Statement

```python
if cpu > 80:
    print("High CPU Usage")
```

Executes only if the condition is True.

---

# else Statement

```python
if cpu > 80:
    print("High CPU")
else:
    print("CPU Normal")
```

Runs when the previous condition is False.

---

# elif Statement

```python
if cpu > 90:
    print("Critical")
elif cpu > 70:
    print("Warning")
else:
    print("Healthy")
```

Allows multiple conditions to be checked.

---

# Logical Operators

## and

Both conditions must be True.

```python
if cpu > 80 and memory > 80:
```

---

## or

Only one condition must be True.

```python
if cpu > 90 or memory > 90:
```

---

## not

Reverses a Boolean value.

```python
if not service_running:
```

---

# Nested if

A conditional statement inside another conditional statement.

Useful when one decision depends on another.

---

# What I Learned

- Programs can make decisions.
- Conditions evaluate to True or False.
- if, elif and else create decision logic.
- Logical operators combine multiple conditions.

---

# Real Cloud Engineer Use Case

Monitoring systems use conditional statements to determine whether CPU, memory, disk, or service status requires alerts. Instead of manually checking every server, automation scripts evaluate thresholds and notify engineers only when necessary.
