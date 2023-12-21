# Написать игру в “Крестики-нолики”. Можете использовать
# любые парадигмы, которые посчитаете наиболее
# подходящими. Можете реализовать доску как угодно - как
# одномерный массив или двумерный массив (массив массивов).
# Можете использовать как правила, так и хардкод, на своё
# усмотрение. Главное, чтобы в игру можно было поиграть через
# терминал с вашего компьютера.

board = [' ' for x in range(10)]

def insert_letter(letter, pos):
    board[pos] = letter

def space_is_free(pos):
    return board[pos] == ' '

def print_board(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

def is_winner(bo, le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or \
           (bo[4] == le and bo[5] == le and bo[6] == le) or \
           (bo[1] == le and bo[2] == le and bo[3] == le) or \
           (bo[7] == le and bo[4] == le and bo[1] == le) or \
           (bo[8] == le and bo[5] == le and bo[2] == le) or \
           (bo[9] == le and bo[6] == le and bo[3] == le) or \
           (bo[7] == le and bo[5] == le and bo[3] == le) or \
           (bo[9] == le and bo[5] == le and bo[1] == le)

def player_move():
    run = True
    while run:
        move = input("Выберите позицию для хода (1-9): ")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if space_is_free(move):
                    run = False
                    insert_letter('X', move)
                else:
                    print("Эта позиция уже занята!")
            else:
                print("Введите число от 1 до 9!")
        except:
            print("Введите число!")

def comp_move():
    possible_moves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possible_moves:
            board_copy = board[:]
            board_copy[i] = let
            if is_winner(board_copy, let):
                move = i
                return move

    corners_open = []
    for i in possible_moves:
        if i in [1,3,7,9]:
            corners_open.append(i)
    if len(corners_open) > 0:
        move = select_random(corners_open)
        return move

    if 5 in possible_moves:
        move = 5
        return move

    edges_open = []
    for i in possible_moves:
        if i in [2,4,6,8]:
            edges_open.append(i)
    if len(edges_open) > 0:
        move = select_random(edges_open)

    return move

def select_random(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]

def is_board_full(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def main():
    print("Добро пожаловать в игру Крестики-нолики!")
    print_board(board)

    while not(is_board_full(board)):
        if not(is_winner(board, 'O')):
            player_move()
            print_board(board)
        else:
            print("Компьютер победил!")
            break

        if not(is_winner(board, 'X')):
            move = comp_move()
            if move == 0:
                print("Ничья!")
            else:
                insert_letter('O', move)
                print("Компьютер сделал ход на позицию", move, ":")
                print_board(board)
        else:
            print("Вы победили!")
            break

    if is_board_full(board):
        print("Ничья!")

while True:
    answer = input("Хотите сыграть в Крестики-нолики? (да/нет): ")
    if answer.lower() == 'да' or answer.lower() == 'yes':
        board = [' ' for x in range(10)]
        print('-----------------------------------')
        main()
    else:
        break