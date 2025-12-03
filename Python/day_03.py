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


def find_max_jolt_recursive(batteries_w_len: JoltDict, current_number: int, used: List[int], length: int,
                            acc: int) -> Optional[int]:
    batteries, max_len = batteries_w_len
    if length == 0:
        return acc + current_number
    # additional pruning
    if length > max_len - used[-1]:
        return None
    for key, val in batteries.items():
        for v in val:
            if v > used[-1]:
                used.append(v)
                if res := find_max_jolt_recursive(batteries_w_len, key, used, length - 1, (acc + current_number) * 10):
                    return res
                used.pop()
    return None


def find_max_jolt(batteries: JoltDict, length: int = 2) -> int:
    for k, v in batteries[0].items():
        if res := find_max_jolt_recursive(batteries, k, [v[0]], length - 1, 0):
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
