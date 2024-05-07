# Legend
# X for placing ship and hit battleship
# '-' for available space
# '-' for missed shot
from random import randint


# Defining the user's board and the Computer's board

user_board = [[' '] * 10 for i in range(10)]
computer_board = [[' '] * 10 for i in range(10)]

letters_to_numbers = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9}

def print_board():
    print("A B C D E F G")
    print("-------------")
    row_number = 1
    for row in board:
        print(row_number, "|".join(row))
        row_number += 1

def create_ships():
    for ship in range(5):
        ship_row, ship_column = randint(0,9), randint(0,9)
        while board[ship_row][ship_column] == 'x':
            ship_row, ship_column = randint(0,9), randint(0,9)
        board[ship_row][ship_column] = 'x'
def get_ship_location():
    row = input('Please enter a ship row 1-10').lower
    while row not in '12345678':
        print('Please enter a valid row')
    row = input('Please enter a ship row 1-10')
    column = input('Please enter a ship column A-J').lower
    while column not in 'abcdefghij':
        print("Please enter a valid column")
        column = input ('Please enter a ship column').lower
    return int(row) - 1, letters_to_numbers[column]


def count_hit_ships():
    count = 0
    for row in board:
        for column in row:
            if column == 'x':
                count += 1
    return count

create_ships()
turns = 10
print_board(user_board)
print_board(computer_board)
# while turns > 0:
    

