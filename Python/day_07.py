from functools import cache
from typing import List, Dict, Set, Tuple

from aoc import get_lines, Point


def parse_input(lines: List[str]) -> Tuple[Point, int, Dict[int, Set[int]]]:
    return (Point(x=lines[0].find('S'), y=0), len(lines),
            {y: {x for x, c in enumerate(line) if c == "^"}
             for y, line in enumerate(lines) if any(c == "^" for c in line)})


def part_1(start: Point, splitters: Dict[int, Set[int]]) -> int:
    cur = {start.x}
    total_splits = 0
    for s in splitters.values():
        splits = cur & s
        cur = (cur - splits) | {n for x in splits for n in (x + 1, x - 1)}
        total_splits += len(splits)
    return total_splits


def part_2(start: Point, y_max: int, splitters: Dict[int, Set[int]]) -> int:
    @cache
    def dfs(p: Point) -> int:
        if p.y >= y_max:
            return 1
        if p.x in splitters.get(p.y, set()):
            return dfs(Point(x=p.x - 1, y=p.y + 1)) + dfs(Point(x=p.x + 1, y=p.y + 1))
        return dfs(Point(p.x, p.y + 1))
    return dfs(start)


def main():
    lines = get_lines("input_07.txt")
    start, y_max, splitters = parse_input(lines)
    print("Part 1:", part_1(start, splitters))
    print("Part 2:", part_2(start, y_max, splitters))


if __name__ == '__main__':
    main()
