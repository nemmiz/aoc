class IllegalCharacter(Exception):
    def __init__(self, score):
        super().__init__()
        self.score = score

class IncompleteLine(Exception):
    def __init__(self, score):
        super().__init__()
        self.score = score

OPPOSITE = {
    '(': ')', '[': ']', '{': '}', '<': '>',
    ')': '(', ']': '[', '}': '{', '>': '<',
}

SCORE_PART1 = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

SCORE_PART2 = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}

def check_line(line):
    openings = []
    for c in line:
        if c in ('(', '[', '{', '<'):
            openings.append(c)
        elif openings and openings[-1] == OPPOSITE[c]:
            openings.pop()
        else:
            raise IllegalCharacter(SCORE_PART1[c])
    if openings:
        score = 0
        for c in reversed(openings):
            score = score * 5 + SCORE_PART2[OPPOSITE[c]]
        raise IncompleteLine(score)


with open('../input/10.txt') as stream:
    lines = [line.strip() for line in stream.readlines()]

part1_score = 0
part2_scores = []
for line in lines:
    try:
        check_line(line)
    except IllegalCharacter as err:
        part1_score += err.score
    except IncompleteLine as err:
        part2_scores.append(err.score)

print(part1_score)
part2_scores.sort()
print(part2_scores[len(part2_scores)//2])
