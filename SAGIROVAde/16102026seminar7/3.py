"""Task3. Gazzetique"""
import sys
from collections import Counter

input_data = """6
Белое солнце пустыни
Бриллиантовая рука
Белое солнце пустыни
Белое солнце пустыни
Гараж
Бриллиантовая рука
"""

lines = input_data.splitlines()
n = int(lines[0].strip())

counter = Counter()
for i in range(1, n + 1):
    name = lines[i].strip()
    counter[name] += 1

for name, votes in sorted(counter.items(), key=lambda kv: (-kv[1], kv[0])):
    print(name, votes)