use std::collections::HashSet;


fn parse_input(in_str: &str) -> Vec<(String, String)> {
    in_str
        .split(',')
        .filter_map(|token| {
            let mut parts = token.splitn(2, '-');
            Some((parts.next()?.to_string(), parts.next()?.to_string()))
        })
        .collect()
}


fn get_invalids(pair: &(String, String), repeats: usize, seen: &mut HashSet<String>) -> u64 {
    if repeats == 0 { return 0; }

    let (lower_str, upper_str) = pair;
    let lower: u64 = lower_str.parse().unwrap_or(0);
    let upper: u64 = upper_str.parse().unwrap_or(0);

    let length_a = lower_str.len().checked_div(repeats).unwrap_or(0);
    let length_b = upper_str.len().checked_div(repeats).unwrap_or(0);

    let pattern_a_str = if length_a > 0 { &lower_str[..length_a] } else { "1" };
    
    let mut pattern_b_str = if length_b > 0 { 
        upper_str[..length_b].to_string() 
    } else { 
        "1".to_string() 
    };

    if length_a > length_b {
        pattern_b_str.extend(std::iter::repeat_n('0', length_a - length_b));
    }
    
    let pattern_a: u64 = pattern_a_str.parse().unwrap_or(1);
    let pattern_b: u64 = pattern_b_str.parse().unwrap_or(0);

    (pattern_a..=pattern_b).fold(0, |acc, i| {
        let i_str = i.to_string();
        let candidate = i_str.repeat(repeats);
        
        let candidate_int: u64 = match candidate.parse() {
            Ok(val) => val,
            Err(_) => return acc,
        };

        if candidate_int >= lower && candidate_int <= upper && seen.insert(candidate) {
            acc + candidate_int
        } else {
            acc
        }
    })
}

fn cnt_all_invalid_sequences(pair: &(String, String)) -> u64 {
    let mut seen: HashSet<String> = HashSet::new();
    let upper_len = pair.1.len();

    (2..=upper_len)
        .map(|i| get_invalids(pair, i, &mut seen))
        .sum()
}


fn part_1(pairs: &[(String, String)]) -> u64 {
    pairs.iter()
        .map(|pair| {
            let mut seen: HashSet<String> = HashSet::new();
            get_invalids(pair, 2, &mut seen)
        })
        .sum()
}

fn part_2(pairs: &[(String, String)]) -> u64 {
    pairs.iter()
        .map(cnt_all_invalid_sequences)
        .sum()
}



fn main() {
    let input = include_str!("../../../inputs/input_02.txt").replace('\n', "");
    let pairs = parse_input(&input);

    println!("Part 1: {}", part_1(&pairs));
    println!("Part 2: {}", part_2(&pairs));
}

