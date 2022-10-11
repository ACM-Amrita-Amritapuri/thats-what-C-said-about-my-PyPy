global N
N = 4

def isSafe(board, row, col):

	# Check row rows
	for i in range(col):
		if board[row][i] == 1:
			return False

	# Check upper diagonal
	for i in range(row, -1, -1):
		for j in range(col, -1, -1):
			if board[i][j] == 1:
				return False

	# Check lower diagonal
	for i in range(row, N, 1):
		for j in range(col, -1, -1):
			if board[i][j] == 1:
				return False

	return True

def solve(board, col):
	
	# checks all queens are placed
	if col >= N:
		return True

	for i in range(N):
		if isSafe(board, i, col):
			board[i][col] = 1

			if solve(board, col + 1) == True:
				return True

			board[i][col] = 0
	return False

def printboard(board):
	for i in range(N):
		for j in range(N):
			print (board[i][j], end = " ")
		print()

board = [[0, 0, 0, 0],
		[ 0, 0, 0, 0],
		[ 0, 0, 0, 0],
		[ 0, 0, 0, 0]]

if solve(board, 0) == False:
	print ("Solution does not exist")
else:
	printboard(board)
