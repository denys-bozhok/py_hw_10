class Habits:
    def __init__(self, forfeit):
        self.forfeit = forfeit


class Smoking(Habits):
    def __init__(self, forfeit, income, isSmoking=False):
        super().__init__(forfeit)
        self.isSmoking = isSmoking
        self.income = income


class Alcohol(Habits):
    def __init__(self, forfeit, income, isAlco=False):
        super().__init__(forfeit)
        self.isAlco = isAlco
        self.income = income
