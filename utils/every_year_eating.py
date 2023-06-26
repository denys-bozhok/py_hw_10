def every_year_eating(hero: dict) -> dict:
    if hero["iq"] == 88:
        hero["capital"] += 100
        hero["endpoint"] -= 0.8
        return hero
    else:
        user_choose_eat = 0
        while user_choose_eat == 0:
            try:
                user_choose_eat = int(input("U need to eat. Enter lvl of you choose\n"
                                            "1) 100$\n2) 200$\n3) 300$\n"))
            except:
                print("Error data, try again")

            match user_choose_eat:
                case 1:
                    hero["capital"] -= 100
                    hero["endpoint"] -= 0.8
                case 2:
                    hero["capital"] -= 200
                    hero["endpoint"] -= 0.2
                case 3:
                    hero["capital"] -= 300
                    hero["endpoint"] += 0.2
                case _:
                    print("Error number, try again")
        return hero
