from typing import List, Dict, Optional
from collections import defaultdict
import heapq

from aoc import get_lines


JoltDict = Dict[int, List[int]]


def parse_input(lines: List[str]) -> List[JoltDict]:
    dics = []
    for line in lines:
        dic = defaultdict(list)
        for i, c in enumerate(line):
            heapq.heappush(dic[int(c)], i)
        dics.append(dict(sorted(dic.items(), reverse=True)))
    return dics


def find_max_jolt_recursive(dic: JoltDict, current_number: int, used: List[int], length: int, acc: int) \
        -> Optional[int]:
    if length == 0:
        return acc + current_number
    for key, val in dic.items():
        for v in val:
            if v > used[-1]:
                used.append(v)
                if res := find_max_jolt_recursive(dic, key, used, length - 1, (acc + current_number) * 10):
                    return res
                used.pop()
    return None


def find_max_jolt(dic: JoltDict, length: int = 1) -> int:
    for k, v in dic.items():
        if res := find_max_jolt_recursive(dic, k, [v[0]], length, 0):
            return res


def part_1(dics: List[JoltDict]) -> int:
    return sum(map(find_max_jolt, dics))


def part_2(dics: List[JoltDict]) -> int:
    return sum(find_max_jolt(d, 11) for d in dics)


def main():
    lines = get_lines("input_03.txt")
    dics = parse_input(lines)
    print("Part 1:", part_1(dics))
    print("Part 2:", part_2(dics))


if __name__ == '__main__':
    main()
