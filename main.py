import time

from Day3 import Day3

start_time = time.time()

day = Day3()

day.part1()

print("--- Part 1: %s ms ---" % ((time.time() - start_time) * 1000))
start_time = time.time()

day.part2()

print("--- Part 2: %s ms ---" % ((time.time() - start_time) * 1000))
