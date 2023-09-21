from random import randrange

board = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
def display_board(board):
    # The function accepts one parameter containing the board's current status
    print('''
            +-------+-------+-------+
            |       |       |       |
            |   ''',board[0][0],'''   |   ''',board[0][1],'''   |   ''',board[0][2],'''   |
            |       |       |       |
            +-------+-------+-------+
            |       |       |       |
            |   ''',board[1][0],'''   |   ''',board[1][1],'''   |   ''',board[1][2],'''   |
            |       |       |       |
            +-------+-------+-------+
            |       |       |       |
            |   ''',board[2][0],'''   |   ''',board[2][1],'''   |   ''',board[2][2],'''   |
            |       |       |       |
            +-------+-------+-------+
            ''', sep='')

def freeFields(board):
    free_squares = []
    for i in range(3):
        for j in range(3):
            if type(board[i][j]) is not str:
                free_squares.append((i,j))# The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    return free_squares


def enter_move(board):
    while True:
        try:
            move = int(input('Enter your move: '))
        except:
            print("Wrong input. Try again...")

        c = (move - 1) % 3
        r = (move - 1) // 3
        if (r, c) in freeFields(board):
            board[r][c] = 'O'
            break


def victory(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]\
        or board[0][i] == board[1][i] == board[2][i]:
            return True # The function analyzes the board's status in order to check if
                          # the player using 'O's or 'X's has won the game
    if board[0][0] == board[1][1] == board[2][2]\
    or board[0][2] == board[1][1] == board[2][0]:
        return True
    

def isTie(board):
    if freeFields(board) == []:
        return True
    return


def draw_move(board):
    cur_pos = []
    while True:
        comp = randrange(9)# The function draws the computer's move and updates the board.
        if comp not in cur_pos:
            c = comp % 3
            r = comp // 3
            if (r, c) in freeFields(board):
                board[r][c] = 'X'
                cur_pos.append(comp)
                break
            

starter = int(input('Select starter\n1)Player\t\t2)Computer\n'))
while True:
    if starter == 2:
        draw_move(board)
        starter = None # So this isn't repeated

    display_board(board)
    enter_move(board)

    # Checking if player wins
    if victory(board):
        display_board(board)
        print('You win!')
        break

    if isTie(board):
        display_board(board)
        print('Tied!')
        break

    draw_move(board)

    # Checking if computer wins
    if victory(board):
        display_board(board)
        print('Computer wins!')
        break

    if isTie(board):
        display_board(board)
        print('Tied!')
        break