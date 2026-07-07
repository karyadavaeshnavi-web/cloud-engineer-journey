# Day 22 - Python Loops

servers = ["web01", "web02", "db01"]

print("===== SERVER CHECK =====")

for server in servers:
    print("Checking", server)

print()

print("===== SERVER NUMBERS =====")

for i in range(1, 6):
    print("Server", i)

print()

count = 1

print("===== HEALTH CHECK =====")

while count <= 5:
    print("Health Check", count)
    count += 1

print()

cpu_usage = [45, 82, 95]

print("===== CPU STATUS =====")

for cpu in cpu_usage:

    if cpu > 90:
        print(cpu, "- Critical")

    elif cpu > 70:
        print(cpu, "- Warning")

    else:
        print(cpu, "- Healthy")
