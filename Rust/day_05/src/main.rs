use std::cmp::max;

type Range = (u64, u64);

type Ranges = Vec<Range>;

type Ids = Vec<u64>;

fn parse_input(input: &str) -> (Ranges, Ids) {
    let mut parts = input.splitn(2, "\n\n");
    let ranges_str = parts.next().unwrap_or("");
    let ids_str = parts.next().unwrap_or("");

    let mut ranges: Ranges = ranges_str
        .lines()
        .filter_map(|line| {
            let mut parts = line.splitn(2, '-');
            let start = parts.next()?.parse::<u64>().ok()?;
            let end = parts.next()?.parse::<u64>().ok()?;
            Some((start, end))
        })
        .collect();


    ranges.sort_unstable_by_key(|r| r.0);

    let ids: Ids = ids_str
        .lines()
        .filter_map(|line| line.parse::<u64>().ok())
        .collect();

    (ranges, ids)
}


fn part_1(ranges: &Ranges, ids: &Ids) -> u64 {
    ids.iter().filter(|id| ranges.iter().any(|r| r.0 <= **id && **id <= r.1)).count() as u64    
}


fn part_2(ranges: Ranges) -> u64 {
    if ranges.is_empty() {
        return 0;
    }
    let mut merged_ranges: Vec<Range> = Vec::new();
    let mut current_range = ranges[0];
    for next_range in ranges.into_iter().skip(1) {
        if current_range.1 >= next_range.0 {
            current_range.1 = max(current_range.1, next_range.1);
        } else {
            merged_ranges.push(current_range);
            current_range = next_range;
        }
    }
    merged_ranges.push(current_range);

    merged_ranges.iter()
        .map(|r| r.1 - r.0 + 1)
        .sum()
}


fn main() {
    let input = include_str!("../../../inputs/input_05.txt");
    let (ranges, ids) = parse_input(input);
    println!("Part 1: {}", part_1(&ranges, &ids));
    println!("Part 2: {}", part_2(ranges));
}

