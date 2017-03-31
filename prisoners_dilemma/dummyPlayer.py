import random

class MyPlayer:
    '''DummyPlayer'''  # TODO - vymyslet zpusob, jakym hraje
    """
        navrh matice    payoff_matrix = [[(4,4), (1,6)],[(6,1), (2,2)]]
        obecne          payoff_matrix[coop, deffect]
    """

    def __init__(self, payoff_matrix,*number_of_iterations):  # hrac dostane vzdy payoff_matrix (2x2), number_of_iterations neni poviny -> metoda nesmi crashnout
        # pro nacteni cisla z matice payoff_matrix[0][0][0] -> (4,4) je tuple

        self.matrix_coop1 = payoff_matrix[0][0][0]  # numbers from matrix
        self.matrix_coop2 = payoff_matrix[0][1][0]
        self.matrix_def1 = payoff_matrix[1][0][0]
        self.matrix_def2 = payoff_matrix[1][1][0]

        print(self.matrix_coop1, self.matrix_coop2)
        print(self.matrix_def1, self.matrix_def2)
        self.move_record = []

    def move(self):
        return random.randint(0,1)
        #return True

    def record_opponents_move(self, opponent_move):  # vstup je posledni protivnikuv tah FALSE, TRUE
        if (opponent_move):
            self.move_record.append(0)
        else:
            self.move_record.append(1)


