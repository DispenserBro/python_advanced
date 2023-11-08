from itertools import combinations

def is_attacking(q1, q2):
    # Проверяем, бьют ли ферзи друг друга
    return q1[0] == q2[0] or q1[1] == q2[1] or abs(q1[0] - q2[0]) == abs(q1[1] - q2[1])

def check_queens(queens):
    # Проверяем все возможные пары ферзей
    for q1, q2 in combinations(queens, 2):
        if is_attacking(q1, q2):
            return False
    return True


if __name__ == "__main__":
    print(check_queens([(1, 2), (8, 2), (6, 7), (1, 1), (8, 1), (8, 3), (4, 4), (1, 3)]))
    print(check_queens([(8, 8), (1, 2), (6, 3), (6, 6), (7, 3), (1, 8), (7, 4), (7, 6)]))
    print(check_queens([(4, 6), (7, 2), (1, 3), (3, 2), (4, 5), (5, 2), (7, 7), (8, 4)]))
    print(check_queens([(2, 2), (3, 1), (4, 7), (3, 3), (1, 3), (5, 8), (5, 3), (1, 1)]))