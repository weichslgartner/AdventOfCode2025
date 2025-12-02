from aoc import input_as_str


def parse_input(in_str):
    return [token.split("-", maxsplit=1) for token in in_str.split(",")]


def get_invalids(pair, repeats=2, seen=None):
    seen = set() if not seen else seen
    lower, upper = map(int, pair)
    length_a, length_b = len(pair[0]) // repeats, len(pair[1]) // repeats
    pattern_a = pair[0][:length_a] if length_a != 0 else "1"
    pattern_b = pair[1][:length_b] + "0"*(length_a-length_b) # fill with 0 if upper pattern is too short
    return sum(
        int(candidate)
        for i in range(int(pattern_a), int(pattern_b) + 1)
        if (candidate := str(i) * repeats)
        and lower <= int(candidate) <= upper
        and candidate not in seen
        and not seen.add(candidate)
    )


def cnt_all_invalid_sequences(pair):
    seen = set()
    return sum(get_invalids(pair, repeats=i, seen=seen) for i in range(2, len(pair[1]) + 1))


def part_1(pairs):
    return sum(map(get_invalids, pairs))


def part_2(pairs):
    return sum(map(cnt_all_invalid_sequences, pairs))


def main():
    lines = input_as_str("input_02.txt").replace("\n", "")
    lines = parse_input(lines)
    print("Part 1:", part_1(lines))
    print("Part 2:", part_2(lines))


if __name__ == '__main__':
    main()
