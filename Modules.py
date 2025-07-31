# 🔹 Types of Modules:
# Built-in Modules – come with Python (math, os, random, datetime, etc.)

# User-defined Modules – your own Python files

# Third-party Modules – installed via pip (requests, numpy, pandas, etc.)

import math
import random
import datetime
import os as system
from math import sqrt, pi
import requests

print(math.pi)
print(math.factorial(5))
print(random.choice(["1", "2", "3"]))
print(datetime.datetime.now())
print(datetime.date(2000, 11, 28))


response = requests.get("https://api.github.com")
print(response.status_code)
print(response.json())
