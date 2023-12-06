import sys
from Base import Base


class Day6(Base):
    def __init__(self) -> None:
        super().__init__("Day6")

    def part1(self):
        print("Part1")
        lines = self.read_input_as_lines()
        durations = [int(time) for time in lines[0].split()[1:]]
        targets = [int(time) for time in lines[1].split()[1:]]

        total_wins = []

        for i, duration in enumerate(durations):
            target = targets[i]

            wins = []
            for x in range(1, duration):
                result = x * (duration - x)
                if (result > target):
                    wins.append(x)

            total_wins.append(len(wins))

        total = 1
        for win in total_wins:
            total *= win

        print(f"Answer: {total}")

    def part2(self):
        print("Part2")
        lines = self.read_input_as_lines()
        duration = int(lines[0].split(":")[1].replace(" ", ""))
        target = int(lines[1].split(":")[1].replace(" ", ""))

        wins = []
        for x in range(1, duration):
            result = x * (duration - x)
            if (x % 100000 == 0):
                print(f"working... ({x}/{duration})")

            if (result > target):
                wins.append(x)

        print(f"Answer: {len(wins)}")
