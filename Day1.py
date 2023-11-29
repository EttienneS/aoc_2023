from Base import Base


class Day1(Base):
    def __init__(self) -> None:
        super().__init__("Day1")

    def part1(self):
        print(f"{self.name} part1 2")
        print(super().read_input_as_lines())
