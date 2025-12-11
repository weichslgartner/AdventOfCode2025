from collections import defaultdict
from aoc import get_lines


def parse_input(lines):
    graph = defaultdict(list)
    for line in lines:
        parent, children = line.split(": ",maxsplit=1)
        for child in children.split(" "):
            graph[parent].append(child)
    return graph

def dfs(node, graph):
    if node == "out":
        return 1
    res = 0
    for child in graph[node]:
        res += dfs(child, graph)
    return res

def part_1(graph):
    return dfs("you", graph)



def part_2(graph):
    from functools import cache
    @cache
    def dfs_part2(node, fft, dac ):
        if node == "out" and fft and dac:
            return 1
        if node == "fft":
            fft = True
        if node == "dac":
            dac = True
        res = 0
        for child in graph[node]:
            res += dfs_part2(child, fft, dac)
        return res

    return dfs_part2("svr", False, False)


def main():
    lines = get_lines("input_11.txt")
    graph = parse_input(lines)
    print("Part 1:", part_1(graph))
    print("Part 2:", part_2(graph))


if __name__ == '__main__':
    main()
