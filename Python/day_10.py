from typing import List, Tuple
from aoc import get_lines
from z3 import Int, Optimize, sat
from collections import deque


def parse_input(
    lines: List[str],
) -> Tuple[List[Tuple[bool, ...]], List[List[List[int]]], List[List[int]]]:
    lights_diagram = []
    wirings = []
    joltage_reqs = []
    for line in lines:
        wiring = []
        for token in line.split():
            if "[" in token and "]" in token:
                lights_diagram.append(tuple(x == "#" for x in token[1:-1]))
            elif "(" in token:
                wiring.append([int(x) for x in token[1:-1].split(",")])
            else:
                wirings.append(wiring)
                joltage_reqs.append([int(x) for x in token[1:-1].split(",")])
    return lights_diagram, wirings, joltage_reqs


def part_1(
    lights_diagram: List[Tuple[bool, ...]], wirings: List[List[List[int]]]
) -> int:
    overall = 0
    for lights, wiring in zip(lights_diagram, wirings):
        wiring_masks = [sum(1 << i for i in w) for w in wiring]
        target_state = sum(1 << i for i, light in enumerate(lights) if light)
        queue = deque([(0, 0)])
        visited = {0: 0}
        while queue:
            state, presses = queue.popleft()
            if state == target_state:
                overall += presses
                break
            for mask in wiring_masks:
                new_state = state ^ mask
                if new_state not in visited or visited[new_state] > presses + 1:
                    visited[new_state] = presses + 1
                    queue.append((new_state, presses + 1))
    return overall


def part_1_z3(
    lights_diagram: List[Tuple[bool, ...]], wirings: List[List[List[int]]]
) -> int:
    overall = 0
    for lights, wiring in zip(lights_diagram, wirings):
        cs = []
        xs = []
        for i, wire in enumerate(wiring):
            c = [1 if i in wire else 0 for i in range(len(lights))]
            cs.append(c)
            xs.append(Int(f"x{i}"))
        opt = Optimize()
        for i in range(len(lights)):
            opt.add(
                (sum(xs[j] * cs[j][i] for j in range(len(xs))) % 2)
                == (1 if lights[i] else 0)
            )
        opt.add([xs[i] >= 0 for i in range(len(xs))])
        opt.minimize(sum(xs))
        if opt.check() == sat:
            m = opt.model()
            total_presses = sum(m.evaluate(x).as_long() for x in xs) # type: ignore
            overall += total_presses
        else:
            print("No solution")
    return overall


def part_2(wirings: List[List[List[int]]], joltage_reqs: List[List[int]]) -> int:
    return sum(
        calculate_minimum_presses(wiring, joltage_req)
        for wiring, joltage_req in zip(wirings, joltage_reqs)
    )


def calculate_minimum_presses(wiring: List[List[int]], joltage_req: List[int]) -> int:
    cs = []
    xs = []
    for i, wire in enumerate(wiring):
        c = [1 if i in wire else 0 for i in range(len(joltage_req))]
        cs.append(c)
        xs.append(Int(f"x{i}"))
    opt = Optimize()
    for i in range(len(joltage_req)):
        opt.add(sum(xs[j] * cs[j][i] for j in range(len(xs))) == joltage_req[i])
    opt.add([xs[i] >= 0 for i in range(len(xs))])
    opt.minimize(sum(xs))
    if opt.check() == sat:
        m = opt.model()
        total_presses = sum(m.evaluate(x).as_long() for x in xs) # type: ignore
        return total_presses
    print("No solution")
    return 0


def main() -> None:
    lines = get_lines("input_10.txt")
    lights_diagram, wirings, joltage_reqs = parse_input(lines)
    print("Part 1:", part_1(lights_diagram, wirings))
    print("Part 2:", part_2(wirings, joltage_reqs))


if __name__ == "__main__":
    main()
