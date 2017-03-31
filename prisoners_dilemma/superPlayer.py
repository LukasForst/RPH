class MyPlayer:
    """Muj uzasny hrac, ktery se pomalu uci premyslet"""

    def __init__(self, payoff_matrix, number_of_iterations=None, history=[]):
        self.payoff = payoff_matrix
        self.number_of_iterations = number_of_iterations
        self.history = history

    def move(self):
        COOPERATE = 0
        DEFECT = 1
        iteration = 1

        # Testuji, jestli hra bezi ponekolikate
        if iteration > 1:

            # Pokud v predchozim kole jsme hrali COOPERATE
            if self.history[-2] == 0:

                # Testuji, jestli souper taky zvolil COOPERATE
                # a oba jsme dostali 4 body
                if self.history[-1] == 0:
                    iteration += 1
                    return bool(COOPERATE)

                # Anebo hral DEFECT
                # a ja mam 1 bod, souper 6
                else:
                    iteration += 1
                    return bool(DEFECT)

            # Anebo v predchozim kole jsme hrali DEFECT
            else:

                # Testuji, jestli souper taky zvolil DEFECT
                # a oba jsme dostali 2 body
                if self.history[-1] == 1:
                    iteration += 1
                    return bool(COOPERATE)

                # Anebo hral COOPERATE
                # a ja mam 1 bod, souper 6, predpokladam, ze bude hrat DEFECT
                else:
                    iteration += 1
                    return bool(DEFECT)

        # Hrajeme poprve
        # Nevime, jak bude hrat souper
        else:
            # Testuji jestli se mi vyplati spolupracovat nebo podvest
            # Predpokladam, ze jsem hracem A
            #
            # Podle dane maice zjistim, ze se vyplati podvest (DEFECT)
            if self.payoff[COOPERATE][COOPERATE][0] + self.payoff[COOPERATE][DEFECT][0] > \
                            self.payoff[DEFECT][COOPERATE][0] + self.payoff[DEFECT][DEFECT][0]:
                iteration += 1
                return bool(COOPERATE)
            else:
                iteration += 1
                return bool(DEFECT)

    def record_opponents_move(self, opponent_move):
        self.history.append(opponent_move)