import os
clear = lambda : os.system('cls')

import random

def space_check(board, position):
    return board[position] == ' ' 

def full_board_check(board):
    for item in range(1,10):
        if board[item] == ' ':
            return False
    return True

def player_choice(board):
    global count
    value = player_input()
    result = space_check(board,value)
    while not result:
        print('')
        print("That position is full")
        count -= 1
        value = player_input()
        result = space_check(board,value)
    return value


def marker():
    if count%2 == 0:
        return "X"
    else:
        return "O"

def replay():
    ans = input('\nDo you want to play again? "Yes" or "No" : ')
    return ans == "Yes"
        
def display_board(Board):
    print(' \t |\t   |\t\n    {0}    |    {1}    |    {2}     \n\t |\t   |\t\t\n-----------------------------\n\t |\t   |\t\n    {3}    |    {4}    |    {5}   \n\t |\t   |\t\t\n-----------------------------\n \t |\t   |\t\n    {6}    |    {7}    |    {8}    \n\t |\t   |         '.format(Board[7],Board[8],Board[9],Board[4],Board[5],Board[6],Board[1],Board[2],Board[3]))

def player_input():
    global count
    val = 'temp'
    if count%2 == 0:
        while val not in [1,2,3,4,5,6,7,8,9]:
            val = int(input ("\nEnter your choice, Player 1:"))
            if val not in [1,2,3,4,5,6,7,8,9]:
                print("Incorrect Choice, try again!")
        count += 1
    else:
        while val not in [1,2,3,4,5,6,7,8,9]:
            val = int(input ("\nEnter your choice, Player 2:"))
            if val not in [1,2,3,4,5,6,7,8,9]:
                print("Incorrect Choice, try again!")
        count += 1
    return val

def place_marker(board, marker, position):
    if count%2 == 0:
        board[position] = marker
    else:
        board[position] = marker

def win_check(Board, mark):
    return (Board[1] == mark and Board[2] == mark and Board[3] == mark) or (Board[4] == mark and Board[5] == mark and Board[6] == mark) or (Board[7] == mark and Board[8] == mark and Board[9] == mark) or (Board[1] == mark and Board[4] == mark and Board[7] == mark) or (Board[2] == mark and Board[5] == mark and Board[8] == mark) or (Board[3] == mark and Board[6] == mark and Board[9] == mark) or (Board[7] == mark and Board[5] == mark and Board[3] == mark) or (Board[9] == mark and Board[5] == mark and Board[1] == mark)

while True:
    clear()
    print('Welcome to Tic Tac Toe!\nX starts first\n ')
    flag = True
    count = 0
    board = [' ']*10
    while not full_board_check(board):
        print("")
        display_board(board)
        print("")
        place_marker(board,marker(),player_choice(board))
        clear()
        if win_check(board,"X"):                                           
            print('')
            display_board(board)
            print('')
            print("The winner is player 1!")
            flag = False
            break
        elif win_check(board,"O"):
            print("")
            display_board(board)
            print('')
            print("The winner is player 2!")
            flag = False
            break
  
    if flag:
        print('')
        display_board(board)
        print('\nIt is a draw!')
    
    if not replay():
              break

print("\nAuthor: Arin Khatua\nVersion: 1.0\nThanks for playing!")
rand = input("")