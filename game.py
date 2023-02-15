import random
# WELCOME MESSAGE
print('Tic-Tac-Toe')
print('*********')
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

# CREATE PLAYERS
player = Player('Player')
cpu = Player('CPU')

# BOARD CLASS
class Board():
    board = [["[1]", "[2]", "[3]"], ["[4]", "[5]", "[6]"], ["[7]", "[8]", "[9]"]]
    # Board spaces
    topLeft = board[0][0]
    topCenter = board[0][1]
    topRight = board[0][2]
    midLeft = board[1][0]
    midCenter = board[1][1]
    midRight = board[1][2]
    bottomLeft = board[2][0]
    bottomCenter = board[2][1]
    bottomRight = board[2][2]
    # Scoring threes
    topRow = [topLeft, topCenter, topRight]
    middleRow = [midLeft, midCenter, midRight]
    bottomRow = [bottomLeft, bottomCenter, bottomRight]
    leftColumn = [topLeft, midLeft, bottomLeft]
    centerColumn = [topCenter, midCenter, bottomCenter]
    rightColumn = [topRight, midRight, bottomRight]
    topDiagonal = [topLeft, midCenter, bottomRight]
    bottomDiagonal = [bottomLeft, midCenter, topRight]

    def __init__(self):
        for arr in self.board:
            for space in arr:
                print(space, end="")
            print()

# GAME
def startGame():
    player.setPlayerSymbol()
    ## CREATE NEW BOARD
    board = Board()
    ## PLAYERS MOVE LOOP:
    ### PLAYER MOVE:
    #### DRAW MOVE ON BOARD
    #### CHECK FOR WIN
    ### CPU MOVE:
    #### DRAW MOVE ON BOARD
    #### CHECK FOR WIN
    ## PRINT RESULT
    print('Score:\nPlayer: ' + str(player.score) + '\nCPU: ' + str(cpu.score))
    ## ASK FOR ANOTHER GAME
    def anotherGame():
        another = input('Do you want to play another round? (Y/N): ')
        if another == 'y':
            startGame()
        elif another == 'n':
            print("Thank you for playing!")
        else:
            anotherGame()
    anotherGame()

startGame()