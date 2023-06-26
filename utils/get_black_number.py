from random import randint


def get_black_number(hero: dict, history: str, call: bool) -> bool:

    is_black_number = randint(0, 100)

    # Рандомное число, выпадает каждый год. Если рандомное число равно 66 - игра окончена.
    # Если при этом пользователь купил уже ТЕЛЕФОН - он может позвонить в скорую.
    # С вероятностью 50% выживет или нет.

    if is_black_number == 66:

        for el in hero["bag"]:
            if el == "Nokia-3310":
                print("U have some incidante. But U have phone. Call ambulance :")
                history += f'{hero["age"]} - ' \
                           f'U have some incidante. But U have phone. Call ambulance :\n'

                return call

            else:
                print("\nSorry, your game is over by FORTUNA\n")
                history += f'{hero["age"]} - ' \
                           f'U have some incidante./'

                return False
    else:
        return True
