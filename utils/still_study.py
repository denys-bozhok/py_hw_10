def still_study(hero):

    while True:
        is_still_student = input(
            "Do you want to trow away or go to study? :\n"
            "(If [y] - you have + 1000$ and -2 point of social status\n"
            "If [n] - your social status will save)\n")

        if is_still_student == "y":
            hero["capital"] += 1000
            hero["social_status"] -= 2
            break

        if is_still_student == "n":
            hero["education_lvl"] += 1
            break
        else:
            print("Please choose y/n")


def study_in_academy(hero, educations_arr):

    while True:
        is_still_student = input(
            "Do you want to go to Academy? :\n")

        if is_still_student == "y":
            if hero["iq"] == 123:
                hero["capital"] -= int(educations_arr[1]["cost"])
                hero["education_lvl"] = educations_arr[1]["lvl"]
                break
            elif hero["iq"] == 113:
                hero["capital"] -= int(educations_arr[2]["cost"])
                hero["education_lvl"] = educations_arr[2]["lvl"]
                break
            else:
                hero["capital"] -= int(educations_arr[3]["cost"])
                hero["education_lvl"] = educations_arr[3]["lvl"]
                break

        if is_still_student == "n":
            break
        else:
            print("Please choose y/n")
