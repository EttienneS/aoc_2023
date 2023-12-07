import time

from Day7 import Day7

start_time = time.time()

day = Day7()

day.part1()

print("--- Part 1: %s ms ---" % ((time.time() - start_time) * 1000))
start_time = time.time()

day.part2()

print("--- Part 2: %s ms ---" % ((time.time() - start_time) * 1000))
