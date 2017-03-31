class MyPlayer:
    """Plays according to the profit from matrix, in the end plays to win."""

    def __init__(self, payoff_matrix,number_of_iterations = 0):
        # player always get payoff_matrix (2x2), number_of_iterations is optional

        self.matrix_coop1 = payoff_matrix[0][0][0]  # numbers from matrix
        self.matrix_coop2 = payoff_matrix[0][1][0]  # matrix comes from game eg.
        self.matrix_def1 = payoff_matrix[1][0][0]   # 4,4 - 1,6
        self.matrix_def2 = payoff_matrix[1][1][0]   # 6,1 - 2,2

        self.tactics_changed = False  # change switch, used for controlling of changing tactics
        self.special_tactics = None  # get special tactics based on maximum opponents loss
        self.cooperate_move = None
        self.tactics = None  # final return tactics

        self.opponent_move_record = []  # recording opponent moves
        self.number_of_rounds = 0

        if (number_of_iterations != 0):  # number of iterations available or not
            self.number_of_iterations = number_of_iterations[0]
            self.iterations_available = True
        else:
            self.iterations_available = False

        MyPlayer.set_tactics(self)  # get starting tactics based on matrix analysis

    def record_opponents_move(self, opponent_move):  # recording opponents move - FALSE = cooperate, TRUE = defect
        self.opponent_move_record.append(opponent_move)

    def move(self):
        if(self.number_of_rounds == 10 or self.number_of_rounds == 12):
            MyPlayer.try_cooperate(self)  # player tries to cooperate with opponent

        if(self.iterations_available):  # check for availability of number_of_iterations
            if(self.number_of_iterations < self.number_of_rounds + 15):  # for last 15 rounds will player use special_tactics
                return self.special_tactics

        if(self.number_of_rounds > 12 and self.number_of_rounds%2 == 0):
            MyPlayer.check_cheating(self)

        print(self.tactics)
        self.number_of_rounds += 1
        return self.tactics

    def set_tactics(self):  # if there're more points for defect, player plays defect, otherwise coop
        if((self.matrix_coop1 + self.matrix_coop2) < (self.matrix_def1 + self.matrix_def2)):
            self.basic_tactics = True  # DEFECT
        else:
            self.basic_tactics = False  # COOPERATE

        if(self.matrix_coop1 == 0 or self.matrix_coop1 == 0):
            self.basic_tactics = False
        elif(self.matrix_def1 == 0 or self.matrix_def2 == 0):
            self.basic_tactics = True

        self.tactics = self.basic_tactics

        if(self.matrix_coop1 > self.matrix_def2):  # cooperate move  - possibility, that 2x defect is bigger than coop
            self.cooperate_move = False
        else:
            self.cooperate_move = True

        if(max(self.matrix_coop1, self.matrix_coop2) >= max(self.matrix_def1, self.matrix_def2)):  # player will find biggest reward and set it as a special_tactics
            self.special_tactics = False
        else:
            self.special_tactics = True

    def try_cooperate(self):
        if(self.tactics_changed == False and self.opponent_move_record[-1]):
            self.tactics = self.cooperate_move
            self.tactics_changed = True
        else:
            if(self.opponent_move_record[-1] != self.cooperate_move):
                self.tactics = self.basic_tactics
                self.tactics_changed = False

    def check_cheating(self):  # checking if is the opponent defecting me while I cooperate
        if(self.opponent_move_record[-1] == self.opponent_move_record[-2] == self.opponent_move_record[-3] == self.cooperate_move):
            self.tactics = self.cooperate_move
        else:
            self.tactics = self.basic_tactics
