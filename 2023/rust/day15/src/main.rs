fn hash(s: &str) -> u32 {
    let mut current = 0;

    for c in s.chars() {
        let code = c as u32;
        current += code;
        current *= 17;
        current &= 255;
    }

    current
}

struct Box {
    lenses: Vec<(&'static str, i32)>,
}

impl Box {
    fn new() -> Self {
        Self { lenses: vec![] }
    }

    fn insert_or_replace(&mut self, label: &'static str, value: i32) {
        let index = self.lenses.iter().position(|lens| lens.0 == label);
        match index {
            Some(i) => self.lenses[i] = (label, value),
            None => self.lenses.push((label, value)),
        }
    }

    fn remove(&mut self, label: &str) {
        let index = self.lenses.iter().position(|lens| lens.0 == label);
        if let Some(i) = index {
            self.lenses.remove(i);
        }
    }

    fn focusing_power(&self, box_index: usize) -> usize {
        let mut result = 0;
        for (lens_index, &lens) in self.lenses.iter().enumerate() {
            result += (box_index + 1) * (lens_index + 1) * lens.1 as usize;
        }
        result
    }
}

fn part1(steps: &[&'static str]) {
    println!("{}", steps.iter().map(|&step| hash(step)).sum::<u32>());
}

fn part2(steps: &[&'static str]) {
    let mut boxes = vec![];

    for _ in 0..256 {
        boxes.push(Box::new());
    }

    for &step in steps.iter() {
        if step.ends_with('-') {
            let label = &step[..step.len() - 1];
            let index = hash(label) as usize;
            boxes[index].remove(label);
        } else {
            let label = &step[..step.len() - 2];
            let value = step.chars().last().unwrap().to_digit(10).unwrap();
            let index = hash(label) as usize;
            boxes[index].insert_or_replace(label, value as i32);
        }
    }

    let mut result = 0;
    for (i, b) in boxes.iter().enumerate() {
        result += b.focusing_power(i);
    }
    println!("{}", result);
}

fn main() {
    let input = include_str!("../../../input/15.txt").trim_end();
    let steps = input.split(',').collect::<Vec<_>>();

    part1(&steps);
    part2(&steps);
}
