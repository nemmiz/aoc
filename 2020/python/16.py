import re

def within_range(rule, number):
    if number >= rule[1] and number <= rule[2]:
        return True
    if number >= rule[3] and number <= rule[4]:
        return True
    return False

def get_invalid_numbers(rules, numbers):
    invalid = []
    for number in numbers:
        for rule in rules:
            if within_range(rule, number):
                break
        else:
            invalid.append(number)
    return invalid

def get_matching_rules(rules, numbers):
    matches = set()
    for rule in rules:
        if all(within_range(rule, number) for number in numbers):
            matches.add(rule[0])
    return matches

def find_column_that_matches_only_one(col_matches):
    for i, m in col_matches.items():
        if len(m) == 1:
            return i

def filter_matches(col_matches, field_to_remove):
    new = {}
    for col, matches in col_matches.items():
        if field_to_remove in matches:
            if len(matches) > 1:
                new[col] = matches - {field_to_remove}
        else:
            new[col] = matches
    return new

def part1(rules, tickets):
    acc = 0
    for ticket in tickets:
        acc += sum(get_invalid_numbers(rules, ticket))
    print(acc)

def part2(rules, tickets, my_ticket):
    tickets = [ticket for ticket in tickets if not get_invalid_numbers(rules, ticket)]
    col_matches = {}
    for col in range(len(my_ticket)):
        col_numbers = [ticket[col] for ticket in tickets]
        matches = get_matching_rules(rules, col_numbers)
        col_matches[col] = matches
    col_map = {}
    while col_matches:
        col = find_column_that_matches_only_one(col_matches)
        field = next(iter(col_matches[col]))
        col_map[field] = col
        col_matches = filter_matches(col_matches, field)
    result = 1
    for field, col in col_map.items():
        if field.startswith('departure'):
            result *= my_ticket[col]
    print(result)

with open('../input/16.txt') as stream:
    rules = []
    tickets = []
    for line in stream:
        if m := re.match(r'(.*): (\d+)-(\d+) or (\d+)-(\d+)', line):
            rules.append((m.group(1), int(m.group(2)), int(m.group(3)), int(m.group(4)), int(m.group(5))))
        elif line[0].isdigit():
            tickets.append([int(x) for x in line.split(',')])
    my_ticket = tickets[0]
    nearby_tickets = tickets[1:]

part1(rules, nearby_tickets)
part2(rules, nearby_tickets, my_ticket)
