# Day 24 - Modules

import math
import random
import os
import sys
from datetime import datetime
import subprocess

print("===== MATH MODULE =====")
print("Square Root:", math.sqrt(81))
print("Ceiling:", math.ceil(4.2))
print("Floor:", math.floor(4.9))

print()

print("===== RANDOM MODULE =====")
servers = ["web01", "web02", "db01"]
print("Random Server:", random.choice(servers))

print()

print("===== DATETIME MODULE =====")
print(datetime.now())

print()

print("===== OS MODULE =====")
print("Current Directory:", os.getcwd())
print("Files:", os.listdir())

print()

print("===== SYS MODULE =====")
print(sys.version)

print()

print("===== SUBPROCESS MODULE =====")
subprocess.run(["pwd"])
