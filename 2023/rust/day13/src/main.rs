use std::collections::HashSet;

#[derive(PartialEq, Eq, Clone)]
enum Reflection {
    Row(usize),
    Col(usize),
}

impl Reflection {
    fn score(&self) -> usize {
        match self {
            Reflection::Row(i) => *i * 100,
            Reflection::Col(i) => *i,
        }
    }
}

struct Pattern {
    width: usize,
    height: usize,
    rocks: HashSet<(usize, usize)>,
}

impl Pattern {
    fn new(lines: &[&str]) -> Self {
        let mut max_x = 0;
        let mut max_y = 0;
        let mut rocks = HashSet::new();

        for (y, line) in lines.iter().enumerate() {
            max_y = std::cmp::max(max_y, y);
            for (x, c) in line.chars().enumerate() {
                max_x = std::cmp::max(max_x, x);
                if c == '#' {
                    rocks.insert((x, y));
                }
            }
        }

        Self {
            width: max_x + 1,
            height: max_y + 1,
            rocks,
        }
    }

    fn row(&self, i: usize) -> String {
        let mut tmp = String::with_capacity(self.width);
        for x in 0..self.width {
            if self.rocks.contains(&(x, i)) {
                tmp.push('#');
            } else {
                tmp.push('.');
            }
        }
        tmp
    }

    fn col(&self, i: usize) -> String {
        let mut tmp = String::with_capacity(self.height);
        for y in 0..self.height {
            if self.rocks.contains(&(i, y)) {
                tmp.push('#');
            } else {
                tmp.push('.');
            }
        }
        tmp
    }

    fn find_horizontal_reflection(&self, ignore: Option<Reflection>) -> Option<Reflection> {
        for i in 1..self.height {
            for j in 0.. {
                if (j > i - 1) || (j + i >= self.height) {
                    let result = Some(Reflection::Row(i));
                    if result != ignore {
                        return result;
                    }
                    break;
                }

                let above = self.row(i - 1 - j);
                let below = self.row(i + j);

                if above != below {
                    break;
                }
            }
        }
        None
    }

    fn find_vertical_reflection(&self, ignore: Option<Reflection>) -> Option<Reflection> {
        for i in 1..self.width {
            for j in 0.. {
                if (j > i - 1) || (j + i >= self.width) {
                    let result = Some(Reflection::Col(i));
                    if result != ignore {
                        return result;
                    }
                    break;
                }

                let left = self.col(i - 1 - j);
                let right = self.col(i + j);

                if left != right {
                    break;
                }
            }
        }
        None
    }

    fn find_reflection(&self, ignore: Option<Reflection>) -> Option<Reflection> {
        self.find_horizontal_reflection(ignore.clone())
            .or(self.find_vertical_reflection(ignore.clone()))
    }

    fn find_reflection_with_smudge(&self) -> Option<Reflection> {
        let ignore = self.find_reflection(None);
        for y in 0..self.height {
            for x in 0..self.width {
                let p = self.with_smudge(x, y);
                let r = p.find_reflection(ignore.clone());
                if r.is_some() {
                    return r;
                }
            }
        }
        None
    }

    fn with_smudge(&self, x: usize, y: usize) -> Self {
        let mut rocks = self.rocks.clone();

        if rocks.contains(&(x, y)) {
            rocks.remove(&(x, y));
        } else {
            rocks.insert((x, y));
        }

        Self {
            width: self.width,
            height: self.height,
            rocks,
        }
    }
}

fn main() {
    let input = include_str!("../../../input/13.txt");
    let mut buffer = vec![];
    let mut patterns = vec![];

    for line in input.lines() {
        if !line.is_empty() {
            buffer.push(line);
        } else if !buffer.is_empty() {
            patterns.push(Pattern::new(&buffer));
            buffer.clear();
        }
    }

    if !buffer.is_empty() {
        patterns.push(Pattern::new(&buffer));
    }

    let part1: usize = patterns
        .iter()
        .map(|p| p.find_reflection(None).unwrap().score())
        .sum();
    println!("{}", part1);

    let part2: usize = patterns
        .iter()
        .map(|p| p.find_reflection_with_smudge().unwrap().score())
        .sum();
    println!("{}", part2);
}
