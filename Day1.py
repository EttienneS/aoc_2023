from Base import Base


class Day1(Base):
    def __init__(self) -> None:
        super().__init__("Day1")

    def part1(self):
        lines = self.read_input_as_lines()
        self.parse_lines(lines)

    def parse_lines(self, lines):
        answer = 0
        for line in lines:
            first = ""
            last = ""
            for char in line:
                try:
                    int(char)
                    if first == "":
                        first = char
                    last = char
                except ValueError:
                    pass
            # print(first + last)
            answer += int(first + last)

        print(answer)

    def part2(self):
        # some inputs use letterss from the first number to make the second number
        # for example eightwo so just blindly replacing all the words with numbers and reusing part 1 wont work
        # while this is a bit more initial data massaging it only has to happen for all lines
        options = {
            "one": "o1e",
            "two": "t2o",
            "three": "t3e",
            "four": "f4r",
            "five": "f5e",
            "six": "s6x",
            "seven": "s7n",
            "eight": "e8t",
            "nine": "n9e",
        }

        lines = []

        for line in self.read_input_as_lines():
            for opt in options:
                line = line.replace(opt, options[opt])
            lines.append(line)

        self.parse_lines(lines)

    def part2_alt(self):
        # this is slower as it has to search each line twice for each option and has more options
        # so this does ~19 left to right and then another 19 right to left per line (1000 lines * 38 search = 38000)
        options = {
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9,
        }

        for x in range(0, 10):
            options[str(x)] = x

        answer = 0
        for line in self.read_input_as_lines():
            firstIndex = 999
            lastIndex = -999
            first = 0
            last = 0

            for option in options:
                try:
                    # search from the front to find the first index
                    optFirst = line.index(option)
                    if optFirst < firstIndex:
                        first = options[option]
                        firstIndex = optFirst

                    # search from the back to find the last index of the thing (in case there is more than one)
                    optLast = line.rindex(option)
                    if optLast > lastIndex:
                        last = options[option]
                        lastIndex = optLast
                except ValueError:
                    # if the item does not exist at all skip and go to the next
                    pass

            value = str(first) + str(last)
            # print(line + ": " + value)
            answer += int(value)
        print(answer)
