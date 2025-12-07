from collections import defaultdict
from typing import List

from aoc import get_lines, Point


def parse_input(lines: List[str]):
    start = None
    splitters = defaultdict(set)
    for y,line in enumerate(lines):
        for x,c in enumerate(line):
            if c == "S":
                start = Point(x,y)
            elif c == "^":
                splitters[y].add(x)
    return start, splitters


def part_1(start, splitters):
    cur = {start.x}
    total_splits = 0
    for s in splitters.values():
        splits = cur.intersection(s)
        total_splits += len(splits)
        cur = cur - splits
       # print(cur)
        for x in splits:
            if (x+1) not in s:
                cur.add(x+1)
            if (x - 1) not in s:
                cur.add(x-1)
        #print(cur)
        for x in range(143):
            if x in s:
                print("^",end="")
            elif x in cur:
                print("|", end="")
            else:
                print(".", end="")
        print()
        for x in range(143):
            if x in cur:
                print("|", end="")
            else:
                print(".", end="")
        print()
    return total_splits


def part_2(lines):

    pass


def main():
    lines = get_lines("input_07.txt") # 1332 too low
    start, splitters = parse_input(lines)
    print("Part 1:", part_1(start, splitters))
    print("Part 2:", part_2(lines))


if __name__ == '__main__':
    main()
