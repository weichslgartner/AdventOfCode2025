from typing import Set, List

from aoc import get_lines, Point, get_neighbours_8_no_filter, parse_grid


def parse_input(lines: List[str]) -> Set[Point]:
    return parse_grid(lines, symbol='@')


def part_1(rolls: Set[Point]) -> int:
    return sum(map(lambda roll: len(get_neighbours_8_no_filter(roll) & rolls) < 4, rolls))


def part_2(rolls: Set[Point]) -> int:
    cnt = 0
    while True:
        to_remove = {roll for roll in rolls if len(get_neighbours_8_no_filter(roll) & rolls) < 4}
        if len(to_remove) == 0:
            return cnt
        cnt += len(to_remove)
        rolls -= to_remove


def main():
    lines = get_lines("input_04.txt")
    rolls = parse_input(lines)
    print("Part 1:", part_1(rolls))
    print("Part 2:", part_2(rolls))


if __name__ == '__main__':
    main()
