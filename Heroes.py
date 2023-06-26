from random import randint

from utils.name_generator import name_generator

from constants import *


class Human:
    years_old = 0

    def __init__(self, name=name_generator(NAMES_BY_DEFAULT, 0, 2), capital=CAPITAL_BY_DEFAULT["poor"], endpoint=END_POINT_BY_DEFAULT["poor"], social_status=SOCIAL_STATUS_BY_DEFAULT["poor"], iq=IQ_BY_DEFAULT["poor"], bag=BAG_BY_DEFAULT["poor"]):
        self.name = name
        self.age = self.years_old
        self.capital = capital
        self.endpoint = endpoint
        self.social_status = social_status
        self.iq = iq
        self.bag = bag


class PoorHuman(Human):
    def __init__(self, name):
        super().__init__(name=name)


class AvarageHuman(Human):
    def __init__(
            self,
            name,
            capital=CAPITAL_BY_DEFAULT["average"],
            endpoint=END_POINT_BY_DEFAULT["average"],
            social_status=SOCIAL_STATUS_BY_DEFAULT["average"],
            iq=IQ_BY_DEFAULT["average"],
            bag=BAG_BY_DEFAULT["average"],
    ):
        super().__init__(
            name,
            capital,
            endpoint,
            social_status,
            iq,
            bag
        )


class RichHuman(Human):
    def __init__(self,
                 name="",
                 capital=CAPITAL_BY_DEFAULT["rich"],
                 endpoint=END_POINT_BY_DEFAULT["rich"],
                 social_status=SOCIAL_STATUS_BY_DEFAULT["rich"],
                 iq=IQ_BY_DEFAULT["rich"],
                 bag=BAG_BY_DEFAULT["rich"],

                 ):
        super().__init__(
            name,
            capital,
            endpoint,
            social_status,
            iq,
            bag,
        )
