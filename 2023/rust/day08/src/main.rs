use num::integer::lcm;
use std::collections::HashMap;

fn part1(instructions: &str, lookup: &HashMap<&str, (&str, &str)>) {
    let mut current = "AAA";

    for (count, instruction) in instructions.chars().cycle().enumerate() {
        if current == "ZZZ" {
            println!("{}", count);
            return;
        }

        let &(left, right) = lookup.get(current).unwrap();

        match instruction {
            'L' => current = left,
            'R' => current = right,
            _ => panic!(),
        };
    }
}

fn part2(instructions: &str, lookup: &HashMap<&str, (&str, &str)>) {
    let starts: Vec<&str> = lookup
        .keys()
        .filter(|k| k.ends_with('A'))
        .map(|k| *k)
        .collect();

    let mut result = 1;

    for &start in starts.iter() {
        let mut current = start;

        for (count, instruction) in instructions.chars().cycle().enumerate() {
            if current.ends_with('Z') {
                result = lcm(result, count);
                break;
            }

            let &(left, right) = lookup.get(current).unwrap();

            match instruction {
                'L' => current = left,
                'R' => current = right,
                _ => panic!(),
            };
        }
    }

    println!("{}", result);
}

fn main() {
    let input = include_str!("../../../input/08.txt");

    let lines: Vec<&str> = input.lines().collect();
    let instructions = lines[0];

    let mut lookup = HashMap::new();

    for &line in lines[2..].iter() {
        let from = &line[..3];
        let left = &line[7..10];
        let right = &line[12..15];

        lookup.insert(from, (left, right));
    }

    part1(instructions, &lookup);
    part2(instructions, &lookup);
}
