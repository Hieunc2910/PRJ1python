# Write a program to compute the number of sudoku solutions (fill the zero elements of a given partial sudoku table)
# Fill numbers from 1, 2, 3, .., 9 to 9 x 9 table so that:
# Numbers of each row are distinct
# Numbers of each column are distinct
# Numbers on each sub-square 3 x 3 are distinct
# Input
# Each line i (i = 1, 2, ..., 9) contains elements of the i
# th
#  row of the Sudoku table: elements are numbers from 0 to 9 (value 0 means the empty cell of the table)
# Output
# Write the number of solutions found
def is_valid(board, row, col, num, rows, cols, boxes):
    if num in rows[row] or num in cols[col] or num in boxes[(row // 3) * 3 + col // 3]:
        return False
    return True

def find_empty_location(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def count_solutions(board):
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    # Initialize the sets with the current board state
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                num = board[i][j]
                rows[i].add(num)
                cols[j].add(num)
                boxes[(i // 3) * 3 + j // 3].add(num)

    def solve_and_count(board):
        find = find_empty_location(board)
        if not find:
            return 1
        else:
            row, col = find
        count = 0
        for num in range(1, 10):
            if is_valid(board, row, col, num, rows, cols, boxes):
                board[row][col] = num
                rows[row].add(num)
                cols[col].add(num)
                boxes[(row // 3) * 3 + col // 3].add(num)

                count += solve_and_count(board)

                board[row][col] = 0
                rows[row].remove(num)
                cols[col].remove(num)
                boxes[(row // 3) * 3 + col // 3].remove(num)
        return count

    return solve_and_count(board)

board = []
for i in range(9):
    board.append(list(map(int, input().split())))

print(count_solutions(board))