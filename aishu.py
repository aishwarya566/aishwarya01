def print_board(board):
    for r in board:
        print(" ".join("Q" if c == 1 else "." for c in r))
    print("-" * 25)


def is_safe(board, row, col, n):
    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def manual_n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    row = 0

    while row < n:
        print("\nCurrent Board:")
        print_board(board)

        try:
            col = int(input(f"Enter column (0-{n-1}) for row {row}: "))
        except:
            print("Invalid input! Enter number only.")
            continue

        if col < 0 or col >= n:
            print("Column out of range!")
            continue

        if is_safe(board, row, col, n):
            board[row][col] = 1
            row += 1
        else:
            print("❌ Conflict! Backtracking to previous row...")
            if row == 0:
                print("Cannot backtrack further. Start again.")
            else:
                # remove previous queen
                row -= 1
                for c in range(n):
                    board[row][c] = 0

    print("\n✅ FINAL SOLUTION:")
    print_board(board)


manual_n_queens(8)
