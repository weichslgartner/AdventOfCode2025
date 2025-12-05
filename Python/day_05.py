from aoc import input_as_str
from typing import List, Tuple


def parse_input(lines: str) -> Tuple[List[Tuple[int, int]], List[int]]:
    ranges, ids = lines.split("\n\n", maxsplit=1)
    ranges = [tuple(map(int, r.split("-", maxsplit=1))) for r in ranges.splitlines()]
    return ranges, [int(i) for i in ids.splitlines()]


def part_1(ranges: List[Tuple[int, int]], ids: List[int]) -> int:
    fresh_ids = 0
    for i in ids:
        for r in ranges:
            if r[0] <= i <= r[1]:
                fresh_ids += 1
                break
    return fresh_ids


def part_2(ranges: List[Tuple[int, int]]) -> int:
    if len(ranges) < 2:
        return ranges
    ranges.sort()
    merged_ranges = []
    cur = ranges[0]
    for r in ranges[1:]:
        if cur[1] >= r[0]:
            cur = (cur[0], max(cur[1], r[1]))
        else:
            merged_ranges.append(cur)
            cur = r
    merged_ranges.append(cur)
    return sum(r[1] - r[0] + 1 for r in merged_ranges)


def main() -> None:
    lines = input_as_str("input_05.txt")
    ranges, ids = parse_input(lines)
    print("Part 1:", part_1(ranges, ids))
    print("Part 2:", part_2(ranges))


if __name__ == '__main__':
    main()
