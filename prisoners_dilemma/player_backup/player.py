class MyPlayer:

    """analyzuje matici,hraje podle ni,pokusi se nejvyhodneji kooperovat s protivníkem"""

    #    navrh matice    payoff_matrix[[(4,4), (1,6)],[(6,1), (2,2)]]
    #    4,4 - 1,6
    #    6,1 - 2,2
    #    obecne          payoff_matrix[coop, defect]
    #    cilem je nasbirat co nejmene bodu

    def __init__(self, payoff_matrix, *number_of_iterations): # number_of_iterations nemusi program dostat

        self.opponent_move_record = [] # pole se zaznamem tahu
        self.my_last_turn = None
        self.tactic = None # konecna taktika
        self.found_tactic = None # taktika sledovani oponenta
        self.changed = False # prepinac, pokud zmenim taktiku podle soupere = True
        self.iterations_available = False # dostupnost poctu iteraci
        self.steps = 0 # je rychlejsi pouzivat steps counting nez pokazde se dotazovat na len(self.opponent_move_record)

        self.matrix_coop1 = payoff_matrix[0][0][0] # dosazeni do promenych z poli
        self.matrix_coop2 = payoff_matrix[1][0][0]
        self.matrix_def1 = payoff_matrix[0][1][0]
        self.matrix_def2 = payoff_matrix[1][1][0]

        if(number_of_iterations):  # overeni, zdali je number_of_iteration k dispozici
            self.iterations = number_of_iterations[0]
            self.iterations_available = True
        else:
            self.iterations_available = False

        MyPlayer.get_basic_tactic(self)

    def record_opponents_move(self, opponent_move): # vstup je posledni protivnikuv tah FALSE = cooperate, TRUE = defect
        if(opponent_move):
            self.opponent_move_record.append(True) # defect
        else:
            self.opponent_move_record.append(False) # cooperate

    def get_basic_tactic(self): # metoda pro zjisteni idealni taktiky
        if((self.matrix_coop1 + self.matrix_coop2) < (self.matrix_def1 + self.matrix_def2)): # analyza matice, pokud je soucet vice bodu za coop tak def jinak opacne
            self.basic_tactics = True # klasicka taktika vypoctena z vyhodnosti matice
        else:
            self.basic_tactics = False
        self.tactic = self.basic_tactics

    def opponent_same_tactic(self): # zjisteni, jestli protivnik nehraje porad stejne
        opponent_basic_move = self.opponent_move_record[0]
        opponent_same_tactic = False

        for i in range(1,self.steps):
            if(self.opponent_move_record[i] == opponent_basic_move):
                opponent_same_tactic = True
            else:
                opponent_same_tactic = False
                break

        if(opponent_same_tactic and self.opponent_move_record[-1]): # pokud ma porad stejnou taktiku a hraje Defect
            if(self.matrix_coop2 > self.matrix_def2):
                self.basic_tactics = True
                self.changed = True
            elif(self.matrix_coop2 < self.matrix_def2):
                self.basic_tactics = False
                self.basic_tactics = True
            else:
                MyPlayer.get_basic_tactic(self)

        elif(opponent_same_tactic and not self.opponent_move_record[-1]): # pokud ma porad stejnou taktiku a hraje Cooperate
            if(self.matrix_coop1 > self.matrix_coop2):
                self.basic_tactics = False
                self.changed = True
            elif(self.matrix_def1 < self.matrix_def2):
                self.basic_tactics = True
                self.changed = True
            else:
                MyPlayer.get_basic_tactic(self)


    def get_opponent_tactic(self): # zjisteni, zdali nehraje protivnik porad stejne

        # kontrola provedenych kroku
        # provadi se pouze pokud byla hrana vice nez 4 kola
        # take pouze pokud se schoduje posledni a predposledni tah soupere
        # diky tomu se da zjistit, zdali delsi dobu nehraje stejne tahy

        if(not self.changed):
            if (self.opponent_move_record[-1] == self.opponent_move_record[-2] == self.opponent_move_record[-3] == self.my_last_turn):
                if (self.matrix_coop2 < self.matrix_def2):
                    self.found_tactic = False
                else:
                    self.found_tactic = True
                self.tactic = self.found_tactic
                self.changed = True

        else: #pokud se protivnik neprispusobi, nastavi se klasicka taktika zpet
            if (self.opponent_move_record[-1] == self.opponent_move_record[-2] and self.my_last_turn != self.opponent_move_record[-1]):
                self.tactic = self.basic_tactics
                self.changed = False

    def opponent_cheating_check(self): # pokud e prizpusobim hraci a on mi zacne podvadet nastavim zpet klasickou taktiku
        for i in range(self.steps-1, self.steps-5, -1):
            if(self.my_last_turn != self.opponent_move_record[i]):
                MyPlayer.get_basic_tactic(self)
                self.changed = False
                break

    def move(self):  # vyhodnoceni a predani tahu pocitaci
        if (self.steps == 5 or self.steps == 6):  # po trech krocich se zkontroluje, jestli nehraju proti podobnemu hraci, jako jsem ja
            MyPlayer.get_opponent_tactic(self)
        elif (self.steps == 10 and not self.changed):  # po deseti krocich se zjisti, jestli protivnik nehraje porad stejne
            MyPlayer.opponent_same_tactic(self)
        elif(self.steps > 12 and self.steps%5 == 0 and self.changed):  # kontrola, zdali me protivnik nepodvadi pri nejvyhodnejsi taktice pro nas oba
            MyPlayer.opponent_cheating_check(self)

        self.steps += 1# pocet probehlych iteraci
        self.my_last_turn = self.tactic
        return self.tactic

