import random
import sys
import os
import time

class game_of_life:

    def __init__(self):
        self.row = 0
        self.column = 0
        self.board = []
        self.random = 0

    def get_board(self):
        x_cord = 0
        y_cord = 0
        row = input("Input row (1-60): ")
        column = input("Input column (1-60): ")
        rand_num = input("number of random life-form: ")

        self.row = int(row)
        self.column = int(column)
        self.random = int(rand_num)

        if (self.row > 60 or self.column > 60 or self.random > (self.row * self.column) ):
            return -1
        self.board = [['.' for i in range(0,int(column)+2)] for k in range (0,int(row)+2)]

        for row in range(self.row+2):
            for column in range(self.column+2):
                if (row == 0 or row == self.row+1):
                    self.board[row][column] = '#'
                elif (column == 0 or column == self.column+1):
                    self.board[row][column] = '#'



        for x in range(0,int(rand_num)):
            occupied = True
            while (occupied == True):
                x_cord = random.randrange(1,self.column+1)
                y_cord = random.randrange(1,self.row+1)
                if (self.board[y_cord][x_cord] == '.'):
                    occupied = False
            self.board[y_cord][x_cord] = 'O'


    
    def printboard(self):
        for row in self.board:
            for column in row:
                print(column, end = " ")
            print('')
    

def game_over(game):
    for row in game.board:
            for column in row:
                if (column == 'O'):
                    return False
    
    return True

def scanboard(game):
    templateboard = [[0 for i in range(0,game.column+2)] for k in range (0,game.row+2)]
    updateboard = [['.' for i in range(0,game.column+2)] for k in range (0,game.row+2)]

    for row in range(0,game.row+2):
        for column in range(0,game.column+2):
            if (game.board[row][column] == 'O'):
                templateboard[row][column] = 1
                updateboard[row][column] = 'O'

    

    for row in range(1,game.row+1):
        for column in range(1,game.column+1):
            chart_stats = templateboard[row][column+1]+templateboard[row][column-1]
            chart_stats = chart_stats + templateboard[row+1][column]+templateboard[row-1][column]
            chart_stats = chart_stats + templateboard[row+1][column-1] + templateboard[row+1][column+1]
            chart_stats = chart_stats + templateboard[row-1][column-1] + templateboard[row-1][column+1]

            if (game.board[row][column] == '.'):
                if (chart_stats == 3):
                    updateboard[row][column] = 'O'
            
            else:
                if (chart_stats > 3):
                    updateboard[row][column] = '.'
                elif(chart_stats < 2):
                    updateboard[row][column] = '.'
                elif(chart_stats == 3 or chart_stats == 2):
                    updateboard[row][column] = 'O'
            chart_stats = 0

    for row in range(1,game.row+1):
        for column in range(1,game.column+1):
            if (updateboard[row][column] == '.'):
                game.board[row][column] = '.'
            else:
                game.board[row][column] = 'O'

def playGOF():
    n = 1
    os.system("clear")
    print("Welcome to Conway's Game of Life!!!")
    game = game_of_life()
    while (game.get_board() == -1):
        print("input is invalid pls type in again!")
        continue
    game_not_end = False
    game.printboard()
    time.sleep(1/3)

    while(game_over(game) == False):
        os.system("clear")
        scanboard(game)
        game.printboard()
        print("This is generation " + str(n))
        print("You can do Ctrl + C to exit the game")
        n = n + 1
        time.sleep(1/3)
        print("")
        if (n == 100):
            os.system("clear")
            print("Wow your world is a century old!")
            time.sleep(2)
            
        elif (n == 1000):
            os.system("clear")
            print("All heil to the never ending empire!")
            time.sleep(2)
    
    print("Game has eneded... Your world lasted " + str(n) + " generations")
    decision = input("Start the game again? (Y/N):")

    while(True):
        if (decision == 'Y' or decision == 'y'):
            playGOF()
        elif (decision == 'N' or decision == 'n'):
            exit()
        else:
            print("Please type in your choice again!")
            decision = input("Start the game again? (Y/N):")

if __name__ == '__main__':
    print(locals())
    playGOF()
            

