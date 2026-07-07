# Day 25 - File Handling

from datetime import datetime

# Write to hello.txt
with open("04-python-automation/reports/hello.txt", "w") as file:
    file.write("Hello Cloud Engineer")

# Append to hello.txt
with open("04-python-automation/reports/hello.txt", "a") as file:
    file.write("\nPython Automation")

# Read hello.txt
with open("04-python-automation/reports/hello.txt", "r") as file:
    print(file.read())

# Read server list
print("\n===== SERVERS =====")

with open("04-python-automation/reports/servers.txt", "w") as file:
    for server in file:
        print(server.strip())

# Create a monitoring report
with open("04-python-automation/reports/server_report.txt", "w") as file:

    file.write("===== SERVER REPORT =====\n")
    file.write(f"Generated: {datetime.now()}\n")
    file.write("CPU Usage: 72%\n")
    file.write("Memory Usage: 65%\n")
    file.write("Disk Usage: 81%\n")

print("\nServer report generated successfully.")
