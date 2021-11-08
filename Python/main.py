from player import HumanPlayer,ComputerPlayer
import time
import math
class TictacToe:
    def __init__(self):
        self.board = [' ' for x in range(9)] 
        self.current_winner = None

# make the tic tac toe board
    def print_board(self):
        for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def make_move(self,square,letter):
        # which squares are available for that player
        #and wht the letter for that player
        if self.board[square] == ' ':
            self.board[square] = letter
            
            if self.winner(square,letter):
                self.current_winner = letter
            return True
        return False
    
    # here we are cheking the position of how one player can win
    def winner(self,square,letter):
        # first check row
        row_ind = square //3
        row = self.board[row_ind*3 : (row_ind+1)*3 ]
        if all(spot == letter for spot in row):
            return True
        # check for column
        col_ind = square % 3
        col = [self.board[col_ind+i*3] for i in range(3)]
        if all( spot == letter for spot in col):
            return True
        diagonal_ind = square % 2
        if diagonal_ind == 0:
            # [0,4,8] or [2,4,6]
            diagonal1 = [self.board[i] for i in [0,4,8]]
            if all(spot == letter for spot in diagonal1):
                return True
            diagonal2 = [self.board[i] for i in [2,4,6]]
            if all(spot == letter for spot in diagonal2):
                return True
        # if all the checks fails
        return False
    
    def empty_squares(self):
        # check for empty square
        return ' ' in self.board
        
    def num_empty_squares(self):
        # return len(self.available_moves()) 
        return self.board.count(' ')
    def available_moves(self):
            # here we will append the available moves 
        moves = []
        
        for index , spot in enumerate(self.board):
            if spot == " ":
                # if the spot is blank or empty it will append that index
                moves.append(index)
        return moves
    # def available_moves(self):
    #     return [i for i, x in enumerate(self.board) if x == " "]
        
def play(game,x_player,y_player,print_game=True):
    
    # return the winner of the game ! or it will tie!!!
    if print_game:
        game.print_board_nums()
    letter = 'X' # starting letter for tic tac toe board
    
    # loop through while the game still has empty square
    # and unless of empty square we will break the loop
    while game.empty_squares():
        if letter == 'O':
            square = y_player.get_move(game)
        else:
            square = x_player.get_move(game)

        # lets define a function for making moves
        if game.make_move(square,letter):
            # after each move just print the game
            if print_game:
                print(letter + " make a move to that square {}".format(square))
                game.print_board()
                print(' ') # just emply line
        # need to change the player after each move
        
            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                    break
                # ends the loop and exits the game
                else:
                    return letter  
            # else we just switch player and carry forward to
            # the game
            
            letter = 'O' if letter == 'X' else 'X'  # switches player
            
        time.sleep(.80)
        
    if game.current_winner == None:
        print('It\'s a tie')
        
            

if __name__ == '__main__':
    x_player = HumanPlayer('X')
    y_player = ComputerPlayer('O')
    t = TictacToe()
    play(t,x_player,y_player,print_game=True)
    
    
