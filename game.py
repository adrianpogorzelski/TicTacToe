import random
import math

# PLAYER CLASS
class Player():
    def __init__(self, controlledBy):
        self.score = 0
        self.symbol = 0
        self.controlledBy = controlledBy
        self.setName()

    def setName(self):
        self.playerName = 'CPU'
        if self.controlledBy == 'Player':
            self.playerName = input("Enter " + self.controlledBy + " name: ")

    def setPlayerSymbol(self):
        r = random.randint(0, 1)
        if r == 0:
            self.symbol = 'O'
            cpu.symbol = 'X'
        else:
            self.symbol = 'X'
            cpu.symbol = 'O'
        print('*********')
        print("Playing as " + player.symbol)

# BOARD CLASS
class Board():
    def __init__(self):
        # CREATE BOARD
        self.board = [1,2,3,4,5,6,7,8,9]

        # Scoring threes
        self.topRow = [self.board[0], self.board[1], self.board[2]]
        self.middleRow = [self.board[3], self.board[4], self.board[5]]
        self.bottomRow = [self.board[0], self.board[0], self.board[0]]
        self.leftColumn = [self.board[0], self.board[0], self.board[0]]
        self.centerColumn = [self.board[0], self.board[0], self.board[0]]
        self.rightColumn = [self.board[0], self.board[0], self.board[0]]
        self.topDiagonal = [self.board[0], self.board[0], self.board[0]]
        self.bottomDiagonal = [self.board[0], self.board[0], self.board[0]]
        # Print board

    def drawBoard(self):
        print("[" + str(self.board[0]) + "] [" + str(self.board[1]) + "] [" + str(self.board[2]) + "]")
        print("[" + str(self.board[3]) + "] [" + str(self.board[4]) + "] [" + str(self.board[5]) + "]")
        print("[" + str(self.board[6]) + "] [" + str(self.board[7]) + "] [" + str(self.board[8]) + "]")

    def checkMove(self, input):
        if int(input) in self.board:
            return True

    # Players move
    def playerMove(self):
        ### PLAYER MOVE:
        playerInput = input('Your move (1-9): ')
        if self.checkMove(playerInput):
            self.board[int(playerInput) - 1] = player.symbol
        else:
            self.playerMove()
        self.drawBoard()
        self.cpuMove()
        #### DRAW MOVE ON BOARD
        #### CHECK FOR WIN
    ### CPU MOVE:
    def cpuMove(self):
        print('CPU move')
        cpuInput = random.randint(0, 8)
        if self.checkMove(cpuInput):
            self.board[int(cpuInput) - 1] = cpu.symbol
        else:
            self.cpuMove()
        self.drawBoard()
        self.playerMove()
    #### DRAW MOVE ON BOARD
        #### CHECK FOR WIN

def startGame():
    player.setPlayerSymbol()
    board = Board()
    board.drawBoard()
    if player.symbol == 'O':
        board.playerMove()
    else:
        board.cpuMove()

    ## PRINT RESULT
    print('Score:\n'+ player.playerName +': ' + str(player.score) + '\nCPU: ' + str(cpu.score))
    ## ASK FOR ANOTHER GAME
    def anotherGame():
        another = input('Do you want to play another round? (Y/N): ')
        if another.lower() == 'y':
            startGame()
        elif another.lower() == 'n':
            print("Thank you for playing!")
        else:
            anotherGame()
    anotherGame()

# GAME
if __name__=='__main__':
    # WELCOME MESSAGE
    print('Tic-Tac-Toe')
    print('*********')

    # CREATE PLAYERS
    player = Player('Player')
    cpu = Player('CPU')

    # START GAME
    startGame()