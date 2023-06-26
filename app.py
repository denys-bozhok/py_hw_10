# Game where u should live usual life
# Game starts when user age is 0
# And every step of cycle add 1 to user age
# We should have a bag by default = []

# On the way of life we ,might to buy : car , home , some rich stuff and it will
# add bonus to our social_status

# On the start of this game by random user get it's material_status :
#  poor , avarage , rich

# poor - 70 y.o
# avarage- 85 y.o
# rich - 90 y.o

# social_status
# poor - 10
# avarage - 15
# rich - 30

# start_capital - depended of material_status
# poor - 500
# avarage - 1000
# rich - 10000000

# When child was born it's will recieve an IQ by random : 0 - 130 (since 75)
# When user 16 yo -> he might leave from school and get a job (-13 IQ ,+1000$ (once))
# When user 23 yo -> he might to become a student in University (+35 IQ ,-1500$ (once)/ +1500$ (for rich)) (if user was poor but become an avarage -> it can't get a degree)

# every year we might to eat on : 100(user_age-0.5) , 200(user_age-0.2) , 300(user_age+0.2)

# prof : unemployed  (75-80) (at least 100 on food) ,(80-100) Redneck(user_money + 420) , (100-130)businessman(user_money + 1500)

# if user doesn't have a money -> Game over
# Every year if in random we get next values : 13 ,23 -> Game over (Suddenly player become a deadman)

# On every iterattion we should track if user age bigger than it should

# Also we should cover cases with junk-lifestyle :
# When hero is 18 years old he might begin to smoke if it will be -> we should subtrack 88 - 15 (once + 300$)
# if user_age is more than 23 it might have a chance to have a widding every year before 50
# if user decide to have a widding -> it takes 10 years from current age
# Every year after wedding user get a chance to become an alco and then it takes also 10 years (+200$ every year)

# When game stops : show history of human and it's bag  bag become an empty package

# -> Game over

# CLASSES
# Creature
# Human  -> blueprint (abstract class)
# PoorHuman / AvarageHuman / RichHuman

# JunkHarbit : Harbit (abs) , Smoke , Drink , etc ...
# By default : damage
# Custom effects : risk_of_accident , sudden_hart_attack , black_lungs(passive = - 0.8)

# JOB : WorthJob , AvarageJob , Business

# EDUCATION : PoorSchool ,AvarageSchool , BusinessSchool

# Staff  : Car , House , Phone , Computer ...

# Props
# BY DEFAULT = money , end_point , social_status , IQ , bag ,start_capital

# CUSTOM = education , isSmoke , isDrunk

from Heroes import *
from Education import *
from Job import *
from Junk import *
from Goods import *

from utils.random_pick import random_pick
from utils.get_instance import get_instance

from game import game


def main():
    is_running = True
    while is_running:
        user_pick = input("Do you wonna play now? y/n?\n")

        if user_pick != "y":
            print("Goodbye!")
            break

        # ОБЪЯВЛЯЮ ИНСТЕНСЫ

        human_name = input("Enter your name :\n")

        humans = (PoorHuman(human_name),
                  AvarageHuman(human_name),
                  RichHuman(human_name))

        educations = (Education(),
                      Oxford(),
                      Academind(),
                      KhanAcademy())

        hurbits = (Smoking(15, 300, False),
                   Alcohol(10, 200, False))

        jobs = (Waiter("shepherd of bald ostriches", 300, True),
                Builder("builder of intergalactic structures", 500, False),
                SoftwareEngineer("developer of a social network for black gay old men with cerebral palsy",
                                 2000, False, True),
                Teacher("physiognomy teacher in China", 800, False))

        goods = (Car("Aveo", 10, 5, 5000),
                 House("House", 20, 10, 50000),
                 Phone("Nokia-3310", 3, True, 500),
                 Laptop("MacBook", 7, 1000))

        # СОЗДАЮ МАСИВЫ ИНСТЕНСОВ

        goods_arr = []

        for g in goods:
            goods_arr.append(get_instance(g))

        jobs_arr = []

        for job in jobs:
            jobs_arr.append(get_instance(job))

        hurbits_arr = []

        for h in hurbits:
            hurbits_arr.append(get_instance(h))

        educations_arr = []

        for educ in educations:
            educations_arr.append(get_instance(educ))

        picked_hero = random_pick(humans, 0, len(humans) - 1)

        hero = get_instance(picked_hero)

        if hero:
            current_age = (hero["age"])
            end_point = hero["endpoint"]
            game(hero,
                 current_age,
                 end_point,
                 educations_arr,
                 jobs_arr,
                 hurbits_arr,
                 goods_arr)


if __name__ == "__main__":
    main()
