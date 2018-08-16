import random


def print_board():
    num = int(len(board) + 1 / 3)
    for i in range(num):
        for j in range(3):
            print(board[i][j], end=" ")
        print("")


def play(line, column, playerSign, player_type):
    if board[line][column] == '.':
        board[line][column] = playerSign
    else:
        if player_type == "real":
            print("you can not do that!!")
            line = int(input("enter number of line")) - 1
            column = int(input("enter number of column")) - 1
            play(line, column, playerSign, "computer")
        else:
            line = random.randint(0, 2)
            column = random.randint(0, 2)
            play(line, column, playerSign, "computer")


def is_winner(playerSign):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == playerSign:
            return True
        elif board[0][i] == board[1][i] == board[2][i] == playerSign:
            return True
    if board[0][0] == board[1][1] == board[2][2] == playerSign or board[0][2] == board[1][1] == \
            board[2][0] == playerSign:
        return True
    return False


def game(playerSign, type_of_player) -> bool:
    if 'turns' not in game.__dict__:
        game.turns = 0
    elif game.turns == 9:
        print_board()
        print("too close, it's a tie")
        return False
    game.turns += 1
    if type_of_player == "real":
        print("this is %s turn" % playerSign)
        print_board()
        line = int(input("enter number of line")) - 1
        column = int(input("enter number of column")) - 1
        play(line, column, playerSign, "real")
    elif type_of_player == "computer":
        line = random.randint(0, 2)
        column = random.randint(0, 2)
        play(line, column, playerSign, "computer")
    if is_winner(playerSign):
        print_board()
        print("%s win!!!" % playerSign)
        return False
    return True


board = [
    ['.',
     '.',
     '.'],
    ['.',
     '.',
     '.'],
    ['.',
     '.',
     '.']
]

playing = True
game_mode = int(input("choose the game mode: for 1 player enter 1 and for 2 players enter 2"))
while game_mode != 1 and game_mode != 2:
    print("you can't do that \n")
    game_mode = int(input("choose the game mode: for 1 player enter 1 and for 2 players enter 2"))
if game_mode == 2:
    while playing:
        playing = game('o', "real")
        if not playing:
            break
        playing = game('x', "real")
else:
    sign = input("choose your sign, x or o")
    while sign != 'x' and sign != 'o':
        print("you can't do that!!!\n")
        sign = input("choose your sign, x or o")
    while playing:
        playing = game(sign, "real")
        if not playing:
            break
        elif sign == 'x':
            playing = game('o', "computer")
        else:
            playing = game('x', "computer")
