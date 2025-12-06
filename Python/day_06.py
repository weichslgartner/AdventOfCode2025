from functools import reduce
from operator import add, imul
from typing import List, Callable, Tuple

from aoc import get_lines

OperatorFunc = Callable[[int, int], int]


def parse_input(lines: List[str]) -> Tuple[List[List[int]], List[List[int]], List[OperatorFunc]]:
    ops = {"*": imul, "+": add}
    split_lines = [line.split() for line in lines[:-1]]
    numbers_part1 = [[int(cols[i]) for cols in split_lines]for i in range(len(split_lines[0]))]
    numbers_part2 = []
    cur_list = []
    for idx in range(len(lines[0]) - 1, -1, -1):
        cur = 0
        for line in lines[:-1]:
            if line[idx] != " ":
                cur = cur * 10 + int(line[idx])
        if cur != 0:
            cur_list.append(cur)
        else:
            numbers_part2.append(cur_list)
            cur_list = []
    numbers_part2.append(cur_list)
    return numbers_part1, numbers_part2, [ops[c] for c in lines[-1].split()]


def part_1(numbers: List[List[int]], operators: List[OperatorFunc]) -> int:
    return sum(reduce(operators[i], n) for i, n in enumerate(numbers))


def part_2(numbers: List[List[int]], operators: List[OperatorFunc]) -> int:
    return sum(reduce(operators[len(operators) - 1 - i], n) for i, n in enumerate(numbers))


def main() -> None:
    lines = get_lines("input_06.txt")
    numbers_part1, numbers_part2, operators = parse_input(lines)
    print("Part 1:", part_1(numbers_part1, operators))
    print("Part 2:", part_2(numbers_part2, operators))


if __name__ == '__main__':
    main()
