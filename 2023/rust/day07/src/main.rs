use std::collections::HashMap;

#[derive(Debug, PartialEq, Eq, PartialOrd, Ord)]
enum Kind {
    HighCard,
    OnePair,
    TwoPair,
    ThreeOfAKind,
    FullHouse,
    FourOfAKind,
    FiveOfAKind,
}

#[derive(Debug, PartialEq, Eq, PartialOrd, Ord)]
struct Hand {
    kind: Kind,
    cards: [i32; 5],
}

impl Hand {
    fn new(cards: &str) -> Self {
        Self::create(cards, cards, false)
    }

    fn new_strongest(cards: &str) -> Self {
        let chars: Vec<char> = cards.chars().collect();
        let all = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2'];

        let choices = |i| {
            if chars[i] == 'J' {
                all.as_slice()
            } else {
                &chars[i..i + 1]
            }
        };

        let a = choices(0);
        let b = choices(1);
        let c = choices(2);
        let d = choices(3);
        let e = choices(4);

        let mut strongest = Hand::create(cards, cards, true);

        for aa in a.iter() {
            for bb in b.iter() {
                for cc in c.iter() {
                    for dd in d.iter() {
                        for ee in e.iter() {
                            let cards2 = format!("{}{}{}{}{}", aa, bb, cc, dd, ee);
                            let hand = Hand::create(&cards2, cards, true);
                            strongest = std::cmp::max(strongest, hand);
                        }
                    }
                }
            }
        }

        strongest
    }

    fn create(cards: &str, actual_cards: &str, j_weakest: bool) -> Self {
        let mut cc: HashMap<char, i32> = HashMap::new();
        for c in cards.chars() {
            *cc.entry(c).or_insert(0) += 1;
        }

        let kind = {
            if cc.len() == 1 {
                Kind::FiveOfAKind
            } else if cc.len() == 5 {
                Kind::HighCard
            } else {
                let mut counts: Vec<i32> = cc.values().map(|x| *x).collect();
                counts.sort();

                match counts.as_slice() {
                    [1, 4] => Kind::FourOfAKind,
                    [2, 3] => Kind::FullHouse,
                    [1, 1, 3] => Kind::ThreeOfAKind,
                    [1, 2, 2] => Kind::TwoPair,
                    [1, 1, 1, 2] => Kind::OnePair,
                    _ => panic!(),
                }
            }
        };

        let nums: Vec<i32> = actual_cards
            .chars()
            .map(|c| match c {
                '2' => 2,
                '3' => 3,
                '4' => 4,
                '5' => 5,
                '6' => 6,
                '7' => 7,
                '8' => 8,
                '9' => 9,
                'T' => 10,
                'J' if j_weakest => 1,
                'J' if !j_weakest => 11,
                'Q' => 12,
                'K' => 13,
                'A' => 14,
                _ => panic!(),
            })
            .collect();

        Self {
            kind,
            cards: [nums[0], nums[1], nums[2], nums[3], nums[4]],
        }
    }
}

fn solve(input: &str, new_hand: fn(&str) -> Hand) {
    let mut hands = vec![];
    for line in input.lines() {
        let hand = new_hand(&line[..5]);
        let bet: i32 = line[6..].parse().unwrap();

        hands.push((hand, bet));
    }

    hands.sort();

    let mut result = 0;
    for (i, &(_, bet)) in hands.iter().enumerate() {
        result += (i as i32 + 1) * bet;
    }

    println!("{:?}", result);
}

fn main() {
    let input = include_str!("../../../input/07.txt");

    solve(input, Hand::new);
    solve(input, Hand::new_strongest);
}
