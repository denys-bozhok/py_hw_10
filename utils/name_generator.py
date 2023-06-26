from random import randint


def name_generator(names: list, start_point: int, end_point: int) -> str:
    return names[randint(start_point, end_point)] + str(randint(10000, 40000))
