#[derive(Debug)]
struct RangeGroup {
    ranges: Vec<(u64, u64, u64)>,
}

impl RangeGroup {
    fn map(&self, n: u64) -> u64 {
        for range in self.ranges.iter() {
            if n >= range.1 && n < (range.1 + range.2) {
                return n - range.1 + range.0;
            }
        }
        return n;
    }
}

fn parse_input(input: &str) -> (Vec<u64>, Vec<RangeGroup>) {
    let mut seeds = vec![];
    let mut groups = vec![];
    let mut ranges = vec![];

    for line in input.lines() {
        if line.is_empty() {
            continue;
        } else if line.starts_with("seeds:") {
            for tmp in line[7..].split_ascii_whitespace() {
                seeds.push(tmp.parse::<u64>().unwrap());
            }
        } else if line.contains("map:") {
            if ranges.len() > 0 {
                let group = RangeGroup { ranges };
                ranges = vec![];
                groups.push(group);
            }
        } else {
            let nums: Vec<u64> = line
                .split_ascii_whitespace()
                .map(|s| s.parse::<u64>().unwrap())
                .collect();
            assert_eq!(nums.len(), 3);
            ranges.push((nums[0], nums[1], nums[2]));
        }
    }

    if ranges.len() > 0 {
        let group = RangeGroup { ranges };
        groups.push(group);
    }

    (seeds, groups)
}

fn part1(seeds: &[u64], groups: &[RangeGroup]) {
    let mut min = u64::MAX;

    for &seed in seeds.iter() {
        let mut num = seed;
        for group in groups.iter() {
            num = group.map(num)
        }

        min = std::cmp::min(min, num);
    }

    println!("{}", min);
}

fn part2(seeds: &[u64], groups: &[RangeGroup]) {
    let mut min = u64::MAX;

    for chunk in seeds.chunks(2) {
        for seed in chunk[0]..(chunk[0] + chunk[1]) {
            let mut num = seed;
            for group in groups.iter() {
                num = group.map(num)
            }

            min = std::cmp::min(min, num);
        }
    }

    println!("{}", min);
}

fn main() {
    let input = include_str!("../../../input/05.txt");
    let (seeds, groups) = parse_input(input);

    part1(&seeds, &groups);
    part2(&seeds, &groups);
}
