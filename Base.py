from typing import List


class Base:
    def __init__(self, name) -> None:
        self.name = name

    def read_input_as_lines(self, part="") -> List[str]:
        file_path = self.get_input_file_for_part(part)

        with open(file_path, "r") as file:
            # Read all lines from the file into a list
            lines = file.readlines()

        return [line.strip() for line in lines]

    def read_input_as_string(self, part="", seperator="") -> str:
        return seperator.join(self.read_input_as_lines(part))

    def read_input_as_int_array(self, part="", split=",") -> List[int]:
        input_strings = self.read_input_as_string(part, seperator=split).split(split)
        return [int(num) for num in input_strings]

    def get_input_file_for_part(self, part):
        file_path = f"Inputs/{self.name}"
        if part != "":
            file_path += f"_{part}.txt"
        else:
            file_path += ".txt"
        return file_path

    def part1(self):
        print("--- PART 1 NOT IMPLEMENTED YET ---")

    def part2(self):
        print("--- PART 2 NOT IMPLEMENTED YET ---")
