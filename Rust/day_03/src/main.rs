use std::collections::BTreeMap;
type JoltDict = (BTreeMap<u8, Vec<u32>>, usize);

fn parse_input(input: &str) -> Vec<JoltDict> {
    let mut battery_list: Vec<JoltDict> = Vec::new();
    for line in input.lines() {
        let mut batteries: BTreeMap<u8, Vec<u32>> = BTreeMap::new();
        for (i, c) in line.chars().enumerate() {
            if let Some(jolt) = c.to_digit(10) {
                batteries.entry(jolt as u8).or_default().push(i as u32);
            }
        }
        battery_list.push((batteries, line.len()));
    }
    battery_list
}

fn find_max_jolt_recursive(
    batteries: &JoltDict,
    current_number: u64,
    last_idx: u32,
    length: u32,
    acc: u64,
) -> Option<u64> {
    if length == 0 {
        return Some(acc + current_number);
    }
    if length > batteries.1 as u32 - last_idx {
        return None;
    }
    for key in batteries.0.keys().rev() {
        if let Some(val) = batteries.0.get(key) {
            let i = val.partition_point(|&v| v <= last_idx);
            if i < val.len() {
                if let Some(res) =
                    find_max_jolt_recursive(batteries, *key as u64, val[i], length - 1,  (acc + current_number) * 10u64)
                {
                    return Some(res);
                }
            }
        }
    }
    None
}

fn find_max_jolt(batteries: &JoltDict, length: u32) -> u64 {
    for k in batteries.0.keys().rev() {
        if let Some(v) = batteries.0.get(k) {
            if let Some(res) = find_max_jolt_recursive(
                batteries,
                *k as u64,
                v.first().cloned().unwrap(),
                length - 1,
                0u64,
            ) {
                return res;
            }
        }
    }
    0u64
}

fn part_1(batteries: &[JoltDict]) -> u64 {
    batteries.iter().map(|b| find_max_jolt(b, 2)).sum::<u64>()
}

fn part_2(batteries: &[JoltDict]) -> u64 {
    batteries.iter().map(|b| find_max_jolt(b, 12)).sum::<u64>()
}

fn main() {
    let input = include_str!("../../../inputs/input_03.txt");
    let batteries = parse_input(input);
    println!("Part 1: {}", part_1(&batteries));
    println!("Part 2: {}", part_2(&batteries));
}
