def read_groups(lines):
    groups = []
    current = []
    for line in lines:
        if line:
            current.append(line.strip())
        else:
            groups.append(current)
            current = []
    if current:
        groups.append(current)
    return groups

def read_group_answers(groups):
    group_answers = []
    for group in groups:
        answers = set()
        for person in group:
            answers.update(set(person))
        group_answers.append(answers)
    return group_answers

def part1(group_answers):
    print(sum(len(a) for a in group_answers))

def part2(groups, group_answers):
    acc = 0
    for group, answers in zip(groups, group_answers):
        for answer in answers:
            if all(answer in person for person in group):
                acc += 1
    print(acc)        

with open('../input/06.txt') as stream:
    lines = [line.strip() for line in stream]

groups = read_groups(lines)
group_answers = read_group_answers(groups)
part1(group_answers)
part2(groups, group_answers)
