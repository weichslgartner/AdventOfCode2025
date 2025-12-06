from functools import reduce

from aoc import get_lines
from operator import add, imul


def parse_input(lines):
    ops = {"*": imul, "+": add}
    numbers_part1 = [[] for _ in range(len(lines[0].split()))]
    numbers_part2 = []
    cur_list = []
    for idx in range(len(lines[0])-1,-1,-1):
        cur = 0
        for l in lines[:-1]:
            if l[idx] != " ":
                cur = cur*10 + int(l[idx])
        if cur != 0:
            cur_list.append(cur)
        else:
            numbers_part2.append(cur_list)
            cur_list = []
    numbers_part2.append(cur_list)
    [[numbers_part1[i].append(int(c)) for i, c in enumerate(line.split())] for line in lines[:-1]],
    return numbers_part1,numbers_part2, [ops[c] for c in lines[-1].split()]


def part_1(numbers, operators):
    return sum(reduce(operators[i], n) for i, n in enumerate(numbers))


def part_2(numbers, operators):
    return sum(reduce(operators[len(operators)-1-i], n) for i, n in enumerate(numbers))


def main():
    lines = get_lines("input_06.txt")
    numbers_part1,numbers_part2, operators = parse_input(lines)
    print("Part 1:", part_1(numbers_part1, operators))
    print("Part 2:", part_2(numbers_part2, operators))


if __name__ == '__main__':
    main()
