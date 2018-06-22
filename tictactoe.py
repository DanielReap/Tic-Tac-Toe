import sys

class TicTacToe:
    
    def __init__(self):
        self.board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.players = ['X', 'Y']
        self.end = False
    
    def reset(self):
        self.board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.defPlayer()
    
    def defPlayer(self):
        self.player1 = raw_input('X or Y? ').upper()
        if self.player1 in self.players:
            if 'X' in self.player1:
                self.player2 = 'Y'
                self.player1 = 'X'
            else:
                self.player2 = 'X'
                self.player1 = 'Y'
            self.crntPlayer = self.player1
        else:
            print 'Please enter X or Y'
            self.defPlayer()
    
    def doMoves(self):
        try:
            self.printBoard()
            self.move = raw_input(self.crntPlayer + ', Where do you want to go? (1-9): ')
            if isinstance(int(self.move), int) == False: print '[ERROR] Please select a number!'
            else:
                if int(self.move) > 0 and int(self.move) <= 9:
                    if isinstance(self.board[int(self.move) - 1], int):
                        self.board[int(self.move) - 1] = self.crntPlayer
                        self.checkWin()
                        if self.crntPlayer == self.player1: self.crntPlayer = self.player2
                        else: self.crntPlayer = self.player1
                    else:
                        print 'Tile has been taken, try another!'
                else:
                    print 'Please select a number on the board!'
        except:
            print '[ERROR] Incorrect input, please try again!'
    
    def checkRow(self, move1, move2, move3):
        for i in self.players:
            if self.board[int(move1) - 1] == i and self.board[int(move2) - 1] == i and self.board[int(move3) - 1] == i:
                self.iswinner = self.crntPlayer
                return True
    
    def winner(self):
        if isinstance(self.iswinner, str):
            self.printBoard()
            print 'Player ' + self.iswinner + ' wins!'
            result = raw_input('Play again? (Y or N): ')
            if result.lower() == 'y':
                self.reset()
            else:
                if result.lower() == 'n':
                    self.end = True
                    print 'Thanks for playing!'
    
    def checkWin(self):
        win_rows = ['1,2,3', '4,5,6', '7,8,9', '1,4,7', '1,5,9', '2,5,8', '3,6,9', '3,5,6', '7,5,3']
        for i in win_rows:
            x = i.split(',')
            if self.checkRow(int(x[0]), int(x[1]), int(x[2])): self.winner()
        
    def printBoard(self):
        print '|', self.board[0], '|', self.board[1], '|', self.board[2], '|'
        print '-------------'
        print '|', self.board[3], '|', self.board[4], '|', self.board[5], '|'
        print '-------------'
        print '|', self.board[6], '|', self.board[7], '|', self.board[8], '|'

game = TicTacToe()
game.defPlayer()
while True:
    if game.end == True:
        break
    game.doMoves()
    