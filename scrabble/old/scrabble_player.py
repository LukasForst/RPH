import config_scrabble

class ScrabblePlayer:
    rows = 15
    columns = 15

    def __init__(self, dictionary_path):
        self.halfIDX = int(self.rows / 2) - 1

        self.is_first_move = True

        self.all_dictionary_words = {}

        self.hand_letters = ""

        with open(dictionary_path, encoding='utf-8') as file:
            for line in file.read().split('\n'):
                self.all_dictionary_words[line.upper()] = self.evaluate_word(line)

    def play(self, board, hand_letters):
        """
        buď textový řetězec s písmeny, která si hráč přeje místo tahu vyměnit (string)
        nebo 2D list se stavem desky po tahu
        :param board:
        :param hand_letters:
        :return:
        """
        possible_words = {}
        self.hand_letters = hand_letters
        hand_letters = ''.join(sorted(hand_letters.upper()))

        for word in self.all_dictionary_words.keys():
            word_sorted = ''.join(sorted(word))

            if word_sorted in hand_letters:
                possible_words[word] = self.all_dictionary_words[word]

        if len(possible_words) == 0:
            self.change_letters()

        else:
            return self.place_word(board, possible_words)

    def place_word(self, board, possible_words = {}):

        if not self.is_first_move:
            is_final = False

            final_words = {}
            final_word = ""

            start_row = 0
            start_column = 0
            direction = ""

            free_space = self.get_free_space(board, possible_words)



            for word in possible_words.keys():
                for space in free_space.values():
                    pass #TODO




            final_word = max(final_words, key=final_words.get)

            if "right" in direction:
                idx = 0
                tmp = list(final_word)

                for i in range(start_column, start_column+len(final_word)):
                    board[start_row][i] = tmp[idx]
                    idx += 1
            elif "down" in direction:
                idx = 0
                tmp = list(final_word)

                for i in range(start_row, start_row + len(final_word)):
                    board[i][start_column] = tmp[idx]
                    idx += 1
            else:
                self.change_letters()

        else:
            word = max(possible_words, key=possible_words.get)
            idx = 0
            for i in range(self.halfIDX, self.halfIDX + len(word)):
                tmp = list(word)
                board[7][i] = tmp[idx]
                idx += 1

            self.is_first_move = False
            return board

    def evaluate_word(self, word):

        final_value = 0
        letter_value = config_scrabble.letter_value

        for key in letter_value.keys():
            for letter in word:
                if(key == letter):
                    final_value += letter_value[key]

        return final_value

    def change_letters(self):
        return self.hand_letters

    def get_free_space(self, board, possible_words):
        right_free_space = {[0, 0] : 0}
        down_free_space = {[0, 0] : 0}
        free_space = 0

        for row in range(self.rows):
            for column in range(self.columns):
                if board[row][column] == '-':
                    continue



        """
        for row in range(self.rows):
            for column in range(self.columns):
                if (row == 0):
                    tmp_column = column

                    while (board[row][tmp_column] == '*' and board[row + 1][tmp_column] == '*'):
                        free_space += 1
                elif (row == self.rows - 1):
                    tmp_column = column

                    while (board[row][tmp_column] == '*' and board[row - 1][tmp_column] == '*'):
                        free_space += 1
                else:
                    tmp_column = column

                    while (board[row][tmp_column] == board[row - 1][tmp_column] == board[row - 1][
                        tmp_column] == '*'):
                        free_space += 1

                if (free_space > min(possible_words, key=possible_words.get)):
                    right_free_space[[row, column + 1]] = free_space
        """

if __name__ == '__main__':

    sc = ScrabblePlayer('dictionary.txt')

    board = config_scrabble.board

    result = sc.play(board, "HELLO")

    for i in range(len(result)):
        print(result[i])

    print('\n\n')
    board = config_scrabble.board

    result = sc.play(board, "HELLO")

    for i in range(len(result)):
        print(result[i])