size = 8
solutions = []

def solve():
	board = [[0 for y in range(size)] for x in range(size)]
	placing_queen (0 , board)
	print(len(solutions))

def placing_queen(row, board):
	if row >= size:
		return

	for i in range(0, len(board)):
		if is_safe(board , row, i):
			board[row][i] = 1

			if row == len(board) - 1:
				solutions.append(1)
				board[row][i] = 0
				return

			placing_queen(row + 1, board)
			board[row][i] = 0

def is_safe(board , row , column):
	queens = []
	for r in range(0 , len(board)):
		for c in range(0 , len(board)):
			if board[r][c] == 1:
				q = (r , c)
				queens.append(q)
	for (r , c) in queens:
		if row == r: 
			return False
		if column == c:
			return False
		if (row + column) == r + c:
			return False
		if (column - row) == c - r:
			return False
	return True
solve()