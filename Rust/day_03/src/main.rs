use std::collections::BTreeMap;
type JoltDict = (BTreeMap<u8 , Vec<u32>>, usize);

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
    used: &mut Vec<u32>,
    length: u32,
    acc: u64,
) -> Option<u64> {
    if length == 0 {
        return Some(acc + current_number);
    }
    if length > batteries.1 as u32 - used.len() as u32 {
        return None;
    }
    for key in batteries.0.keys().rev() {
        if let Some(val) = batteries.0.get(key) {
            for &v in val {
                if v > *used.last().unwrap() {
                    used.push(v);
                    let new_acc = (acc + current_number) * 10u64;
                    if let Some(res) =
                        find_max_jolt_recursive(batteries, *key as u64, used, length - 1, new_acc)
                    {
                        return Some(res);
                    }
                    used.pop();
                }
            }
        }
    }
    None
}

fn find_max_jolt(batteries: &JoltDict, length: u32) -> u64 {
    for k in batteries.0.keys().rev() {
        if let Some(v) = batteries.0.get(k) {
            let mut used = vec![v.first().cloned().unwrap()];
            if let Some(res) =
                find_max_jolt_recursive(batteries, *k as u64, &mut used, length - 1, 0u64)
            {
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
