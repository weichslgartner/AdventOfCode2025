from aoc import get_lines
from collections import defaultdict


def parse_input(lines):
    dics = []
    for line in lines:
        dic = defaultdict(list)
        for i, c in enumerate(line):
            dic[int(c)].append(i)
            dic[int(c)].sort()
        dics.append(dict(sorted(dic.items(), reverse=True)))
    return dics


def find_max_jolt_recursive(dic, current_number, used, length, acc):
    if length == 0:
        return acc + current_number
    for key, val in dic.items():
        for v in val:
            if v > used[-1]:
                used.append(v)
                if res := find_max_jolt_recursive(dic, key, used, length - 1, (acc + current_number) * 10):
                    return res
                if used[-1] == v:
                    del used[-1]
    return None


def find_max_jolt(dic, length=1):
    for k, v in dic.items():
        if res := find_max_jolt_recursive(dic, k, [v[0]], length, 0):
            return res


def part_1(dics):
    return sum(map(find_max_jolt, dics))


def part_2(dics):
    return sum(find_max_jolt(d, 11) for d in dics)


def main():
    lines = get_lines("input_03.txt")
    dics = parse_input(lines)
    print("Part 1:", part_1(dics))
    print("Part 2:", part_2(dics))


if __name__ == '__main__':
    main()
