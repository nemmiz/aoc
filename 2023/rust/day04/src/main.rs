use std::collections::HashSet;

fn main() {
    let input = include_str!("../../../input/04.txt");

    let mut matches = vec![];

    for line in input.lines() {
        let colon = line.find(':').unwrap();
        let pipe = line.find('|').unwrap();

        let wn = &line[colon + 1..pipe];
        let mn = &line[pipe + 1..];

        let winning_numbers: HashSet<i32> = wn
            .split_ascii_whitespace()
            .map(|s| s.parse::<i32>().unwrap())
            .collect();

        let numbers_i_have: HashSet<i32> = mn
            .split_ascii_whitespace()
            .map(|s| s.parse::<i32>().unwrap())
            .collect();

        matches.push(numbers_i_have.intersection(&winning_numbers).count());
    }

    let mut part1 = 0;

    for n in matches.iter() {
        let mut value = 0;

        for _ in 0..*n {
            value = match value {
                0 => 1,
                x => x * 2,
            };
        }

        part1 += value;
    }

    println!("{}", part1);

    let mut num_cards: Vec<usize> = matches.iter().map(|_| 1).collect();

    for i in 0..num_cards.len() {
        let multiplier = num_cards[i];
        for j in 0..matches[i] {
            num_cards[i + j + 1] += multiplier;
        }
    }

    let part2: usize = num_cards.iter().sum();
    println!("{}", part2);
}
