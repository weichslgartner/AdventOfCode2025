from aoc import input_as_str


def is_invalid(id_str: str) -> bool:
    return id_str[:len(id_str) // 2] == id_str[len(id_str) // 2:]


def parse_input(in_str):
    return [token.split("-", maxsplit=1) for token in in_str.split(",")]


def part_1(pairs):
    invalid_ids_sum = 0
    for pair in pairs:
        lower = int(pair[0])
        upper = int(pair[1])
        p0 = pair[0][:len(pair[0]) // 2]
        if len(p0) == 0:
            p0 = "1"
        p1 = pair[1][:len(pair[1]) // 2]
        print("range",pair,p0,p1)

        if int(p1) <  int(p0):
            p1 += "0"
        print(lower,upper)
        for i in range(int(p0),int(p1)+1):
            candidate = str(i) + str(i)
            print(candidate)
            if lower <= int(candidate) <= upper:
                print(candidate, "invalid",invalid_ids_sum)
                invalid_ids_sum += int(candidate)
    return invalid_ids_sum

def part_2(lines):
    pass


def main():
    lines = input_as_str("input_02.txt").replace("\n", "")
    lines = parse_input(lines)
    print("Part 1:", part_1(lines))
    print("Part 2:", part_2(lines))


if __name__ == '__main__':
    main()
