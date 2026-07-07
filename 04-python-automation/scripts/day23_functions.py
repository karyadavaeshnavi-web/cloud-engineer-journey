# Day 23 - Functions

def greet():
    print("Welcome Cloud Engineer")


def greet_user(name):
    print("Hello", name)


def add(a, b):
    return a + b


def check_server(server):
    print("Checking", server)


servers = ["web01", "web02", "db01"]

greet()

print()

greet_user("Vaeshnavi")

print()

result = add(10, 20)

print("Addition:", result)

print()

for server in servers:
    check_server(server)
