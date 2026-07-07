# Day 21 - Decision Making

server_name = "web01"

cpu = 72

memory = 85

disk = 91

print("===== SERVER HEALTH =====")
print("Server:", server_name)

if cpu > 80:
    print("CPU Status : High")
else:
    print("CPU Status : Normal")

if memory > 80:
    print("Memory Status : Warning")
else:
    print("Memory Status : Normal")

if disk > 90:
    print("Disk Status : Critical")
else:
    print("Disk Status : Healthy")
