from random import randint


def random_pick(collections: tuple, since, to):
    try:
        return collections[randint(since, to)]
    except:
        return "Error !"