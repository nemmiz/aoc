#[derive(Debug)]
struct Symbol {
    c: char,
    pub x: i32,
    pub y: i32,
}

impl Symbol {
    fn new(x: usize, y: usize, c: char) -> Self {
        Self {
            x: x as i32,
            y: y as i32,
            c,
        }
    }

    fn gear_ratio(&self, numbers: &[Number]) -> Option<u32> {
        if self.c != '*' {
            return None;
        }

        let adjacent_numbers: Vec<_> = numbers.iter().filter(|&n| n.is_adjacent(self)).collect();

        if adjacent_numbers.len() == 2 {
            return Some(adjacent_numbers[0].num * adjacent_numbers[1].num);
        }

        None
    }
}

#[derive(Debug)]
struct Number {
    x1: i32,
    x2: i32,
    y: i32,
    pub num: u32,
}

impl Number {
    fn new(x: usize, y: usize, d: u32) -> Self {
        Self {
            x1: x as i32,
            x2: x as i32,
            y: y as i32,
            num: d,
        }
    }

    fn add_digit(self, d: u32) -> Self {
        Self {
            x1: self.x1,
            x2: self.x2 + 1,
            y: self.y,
            num: self.num * 10 + d,
        }
    }

    fn is_adjacent(&self, symbol: &Symbol) -> bool {
        symbol.x >= (self.x1 - 1)
            && symbol.x <= (self.x2 + 1)
            && symbol.y >= (self.y - 1)
            && symbol.y <= (self.y + 1)
    }

    fn is_adjacent_to_any_symbol(&self, symbols: &[Symbol]) -> bool {
        for symbol in symbols.iter() {
            if self.is_adjacent(symbol) {
                return true;
            }
        }
        false
    }
}

fn main() {
    let input = include_str!("../../../input/03.txt");

    let mut symbols = vec![];
    let mut nums = vec![];
    let mut num: Option<Number> = None;

    for (y, line) in input.lines().enumerate() {
        for (x, c) in line.chars().enumerate() {
            if let Some(d) = c.to_digit(10) {
                num = match num {
                    Some(n) => Some(n.add_digit(d)),
                    None => Some(Number::new(x, y, d)),
                }
            } else {
                if c != '.' {
                    symbols.push(Symbol::new(x, y, c));
                }
                if let Some(n) = num {
                    nums.push(n);
                    num = None;
                }
            }
        }
        if let Some(n) = num {
            nums.push(n);
            num = None;
        }
    }

    let part1: u32 = nums
        .iter()
        .filter(|&n| n.is_adjacent_to_any_symbol(&symbols))
        .map(|n| n.num)
        .sum();

    let part2: u32 = symbols.iter().filter_map(|s| s.gear_ratio(&nums)).sum();

    println!("{}", part1);
    println!("{}", part2);
}
