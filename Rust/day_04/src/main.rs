use std::collections::HashSet;
use aoc::Point;

fn parse_input(input: &str, symbol: char) -> HashSet<Point> {
    input.lines()
        .enumerate()
        .flat_map(|(y, line)| {
            line.chars()
                .enumerate()
                .filter(|(_x, c)| *c == symbol)
                .map(|(x, _c)| Point { x: x as isize, y: y as isize })
                .collect::<Vec<Point>>()
        })
        .collect()
}

fn get_neighbours_8_no_filter(p: Point) -> HashSet<Point> {
    let mut neighbours = HashSet::new();
    for dx in -1..=1isize {
        for dy in -1..=1isize {
            if dx != 0 || dy != 0 {
                neighbours.insert(Point { x: p.x + dx, y: p.y + dy });
            }
        }
    }
    neighbours
}



fn part_1(rolls: &HashSet<Point>) -> usize {
    rolls.iter()
        .map(|&roll| {
            let neighbours = get_neighbours_8_no_filter(roll);
            let intersect_size = neighbours.intersection(rolls).count();
            intersect_size < 4
        })
        .filter(|&is_less_than_4| is_less_than_4)
        .count()
}

fn part_2(initial_rolls: HashSet<Point>) -> usize {
    let mut rolls = initial_rolls;
    let mut cnt: usize = 0;
    loop {
        let to_remove: HashSet<Point> = rolls.iter()
            .filter(|&&roll| {
                let neighbours = get_neighbours_8_no_filter(roll);
                let intersect_size = neighbours.intersection(&rolls).count();
                intersect_size < 4
            })
            .cloned()
            .collect();

        if to_remove.is_empty() {
            return cnt;
        }

        cnt += to_remove.len();

        for roll in &to_remove {
            rolls.remove(roll);
        }
    }
}

fn main() {
    let input = include_str!("../../../inputs/input_04.txt");
    let initial_rolls = parse_input(input, '@');

    println!("Part 1: {}", part_1(&initial_rolls));
    println!("Part 2: {}", part_2(initial_rolls));
}

