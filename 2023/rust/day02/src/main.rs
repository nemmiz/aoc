fn main() {
    let input = include_str!("../../../input/02.txt");

    let mut part1 = 0;
    let mut part2 = 0;

    for (index, line) in input.lines().enumerate() {
        let line = line
            .chars()
            .skip_while(|&c| c != ':')
            .skip_while(|&c| c == ':' || c == ' ')
            .filter(|&c| c != ',')
            .collect::<String>();

        let mut possible = true;
        let mut max_red = 0;
        let mut max_green = 0;
        let mut max_blue = 0;

        for handful in line.split(';') {
            let handful = handful
                .split(' ')
                .filter(|s| !s.is_empty())
                .collect::<Vec<_>>();

            for chunk in handful.as_slice().chunks(2) {
                let count: i32 = chunk[0].parse().unwrap();
                match chunk[1] {
                    "red" => {
                        if count > 12 {
                            possible = false;
                        }
                        max_red = std::cmp::max(max_red, count);
                    }

                    "green" => {
                        if count > 13 {
                            possible = false;
                        }
                        max_green = std::cmp::max(max_green, count);
                    }

                    "blue" => {
                        if count > 14 {
                            possible = false;
                        }
                        max_blue = std::cmp::max(max_blue, count);
                    }
                    _ => (),
                }
            }
        }

        if possible {
            part1 += index + 1;
        }

        part2 += max_red * max_green * max_blue;
    }

    println!("{}", part1);
    println!("{}", part2);
}
