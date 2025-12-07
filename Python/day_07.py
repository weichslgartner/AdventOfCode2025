from collections import defaultdict
from functools import cache
from typing import List

from aoc import get_lines, Point

y_max = 0
splitters = defaultdict(set)


def parse_input(lines: List[str]):
    global y_max, splitters
    start = None
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "S":
                start = Point(x, y)
            elif c == "^":
                splitters[y].add(x)
        y_max = max(y, y_max)
    return start, splitters


def part_1(start):
    global splitters
    cur = {start.x}
    total_splits = 0
    for s in splitters.values():
        splits = cur.intersection(s)
        total_splits += len(splits)
        cur = cur - splits
        for x in splits:
            if (left := x + 1) not in s:
                cur.add(left)
            if (right := x - 1) not in s:
                cur.add(right)
    return total_splits


@cache
def dfs(p: Point) -> int:
    if p.y >= y_max:
        return 1
    if p.x in splitters[p.y]:
        res = 0
        if (p.x - 1) not in splitters[p.y]:
            res += dfs(Point(x=p.x - 1, y=p.y + 1))
        if (p.x + 1) not in splitters[p.y]:
            res += dfs(Point(x=p.x + 1, y=p.y + 1))
        return res
    return dfs(Point(p.x, p.y + 1))


def part_2(start):
    return dfs(start)


def main():
    lines = get_lines("input_07.txt")  # 1332 too low
    start = parse_input(lines)
    print("Part 1:", part_1(start))
    print("Part 2:", part_2(start))


if __name__ == '__main__':
    main()
