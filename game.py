from Goods import Phone

from utils.get_dict_info import get_dict_info
from utils.is_game_over import is_game_over
from utils.is_first_appearance import is_first_appearance
from utils.still_study import still_study, study_in_academy
from utils.chance_to_maried import chance_to_maried
from utils.still_alco import still_alco
from utils.still_smoke import still_smoke
from utils.get_a_job import get_a_job
from utils.every_year_eating import every_year_eating
from utils.bie_goods import bie_goods
from utils.get_black_number import get_black_number


def game(hero: dict,
         current_age: int,
         end_point: int,
         educations_arr: list,
         jobs_arr: list,
         hurbits_arr: list,
         goods_arr):

    # Декларирую переменные для игры переменные

    hero["education_lvl"] = educations_arr[0]["lvl"]
    call = Phone.call_ambulance(Phone("Nokia-3310", 3, True, 500))
    hero_job = {}
    is_alive = True
    is_married = False
    is_alco = hurbits_arr[1]["isAlco"]
    is_smoke = hurbits_arr[0]["isSmoking"]
    history = ""

    while current_age < end_point and is_alive:

        is_living_year = input("\ndo U want to live this year? [y/n] :\n")

        if is_living_year == "n":
            print("See U soon!")
            return False
        elif is_living_year != "y":
            print("Choose y/n")
            continue

        if current_age == 1:
            is_first_appearance(hero, get_dict_info)

        if 2 <= current_age <= end_point:
            every_year_eating(hero)

        if 15 <= current_age <= end_point:
            bie_goods(hero, goods_arr)

        if current_age == 15:
            bie_goods(hero, goods_arr)

        if current_age == 16:
            still_study(hero)
            if hero["education_lvl"] != 0:
                history += f'{hero["age"]} - ' \
                           f'U go to study in height school./'

        if 18 <= current_age <= end_point and not is_smoke:
            is_smoke = still_smoke()
            if is_smoke:
                end_point -= hurbits_arr[0]["forfeit"]
                hero["capital"] += hurbits_arr[0]["income"]
                history += f'{hero["age"]} - ' \
                           f'U started Smoking./'

        if 23 <= current_age <= 50 and not is_married:
            is_married = chance_to_maried(is_married)
            if is_married:
                end_point -= 10
                history += f'{hero["age"]} - ' \
                           f'U was married./'

        if current_age == 24:
            if hero["education_lvl"] != 0:
                study_in_academy(hero, educations_arr)
                if hero["education_lvl"] > 1:
                    history += f'{hero["age"]} - ' \
                               f'U go to University./'

        if current_age == 30:
            hero_job = get_a_job(hero, jobs_arr)
            history += f'{hero["age"]} - ' \
                       f'U have a job./'

        if 31 <= current_age <= end_point:
            hero["capital"] += hero_job["annual_income"] + 100 * hero["education_lvl"]
            print(f"You have income : "
                  f"{hero_job['annual_income'] + 100 * hero['education_lvl']}$")

        if is_married and not is_alco:
            is_alco = still_alco()
            if is_alco:
                end_point -= hurbits_arr[1]["forfeit"]
                history += f'{hero["age"]} - ' \
                           f'U start to Drink./'

        if is_alco:
            print("Money for drunk! +200$")
            hero["capital"] += hurbits_arr[1]["income"]

        is_alive = is_game_over(hero["capital"])
        is_alive = get_black_number(hero, history, call)

        get_dict_info(hero)

        current_age += 1
        hero["age"] += 1

    print("U DIE! See U soon!")

    history_arr = history.split("/")

    print(f"\nYour history :".upper())

    for history_el in history_arr:
        print(history_el)

    print(f"\nYour bag :".upper())

    for bag_el in hero["bag"]:
        print(bag_el)

    print("GAME OVER")
