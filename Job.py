class Job:
    def __init__(self, prof, annual_income):
        self.prof = prof
        self.annual_income = annual_income


class Waiter(Job):
    def __init__(self, prof, annual_income, isPoor=True):
        super().__init__(prof, annual_income)
        self.isPoor = isPoor


class Builder(Job):
    def __init__(self, prof, annual_income, isPoor=False):
        super().__init__(prof, annual_income)
        self.isPoor = isPoor


class SoftwareEngineer(Job):
    def __init__(self, prof, annual_income, isPoor=False, isIT=True):
        super().__init__(prof, annual_income)
        self.isPoor = isPoor
        self.isIT = isIT


class Teacher(Job):
    def __init__(self, prof, annual_income, isPoor=False):
        super().__init__(prof, annual_income)
        self.isPoor = isPoor
