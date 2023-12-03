from Base import Base


class Day2(Base):
    def __init__(self) -> None:
        super().__init__("Day2")

    def part1(self):
        print("Part1")

        limits = {"red": 12, "green": 13, "blue": 14}
        limit_total = 39

        total = 0
        for line in self.read_input_as_lines():
            parts = line.split(":")
            gameId = int(parts[0].split(" ")[1])

            possible = True
            for game in parts[1].split(";"):
                game_limits = limits.copy()
                total_plays = limit_total

                plays = [play.strip() for play in game.split(",")]
                for play in plays:
                    play_parts = play.split(" ")
                    num = int(play_parts[0])
                    col = play_parts[1]

                    game_limits[col] -= num
                    total_plays -= num

                if any(game_limits[key] < 0 for key in game_limits):
                    possible = False
                    break

                if total_plays < 0:
                    possible = False
                    break

            if possible:
                total += gameId

        print("Answer: ", total)

    def part2(self):
        print("Part2")

        totalPower = 0
        for line in self.read_input_as_lines():
            parts = line.split(":")

            gameMin = {}
            for game in parts[1].split(";"):
                plays = [play.strip() for play in game.split(",")]
                for play in plays:
                    play_parts = play.split(" ")
                    num = int(play_parts[0])
                    col = play_parts[1]

                    if col not in gameMin or gameMin[col] < num:
                        gameMin[col] = num

            power = 1
            for item in gameMin:
                power *= gameMin[item]

            totalPower += power

        print("Answer: ", totalPower)
