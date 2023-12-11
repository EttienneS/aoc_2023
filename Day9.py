from Base import Base
from typing import List


class Day9(Base):
    def __init__(self) -> None:
        super().__init__("Day9")

    def part1(self):
        print("Part1")

        total = 0
        for line in self.read_input_as_lines():
            sequences = self.get_sequences(line)
            last = 0
            for seq in sequences[1:]:
                last += seq[-1]

            print(last)
            total += last

        print(f"Answer: {total}")

    def part2(self):
        print("Part2")

        total = 0

        for line in self.read_input_as_lines():
            sequences = self.get_sequences(line)
            prev = 0

            for i in range(0, len(sequences) - 1):
                prev = sequences[i + 1][0] - prev

            total += prev

        print(f"Answer: {total}")

    def get_sequences(self, line):
        sequences = []
        current = 0

        sequences.append([int(part) for part in line.split()])

        while not all(num == 0 for num in sequences[current]):
            nextSeq = self.get_next_sequence(sequences[current])
            sequences.append(nextSeq)
            current += 1

        sequences.reverse()
        return sequences

    def get_next_sequence(self, sequence) -> List:
        next_seq = []
        length = len(sequence) - 1
        for i, num in enumerate(sequence):
            if i < length:
                next_seq.append(sequence[i + 1] - num)

        return next_seq
