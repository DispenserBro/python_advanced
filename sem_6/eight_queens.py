from itertools import combinations
import random
from time import sleep


def generate_boards():
    board_list = []

    while len(board_list) < 4:
        queens = []
        
        while len(queens) < 8:
            q1 = random.randint(1, 8)
            q2 = random.randint(1, 8)
            queens.append((q1, q2))
        # print(queens)
        
        if check_queens(queens):
            board_list.append(queens)
        print('----------------------------------------------------------------')
    print(board_list)
    return board_list


def is_attacking(q1, q2):
    sleep(0.15)
    if q1[0] == q2[0] or q1[1] == q2[1] or abs(q1[0] - q2[0]) == abs(q1[1] - q2[1]):
        print("nope!")
        return True
    print('yay!')
    return False


def check_queens(queens):
    combs = combinations(queens, 2)
    print(f'length = {len(list(combs))}')
    
    for idx, queens in enumerate(combinations(queens, 2), 1):
        print(idx, end=' ')
        if is_attacking(queens[0], queens[1]):
            return False
    
    return True


generate_boards()
# print(board_list)