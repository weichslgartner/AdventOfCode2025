from aoc import input_as_str
from itertools import combinations


def parse_input(lines):
    ranges, ids = lines.split("\n\n", maxsplit=1)
    ranges = [tuple(map(int, r.split("-", maxsplit=1))) for r in ranges.splitlines()]
    return ranges, [int(i) for i in ids.splitlines()]


def part_1(ranges, ids):
    fresh_ids = 0
    for i in ids:
        for r in ranges:
            if r[0] <= i <= r[1]:
                fresh_ids += 1
                break
    return fresh_ids


def do_overlap(range1, range2):
    return range1[0] <= range2[1] and range2[0] <= range1[1]


def part_2(ranges):
    if len(ranges) < 2:
        return ranges
    ranges.sort()
    merged_ranges = []
    cur = ranges[0]
    for r in ranges[1:]:
        if do_overlap(cur, r):
            cur = (cur[0], max(cur[1], r[1]))
        else:
            merged_ranges.append(cur)
            cur = r
    merged_ranges.append(cur)
    return sum(r[1] - r[0] + 1 for r in merged_ranges)


def main():
    lines = input_as_str("input_05.txt")
    ranges, ids = parse_input(lines)
    print("Part 1:", part_1(ranges, ids))
    print("Part 2:", part_2(ranges))


if __name__ == '__main__':
    main()
