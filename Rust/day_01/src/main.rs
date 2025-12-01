type Rotation = (char, i32);

fn parse_input(lines: &str) -> Vec<Rotation> {
    lines
        .lines()
        .filter(|line| !line.is_empty())
        .map(|line| {
            let op = line
                .chars()
                .next()
                .expect("Line must start with an operator");
            let n = line[1..]
                .parse::<i32>()
                .expect("Rotation value must be an integer");
            (op, n)
        })
        .collect()
}

fn is_zero(numb: i32, _numb_old: i32) -> u32 {
    if numb % 100 == 0 {
        1
    } else {
        0
    }
}

fn count_zero_crossings(numb: i32, numb_old: i32) -> u32 {
    let cnt: u32 = if (numb <= 0 && numb_old != 0) || (numb_old == 0 && numb == 0) {
        1
    } else {
        0
    };
    cnt + numb.unsigned_abs() / 100
}

fn solve(rotations: &[Rotation], condition: impl Fn(i32, i32) -> u32) -> u32 {
    rotations
        .iter()
        // state holds the current modded value (starts at 50)
        .scan(50i32, |state, (r, n)| {
            let prev_mod = *state;
            let unmod = match r {
                'R' => prev_mod + n,
                'L' => prev_mod - n,
                _ => panic!("Invalid rotation direction: {}", r),
            };
            *state = unmod % 100;
            Some(condition(unmod, prev_mod))
        })
        .sum()
}

fn part_1(rotations: &[Rotation]) -> u32 {
    solve(rotations, is_zero)
}

fn part_2(rotations: &[Rotation]) -> u32 {
    solve(rotations, count_zero_crossings)
}

fn main() {
    let rotations = parse_input(include_str!("../../../inputs/input_01.txt"));
    println!("Part 1: {}", part_1(&rotations));
    println!("Part 2: {}", part_2(&rotations));
}
