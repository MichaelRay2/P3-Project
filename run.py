# Legend
# X for placing ship and hit battleship
# '-' for available space
# '-' for missed shot

import gspread
from google.oauth2.service_account import Credentials
# from random import randint

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('MR - Project 3')

score_sheet = SHEET.worksheet('results')

data = score_sheet.get_all_values()

print(data)

def get_score():
    global score
    score = int(input("Enter a score"))
    print(score)

get_score()

def update_score_sheet():
    score_sheet.update_cell(3,1,score)


update_score_sheet()



# def update_score_sheet(new_score, worksheet):
#     """
#     Updates scoresheet based on result of game
#     """


# Defining the user's board and the Computer's board

# HIDDEN_BOARD = [[' '] * 8 for x in range(8)]
# GUESS_BOARD = [[' '] * 8 for x in range(8)]

# letters_to_numbers = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}

# def print_board(board):
#     print("  A B C D E F G H")
#     print("  -------------")
#     row_number = 1
#     for row in board:
#         print("%d|%s|" % (row_number, "|".join(row)))
#         row_number += 1

# def create_ships(board):
#     for ship in range(5):
#         ship_row, ship_column = randint(0,7), randint(0,7)
#         while board[ship_row][ship_column] == 'x':
#             ship_row, ship_column = randint(0,7), randint(0,7)
#         board[ship_row][ship_column] = 'x'
# def get_ship_location():
#     row = input('Please enter a ship row 1-8')
#     while row not in '12345678':
#         print('Please enter a valid row')
#         row = input('Please enter a ship row 1-8')
#     column = input('Please enter a ship column A-H').upper()
#     while column not in 'ABCDEFGH':
#         print("Please enter a valid column")
#         column = input('Please enter a ship column').upper()
#     return int(row) - 1, letters_to_numbers[column]


# def count_hit_ships(board):
#     count = 0
#     for row in board:
#         for column in row:
#             if column == 'x':
#                 count += 1
#     return count

# create_ships(HIDDEN_BOARD)
# turns = 10
# print('Welcome to Battleships')
# while turns > 0:
#     # print_board(HIDDEN_BOARD)
#     print_board(GUESS_BOARD)
#     row, column = get_ship_location()
#     if GUESS_BOARD[row][column] == '-':
#         print('You already guessed that')
#     elif HIDDEN_BOARD[row][column] == 'x':
#         print('Nice, you hit a ship!!')
#         GUESS_BOARD[row][column] = 'x'
#         turns -= 1
#     else:
#         print("You missed")
#         GUESS_BOARD[row][column] = '-'
#         turns -= 1
#     if count_hit_ships(GUESS_BOARD) == 5:
#         print('You won the game')
#         result = "You Win."
#         break
#     print('You have ' + str(turns) + ' turns remaining')
#     if turns == 0:
#         print('Sorry, you ran out of turns, the game is Over.')
#         result = "You Lose."
#         break

# print(result)

# def update_score_sheet()
#     """
#     Update scoresheet
#     """
#     print("Updating scoresheet")
#     sales_worksheet
    


# while turns > 0:
    

