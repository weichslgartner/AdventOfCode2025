from aoc import get_lines, Point
from itertools import combinations


def parse_input(lines):
    return [Point(*map(int, line.split(","))) for line in lines]


def part_1(points):
    max_area = 0
    for p1, p2 in combinations(points, 2):
        area = (abs(p1.x - p2.x) + 1) * (abs(p1.y - p2.y) + 1)
        max_area = max(max_area, area)
    return max_area


def part_2(points):
    lines = []
    inner_points = []
    for p1, p2 in zip(points, points[1:]):
        lines.append((p1, p2))
        if abs(p1.x - p2.x) > 5000:
            inner_points.append(max([p1, p2], key=lambda p: p.x))
    lines.append((points[-1], points[0]))
    max_area = 0
    best = None
    # upper half
    p1 = max(inner_points, key=lambda p: p.y)
    for p2 in points:
        if p1 == p2 or p2.y < p1.y:
            continue
        to_check = Point(p1.x, p2.y)
        lines_to_check = []
        for line in lines:
            if line[0] == p1 or line[1] == p1:
                continue
            if (
                min(line[0].x, line[1].x) <= to_check.x <= max(line[0].x, line[1].x)
            ) and line[0].y >= p1.y:
                lines_to_check.append(line)
        if all(to_check.y <= min(line[0].y, line[1].y) for line in lines_to_check):
            area = (abs(p1.x - p2.x) + 1) * (abs(p1.y - p2.y) + 1)
            if area > max_area:
                max_area = area
                best = [p1, Point(p1.x, p2.y), p2, Point(p2.x, p1.y), p1]
    p1 = min(inner_points, key=lambda p: p.y)
    lines_to_check = []

    for p2 in points:
        if p1 == p2 or p2.y > p1.y:
            continue
        to_check = Point(p1.x, p2.y)
        for line in lines:
            if line[0] == p1 or line[1] == p1:
                continue
            if (
                min(line[0].x, line[1].x) <= to_check.x <= max(line[0].x, line[1].x)
            ) and line[0].y <= p1.y:
                lines_to_check.append(line)
        if all(to_check.y >= max(line[0].y, line[1].y) for line in lines_to_check):
            area = (abs(p1.x - p2.x) + 1) * (abs(p1.y - p2.y) + 1)
            if area > max_area:
                max_area = area
                best = [p1, Point(p1.x, p2.y), p2, Point(p2.x, p1.y), p1]
    import matplotlib.pyplot as plt
    print(inner_points)
    points.append(points[0])  # to create a closed loop
    xs, ys = zip(*points)  # create lists of x and y values
    # plt.figure()
    # plt.plot(xs,ys)
    # if best:
    #     plt.plot(*zip(*best))
    # plt.show()
    return max_area


def main():
    lines = get_lines("input_09.txt")
    points = parse_input(lines)
    print("Part 1:", part_1(points))
    print("Part 2:", part_2(points))


if __name__ == "__main__":
    main()
