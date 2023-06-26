from utils import get_instance


class Education:
    lvl = 0
    cost = 0

    def __init__(self):
        self.lvl = self.lvl
        self.cost = self.cost


class Oxford(Education):
    lvl = 5
    cost = 800

    def __init__(self):
        super().__init__()


class Academind(Education):
    lvl = 4
    cost = 500

    def __init__(self):
        super().__init__()


class KhanAcademy(Education):
    lvl = 3
    cost = 300

    def __init__(self):
        super().__init__()
