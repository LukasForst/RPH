import csv

""""# test matrix -------------------------------------------------
# self.opponent_color = 1
# self.my_color = 0
# self.board = [\
     [-1,  0,  0,  0, -1,  1, -1,  0], #0
     [-1,  1,  0,  1, -1,  0,  1, -1], #1
     [ 1,  0,  0,  0,  1,  1,  1,  1], #2
     [-1, -1,  1,  0,  0,  0, -1, -1], #3
     [-1,  1,  1,  0,  1,  1,  1,  1], #4
     [ 0, -1,  1,  0,  1,  1, -1, -1], #5
     [-1,  1,  1,  0,  0,  1,  1, -1], #6
     [ 0, -1,  1,  0, -1, -1,  1, -1]] #7

# print(self.diagonal_right_bottom(7,7))
# print(self.diagonal_left_upper(7,7))
# print(self.diagonal_left_bottom(7, 3))
# print(self.left_side(3,2))
# print(self.possible_moves)
# test matrix -------------------------------------------------"""


# --------------------------------------------------------

"""for row in range(0,self.rows-1):
            if (self.board[row][0] == self.opponent_color):
                if(self.board[row+1][0] == self.position_is_empty):
                    self.bottom_side(row,0)
            if (self.board[row][7] == self.opponent_color):
                self.bottom_side(row, 7)

        for column in range(0,self.columns-1):
            if (self.board[0][column] == self.opponent_color):
                if (self.board[0][column + 1] == self.position_is_empty):
                    self.right_side(0, column)
            if(self.board[7][column] == self.opponent_color):
                if(self.board[7][column + 1] == self.position_is_empty):
                    self.right_side(7,column)

        for column in range(1, self.columns):
            if (self.board[0][column] == self.opponent_color):
                if (self.board[0][column - 1] == self.position_is_empty):
                    self.left_side(0, column)
            if (self.board[7][column] == self.opponent_color):
                if (self.board[7][column - 1] == self.position_is_empty):
                    self.left_side(7, column)

        # TODO - vyresit krajni hodnoty

                if (self.board[0][column] == self.opponent_color):
                        if (self.board[0][column + 1] == self.position_is_empty):
                            self.right_side(0, column)
                    if (self.board[7][column] == self.opponent_color):
                        if (self.board[7][column + 1] == self.position_is_empty):
                            self.right_side(7, column)
            if (self.board[row][0] == self.opponent_color):
                if(self.board[row+1][0] == self.position_is_empty):
                    self.bottom_side(row,0)
            if (self.board[row][7] == self.opponent_color):
                self.bottom_side(row, 7)"""
#---------------------------------------------------------
class ReversiIO(object):
    
    @staticmethod
    def save_state_with_moves(file_name,board,moves,move_color):
        with open(file_name, 'wb') as outfile:
            for x in range(len(board)):
                row_string = ''
                for y in range(len(board[x])):
                    row_string += str(board[x][y])+' '
                outfile.write(row_string+'\n')
            outfile.write('\n')
            outfile.write(str(move_color)+'\n')
            outfile.write('\n')
            for i in range(len(moves)):
                row_string = str(moves[i][0])+' '+str(moves[i][1])+' '
                outfile.write(row_string+'\n')
            
            
    @staticmethod
    def load_state_with_moves(file_name):
        board_size = 8 
        board = [-1]*board_size
        player = -1;
        moves = []
        for row in range(board_size):
            board[row] = [-1]*board_size
        with open(file_name, 'r') as f:
            lines = f.readlines()
            for linei in range(0,8):
                stones = lines[linei].split()
                for st_id in range(len(stones)):
                    board[linei][st_id] = int(stones[st_id])
            player = int(lines[9])
            for linei in range(11,len(lines)):
                move = lines[linei].split()
                moves.append((int(move[0]) , int(move[1])))
            #print(board)
            return {'board':board,'player':player,'moves':moves}        

if __name__ == '__main__':
    a = ReversiIO.load_state_with_moves("dataset/game1_state33.txt")

    """if (self.board[0][column] == self.opponent_color):
                            if (self.board[0][column - 1] == self.position_is_empty):
                                self.left_side(0, column)
                            if (self.board[0][column + 1] == self.position_is_empty):
                                self.right_side(0, column)
                        if (self.board[7][column] == self.opponent_color):
                            if (self.board[7][column - 1] == self.position_is_empty):
                                self.left_side(7, column)
                            if (self.board[7][column + 1] == self.position_is_empty):
                                self.right_side(7, column)"""