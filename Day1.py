from Base import Base


class Day1(Base):
    def __init__(self) -> None:
        super().__init__("Day1")

    def part1(self):
        print(f"{self.name} part1")
        print(super().read_input_as_lines())

    def part2(self):
        print(f"{self.name} part2")
        print(super().read_input_as_int_array("2"))
