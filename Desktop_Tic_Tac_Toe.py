##Desktop Tic Tac Toe
import random

StillPlaying=True
Winner=None
CurrentPlayer=None

#Create the game board
GAME_BOARD = ['-', '-', '-',
              '-', '-', '-',
              '-', '-', '-']

#Computer player class
class Player2():
    def __init__(self):
        self.symbol=None
    
    def computer_symbol(self):
        global CurrentPlayer
        if CurrentPlayer == 'X':
            self.symbol = 'O'
        else:
            self.symbol = 'X'
        
    
    def computer_turn(self):
        aimove = random.randint(0,8)
        if aimove >=1 and aimove <=9 and GAME_BOARD[aimove] == '-':
            GAME_BOARD[aimove] = self.symbol
        else:
            return self.computer_turn()
            
#Functionality        
def draw_board():
    print(GAME_BOARD[0], '|', GAME_BOARD[1], '|', GAME_BOARD[2])
    print(GAME_BOARD[3], '|', GAME_BOARD[4], '|', GAME_BOARD[5])
    print(GAME_BOARD[6], '|', GAME_BOARD[7], '|', GAME_BOARD[8])
    
def switch_player(player):
    CurrentPlayer=player
    
def take_turn():
    move = int(input('Choose a tile from 1-9: '))
    try:
        if move >=1 and move <=9 and GAME_BOARD[move-1] == '-':
            GAME_BOARD[move-1] = player_1
        else:
            print("That tile's already taken! Try another.")
            return take_turn()
    except ValueError():
        print("You must choose a number from 1-9, try again!")
        return

##Check for win conditions
def horizontal_win():
    global Winner
    global StillPlaying
    global CurrentPlayer
    if GAME_BOARD[0] == GAME_BOARD[1] == GAME_BOARD[2] and GAME_BOARD[0] != '-':
        print(f"Congratulations {CurrentPlayer}!")
        Winner=CurrentPlayer
        StillPlaying=False
    elif GAME_BOARD[3] == GAME_BOARD[4] == GAME_BOARD[5] and GAME_BOARD[3] != '-':
        print(f"Congratulations {CurrentPlayer}!")
        Winner=CurrentPlayer
        StillPlaying=False
    elif GAME_BOARD[6] == GAME_BOARD[7] == GAME_BOARD[8] and GAME_BOARD[6] != '-':
        print(f"Congratulations {CurrentPlayer}!")
        Winner=CurrentPlayer
        StillPlaying=False
    else:
        pass
        
def diagonal_win():
    global Winner
    global StillPlaying
    global CurrentPlayer
    if GAME_BOARD[0] == GAME_BOARD[4] == GAME_BOARD[8] and GAME_BOARD[0] != '-':
        print(f"Congratulations {CurrentPlayer}!")
        Winner=CurrentPlayer
        StillPlaying=False
    elif GAME_BOARD[6] == GAME_BOARD[4] == GAME_BOARD[2] and GAME_BOARD[6] != '-':
        print(f"Congratulations {CurrentPlayer}!")
        Winner=CurrentPlayer
        StillPlaying=False
    else:
        pass
    
def vertical_win():
    global Winner
    global CurrentPlayer
    global StillPlaying
    if GAME_BOARD[0] == GAME_BOARD[3] == GAME_BOARD[6] and GAME_BOARD[0] != '-':
        print(f"Congratulations {CurrentPlayer}!")
        Winner=CurrentPlayer
        StillPlaying=False
    elif GAME_BOARD[1] == GAME_BOARD[4] == GAME_BOARD[7] and GAME_BOARD[1] != '-':
        print(f"Congratulations {CurrentPlayer}!")
        Winner=CurrentPlayer
        StillPlaying=False
    elif GAME_BOARD[2] == GAME_BOARD[5] == GAME_BOARD[8] and GAME_BOARD[2] != '-':
        print(f"Congratulations {CurrentPlayer}!")
        Winner=CurrentPlayer
        StillPlaying=False
    else:
        pass
##Game
while StillPlaying:
    print("Hello! Welcome to my desktop tic-tac-toe game. Hope you like it!")
    player_1 = input("Please choose X or O: ")
    CurrentPlayer=player_1
    player_2 = Player2()
    player_2.computer_symbol()
    draw_board()
    while not Winner:
        take_turn()
        draw_board()
        horizontal_win()
        vertical_win()
        diagonal_win()
        switch_player(player_2)
        player_2.computer_turn()
        print("                    ")
        draw_board()
play_again = input("Would you like to play again? Y or N: ")
if play_again == 'Y':
    Winner=None
    StillPlaying=True
else:
    print("Ok, thanks for playing!")