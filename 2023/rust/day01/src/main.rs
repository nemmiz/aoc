fn solve(line: &str, pairs: &[(&'static str, i32)]) -> i32 {
    let first = pairs
        .iter()
        .filter_map(|&(word, value)| line.find(word).and_then(|index| Some((index, value))))
        .min()
        .unwrap();

    let last = pairs
        .iter()
        .filter_map(|&(word, value)| line.rfind(word).and_then(|index| Some((index, value))))
        .max()
        .unwrap();

    first.1 * 10 + last.1
}

fn main() {
    let input = include_str!("../../../input/01.txt");

    let mut part1 = 0;
    let mut part2 = 0;

    for line in input.lines() {
        part1 += solve(
            line,
            &[
                ("1", 1),
                ("2", 2),
                ("3", 3),
                ("4", 4),
                ("5", 5),
                ("6", 6),
                ("7", 7),
                ("8", 8),
                ("9", 9),
            ],
        );
        part2 += solve(
            line,
            &[
                ("1", 1),
                ("2", 2),
                ("3", 3),
                ("4", 4),
                ("5", 5),
                ("6", 6),
                ("7", 7),
                ("8", 8),
                ("9", 9),
                ("one", 1),
                ("two", 2),
                ("three", 3),
                ("four", 4),
                ("five", 5),
                ("six", 6),
                ("seven", 7),
                ("eight", 8),
                ("nine", 9),
            ],
        );
    }

    println!("{}", part1);
    println!("{}", part2);
}
