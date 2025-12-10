import sys
from aoc import get_lines
from functools import cache
from z3 import Int, Optimize, sat
# yolo
sys.setrecursionlimit(100000)


def parse_input(lines):
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


def is_same(w1, w2):
    for x, y in zip(w1, w2):
        if x != y:
            return False
    return True


def need_change(state, target):
    change = []
    for i, el in enumerate(zip(state, target)):
        change.append(i)
    return change


def update_state(state, wiring):
    return tuple(not s if i in wiring else s for i, s in enumerate(state))


def update_state_partb(state, wiring):
    state = list(state)
    for w in wiring:
        state[w] += 1
    return tuple(state)


def part_1(lights_diagram, wirings):
    # print(lights_diagram,wirings)
    overall = 0

    for lights, wiring in zip(lights_diagram, wirings):
        best = sys.maxsize
        state_to_presses = dict()
        def dfs(state, target, b_presses):
            if is_same(state, target):
                nonlocal best
                best = min(best, b_presses)
                return
            if b_presses >= best:
                return
            if state in state_to_presses and state_to_presses[state] <= b_presses:
                return
            state_to_presses[state] = b_presses
            for w in wiring:
                new_state = update_state(state, w)
                dfs(new_state, target, b_presses + 1)
            return
        dfs(tuple(False for _ in lights), lights, 0)
        overall += best
    return overall

# too slow does not finish
def part_2_req(wirings, joltage_reqs):
    overall = 0
    for wiring, joltage_req in zip(wirings, joltage_reqs):
        best = sys.maxsize

        @cache
        def dfs(state, target, b_presses):
            if is_same(state, target):
                nonlocal best
                best = min(best, b_presses)
                return
            for s, t in zip(state, target):
                if s > t:
                    return
            if b_presses >= best:
                return
            for w in wiring:
                new_state = update_state_partb(state, w)
                dfs(new_state, target, b_presses + 1)
            return
        dfs(tuple(0 for _ in joltage_req), tuple(i for i in joltage_req), 0)
        print(best)
        overall += best
    return overall


def part_2(wirings, joltage_reqs):
    return sum(calculate_minimum_presses(wiring, joltage_req) for wiring, joltage_req in zip(wirings, joltage_reqs))

def calculate_minimum_presses(wiring, joltage_req):
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
        total_presses = sum(int(str(m.evaluate(xs[i]))) for i in range(len(xs)))
        return total_presses
    print("No solution")
    return 0


def main():
    lines = get_lines("input_10.txt")
    lights_diagram, wirings, joltage_reqs = parse_input(lines)
    print("Part 1:", part_1(lights_diagram, wirings))
    print("Part 2:", part_2(wirings, joltage_reqs))


if __name__ == "__main__":
    main()
