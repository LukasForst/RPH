class MyPlayer:
    '''DummyPlayer'''  # TODO - vymyslet zpusob, jakym hraje
    """
        navrh matice    payoff_matrix[[(4,4), (1,6)],[(6,1), (2,2)]]
        obecne          payoff_matrix[coop, deffect]
    """

    def __init__(self, payoff_matrix,
                 *number_of_iterations):  # hrac dostane vzdy payoff_matrix (2x2), number_of_iterations neni poviny -> metoda nesmi crashnout
        # pro nacteni cisla z matice payoff_matrix[0][0][0] -> (4,4) je tuple
        self.move_record = []
        if (number_of_iterations != None):
            self.iterations = number_of_iterations
            self.iter = True
        else:
            self.iter = False
        self.i = 0
        self.basic_tactic = False

    def move(self):  # TODO taktika tahu
        """if (len(self.move_record)%10 == 0):
            self.i += 1
            if(self.i %2 == 0):
                self.basic_tactic = True
            else:
                self.basic_tactic = False
        if(len(self.move_record) == 3):
            self.basic_tactic = True
        return self.basic_tactic"""
        return False

    def record_opponents_move(self, opponent_move):  # vstup je posledni protivnikuv tah FALSE, TRUE
        if (opponent_move):
            self.move_record.append(0)
        else:
            self.move_record.append(1)


if __name__ == "__main__":
    player = MyPlayer
    print(type(player))


