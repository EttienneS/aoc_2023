from Base import Base


class Day4(Base):
    def __init__(self) -> None:
        super().__init__("Day4")

    def part1(self):
        print("Part1")
        cards = [Card(line) for line in self.read_input_as_lines()]

        total = 0
        for card in cards:
            total += card.getValue()

        print("Total:", total)

    def part2(self):
        print("Part2")
        cards = [Card(line) for i, line in enumerate(self.read_input_as_lines())]

        card_lookup = {}

        for i, card in enumerate(cards):
            card_lookup[i] = 1

        for card in cards:
            card_total = card_lookup[card.id - 1]
            wins = card.getWins()

            print(f"Card {card.id} has {wins} x {card_total}")
            for win in range(0, card.getWins()):
                index = card.id + win

                if index in card_lookup:
                    card_lookup[index] += card_total
                    print(f"Add {card_total}x {index} cards")
                else:
                    print("Skip", index)

        total = 0
        for lookup in card_lookup:
            total += card_lookup[lookup]

        print("Answer:", total)


class Card:
    id: -1
    winning_numbers = []
    current_numbers = []
    counter: 1

    def __init__(self, line) -> None:
        split1 = line.split(":")
        self.id = int(split1[0].split()[1].strip())
        split2 = [part.strip() for part in split1[1].replace("  ", " ").split("|")]

        self.winning_numbers = [int(num.strip()) for num in split2[0].split()]
        self.current_numbers = [int(num.strip()) for num in split2[1].split()]

    def __str__(self):
        return f"Card {self.id}: {self.winning_numbers} | {self.current_numbers}"

    def getValue(self) -> int:
        value = 0
        for current in self.current_numbers:
            if current in self.winning_numbers:
                if value == 0:
                    value = 1
                else:
                    value *= 2

        return value

    def getWins(self) -> []:
        value = 0
        for current in self.current_numbers:
            if current in self.winning_numbers:
                value += 1

        return value
