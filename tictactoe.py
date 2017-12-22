import sys

class TicTacToe:
    
    def __init__(self):
        self.board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.player1 = None
        self.player2 = None
        self.crntPlayer = None
        self.players = ['X', 'Y']
        self.iswinner = None
    
    def defPlayer(self):
        self.player1 = raw_input('X or Y? ')
        if 'x' in self.player1.lower():
            self.player2 = 'Y'
            self.player1 = 'X'
        else:
            self.player2 = 'X'
            self.player1 = 'Y'
        self.crntPlayer = self.player1
    
    def reset(self):
        self.board = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
        self.defPlayer()
    
    def doMoves(self):
        try:
            self.printBoard()
            self.move = raw_input(self.crntPlayer + ', Where do you want to go? (1-9): ')
            if isinstance(int(self.move), int) == False:
                print '[ERROR] Please select a number!'
            else:
                self.board[int(self.move) - 1] = self.crntPlayer
                self.checkWin()
                if self.crntPlayer == self.player1:
                    self.crntPlayer = self.player2
                else:
                    self.crntPlayer = self.player1
        except Exception as e:
            print e
    
    def checkRow(self, move1, move2, move3):
        for i in self.players:
            if self.board[int(move1) - 1] == i and self.board[int(move2) - 1] == i and self.board[int(move3) - 1] == i:
                self.iswinner = self.crntPlayer
                return True
    
    def winner(self):
        if isinstance(self.iswinner, str):
            self.printBoard()
            print 'Player ' + self.crntPlayer + ' wins!'
            result = raw_input('Play again? (Y or N): ')
            if result.lower() == 'y':
                self.reset()
            else:
                print 'Thanks for playing!'
                sys.exit()
    
    def checkWin(self):
        if self.checkRow(1, 2, 3):
            self.winner()
        if self.checkRow(4, 5, 6):
            self.winner()
        if self.checkRow(7, 8, 9):
            self.winner()
        if self.checkRow(1, 4, 7):
            self.winner()
        if self.checkRow(1, 5, 9):
            self.winner()
        if self.checkRow(2, 5, 8):
            self.winner()
        if self.checkRow(3, 6, 9):
            self.winner()
        if self.checkRow(3, 5, 6):
            self.winner()
        
    def printBoard(self):
        print '|', self.board[0], '|', self.board[1], '|', self.board[2], '|'
        print '-------------'
        print '|', self.board[3], '|', self.board[4], '|', self.board[5], '|'
        print '-------------'
        print '|', self.board[6], '|', self.board[7], '|', self.board[8], '|'

game = TicTacToe()
game.defPlayer()
while True:
    game.doMoves()