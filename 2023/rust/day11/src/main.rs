use std::collections::HashSet;

#[derive(Clone)]
struct Image {
    width: usize,
    height: usize,
    galaxies: HashSet<(usize, usize)>,
}

impl Image {
    fn new(input: &str) -> Self {
        let mut galaxies = HashSet::new();
        let mut max_x = 0;
        let mut max_y = 0;

        for (y, line) in input.lines().enumerate() {
            max_y = std::cmp::max(max_y, y);
            for (x, c) in line.chars().enumerate() {
                max_x = std::cmp::max(max_x, x);
                if c == '#' {
                    galaxies.insert((x, y));
                }
            }
        }

        Self {
            width: max_x + 1,
            height: max_y + 1,
            galaxies,
        }
    }

    fn is_empty_row(&self, row: usize) -> bool {
        for x in 0..self.width {
            if self.galaxies.contains(&(x, row)) {
                return false;
            }
        }
        true
    }

    fn is_empty_column(&self, col: usize) -> bool {
        for y in 0..self.height {
            if self.galaxies.contains(&(col, y)) {
                return false;
            }
        }
        true
    }

    fn expand(&mut self, factor: usize) -> Self {
        let rows: Vec<usize> = (0..self.height)
            .filter(|&row| self.is_empty_row(row))
            .collect();

        let cols: Vec<usize> = (0..self.width)
            .filter(|&col| self.is_empty_column(col))
            .collect();

        let mut galaxies = self.galaxies.clone();

        for row in rows.iter().rev() {
            // dbg!(row);
            let mut new = HashSet::new();
            for pos in galaxies.iter() {
                if pos.1 > *row {
                    new.insert((pos.0, pos.1 + factor - 1));
                } else {
                    new.insert((pos.0, pos.1));
                }
            }
            galaxies = new;
        }

        for col in cols.iter().rev() {
            // dbg!(col);
            let mut new = HashSet::new();
            for pos in galaxies.iter() {
                if pos.0 > *col {
                    new.insert((pos.0 + factor - 1, pos.1));
                } else {
                    new.insert((pos.0, pos.1));
                }
            }
            galaxies = new;
        }

        Self {
            width: self.width + cols.len() * (factor - 1),
            height: self.height + rows.len() * (factor - 1),
            galaxies,
        }
    }

    fn sum_distances(&self) -> usize {
        let galaxies: Vec<&(usize, usize)> = self.galaxies.iter().collect();
        let mut sum = 0;

        for i in 0..galaxies.len() - 1 {
            for j in i + 1..galaxies.len() {
                let p0 = galaxies[i];
                let p1 = galaxies[j];
                sum += p0.0.abs_diff(p1.0) + p0.1.abs_diff(p1.1);
            }
        }

        sum
    }
}

fn main() {
    let input = include_str!("../../../input/11.txt");
    let mut image = Image::new(input);

    println!("{}", image.expand(2).sum_distances());
    println!("{}", image.expand(1000000).sum_distances());
}
