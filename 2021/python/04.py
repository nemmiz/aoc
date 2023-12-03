BOARD_CHECKS = (
    (0, 25, 5), (1, 25, 5), (2, 25, 5), (3, 25, 5), (4, 25, 5),
    (0, 5, 1), (5, 10, 1), (10, 15, 1), (15, 20, 1), (20, 25, 1),
)

def check_board(board, nums):
    for start, end, step in BOARD_CHECKS:
        if all(board[i] in nums for i in range(start, end, step)):
            return sum(n for n in board if n not in nums)

def part1(boards, nums):
    for i in range(5, len(nums)):
        drawn_nums = set(nums[:i])
        for board in boards:
            if board_sum := check_board(board, drawn_nums):
                print(board_sum * nums[i-1])
                return

def part2(boards, nums):
    for i in range(5, len(nums)):
        remaining_boards = []
        drawn_nums = set(nums[:i])
        for bi, board in enumerate(boards):
            if board_sum := check_board(board, drawn_nums):
                if len(boards) == 1:
                    print(board_sum * nums[i-1])
                    return
            else:
                remaining_boards.append(board)
        boards = remaining_boards

with open('../input/04.txt') as stream:
    tmp = stream.read().split()
    numbers = [int(n) for n in tmp[0].split(',')]
    tmp = [int(n) for n in tmp[1:]]
    boards = [tmp[i:i+25] for i in range(0, len(tmp), 25)]

part1(boards, numbers)
part2(boards, numbers)
