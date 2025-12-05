from aoc import input_as_str
from typing import List, Tuple


def parse_input(lines: str) -> Tuple[List[Tuple[int, ...]], List[int]]:
    ranges, ids = lines.split("\n\n", maxsplit=1)
    return (sorted([tuple(map(int, r.split("-", maxsplit=1))) for r in ranges.splitlines()]),
            [int(i) for i in ids.splitlines()])


def part_1(ranges: List[Tuple[int, ...]], ids: List[int]) -> int:
    return sum(any(r[0] <= i <= r[1] for r in ranges) for i in ids)


def part_2(ranges: List[Tuple[int, ...]]) -> int:
    # we assume ranges are sorted and len(ranges) > 1
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
