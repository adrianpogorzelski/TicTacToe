import random


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
        self.board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        # Scoring threes
        # Print board

    def drawBoard(self):
        print("[" + str(self.board[0]) + "] [" + str(self.board[1]) + "] [" + str(self.board[2]) + "]")
        print("[" + str(self.board[3]) + "] [" + str(self.board[4]) + "] [" + str(self.board[5]) + "]")
        print("[" + str(self.board[6]) + "] [" + str(self.board[7]) + "] [" + str(self.board[8]) + "]")

    def checkMove(self, input):
        if int(input) in self.board:
            return True

    def checkWin(self):
        topRow = [self.board[0], self.board[1], self.board[2]]
        middleRow = [self.board[3], self.board[4], self.board[5]]
        bottomRow = [self.board[6], self.board[7], self.board[8]]
        leftColumn = [self.board[0], self.board[3], self.board[6]]
        centerColumn = [self.board[1], self.board[4], self.board[7]]
        rightColumn = [self.board[2], self.board[5], self.board[8]]
        topDiagonal = [self.board[0], self.board[4], self.board[8]]
        bottomDiagonal = [self.board[6], self.board[4], self.board[2]]
        if len(set(topRow)) == 1\
                or len(set(middleRow)) == 1 \
                or len(set(bottomRow)) == 1 \
                or len(set(leftColumn)) == 1 \
                or len(set(centerColumn)) == 1 \
                or len(set(rightColumn)) == 1 \
                or len(set(topDiagonal)) == 1 \
                or len(set(bottomDiagonal)) == 1:
            return True

    # Players move
    def playerMove(self):
        ### PLAYER MOVE:
        playerInput = input('Your move (1-9): ')
        if self.checkMove(playerInput):
            self.board[int(playerInput) - 1] = player.symbol
        else:
            self.playerMove()
        #### DRAW MOVE ON BOARD
        self.drawBoard()
        #### CHECK FOR WIN
        if self.checkWin():
            print(player.playerName + " wins!")
            player.score += 1
            game.anotherGame()
        else:
            self.cpuMove()

    ### CPU MOVE:
    def cpuMove(self):
        cpuInput = random.randint(0, 8)
        if self.checkMove(cpuInput):
            print('CPU move')
            self.board[int(cpuInput) - 1] = cpu.symbol
        else:
            self.cpuMove()
        #### DRAW MOVE ON BOARD
        self.drawBoard()
        #### CHECK FOR WIN
        if self.checkWin():
            print("CPU wins!")
            cpu.score += 1
            game.anotherGame()
        else:
            self.playerMove()
        self.playerMove()

class Game():

    def startGame(self):
        player.setPlayerSymbol()
        board = Board()
        board.drawBoard()
        if player.symbol == 'O':
            board.playerMove()
        else:
            board.cpuMove()

    ## ASK FOR ANOTHER GAME
    def anotherGame(self):
        ## PRINT RESULT
        print('Score:\n' + player.playerName + ': ' + str(player.score) + '\nCPU: ' + str(cpu.score))
        self.another = input('Do you want to play another round? (Y/N): ')
        if self.another.lower() == 'y':
            self.startGame()
        elif self.another.lower() == 'n':
            print("Thank you for playing!")
            exit()
        else:
            self.anotherGame()

        self.anotherGame()


# GAME
if __name__ == '__main__':
    # WELCOME MESSAGE
    print('Tic-Tac-Toe')
    print('*********')

    # CREATE PLAYERS
    player = Player('Player')
    cpu = Player('CPU')

    # START GAME
    game = Game()
    game.startGame()
