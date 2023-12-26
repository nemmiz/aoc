use std::collections::HashMap;

fn solve(pattern: &str, criteria: &[usize]) -> usize {
    let pattern: Vec<char> = pattern.chars().collect();
    let mut positions: HashMap<usize, usize> = HashMap::new();
    positions.insert(0, 1);

    for (i, contiguous) in criteria.iter().enumerate() {
        let mut new_positions = HashMap::new();

        for (&pos, &v) in positions.iter() {
            let remaining =
                pattern.len() - criteria[i + 1..].iter().sum::<usize>() + criteria.len() - (i + 1);

            for start in pos..remaining {
                let end = start + contiguous;

                if end <= pattern.len() && !pattern[start..end].contains(&'.') {
                    let is_last_criteria = i == criteria.len() - 1;

                    if (is_last_criteria && !pattern[end..].contains(&'#'))
                        || (!is_last_criteria && end < pattern.len() && pattern[end] != '#')
                    {
                        new_positions
                            .entry(end + 1)
                            .and_modify(|x| *x += v)
                            .or_insert(v);
                    }
                }
                if pattern[start] == '#' {
                    break;
                }
            }
        }

        positions = new_positions;
    }

    positions.values().sum()
}

fn main() {
    let input = include_str!("../../../input/12.txt");

    let mut part1 = 0;
    for line in input.lines() {
        let space = line.find(' ').unwrap();
        let pattern = &line[..space];
        let criteria = &line[space + 1..];
        let criteria: Vec<usize> = criteria.split(',').map(|x| x.parse().unwrap()).collect();
        part1 += solve(pattern, &criteria);
    }
    println!("{}", part1);

    let mut part2 = 0;
    for line in input.lines() {
        let space = line.find(' ').unwrap();
        let pattern = &line[..space];
        let pattern = format!(
            "{}?{}?{}?{}?{}",
            pattern, pattern, pattern, pattern, pattern
        );
        let criteria = &line[space + 1..];
        let mut criteria: Vec<usize> = criteria.split(',').map(|x| x.parse().unwrap()).collect();
        let len = criteria.len();
        criteria.extend_from_within(..len);
        criteria.extend_from_within(..len);
        criteria.extend_from_within(..len);
        criteria.extend_from_within(..len);
        part2 += solve(&pattern, &criteria);
    }
    println!("{}", part2);
}
