import sys
from Base import Base


class Day5(Base):
    def __init__(self) -> None:
        super().__init__("Day5")

    def part1(self):
        print("Part1")
        lines = self.read_input_as_lines()
        seeds = [int(part) for part in lines[0].split(":")[1].split()]
        
        ranges = self.parse_ranges(lines)

        smallest = sys.maxsize
        for seed in seeds:
            for step in ranges:
                for value in ranges[step]:
                    if value.inRange(seed):
                        seed = (seed - value.source) + value.dest
                        break
            
            if seed < smallest:
                smallest = seed

        print(f"Answer: {smallest}") 

    def part2(self):
        print("Part2")
        # this takes about 30 mins to complete
        lines = self.read_input_as_lines()
        
        ranges = self.parse_ranges(lines)

        seeds = [int(seed) for seed in lines[0].split(":")[1].split()]

        seed_maps = []
        for i in range(0, len(seeds), 2):
            seed_maps.append({"start": seeds[i], "end": seeds[i] + seeds[i+1]})

        reversed_keys = list(reversed(list(ranges.keys())))

        for value in range(0, sys.maxsize):
            if value % 10000 == 0: print(f"busy {value}")

            location = value
            for key in reversed_keys:
                for r in ranges[key]:
                    if r.inRangeInv(value):
                        value = (value - r.dest) + r.source
                        #print(f"{key} -> {value}")
                        break
                
                #print(f"{key} -> {value}")

            found = False
            for seed_map in seed_maps:
                if value >= seed_map["start"] and value <= seed_map["end"]:
                    print(f"Answer is Location: {location} -> Seed: {value}")
                    found = True
                    break

            if found: break

        print(f"Done")


    def parse_ranges(self, lines):
        ranges = {}
        last = ""
        for line in lines[1:]:
            if line == "": continue

            if ":" in line:
                last = line.split()[0]
                ranges[last] = []
            else:
                ranges[last].append(Range(line))
        return ranges# Actual: 107430936 # Example: 35    

class Range():

    source:int = -1
    dest:int =-1
    size:int =-1

    def __init__(self, line: str) -> None:
        parts = [int(part) for part in line.split()]
        self.dest = parts[0]
        self.source = parts[1]
        self.size = parts[2]

        pass

    def __str__(self) -> str:
        return f"From {self.source}-{self.source+self.size}, To {self.dest}-{self.dest+self.size}"
    
    def inRange(self, value: int):
        return value >= self.source and value < self.source + self.size
    
    def inRangeInv(self, value: int):
        return value >= self.dest and value < self.dest + self.size
    
