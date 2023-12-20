fn extrapolate(nums: &Vec<i32>) -> i32 {
    let mut diffs = vec![];

    for i in 1..nums.len() {
        diffs.push(nums[i] - nums[i - 1]);
    }

    if diffs.iter().all(|&x| x == 0) {
        return 0;
    }

    diffs.last().unwrap() + extrapolate(&diffs)
}

fn extrapolate_backwards(nums: &Vec<i32>) -> i32 {
    let mut diffs = vec![];

    for i in 1..nums.len() {
        diffs.push(nums[i] - nums[i - 1]);
    }

    if diffs.iter().all(|&x| x == 0) {
        return 0;
    }

    diffs.first().unwrap() - extrapolate_backwards(&diffs)
}

fn main() {
    let input = include_str!("../../../input/09.txt");

    let mut part1 = 0;
    let mut part2 = 0;

    for line in input.lines() {
        let nums: Vec<i32> = line
            .split_ascii_whitespace()
            .map(|x| x.parse().unwrap())
            .collect();

        part1 += nums.last().unwrap() + extrapolate(&nums);
        part2 += nums.first().unwrap() - extrapolate_backwards(&nums);
    }

    println!("{}", part1);
    println!("{}", part2);
}
