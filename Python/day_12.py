from functools import reduce
from operator import imul
from typing import Dict, List, Tuple, Set
from aoc import Point, input_as_str, parse_grid

Region = Tuple[List[int], List[int]]




def parse_input(input_str: str) -> Tuple[Dict[int, Set[Point]], List[Region]]:
    shapes = {}
    regions = []
    for block in input_str.split("\n\n"):
        lines = block.splitlines()
        if "x" in lines[0]:
            for size, gifts  in map(lambda line: line.split(":"),lines):
                regions.append(
                    (
                        list(map(int, size.split("x", maxsplit=1))),
                        list(map(int, gifts.split())),
                    )
                )
        else:
            shape_id = int(lines[0].replace(":","").strip())
            shape = parse_grid(lines[1:], "#")
            shapes[shape_id] = shape

    return shapes, regions


def part_1(shapes: Dict[int, Set[Point]], regions: List[Region]) -> int:
    return sum(reduce(imul,size) >= sum(len(shapes[i])*g for i,g in enumerate(gifts)) for size, gifts in regions)



def main() -> None:
    shapes, regions = parse_input(input_as_str("input_12.txt"))
    print("Part 1:", part_1(shapes, regions))

if __name__ == "__main__":
    main()
