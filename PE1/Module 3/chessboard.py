EMPTY, ROOK, KNIGHT, BISH, PAWN, KING, QUEEN = "_____","ROOK", "KNIGHT", "BISHOP", "PAWN ", "KING", "QUEEN"

board = [[EMPTY for i in range(8)] for j in range(8)]
board[1] = board[6] = [PAWN for k in range(8)]

board[0][0] = board[0][7] = board[7][0] = board[7][7] = ROOK
board[0][1] = board[0][6] = board[7][1] = board[7][6] = KNIGHT
board[0][2] = board[0][5] = board[7][2] = board[7][5] = BISH
board[0][3] = board[7][3] = KING
board[0][4] = board[7][4] = QUEEN

#for row in board:
#    for piece in row:
#        print(piece)
# printing whole board
for m in range(8):
    print(board[m])
