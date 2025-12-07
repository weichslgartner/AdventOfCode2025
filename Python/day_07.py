from collections import defaultdict
from functools import cache
from typing import List, Dict, Set, Tuple

from aoc import get_lines, Point


def parse_input(lines: List[str]) -> Tuple[Point, int, Dict[int, Set[int]]]:
    start = None
    splitters: Dict[int, Set[int]] = defaultdict(set)
    y_max = 0
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "S":
                start = Point(x, y)
            elif c == "^":
                splitters[y].add(x)
        y_max = max(y, y_max)
    return start, y_max, splitters


def part_1(start: Point, splitters: Dict[int, Set[int]]) -> int:
    cur = {start.x}
    total_splits = 0
    for s in splitters.values():
        splits = cur.intersection(s)
        total_splits += len(splits)
        cur -= splits
        for x in splits:
            if (left := x + 1) not in s:
                cur.add(left)
            if (right := x - 1) not in s:
                cur.add(right)
    return total_splits


def part_2(start: Point, y_max: int, splitters: Dict[int, Set[int]]) -> int:
    @cache
    def dfs(p: Point) -> int:
        if p.y >= y_max:
            return 1
        if p.x in splitters.get(p.y, set()):
            res = 0
            if (p.x - 1) not in splitters[p.y]:
                res += dfs(Point(x=p.x - 1, y=p.y + 1))
            if (p.x + 1) not in splitters[p.y]:
                res += dfs(Point(x=p.x + 1, y=p.y + 1))
            return res
        return dfs(Point(p.x, p.y + 1))
    return dfs(start)


def main():
    lines = get_lines("input_07.txt")
    start, y_max, splitters = parse_input(lines)
    print("Part 1:", part_1(start, splitters))
    print("Part 2:", part_2(start, y_max, splitters))


if __name__ == '__main__':
    main()
