from functools import reduce
import operator
from typing import List
from aoc import Point3, get_lines, line_to_int,euclidean_distance_3d
from itertools import combinations

def parse_input(lines):
    points = [line_to_int(line) for line in lines]
    return [Point3(x=p[0],y=p[1],z=p[2]) for p in points]


def part_1(points: List, l_pairs: int = 1000) -> int:
    cluster_map = {}
    clusters = {}
    cur_id = 0
    dist_list = []
    for p1,p2 in combinations(points,2):
        dist = euclidean_distance_3d(p1,p2)
        dist_list.append((dist,p1,p2))
    print(len(dist_list))
    dist_list.sort(key=lambda x: x[0])
    for _,p1,p2 in dist_list[:l_pairs]:
        print(f"considering {p1} {p2}")
        if p1 in cluster_map and p2 in cluster_map:
            if cluster_map[p1] != cluster_map[p2]:
                #print("shit")
                to_delete = cluster_map[p2]
                clusters[cluster_map[p1]].update(clusters[cluster_map[p2]])
                for p in clusters[cluster_map[p2]]:
                    cluster_map[p] = cluster_map[p1]
                del clusters[to_delete]
            next_id = cluster_map[p1]
           # print(cluster_map,clusters,[len(c) for c in clusters.values()])
            continue
        elif p1 in cluster_map:
            next_id = cluster_map[p1]
        elif p2 in cluster_map:
            next_id = cluster_map[p2] 
        else:
            next_id = cur_id
            clusters[next_id] = set()
            cur_id += 1
        clusters[next_id].add(p1)
        clusters[next_id].add(p2)
        cluster_map[p1] = next_id
        cluster_map[p2] = next_id    
       # print(cluster_map,clusters,[len(c) for c in clusters.values()])
    sizes = [len(c) for c in clusters.values()]
    sizes.sort(reverse=True)
    print(sizes)
    return reduce(operator.imul,sizes[0:3])

def part_2(lines):
    pass


def main():
    lines = get_lines("input_08.txt") # too high 1570580
    points = parse_input(lines)
    print("Part 1:", part_1(points))
    print("Part 2:", part_2(points))


if __name__ == '__main__':
    main()
