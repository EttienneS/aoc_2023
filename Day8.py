import math
from Base import Base


class Day8(Base):
    def __init__(self) -> None:
        super().__init__("Day8")

    def part1(self):
        print("Part1")

        lines = self.read_input_as_lines()
        directions = lines[0]
        nodes = self.get_nodes(lines)

        current = "AAA"
        target = "ZZZ"
        steps = 0

        while current != target:
            for direction in directions:
                steps += 1
                current = nodes[current][direction]

                if current == target:
                    break

        print(f"Found path in {steps} steps")

    def part2(self):
        print("Part2")

        lines = self.read_input_as_lines()
        directions = lines[0]
        nodes = self.get_nodes(lines)

        currents = [node for node in nodes if node.endswith("A")]

        loops = []
        for current in currents:
            loop_steps = 0

            found = False
            while not found:
                for direction in directions:
                    loop_steps += 1
                    current = nodes[current][direction]

                    if current.endswith("Z"):
                        found = True
                        break

            loops.append(loop_steps)

        # this problem is a trick, each chain is a circle, so you only need to solve it once
        # then you find the lowest common multiplier (LCM/LCD) for the chains (which python just does for us)
        # that answer is then how many loops would need to be completed, its one of those problems
        # that is not really solvable unless you already know of that type of solution
        lcm = math.lcm(*loops)
        print(f"Found path in {lcm} steps")

    def get_nodes(self, lines):
        nodes = {}
        for node in lines[2:]:
            parts = node.split("=")
            key = parts[0].strip()
            values = parts[1].replace("(", "").replace(")", "").replace(",", "").split()

            nodes[key] = {"L": values[0], "R": values[1]}
        return nodes
