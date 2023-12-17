struct Race {
    time: u64,
    distance: u64,
}

impl Race {
    fn count_wins(&self) -> u64 {
        let mut wins = 0;
        for speed in 1..self.time {
            let remaining_time = self.time - speed;
            let dist = speed * remaining_time;
            if dist > self.distance {
                wins += 1;
            }
        }
        wins
    }
}

fn part1(input: &str) {
    let mut times: Vec<u64> = vec![];
    let mut distances: Vec<u64> = vec![];

    for line in input.lines() {
        if line.starts_with("Time:") {
            let line = &line["Time:".len()..];
            times = line
                .split_ascii_whitespace()
                .map(|n| n.parse().unwrap())
                .collect();
        } else if line.starts_with("Distance:") {
            let line = &line["Distance:".len()..];
            distances = line
                .split_ascii_whitespace()
                .map(|n| n.parse().unwrap())
                .collect();
        }
    }

    let mut result = 1;
    for (t, d) in times.into_iter().zip(distances) {
        let race = Race {
            time: t,
            distance: d,
        };
        result *= race.count_wins();
    }

    println!("{}", result);
}

fn part2(input: &str) {
    let mut race = Race {
        time: 0,
        distance: 0,
    };

    for line in input.lines() {
        if line.starts_with("Time:") {
            let line = &line["Time:".len()..];
            race.time = line.replace(' ', "").parse().unwrap();
        } else if line.starts_with("Distance:") {
            let line = &line["Distance:".len()..];
            race.distance = line.replace(' ', "").parse().unwrap();
        }
    }

    println!("{}", race.count_wins());
}

fn main() {
    let input = include_str!("../../../input/06.txt");

    part1(input);
    part2(input);
}
