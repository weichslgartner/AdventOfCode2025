from functools import reduce
from typing import List, Tuple, Set, Optional
from aoc import input_as_str

RangePair = Tuple[str, str]


def parse_input(in_str: str) -> List[RangePair]:
    return [tuple(token.split("-", maxsplit=1)) for token in in_str.split(",")] # type: ignore


def add_if_invalid(
        seen: Set[str],
        i: int,
        lower: int,
        upper: int,
        repeats: int
) -> Set[str]:
    if (candidate := str(i) * repeats) and lower <= int(candidate) <= upper:
        seen.add(candidate)
    return seen


def get_invalid_sum(pair: RangePair, repeats: int = 2, seen: Optional[Set[str]] = None) -> int:
    seen = set() if not seen else seen
    lower, upper = map(int, pair)
    length_a, length_b = len(pair[0]) // repeats, len(pair[1]) // repeats
    pattern_a = pair[0][:length_a] if length_a != 0 else "1"
    pattern_b = pair[1][:length_b] + "0" * (length_a - length_b)  # fill with 0 if upper pattern is too short
    return sum(map(int, reduce(
        lambda acc, i: add_if_invalid(acc, i, lower, upper, repeats),
        range(int(pattern_a), int(pattern_b) + 1),
        seen
    )))


def cnt_all_invalid_sequences(pair: RangePair) -> int:
    seen = set()
    return sum(get_invalid_sum(pair, repeats=i, seen=seen) for i in range(2, len(pair[1]) + 1))


def part_1(pairs: List[RangePair]) -> int:
    return sum(map(get_invalid_sum, pairs))


def part_2(pairs: List[RangePair]) -> int:
    return sum(map(cnt_all_invalid_sequences, pairs))


def main():
    lines = input_as_str("input_02.txt").replace("\n", "")
    lines = parse_input(lines)
    print("Part 1:", part_1(lines))
    print("Part 2:", part_2(lines))


if __name__ == '__main__':
    main()
