answer_board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def print_board(board):
    for i in range(len(board)):
        for j in range(len(board)):
            print("| {} |".format(board[i][j]), end='')
        print("\n")

print_board(answer_board)

import random

def create_board():
    board = []
    temp = []
    used_numbers = []
    i = 1
    while(True):
        number = random.randint(1, 9)
        if number not in used_numbers:
            used_numbers.append(number)
            temp.append(number)
            if(i == 3):
                board.append(temp)
                temp = []
                i = 1
            else:
                i += 1
            if(len(board) == 3):
                break
    return board

generated_board = create_board()
print_board(generated_board)

def calc_heuristic(board1, board2):
    h = 0
    for i in range(len(board1)):
        for j in range(len(board1)):
            if(board1[i][j] != board2[i][j]):
                h += 1
    return h

calc_heuristic(answer_board, generated_board)

def run_game(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if(board[i][j] == 9):
                nine_x, nine_y = i, j
                break

    print(nine_x, nine_y)

    top, right, bottom, left = True, True, True, True

    if(nine_x == 0):
        top = False
    if(nine_x == len(board)):
        bottom = False
    if(nine_y == 0):
        top = False
    if(nine_y == len(board)):
        top = False

    print(top, right, bottom, left)

    move_set = {'top': -1, 'right': -1, 'bottom': -1, 'left': -1}

    if(top):
        move_set['top'] = board[nine_x-1][nine_y]
    if(right):
        move_set['right'] = board[nine_x][nine_y+1]
    if(bottom):
        move_set['bottom'] = board[nine_x-1][nine_y]
    if(left):
        move_set['left'] = board[nine_x][nine_y-1]

    print(move_set)

run_game(generated_board)

def run_game(board, answer):
    for i in range(len(board)):
        for j in range(len(board)):
            if(board[i][j] == 9):
                nine_x, nine_y = i, j
                break

    move_set = {'top': -1, 'right': -1, 'bottom': -1, 'left': -1}

    if(nine_x != 0):
        move_set['top'] = board[nine_x-1][nine_y]
    if(nine_x != len(board)-1):
        move_set['bottom'] = board[nine_x+1][nine_y]
    if(nine_y != 0):
        move_set['left'] = board[nine_x][nine_y-1]
    if(nine_y != len(board)-1):
        move_set['right'] = board[nine_x][nine_y+1]

    user_move_set = {}

    print("Available Moves:")
    for key, value in move_set.items():
        if(value != -1):
            print("| {} |".format(value), end="")
            user_move_set[value] = key

    user_choice = int(input("\nEnter Value: "))


        

    if user_choice in user_move_set.keys():
        if(user_move_set[user_choice] == 'top'):
            board[nine_x][nine_y] = user_choice
            board[nine_x-1][nine_y] = 9
        elif(user_move_set[user_choice] == 'right'):
            board[nine_x][nine_y] = user_choice
            board[nine_x][nine_y+1] = 9
        elif(user_move_set[user_choice] == 'bottom'):
            board[nine_x][nine_y] = user_choice
            board[nine_x+1][nine_y] = 9
        elif(user_move_set[user_choice] == 'left'):
            board[nine_x][nine_y] = user_choice
            board[nine_x][nine_y-1] = 9
        print("\n")
    else:
        print("Invalid Move")
        
    if(calc_heuristic(board, answer) == 0):
        print("You have won the game!!!")
    else:
        print("Heuristic value: {}".format(calc_heuristic(board, answer)))

print_board(generated_board)

while(True):
    run_game(generated_board, answer_board)
    print_board(generated_board)

len(generated_board)

test_board = [[1,2,3],[4,5,6],[7,9,8]]

print_board(test_board)

while(True):
    run_game(test_board, answer_board)
    print_board(test_board)

l = []
p = []
while True:
    num = random.randint(1, 9)
    if num not in p:
        p.append(num)
    if len(p) == 9:
        break
puzzle = []
for i in p:
    if len(l) != 3:
        l.append(i)
    else:
        puzzle.append(l)  # generating 3*3 matrix
        l = []
        l.append(i)
puzzle.append(l)

print(puzzle)

puzzle = [[1,2,3],[4,5,6],[9,7,8]]

def get_index(puzzle, target):
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] == target:
                return i, j

desired = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
desired_cp = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def print_puzzle(puzzle):
    for i in range(3):
        print('|{}|{}|{}|'.format(puzzle[i][0], puzzle[i][1], puzzle[i][2]))

print_puzzle(puzzle)

while(puzzle != desired):
    print_puzzle(puzzle)
    choice = int(
        input("Enter number(1-8) to move (9 is blank):\nEnter 0 to exit.\n"))
    if choice == 0:
        break
    x, y = get_index(puzzle, choice)
    x_b, y_b = get_index(puzzle, 9)
    d1 = abs(x_b-x)
    d2 = abs(y_b-y)
    if (d1 == 1 and d2 == 1):
        print("Can't touch this")
        continue
    stat = 0
    if d1 == 1 and (d2 == 0 or d2 == 1):
        stat = 1
    elif d2 == 1 and (d1 == 0 or d1 == 1):
        stat = 1
    if stat == 1:
        puzzle[x][y], puzzle[x_b][y_b] = puzzle[x_b][y_b], puzzle[x][y]
    else:
        print("Can't touch this too")
        continue
if(puzzle == desired):
    print("You have won!")
if(choice == 0):
    print("You lost!")

x, y = get_index(puzzle, 6)
print('{}|{}'.format(x, y))

x, y = get_index(puzzle, 9)
print('{}|{}'.format(x, y))

x, y = get_index(puzzle, 7)
print('{}|{}'.format(x, y))