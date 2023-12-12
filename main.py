import time

from Day10 import Day10

start_time = time.time()

day = Day10()

day.part1()

print(f"======== {day.name} ========")
print()
print("--- Part 1: %s ms ---" % ((time.time() - start_time) * 1000))
start_time = time.time()

day.part2()

print("--- Part 2: %s ms ---" % ((time.time() - start_time) * 1000))
print(f"======== {day.name} ========")
