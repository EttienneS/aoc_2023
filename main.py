import time

from Day9 import Day9

start_time = time.time()

day = Day9()

day.part1()

print(f"======== {day.name} ========")
print()
print("--- Part 1: %s ms ---" % ((time.time() - start_time) * 1000))
start_time = time.time()

day.part2()

print("--- Part 2: %s ms ---" % ((time.time() - start_time) * 1000))
print(f"======== {day.name} ========")
