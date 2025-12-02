from aoc import input_as_str


def parse_input(in_str):
    return [token.split("-", maxsplit=1) for token in in_str.split(",")]


def part_1(pairs):
    return sum(map(get_invalids, pairs))


def get_invalids(pair, repeats=2, seen=None):
    invalid_ids_sum = 0
    lower = int(pair[0])
    upper = int(pair[1])
    p0 = pair[0][:len(pair[0]) // repeats]
    if len(p0) == 0:
        p0 = "1"
    p1 = pair[1][:len(pair[1]) // repeats]
    if int(p1) < int(p0):
        p1 += "0"
    for i in range(int(p0), int(p1) + 1):
        candidate = str(i) * repeats
        if lower <= int(candidate) <= upper and (seen is None or candidate not in seen):
            if seen:
                seen.add(candidate)
            invalid_ids_sum += int(candidate)
    return invalid_ids_sum


def part_2(pairs):
    return sum(map(cnt_all_invalid_sequences, pairs))


def cnt_all_invalid_sequences(pair):
    invalid_ids_sum = 0
    seen = set()
    for i in range(2, len(pair[1]) + 1):
        invalid_ids_sum += get_invalids(pair, repeats=i, seen=seen)
    return invalid_ids_sum


def main():
    lines = input_as_str("input_02.txt").replace("\n", "")
    lines = parse_input(lines)
    print("Part 1:", part_1(lines))
    print("Part 2:", part_2(lines))


if __name__ == '__main__':
    main()
