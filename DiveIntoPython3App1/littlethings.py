'''
A tic tac toe game
'''

import random

def draw_board(current_board=[1,2,3,4,5,6,7,8,9]):
    '''
    Print a 3 x 3 tic tac toe board.
    current_board is the list of spaces.
    returns current_board
    '''
    board = '''
{}|{}|{}
=====
{}|{}|{}
=====
{}|{}|{}
        '''
    print(str(current_board))
    print(board.format(2,1,3,4,5,6,7,8,9))


def ask_player(who):
    '''
    Ask player 'num' where they want to go.
    Then return their move
    '''
    r=-1
    while r < 0 or r > 9:
        #Ask for location
        r_raw = input("Player {}'s turn. 0 to quit.\nWhere would you like to go? (1-9): ".format(who))
        try:
            r = int(r_raw)
        except:
            #if there's any error just ask again.
            r = -1
    if not r:
        # zero (0) was entered. quit.
        exit()
    else:
        # a 1-9 was entered. Return that move
        return (r,who)

def place_move(current_board, where,who):
    '''
    take where(1-9) and who(X or O) and place that who in the where list location
    '''
    pass

def check_for_winner(current_board):
    '''
    given a board, returns
    None = no winner
    X = X's won
    O = O's won
    C = Cat's eye - tie
    '''

    X = "X's won"
    O = "O's won"
    C = "Cat's eye - tie"
    
    return None



def play_tictactoe():
    # Main Control function

    #Print the blank board, and return a blank state
    current_board = draw_board()

    winner = None

    while not winner:


        #Ask the user where they want to go
        ask1,ask2 = ask_player('X')
        current_board = place_move(current_board, ask1,ask2)
        draw_board(current_board)

        check_for_winner(current_board)

        #Ask the computer where they want to go
        ask1,ask2 = ask_player('O')
        current_board = place_move(current_board, ask1,ask2)
        draw_board(current_board)

        check_for_winner(current_board)


if __name__ == "__main__":
    play_tictactoe()