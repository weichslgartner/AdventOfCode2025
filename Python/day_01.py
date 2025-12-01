from operator import add, sub
from functools import reduce
from typing import List, Tuple, Callable

from aoc import get_lines

op_dict = {'R': add, 'L': sub}


def parse_input(lines: List[str]) -> List[Tuple[str, int]]:
    return [(line[0], int(line[1:])) for line in lines]


def count_zeros(numb: int, _) -> int:
    return numb % 100 == 0


def count_zero_crossings(numb: int, numb_old: int) -> int:
    cnt = 1 if numb <= 0 and numb_old != 0 else 0
    cnt += abs(numb) // 100
    return cnt


def solve(rotations: List[Tuple[str, int]], condition: Callable[[int, int], int]) -> int:
    cnt = 0
    numb = 50
    numb_old = numb
    for r, n in rotations:
        numb = reduce(op_dict[r], [numb, n])
        cnt += condition(numb, numb_old)
        numb %= 100
        numb_old = numb
    return cnt


def part_1(rotations: List[Tuple[str, int]]) -> int:
    return solve(rotations, count_zeros)


def part_2(rotations: List[Tuple[str, int]]) -> int:
    return solve(rotations, count_zero_crossings)


def main():
    lines = get_lines("input_01.txt")
    rotations = parse_input(lines)
    print("Part 1:", part_1(rotations))
    print("Part 2:", part_2(rotations))


if __name__ == '__main__':
    main()
