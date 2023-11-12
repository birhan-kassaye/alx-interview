#!/usr/bin/python3
import sys

def print_solution(solution):
    for row, col in solution:
        print("[{}, {}]".format(row, col), end=' ')
    print()

def is_safe(solution, row, col):
    for queen in solution:
        if queen[0] == row or queen[1] == col or abs(queen[0] - row) == abs(queen[1] - col):
            return False
    return True

def solve_n_queens_util(n, col, solution):
    if col == n:
        print_solution(solution)
        return

    for row in range(n):
        if is_safe(solution, row, col):
            solution.append([row, col])
            solve_n_queens_util(n, col + 1, solution)
            solution.pop()

def solve_n_queens(n):
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solution = []
    solve_n_queens_util(n, 0, solution)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} N".format(sys.argv[0]))
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        solve_n_queens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
