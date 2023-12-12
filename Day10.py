from Base import Base


class Day10(Base):
    pipe_map = []
    miny: int = -1
    maxy: int = -1
    minx: int = -1
    maxx: int = -1

    startx: int = -1
    starty: int = -1

    def __init__(self) -> None:
        super().__init__("Day10")

        self.load_map()

    def load_map(self):
        for y, line in enumerate(self.read_input_as_lines()):
            row = []

            for x, char in enumerate(line):
                row.append(Cell(x, y, char))

            self.pipe_map.append(row)

        self.miny = 0
        self.maxy = len(self.pipe_map)
        self.minx = 0
        self.maxx = len(self.pipe_map[0])

        for row in self.pipe_map:
            for cell in row:
                type = cell.type

                if type == "|":
                    # | is a vertical pipe connecting north and south.
                    self.add_north(cell)
                    self.add_south(cell)
                elif type == "-":
                    # - is a horizontal pipe connecting east and west.
                    self.add_west(cell)
                    self.add_east(cell)
                elif type == "L":
                    # L is a 90-degree bend connecting north and east.
                    self.add_north(cell)
                    self.add_east(cell)
                elif type == "J":
                    # J is a 90-degree bend connecting north and west.
                    self.add_north(cell)
                    self.add_west(cell)
                elif type == "7":
                    # 7 is a 90-degree bend connecting south and west.
                    self.add_south(cell)
                    self.add_west(cell)
                elif type == "F":
                    # F is a 90-degree bend connecting south and east.
                    self.add_south(cell)
                    self.add_east(cell)
                elif type == ".":
                    # . is ground; there is no pipe in this tile.
                    pass
                else:
                    # S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
                    self.startx = cell.x
                    self.starty = cell.y
                    cell.value = 0

    def part1(self):
        print("Part1")

        start = self.pipe_map[self.starty][self.startx]

        frontier = start.links
        step = 1

        # there are 19670 cells
        while len(frontier) > 0:
            next_frontier = {}
            for cell in frontier:
                cell.value = step
                cell.closed = True

                for link in cell.links:
                    if not link.closed and link not in next_frontier:
                        next_frontier[link] = True
            step += 1

            if len(next_frontier) == 0:
                break
            else:
                frontier = next_frontier.keys()

            # if step % 100 == 0:
            #    self.print_map(use_val=True)

        print(f"Answer: {step - 1}")

    def print_map(self, use_val: bool):
        for row in self.pipe_map:
            if use_val:
                line = "".join(
                    ["_" if cell.value < 0 else str(cell.value)[-1] for cell in row]
                )
                print(line)
            else:
                print("".join([f"{cell.type}" for cell in row]))

    def add_east(self, cell):
        if cell.x + 1 < self.maxx:
            self.link_cells(cell.x, cell.y, cell.x + 1, cell.y)

    def add_west(self, cell):
        if cell.x - 1 >= self.minx:
            self.link_cells(cell.x, cell.y, cell.x - 1, cell.y)

    def add_south(self, cell):
        if cell.y + 1 < self.maxy:
            self.link_cells(cell.x, cell.y, cell.x, cell.y + 1)

    def add_north(self, cell):
        if cell.y - 1 >= self.miny:
            self.link_cells(cell.x, cell.y, cell.x, cell.y - 1)

    def link_cells(self, sx, sy, tx, ty):
        source = self.pipe_map[sy][sx]
        target = self.pipe_map[ty][tx]
        if target not in source.links:
            source.links.append(target)

        if source not in target.links:
            target.links.append(source)

    def part2(self):
        print("Part2")

        total = 0
        Cell.links
        print(f"Answer: {total}")


class Cell:
    x: int = -1
    y: int = -1

    links = []
    type: str = ""
    value = -1
    closed = False

    def __init__(self, x, y, type) -> None:
        self.x = x
        self.y = y
        self.type = type
        self.links = []
        self.value = -1
        self.closed = False
        pass

    def __str__(self) -> str:
        return f"{self.x}:{self.y} {self.type} {self.value}"
