from Base import Base

types = [
    "HighCard",
    "OnePair",
    "TwoPair",
    "ThreeOfAKind",
    "FullHouse",
    "FourOfAKind",
    "FiveOfAKind",
]


class Day7(Base):
    def __init__(self) -> None:
        super().__init__("Day7")

    def part1(self):
        print("Part1")

        hand_groupings = {}
        ranked_hands = self.get_ranked_hands(
            hand_groupings,
            ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"],
            False,
        )

        total = self.get_total(ranked_hands)

        print(f"Answer: {total}")

    def get_total(self, ranked_hands):
        total = 0
        for i, hand in enumerate(ranked_hands):
            total += hand.bid * (i + 1)
            # print(f"{i+1} {hand.raw} {hand.bid} = {hand.bid * (i+1)} ({hand.type} - {hand.value})")
        return total

    def get_ranked_hands(self, hand_groupings, rank, jokers):
        for line in self.read_input_as_lines():
            raw_hand, raw_bid = line.split()
            hand = Hand(raw_hand, raw_bid, rank, jokers)

            if hand.type in hand_groupings:
                hand_groupings[hand.type].append(hand)
            else:
                hand_groupings[hand.type] = [hand]

        ranked_hands = []
        for type in types:
            if type in hand_groupings:
                ssss = sorted(hand_groupings[type], key=lambda x: x.value)
                for hand in ssss:
                    ranked_hands.append(hand)
        return ranked_hands

    def part2(self):
        print("Part2")
        hand_groupings = {}
        ranked_hands = self.get_ranked_hands(
            hand_groupings,
            ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"],
            True,
        )

        total = self.get_total(ranked_hands)

        print(f"Answer: {total}")


class Hand:
    raw: str = ""
    type: str = ""
    bid: int = -1
    value: int = -1

    def __init__(self, hand: str, bid: str, rank, jokers: bool) -> None:
        self.raw = hand
        self.bid = int(bid)

        temp = {}
        temp_value = ""
        for card in hand:
            temp_value += str(hex(rank.index(card)))
            if card in temp:
                temp[card] += 1
            else:
                temp[card] = 1

        # this is kind of odd but it works, we convert each number based on the rank to the
        # hex equivalent and slap them together, then we turn that back into a number to get
        # a sortable unique 'value' for each hand
        self.value = int(temp_value.replace("0x", ""), 16)

        joker = "J"
        if jokers:
            if joker in temp:
                j_count = temp[joker]
                for card in temp:
                    if card != joker:
                        temp[card] += j_count

        parsed = dict(sorted(temp.items(), key=lambda item: item[1], reverse=True))

        combos = len(parsed)
        first = next(iter(parsed))
        count = parsed[first]

        if count == 5:
            type = types[6]  # "FiveOfAKind"
        elif count == 4:
            type = types[5]  # "FourOfAKind"
        elif count == 3:
            # edge case here, if we have a joker in the mix
            # and the main card of the full house is not the joker
            # then that joker should not be counted as a distinct item
            # as it has already been added to the main combo
            if jokers:
                if first != joker and joker in parsed:
                    combos -= 1

            if combos == 2:
                type = types[4]  # "FullHouse"
            else:
                type = types[3]  # "ThreeOfAKind"
        elif count == 2:
            if combos == 3:
                type = types[2]  # "TwoPair"
            else:
                type = types[1]  # "OnePair"
        else:
            type = types[0]  # "HighCard"

        self.type = type
