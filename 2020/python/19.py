import sys
from itertools import product
from copy import deepcopy

def parse_rule(line):
    parts = line.split()
    rule_id = int(parts[0][:-1])
    if len(parts) == 2 and parts[1].startswith('"'):
        return rule_id, parts[1][1:-1]
    if '|' in parts:
        i = parts.index('|')
        list1 = [int(x) for x in parts[1:i]]
        list2 = [int(x) for x in parts[i+1:]]
        return rule_id, (list1, list2)
    return rule_id, [int(x) for x in parts[1:]]

def matches(message, rules, rule_id):
    def _match(msg, rid):
        rule = rules[rid]
        if isinstance(rule, list):
            return _match_list(msg, rule)
        elif isinstance(rule, tuple):
            remainders = []
            for x in rule:
                if isinstance(x, list):
                    remainders += _match_list(msg, x)
                elif isinstance(x, dict):
                    for l in x:
                        if len(msg) >= l:
                            substr = msg[:l]
                            if substr in x[l]:
                                rem = msg[l:]
                                remainders.append(rem)
                else:
                    raise ValueError('unknown rule')
            return remainders
        else:
            raise ValueError('unknown rule')
    def _match_list(msg, rule):
        remainders = [msg]
        for n in rule:
            new_remainders = []
            for rem in remainders:
                rems = _match(rem, n)
                new_remainders += rems
            remainders = new_remainders
        return remainders
    remainders = _match(message, rule_id)
    return '' in remainders

def find_str_rule(rules):
    for i, r in rules.items():
        if isinstance(r, str):
            return i, r

def list_of_strings_to_string(lst):
    if all(isinstance(x, str) for x in lst):
        return ''.join(lst)
    return lst

def find_tuples_of_strings(rules):
    res = []
    for i, r in rules.items():
        if isinstance(r, tuple):
            if all(isinstance(x, str) for x in r):
                res.append(i)
    return res

def update_rule_refs(rules, replacements):
    for i, rule in rules.items():
        if isinstance(rule, list):
            new_list = list_of_strings_to_string([replacements.get(x, x) for x in rule])
            rules[i] = new_list
        elif isinstance(rule, tuple):
            new_list1 = list_of_strings_to_string([replacements.get(x, x) for x in rule[0]])
            new_list2 = list_of_strings_to_string([replacements.get(x, x) for x in rule[1]])
            rules[i] = (new_list1, new_list2)

def rewrite_list(lst, rules, tuples_of_strings):
    if len(lst) != 2:
        return None

    if isinstance(lst[0], str):
        a = [lst[0]]
    elif isinstance(lst[0], int) and lst[0] in tuples_of_strings:
        a = rules[lst[0]]
    else:
        return None

    if isinstance(lst[1], str):
        b = [lst[1]]
    elif isinstance(lst[1], int) and lst[1] in tuples_of_strings:
        b = rules[lst[1]]
    else:
        return None

    return tuple([''.join(p) for p in product(a, b)])

def rewrite_lists(rules):
    rules = deepcopy(rules)
    tos = find_tuples_of_strings(rules)
    
    for n, r in rules.items():
        if isinstance(r, list):
            after = rewrite_list(r, rules, tos)
            if after is not None:
                rules[n] = after
        if isinstance(r, tuple):
            new = []
            for x in r:
                if isinstance(x, list):
                    tmp = rewrite_list(x, rules, tos)
                    if tmp is None:
                        new.append(x)
                    else:
                        for t in tmp:
                            new.append(t)
                else:
                    new.append(x)
            rules[n] = tuple(new)
    return rules

def optimize_strings(rules):
    for i, rule in rules.items():
        if isinstance(rule, tuple):
            strings = {}
            others = []
            for s in rule:
                if isinstance(s, str):
                    strlen = len(s)
                    if strlen not in strings:
                        strings[strlen] = set()
                    strings[strlen].add(s)
                else:
                    others.append(s)
            if strings:
                others.append(strings)
            rules[i] = tuple(others)

def remove_unused_rules(rules):
    used = set()
    used.add(0)
    for i, r in rules.items():
        if isinstance(r, list):
            for n in r:
                if isinstance(n, int):
                    used.add(n)
        if isinstance(r, tuple):
            for t in r:
                if isinstance(t, list):
                    for n in t:
                        if isinstance(n, int):
                            used.add(n)
    all_rules = set(rules.keys())
    rules_to_remove = all_rules - used
    for r in rules_to_remove:
        del rules[r]

def optimize_rules(rules):
    rules = deepcopy(rules)
    while m := find_str_rule(rules):
        update_rule_refs(rules, {m[0]: m[1]})
        del rules[m[0]]
    while True:
        new_rules = rewrite_lists(rules)
        if new_rules == rules:
            break
        rules = new_rules
    remove_unused_rules(rules)
    optimize_strings(rules)
    return rules

def part1(rules, messages):
    rules = optimize_rules(rules)
    print(sum(1 for m in messages if matches(m, rules, 0)))

def part2(rules, messages):
    rules = deepcopy(rules)
    rules[8] = ([42], [42, 8])
    rules[11] = ([42, 31], [42, 11, 31])
    rules = optimize_rules(rules)
    print(sum(1 for m in messages if matches(m, rules, 0)))

rules = {}
messages = []
with open('../input/19.txt') as stream:
    for line in stream:
        line = line.strip()
        if not line:
            continue
        if line[0].isdigit():
            n, rule = parse_rule(line)
            rules[n] = rule
        else:
            messages.append(line.strip())

part1(rules, messages)
part2(rules, messages)
