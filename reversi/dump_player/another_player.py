from random import randint


class MyPlayer:
    """Randomly playing player."""

    def __init__(self, my_color, opponent_color):
        self.name = 'forstluk'  # student username
        self.my_color = my_color  # my color -> 1 or 0
        self.opponent_color = opponent_color  # opponent color -> 1 or 0
        self.board = []  # received board from system
        self.my_return_combination = ()  # my final return
        self.possible_moves = []  # combination of possible moves
        self.rows = 8
        self.columns = 8
        self.position_is_empty = -1

    def move(self, board):
        self.possible_moves = []
        self.board = board
        self.find_possible_moves()
        if(len(self.possible_moves)  ==  0):
            print(self.possible_moves)
            return None
        else:
            self.my_return_combination = self.possible_moves[randint(0, len(self.possible_moves) - 1)]
            return self.my_return_combination

    def find_possible_moves(self): # TODO algoritmus na zjisteni krajnich cisel
        """
        it will find every possible move

        :return: array filled with all possible moves
        """
        for row in range(1, self.rows - 1):
            for column in range(0, self.columns-1):
                if(self.board[row][column] == self.opponent_color):
                    if (self.board[row + 1][column] == self.position_is_empty):
                        self.bottom_side(row, column)
                    if (self.board[row + 1][column + 1] == self.position_is_empty):
                        self.diagonal_right_bottom(row, column)
                    if (self.board[row + 1][column - 1] == self.position_is_empty):
                        self.diagonal_left_bottom(row, column)
                    if (self.board[row - 1][column] == self.position_is_empty):
                        self.upper_side(row, column)
                    if (self.board[row - 1][column + 1] == self.position_is_empty):
                        self.diagonal_right_upper(row, column)
                    if (self.board[row - 1][column - 1] == self.position_is_empty):
                        self.diagonal_left_upper(row, column)
                    if (self.board[row][column + 1] == self.position_is_empty):
                        self.right_side(row,column)
                    if (self.board[row][column - 1] == self.position_is_empty):
                        self.left_side(row, column)

                    if (self.board[0][column] == self.opponent_color):
                        if (self.board[0][column - 1] == self.position_is_empty):
                            self.left_side(0, column)
                        if (self.board[0][column + 1] == self.position_is_empty):
                            self.right_side(0, column)
                    if (self.board[7][column] == self.opponent_color):
                        if (self.board[7][column - 1] == self.position_is_empty):
                            self.left_side(7, column)
                        if (self.board[7][column + 1] == self.position_is_empty):
                            self.right_side(7, column)



    def find_winning_moves(self):  # TODO find best move
        pass

    def diagonal_left_upper(self, row, column):
        """
        checks upper left diagonal position
        :param row: opponents position row
        :param column: opponents position column
        :return: True or False -> found move or not
        """
        diagonal_mover = 1
        if(row-1 < 0 or column-1 < 0):
            return False
        elif(self.board[row-diagonal_mover][column-diagonal_mover] == self.position_is_empty):
            while(row+diagonal_mover < self.rows and column+diagonal_mover < self.columns):
                if(self.board[row+diagonal_mover][column+diagonal_mover] == self.opponent_color):
                    diagonal_mover += 1
                    continue
                elif(self.board[row+diagonal_mover][column+diagonal_mover] == self.position_is_empty):
                    return False
                elif(self.board[row+diagonal_mover][column+diagonal_mover] == self.my_color):
                    self.possible_moves.append((row-1,column-1))
                    return True
                return False
        else:
            return False
    def diagonal_left_bottom(self, row, column):
        """
        checks bottom left diagonal position
        :param row: opponents position row
        :param column: opponents position column
        :return: True or False -> found move or not
        """
        diagonal_mover = 1
        if (row+1 >= self.rows or column - 1 < 0):
            return False
        elif (self.board[row+diagonal_mover][column - diagonal_mover] != self.my_color):
            while (row-diagonal_mover != -1 and column + diagonal_mover < self.columns):
                if (self.board[row - diagonal_mover][column + diagonal_mover] == self.opponent_color):
                    diagonal_mover += 1
                    continue
                elif (self.board[row - diagonal_mover][column + diagonal_mover] == self.position_is_empty):
                    return False
                elif (self.board[row - diagonal_mover][column + diagonal_mover] == self.my_color):
                    self.possible_moves.append((row + 1, column - 1))
                    return True
                return False
        else:
            return False
    def diagonal_right_upper(self, row, column):
        """
        checks upper right diagonal position
        :param row: opponents position row
        :param column: opponents position column
        :return: True or False -> found move or not
        """
        diagonal_mover = 1
        if (row - 1 < 0 or column+1 >= self.columns):
            return False
        elif (self.board[row - diagonal_mover][column + diagonal_mover] != self.my_color):
            while (row + diagonal_mover < self.rows and column - diagonal_mover != -1):
                if (self.board[row + diagonal_mover][column - diagonal_mover] == self.opponent_color):
                    diagonal_mover += 1
                    continue
                elif (self.board[row + diagonal_mover][column - diagonal_mover] == self.position_is_empty):
                    return False
                elif (self.board[row + diagonal_mover][column - diagonal_mover] == self.my_color):
                    self.possible_moves.append((row - 1, column + 1))
                    return True
                return False
        else:
            return False
    def diagonal_right_bottom(self, row,column):
        """
        checks bottom right diagonal position
        :param row: opponents position row
        :param column: opponents position column
        :return: True or False -> found move or not
        """
        diagonal_mover = 1
        if(row+1 >= self.rows or column+1 >= self.columns):
            return False
        elif(self.board[row+diagonal_mover][column+diagonal_mover] == self.position_is_empty):
            while(row-diagonal_mover != -1 and column-diagonal_mover != -1):
                if(self.board[row-diagonal_mover][column-diagonal_mover] == self.opponent_color):
                    diagonal_mover += 1
                    continue
                elif(self.board[row-diagonal_mover][column-diagonal_mover] == self.position_is_empty):
                    return False
                elif(self.board[row-diagonal_mover][column-diagonal_mover] == self.my_color):
                    self.possible_moves.append((row+1,column+1))
                    return True
                return False
        else:
            return False

    def left_side(self, row, column):
        side_mover = 1
        if(column - side_mover == -1):
            return False
        elif(self.board[row][column-side_mover] == self.position_is_empty):
            while (column + side_mover < self.columns):
                if(self.board[row][column+side_mover] == self.opponent_color):
                    side_mover += 1
                    continue
                elif(self.board[row][column+side_mover] == self.position_is_empty):
                    return False
                elif (self.board[row][column+side_mover] == self.my_color):
                    self.possible_moves.append((row, column - 1))
                    return True
                return False
        else:
            return False
    def right_side(self, row, column):
        side_mover = 1
        if (column + side_mover > self.columns):
            return False
        elif (self.board[row][column + side_mover] == self.position_is_empty):
            while (column - side_mover != -1):
                if (self.board[row][column - side_mover] == self.opponent_color):
                    side_mover += 1
                    continue
                elif (self.board[row][column - side_mover] == self.position_is_empty):
                    return False
                elif (self.board[row][column - side_mover] == self.my_color):
                    self.possible_moves.append((row, column + 1))
                    return True
                return False
        else:
            return False
    def upper_side(self, row, column):
        side_mover = 1
        if (row - side_mover == -1):
            return False
        elif (self.board[row - side_mover][column] == self.position_is_empty):
            while (row + side_mover < self.rows -1):
                if (self.board[row+side_mover][column] == self.opponent_color):
                    side_mover += 1
                    continue
                elif (self.board[row+side_mover][column] == self.position_is_empty):
                    return False
                elif (self.board[row+side_mover][column] == self.my_color):
                    self.possible_moves.append((row-1, column))
                    return True
                return False
        else:
            return False
    def bottom_side(self, row, column):
        side_mover = 1
        if (row + side_mover >= self.rows):
            return False
        elif (self.board[row + side_mover][column] == self.position_is_empty):
            while (row + side_mover < self.rows):
                if (self.board[row - side_mover][column] == self.opponent_color):
                    side_mover += 1
                    continue
                elif (self.board[row - side_mover][column] == self.position_is_empty):
                    return False
                elif (self.board[row - side_mover][column] == self.my_color):
                    self.possible_moves.append((row + 1, column))
                    return True
                return False
        else:
            return False
