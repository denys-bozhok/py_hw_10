from random import randint


def still_alco() -> bool:
    chance_to_alco = randint(1, 10)
    if chance_to_alco == 1:
        print("\n!!!!!!!!!!!!!!!!!\n"
              "You start to drunk\n"
              "!!!!!!!!!!!!!!!!!\n")

        return True
