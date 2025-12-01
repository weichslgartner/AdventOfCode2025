use std::ops::{Add, Sub};

type Rotation = (char, i32);

fn parse_input(lines: &str) -> Vec<Rotation> {
    lines.lines()
        .filter(|line| !line.is_empty()) 
        .map(|line| {
            let op = line.chars().next().expect("Line must start with an operator");
            let n = line[1..].parse::<i32>().expect("Rotation value must be an integer");            
            (op, n)
        })
        .collect()
}

fn is_zero(numb: i32, _numb_old: i32) -> i32 {
    if numb % 100 == 0 { 1 } else { 0 }
}


fn count_zero_crossings(numb: i32, numb_old: i32) -> i32 {
    let mut cnt = 0;
    if numb <= 0 && numb_old != 0 {
        cnt += 1;
    }
    cnt += numb.abs() / 100;
    cnt
}

fn solve(rotations: &[Rotation], condition: impl Fn(i32, i32) -> i32) -> i32 {
    let mut cnt = 0;
    let mut numb: i32 = 50;
    let mut numb_old: i32 = numb;
    for (r, n) in rotations {
                match r {
            'R' => {
                numb = numb.add(n); 
            }
            'L' => {
                numb = numb.sub(n);
            }
            _ => panic!("Invalid rotation direction: {}", r),
        }
        
        cnt += condition(numb, numb_old);        
        numb %= 100;
        numb_old = numb;
    }

    cnt
}


fn part_1(rotations: &[Rotation]) -> i32 {
    solve(rotations, is_zero)
}

fn part_2(rotations: &[Rotation]) -> i32 {
    solve(rotations, count_zero_crossings)
}

fn main() {
    let rotations = parse_input(include_str!("../../../inputs/input_01.txt"));
    println!("Part 1: {}", part_1(&rotations));
    println!("Part 2: {}", part_2(&rotations));
}