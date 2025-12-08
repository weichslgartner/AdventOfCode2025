from functools import reduce
from heapq import heapify, heappop, nlargest
from operator import imul
from typing import List, Tuple
from itertools import combinations

from aoc import Point3, get_lines, line_to_int, squared_distance_3d


def parse_input(lines):
    return [
        Point3(x=p[0], y=p[1], z=p[2]) for p in [line_to_int(line) for line in lines]
    ]


def merge_clusters(p1, p2, cluster_map, clusters):
    to_delete = cluster_map[p2]
    clusters[cluster_map[p1]].update(clusters[cluster_map[p2]])
    for p in clusters[cluster_map[p2]]:
        cluster_map[p] = cluster_map[p1]
    del clusters[to_delete]


def connect_points_pair(p1, p2, cluster_map, clusters, cur_id):
    if p1 in cluster_map and p2 in cluster_map:
        if cluster_map[p1] != cluster_map[p2]:
            merge_clusters(p1, p2, cluster_map, clusters)
        return cur_id
    elif p1 in cluster_map:
        next_id = cluster_map[p1]
    elif p2 in cluster_map:
        next_id = cluster_map[p2]
    else:
        next_id = cur_id
        clusters[next_id] = set()
        cur_id += 1
    clusters[next_id].update({p1, p2})
    cluster_map[p1] = next_id
    cluster_map[p2] = next_id
    return cur_id


def solve(points: List, l_pairs: int = 1000) -> Tuple[int, int]:
    cluster_map = {}
    clusters = {}
    cur_id = 0
    three_biggest = 0
    dist_list = [
        (squared_distance_3d(p1, p2), i, p1, p2) 
        for i, (p1, p2) in enumerate(combinations(points, 2))
    ]
    heapify(dist_list)
    i = 1
    while dist_list:
        _, _, p1, p2 = heappop(dist_list)
        cur_id = connect_points_pair(p1, p2, cluster_map, clusters, cur_id)
        # part1
        if i == l_pairs:
            three_biggest = reduce(
                imul, nlargest(3, [len(c) for c in clusters.values()])
            )
        # part 2
        if len(clusters[cluster_map[p1]]) == len(points):
            return three_biggest, p1.x * p2.x
        i+=1
    return 0, 0


def main():
    lines = get_lines("input_08.txt")
    points = parse_input(lines)
    part1, part2 = solve(points)
    print("Part 1:", part1)
    print("Part 2:", part2)


if __name__ == "__main__":
    main()
   
