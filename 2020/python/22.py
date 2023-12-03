from collections import deque

def score(player):
    result = 0
    i = 1
    while player:
        x = player.pop()
        result += x * i
        i += 1
    return result

def play(p1, p2):
    while p1 and p2:
        a = p1.popleft()
        b = p2.popleft()
        if a > b:
            p1.append(a)
            p1.append(b)
        else:
            p2.append(b)
            p2.append(a)
    winner = p1 if p1 else p2
    return score(winner)

def play_recursive(p1, p2):
    played_rounds = set()
    while p1 and p2:
        config = f'{p1},{p2}'
        if config in played_rounds:
            return 1
        played_rounds.add(config)
        a = p1.popleft()
        b = p2.popleft()
        if len(p1) >= a and len(p2) >= b:
            p1_copy = deque(list(p1)[:a])
            p2_copy = deque(list(p2)[:b])
            winner = play_recursive(p1_copy, p2_copy)
            if winner == 1:
                p1.append(a)
                p1.append(b)
            elif winner == 2:
                p2.append(b)
                p2.append(a)
        else:
            if a > b:
                p1.append(a)
                p1.append(b)
            else:
                p2.append(b)
                p2.append(a)
    return 1 if p1 else 2

def part1(deck1, deck2):
    player1 = deque(deck1)
    player2 = deque(deck2)
    print(play(player1, player2))

def part2(deck1, deck2):
    player1 = deque(deck1)
    player2 = deque(deck2)
    winner_num = play_recursive(player1, player2)
    if winner_num == 1:
        print(score(player1))
    elif winner_num == 2:
        print(score(player2))

with open('../input/22.txt') as stream:
    decks = []
    for deck in stream.read().split('\n\n'):
        cards = [int(x) for x in deck.split('\n')[1:]]
        decks.append(cards)

part1(*decks)
part2(*decks)
