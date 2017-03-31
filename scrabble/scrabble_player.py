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

    def evaluate_word(self, word):

        final_value = 0
        letter_value = config_scrabble.letter_value

        for key in letter_value.keys():
            for letter in word:
                if(key == letter):
                    final_value += letter_value[key]

        return final_value

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

        word = max(possible_words, key=possible_words.get)
        idx = 0
        for i in range(self.halfIDX, self.halfIDX + len(word)):
            tmp = list(word)
            board[7][i] = tmp[idx]
            idx += 1

        self.is_first_move = False
        return board

if __name__ == '__main__':
    sc = ScrabblePlayer('dictionary.txt')

    board = config_scrabble.board

    result = sc.play(board, "AHOJEPK")
    for i in result:
        print(i)

