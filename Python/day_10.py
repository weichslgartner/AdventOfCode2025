from collections import defaultdict
from copy import copy
import random
import sys
from aoc import get_lines
from functools import cache
import sys
sys.setrecursionlimit(100000) 

def parse_input(lines):
    lights_diagram = []
    wirings = []
    joltage_reqs = []
    for line in lines:
        wiring = []
        for token in line.split():
            if "[" in token and "]" in token:
                lights_diagram.append(tuple( x=="#" for x in token[1:-1]))
            elif "(" in token:
                wiring.append([int(x) for x in token[1:-1].split(",")])
            else:
                wirings.append(wiring)
                joltage_reqs.append([int(x) for x in token[1:-1].split(",")])
    return lights_diagram, wirings, joltage_reqs

def is_same(w1,w2):
    for x,y in zip(w1,w2):
        if x!=y:
            return False
    return True

def need_change(state,target):
    change = []
    for i, el in enumerate(zip(state,target)):
        change.append(i)
    return change

def update_state(state,wiring):
    return tuple(not s if i in wiring else s for i,s in enumerate(state))

def part_1(lights_diagram, wirings):
    #print(lights_diagram,wirings)
    overall = 0

    for lights,wiring in zip(lights_diagram, wirings):
        w_dict = defaultdict(list)
        for w in wiring:
            for x in w:
                w_dict[x].append(w)
        #print(w_dict)
        best = sys.maxsize
        state_to_presses = dict()
        @cache
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
        print(lights)
        dfs(tuple(False for _ in lights), lights, 0)

        print(best)
        overall += best
    return overall


def part_2(lines):
    pass


def main():
    lines = get_lines("input_10.txt")
    lights_diagram, wirings, joltage_reqs = parse_input(lines)
    print("Part 1:", part_1(lights_diagram, wirings))
    print("Part 2:", part_2(lines))


if __name__ == '__main__':
    main()
