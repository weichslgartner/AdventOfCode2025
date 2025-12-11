from collections import defaultdict
from functools import cache
from typing import List, DefaultDict

from aoc import get_lines


def parse_input(lines: List[str]) -> DefaultDict[str, List[str]]:
    graph = defaultdict(list)
    for line in lines:
        parent, children = line.split(": ", maxsplit=1)
        for child in children.split():
            graph[parent].append(child)
    return graph


def part_1(graph: DefaultDict[str, List[str]]) -> int:
    @cache
    def dfs(node):
        if node == "out":
            return 1
        return sum(dfs(child) for child in graph[node])
    return dfs("you")


def part_2(graph: DefaultDict[str, List[str]]) -> int:
    @cache
    def dfs(node, fft, dac):
        if node == "out" and fft and dac:
            return 1
        if node == "fft":
            fft = True
        if node == "dac":
            dac = True
        return sum(dfs(child, fft, dac) for child in graph[node])
    return dfs("svr", False, False)


def main() -> None:
    lines = get_lines("input_11.txt")
    graph = parse_input(lines)
    print("Part 1:", part_1(graph))
    print("Part 2:", part_2(graph))


if __name__ == "__main__":
    main()
