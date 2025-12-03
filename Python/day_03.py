from bisect import bisect_right
from collections import defaultdict
from typing import List, Dict, Optional, Tuple

from aoc import get_lines

JoltDict = Tuple[Dict[int, List[int]], int]


def parse_input(lines: List[str]) -> List[JoltDict]:
    battery_list = []
    for line in lines:
        batteries = defaultdict(list)
        for i, c in enumerate(line):
            batteries[int(c)].append(i)
        battery_list.append((dict(sorted(batteries.items(), reverse=True)), len(line)))
    return battery_list


def find_max_jolt_recursive(batteries_w_l: JoltDict, current_number: int, last_idx: int, length: int,
                            acc: int) -> Optional[int]:
    batteries, max_len = batteries_w_l
    if length == 0:
        return acc + current_number
    # additional pruning
    if length > max_len - last_idx:
        return None
    for key, val in batteries.items():
        i = bisect_right(val, last_idx)
        if (i < len(val) and
                (res := find_max_jolt_recursive(batteries_w_l, key, val[i], length - 1, (acc + current_number) * 10))):
            return res
    return None


def find_max_jolt(batteries: JoltDict, length: int = 2) -> int:
    for k, v in batteries[0].items():
        if res := find_max_jolt_recursive(batteries, k, v[0], length - 1, 0):
            return res


def part_1(batteries: List[JoltDict]) -> int:
    return sum(find_max_jolt(b, 2) for b in batteries)


def part_2(batteries: List[JoltDict]) -> int:
    return sum(find_max_jolt(b, 12) for b in batteries)


def main():
    lines = get_lines("input_03.txt")
    batteries = parse_input(lines)
    print("Part 1:", part_1(batteries))
    print("Part 2:", part_2(batteries))


if __name__ == '__main__':
    main()
