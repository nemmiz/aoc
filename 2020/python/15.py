def solve(numbers, last_turn):
    last_spoken_at = {n: i+1 for i, n in enumerate(numbers[:-1])}
    initial_turn = len(numbers) + 1
    last_number = numbers[-1]
    for turn in range(initial_turn, last_turn+1):
        if last_number in last_spoken_at:
            next_number = turn - 1 - last_spoken_at[last_number]
        else:
            next_number = 0
        last_spoken_at[last_number] = turn - 1
        last_number = next_number
    print(last_number)

solve([2,0,6,12,1,3], 2020)
solve([2,0,6,12,1,3], 30000000)
