from random import randint


class Property:
    def __init__(self,name, additional_social_status, cost=0):
        self.additional_social_status = additional_social_status
        self.cost = cost
        self.name = name

class Car(Property):
    def __init__(self, name, additional_social_status, additional_lifetime, cost=0):
        super().__init__(name, additional_social_status, cost)
        self.additional_lifetime = additional_lifetime


class House(Property):
    def __init__(self, name, additional_social_status, additional_lifetime, cost=0):
        super().__init__(name, additional_social_status, cost)
        self.additional_lifetime = additional_lifetime


class Phone(Property):
    def __init__(self, name, additional_social_status, increased_chance, cost=0):
        super().__init__(name, additional_social_status, cost)
        self.increased_chance = increased_chance

    def call_ambulance(self):

        isAlive = randint(0, 1)
        if isAlive == 1:
            return "Alive"
        else:
            return "Doctor has been studying by his self"


class Laptop(Property):
    def __init__(self, name, additional_social_status, cost=0):
        super().__init__(name, additional_social_status, cost)

    def get_aducation_into_IT_step(self):
        isHardWorker = randint(0, 8)
        if isHardWorker == 7:
            return 5
        else:
            return 1
