from random import randint


def chance_to_maried(is_married: bool) -> bool:
    if not is_married:
        random_chance_to_maried = randint(1, 20)

        if random_chance_to_maried == 13:
            wife_name = input("Congratulation! U married! Enter name of your wife\n")

            print(f"{wife_name} loves U, but will huck your brain and mai by az! ")

            return True

        return False
