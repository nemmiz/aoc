use core::panic;
use std::collections::HashMap;

struct Platform {
    width: i32,
    height: i32,
    rocks: HashMap<(i32, i32), char>,
}

impl Platform {
    fn new(input: &str) -> Self {
        let mut max_x = 0;
        let mut max_y = 0;
        let mut rocks = HashMap::new();

        for (y, line) in input.lines().enumerate() {
            max_y = std::cmp::max(max_y, y);
            for (x, c) in line.chars().enumerate() {
                max_x = std::cmp::max(max_x, x);
                if c == '#' || c == 'O' {
                    rocks.insert((x as i32, y as i32), c);
                }
            }
        }

        Self {
            width: (max_x + 1) as i32,
            height: (max_y + 1) as i32,
            rocks,
        }
    }

    fn slide_north(&mut self) {
        for x in 0..self.width {
            let mut move_to_y = 0;

            for y in 0..self.height {
                if let Some(c) = self.rocks.get(&(x, y)) {
                    if *c == '#' {
                        move_to_y = y + 1;
                    } else if *c == 'O' {
                        if move_to_y == y {
                            move_to_y += 1;
                        } else {
                            self.rocks.insert((x, move_to_y), *c);
                            self.rocks.remove(&(x, y));
                            move_to_y += 1;
                        }
                    }
                }
            }
        }
    }

    fn slide_south(&mut self) {
        for x in 0..self.width {
            let mut move_to_y = self.height - 1;

            for y in (0..self.height).rev() {
                if let Some(c) = self.rocks.get(&(x, y)) {
                    if *c == '#' {
                        move_to_y = y - 1;
                    } else if *c == 'O' {
                        if move_to_y == y {
                            move_to_y -= 1;
                        } else {
                            self.rocks.insert((x, move_to_y), *c);
                            self.rocks.remove(&(x, y));
                            move_to_y -= 1;
                        }
                    }
                }
            }
        }
    }

    fn slide_west(&mut self) {
        for y in 0..self.height {
            let mut move_to_x = 0;

            for x in 0..self.width {
                if let Some(c) = self.rocks.get(&(x, y)) {
                    if *c == '#' {
                        move_to_x = x + 1;
                    } else if *c == 'O' {
                        if move_to_x == x {
                            move_to_x += 1;
                        } else {
                            self.rocks.insert((move_to_x, y), *c);
                            self.rocks.remove(&(x, y));
                            move_to_x += 1;
                        }
                    }
                }
            }
        }
    }

    fn slide_east(&mut self) {
        for y in 0..self.height {
            let mut move_to_x = self.width - 1;

            for x in (0..self.width).rev() {
                if let Some(c) = self.rocks.get(&(x, y)) {
                    if *c == '#' {
                        move_to_x = x - 1;
                    } else if *c == 'O' {
                        if move_to_x == x {
                            move_to_x -= 1;
                        } else {
                            self.rocks.insert((move_to_x, y), *c);
                            self.rocks.remove(&(x, y));
                            move_to_x -= 1;
                        }
                    }
                }
            }
        }
    }

    fn total_load(&self) -> i32 {
        let mut sum = 0;

        for y in 0..self.height {
            for x in 0..self.width {
                if let Some(c) = self.rocks.get(&(x, y)) {
                    if *c == 'O' {
                        sum += self.height - y;
                    }
                }
            }
        }

        sum
    }
}

fn find_loop(samples: &[i32], threshold: usize) -> (usize, usize) {
    let mut loop_size = 0;

    for size in 1..threshold {
        let mut i = samples.len() - 1;
        let expected = samples[i];
        let mut is_loop = true;

        while i > threshold {
            i -= size;
            if samples[i] != expected {
                is_loop = false;
                break;
            }
        }

        if is_loop {
            loop_size = size;
            break;
        }
    }

    if loop_size == 0 {
        panic!("Failed to find loop size!");
    }

    for start in 0..threshold {
        let expected = samples[start];
        let mut i = start + loop_size;
        let mut ok = true;

        while i < samples.len() {
            if samples[i] != expected {
                ok = false;
                break;
            }
            i += loop_size as usize;
        }

        if ok {
            return (start, loop_size);
        }
    }

    panic!("Failed to find loop start!");
}

fn predict(index: usize, samples: &[i32], loop_start: usize, loop_size: usize) -> i32 {
    let x = index - loop_start;
    let x = x / loop_size;
    let x = x * loop_size;
    let x = index - x;
    samples[x]
}

fn main() {
    let input = include_str!("../../../input/14.txt");
    let mut platform = Platform::new(input);

    platform.slide_north();
    println!("{}", platform.total_load());

    let mut samples = vec![];

    for _ in 0..1000 {
        platform.slide_north();
        platform.slide_west();
        platform.slide_south();
        platform.slide_east();
        samples.push(platform.total_load());
    }

    let (loop_start, loop_size) = find_loop(&samples, 250);

    println!(
        "{}",
        predict(1000000000 - 1, &samples, loop_start, loop_size)
    );
}
