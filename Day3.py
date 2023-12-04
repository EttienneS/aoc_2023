from Base import Base


class Day3(Base):
    def __init__(self) -> None:
        super().__init__("Day3")

    def part1(self):
        print("Part1")

        self.parse_and_get_values([], [])

    def parse_and_get_values(self, stars, parts):
        lines = self.read_input_as_lines()
        arr = [list(line.strip()) for line in lines]
        total = 0

        for y, line in enumerate(lines):
            current = ""
            start = -1
            end = -1
            lineParts = []
            lineNumbers = []

            for x, char in enumerate(line):
                if char.isdigit():
                    current += char
                    if start == -1:
                        start = x
                    end = x

                if not char.isdigit() or x == len(line) - 1:
                    found = False
                    if current != "":
                        for ly in range(y - 1, y + 2):
                            if found:
                                break

                            for lx in range(start - 1, end + 2):
                                if (
                                    lx < 0
                                    or ly < 0
                                    or lx >= len(line)
                                    or ly >= len(lines)
                                ):
                                    pass
                                else:
                                    val = arr[ly][lx]

                                    if val != "." and not val.isdigit():
                                        total += int(current)
                                        found = True
                                        lineParts.append({"start": start, "end": end})
                                        parts.append(
                                            {
                                                "start": start,
                                                "end": end,
                                                "line": y,
                                                "value": int(current),
                                            }
                                        )

                                        if val == "*":
                                            star = {"x": lx, "y": ly}
                                            if star not in stars:
                                                stars.append(star)
                                        break

                        if not found:
                            lineNumbers.append({"start": start, "end": end})

                    current = ""
                    start = -1
                    end = -1

            self.pretty_print_line(line, lineParts, lineNumbers)

        print("Part total:", total)

    def pretty_print_line(self, line, foundParts, foundNumbers):
        printLine = ""

        for cx, c in enumerate(line):
            found = False
            for num in foundNumbers:
                if cx >= num["start"] and cx <= num["end"]:
                    printLine += f"\033[91m{c}\033[0m"
                    found = True

            for part in foundParts:
                if cx >= part["start"] and cx <= part["end"]:
                    printLine += f"\033[92m{c}\033[0m"
                    found = True

            if c == "*":
                printLine += f"\033[93m{c}\033[0m"
                found = True

            if not found:
                printLine += c

        print(printLine)

    def part2(self):
        print("Part2")

        stars = []
        parts = []

        self.parse_and_get_values(stars, parts)

        total = 0

        for star in stars:
            comps = []
            star_x = star["x"]
            star_y = star["y"]

            for part in parts:
                start = part["start"]
                end = part["end"]
                part_y = part["line"]

                for x in range(-1, 2):
                    found = False
                    for y in range(-1, 2):
                        if (
                            start + x == star_x or end + x == star_x
                        ) and part_y + y == star_y:
                            comps.append(part)
                            found = True
                            break

                    if found:
                        break

            if len(comps) > 1:
                print("Found", comps[0]["value"], comps[1]["value"], ":", star)
                total += comps[0]["value"] * comps[1]["value"]

        print("Answer: ", total)
