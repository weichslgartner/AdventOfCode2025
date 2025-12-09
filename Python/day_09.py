from aoc import get_lines, Point
from itertools import combinations

def parse_input(lines):
    return [Point(*map(int, line.split(','))) for line in lines]


def part_1(points):
    max_area = 0
    #p_list  = sorted([(p.x * p.y,p) for p in points])
    #print(p_list)
    for p1, p2 in combinations(points, 2):
        area = (abs(p1.x - p2.x)+1) * (abs(p1.y - p2.y)+1)
        max_area = max(max_area, area)
    return max_area

def part_2(points):
    pass


def main():
    lines = get_lines("input_09.txt")
    points = parse_input(lines)
    print("Part 1:", part_1(points))
    print("Part 2:", part_2(points))


if __name__ == '__main__':
    main()
