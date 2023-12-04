import time

from Day4 import Day4

start_time = time.time()

day = Day4()

day.part1()

print("--- Part 1: %s ms ---" % ((time.time() - start_time) * 1000))
start_time = time.time()

day.part2()

print("--- Part 2: %s ms ---" % ((time.time() - start_time) * 1000))
