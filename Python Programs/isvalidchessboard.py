def is_valid_chessboard(board):
    count_whiteking = 0
    count_blckking=0

    possible_pos = [str(i)+j for j in ['a','b','c','d','e','f','g','h'] for i in range(1,9)]
    possible_pieces = ['pawn','knight','bishop','rook','queen','king']
    for i in board.keys():
        if(i not in possible_pos):
            return False
        elif(board[i].startswith('w') or board[i].startswith('b')==False):
            return board[i].startswith('w') or board[i].startswith('b')
        elif(board[i][1:]not in possible_pieces):
            return False

        return  True

        
print(is_valid_chessboard({'1h': 'bing', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}))