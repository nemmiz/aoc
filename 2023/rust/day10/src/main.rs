use std::{
    collections::{HashMap, HashSet, VecDeque},
    time::TryFromFloatSecsError,
};

#[derive(Clone, Copy)]
#[repr(u8)]
enum Dir {
    N,
    W,
    E,
    S,
}

impl Dir {
    fn opposite(&self) -> Self {
        match self {
            Dir::N => Dir::S,
            Dir::S => Dir::N,
            Dir::E => Dir::W,
            Dir::W => Dir::E,
        }
    }
}

#[derive(Debug, Default, Clone, Copy, PartialEq, Eq, Hash)]
struct Pos {
    x: i32,
    y: i32,
}

impl Pos {
    fn new(x: i32, y: i32) -> Self {
        Self { x, y }
    }
}

fn tile_leads(c: char, dir: Dir) -> bool {
    match dir {
        Dir::N if "|LJS".contains(c) => true,
        Dir::S if "|7FS".contains(c) => true,
        Dir::E if "-LFS".contains(c) => true,
        Dir::W if "-J7S".contains(c) => true,
        _ => false,
    }
}

struct Grid {
    start: Pos,
    tiles: HashMap<Pos, char>,
}

impl Grid {
    fn new(input: &str) -> Self {
        let mut tiles = HashMap::new();
        let mut start = Pos::default();

        for (y, line) in input.lines().enumerate() {
            for (x, c) in line.chars().enumerate() {
                let pos = Pos::new(x as i32, y as i32);
                if c == 'S' {
                    start = pos;
                }
                tiles.insert(pos, c);
            }
        }

        let mut grid = Self { start, tiles };

        let can_move_n = grid.try_move(start, Dir::N).is_some();
        let can_move_s = grid.try_move(start, Dir::S).is_some();
        let can_move_e = grid.try_move(start, Dir::E).is_some();
        let can_move_w = grid.try_move(start, Dir::W).is_some();

        if can_move_n && can_move_s {
            grid.tiles.insert(start, '|');
        } else if can_move_e && can_move_w {
            grid.tiles.insert(start, '-');
        } else if can_move_n && can_move_w {
            grid.tiles.insert(start, 'J');
        } else if can_move_n && can_move_e {
            grid.tiles.insert(start, 'L');
        } else if can_move_s && can_move_w {
            grid.tiles.insert(start, '7');
        } else if can_move_s && can_move_e {
            grid.tiles.insert(start, 'F');
        } else {
            panic!("can't replace S")
        }

        grid
    }

    fn try_move(&self, pos: Pos, dir: Dir) -> Option<Pos> {
        let new = match dir {
            Dir::N => Pos::new(pos.x, pos.y - 1),
            Dir::W => Pos::new(pos.x - 1, pos.y),
            Dir::E => Pos::new(pos.x + 1, pos.y),
            Dir::S => Pos::new(pos.x, pos.y + 1),
        };

        let pos_tile = *self.tiles.get(&pos).unwrap_or(&',');
        let new_tile = *self.tiles.get(&new).unwrap_or(&'.');

        if tile_leads(pos_tile, dir) && tile_leads(new_tile, dir.opposite()) {
            Some(new)
        } else {
            None
        }
    }

    fn find_furthest(&self) -> (i32, HashSet<Pos>) {
        let mut visited = HashSet::new();
        visited.insert(self.start);

        let mut queue = VecDeque::with_capacity(2);
        queue.push_back((self.start, 0));

        let mut max_steps = 0;

        while !queue.is_empty() {
            let (pos, steps) = queue.pop_front().unwrap();

            max_steps = std::cmp::max(max_steps, steps);

            for dir in [Dir::N, Dir::S, Dir::E, Dir::W].iter() {
                if let Some(next) = self.try_move(pos, *dir) {
                    if !visited.contains(&next) {
                        visited.insert(next);
                        queue.push_back((next, steps + 1));
                    }
                }
            }
        }

        (max_steps, visited)
    }

    fn draw(&self) {
        let mut max_x = 0;
        let mut max_y = 0;

        for pos in self.tiles.keys() {
            max_x = std::cmp::max(max_x, pos.x);
            max_y = std::cmp::max(max_y, pos.y);
        }

        for y in 0..max_y + 1 {
            let mut line = String::new();
            for x in 0..max_x + 1 {
                let ch = match *self.tiles.get(&Pos::new(x, y)).unwrap_or(&'.') {
                    '|' => '┃',
                    '-' => '━',
                    'L' => '┗',
                    'J' => '┛',
                    '7' => '┓',
                    'F' => '┏',
                    c => c,
                };
                line.push(ch);
            }
            println!("{}", line);
        }
    }

    fn is_inside(&self, pos: &Pos, loop_tiles: &HashSet<Pos>) -> bool {
        let mut chars = vec![];

        for x in 0..pos.x {
            let tmp = Pos::new(x, pos.y);
            let tile = self.tiles.get(&tmp).map(|x| *x).unwrap_or_default();
            if loop_tiles.contains(&tmp) && "F7JL|".contains(tile) {
                chars.push(tile);
            }
        }

        let mut crossings = 0;
        for (i, &c) in chars.iter().enumerate() {
            if c == '|' {
                crossings += 1;
            } else if i > 0 {
                let prev = chars[i - 1];
                if (c == 'J' && prev == 'F') || (c == '7' && prev == 'L') {
                    crossings += 1;
                }
            }
        }

        crossings % 2 == 1
    }

    fn count_inside_tiles(&mut self, loop_tiles: &HashSet<Pos>) -> usize {
        self.tiles
            .keys()
            .filter(|&pos| !loop_tiles.contains(pos) && self.is_inside(pos, loop_tiles))
            .count()
    }
}

fn main() {
    let input = include_str!("../../../input/10.txt");

    let mut grid = Grid::new(input);

    let (part1, loop_tiles) = grid.find_furthest();
    println!("{}", part1);

    let part2 = grid.count_inside_tiles(&loop_tiles);
    println!("{}", part2);
    // grid.draw();
}
