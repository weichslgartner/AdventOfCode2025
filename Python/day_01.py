from aoc import get_lines, line_to_int


def parse_input(lines):
    return [(line[0], int(line[1:])) for line in lines]


def part_1(rotations):
    pass


def solve(rotations):
    cnt_a = 0
    cnt_b = 0
    numb = 50
    numb_old = 50
    for r, n in rotations:
        if r == 'L':
            numb -= n
        else:
            numb += n
        if numb <= 0 and numb_old != 0:
            cnt_b += 1
        cnt_b += abs(numb) // 100
        numb %= 100
        numb_old = numb
        cnt_a += 1 if numb == 0 else 0
    return cnt_a, cnt_b


def part_2(lines):
    pass


def main():
    lines = get_lines("input_01.txt")
    rotations = parse_input(lines)
    cnt_a, cnt_b = solve(rotations)
    print("Part 1:", cnt_a)
    print("Part 2:", cnt_b)


if __name__ == '__main__':
    main()
