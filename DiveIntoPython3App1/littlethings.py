'''
A tic tac toe game
'''

import os
import random

def draw_board(current_board=[1,2,3,4,5,6,7,8,9]):
    '''
    Print a 3 x 3 tic tac toe board.
    current_board is the list of spaces.
    returns current_board
    '''
    os.system("CLS")
    board = '''
{}|{}|{}
=====
{}|{}|{}
=====
{}|{}|{}
        '''
    print(str(current_board))
    print(board.format(current_board[0],
                       current_board[1],
                       current_board[2],
                       current_board[3],
                       current_board[4],
                       current_board[5],
                       current_board[6],
                       current_board[7],
                       current_board[8],))
    return current_board


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

def SpotTakenException:
    print("SpotTakenException:")
    pass

def place_move(current_board, where,who):
    '''
    take where(1-9) and who(X or O) and place that who in the where list location
    '''
    current_board = list(current_board)

    try:
        current_board.remove(where)
    except:
        raise SpotTakenException

    current_board.insert(where-1,who)

    return current_board

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
        where,who = ask_player('X')
        current_board = place_move(current_board, where,who)
        draw_board(current_board)

        check_for_winner(current_board)

        #Ask the computer where they want to go
        where,who= ask_player('O')
        current_board = place_move(current_board, where,who)
        draw_board(current_board)

        check_for_winner(current_board)


if __name__ == "__main__":
    play_tictactoe()