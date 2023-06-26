def bie_goods(hero: dict, goods_arr: list):
    user_choose = 0

    while user_choose == 0:
        print("You can bie something goods :")
        i = 0

        for g in goods_arr:
            for key, value in g.items():

                if key == "name":
                    print(f"{i+1} {value}")

            for key, value in g.items():
                if key == "cost":
                    print(f"{key} - {value}$\n"
                          f"---------------")

            i += 1

        try:
            user_choose = int(input("Enter a number :\n"))

        except:
            print("Incorrect number")

        match user_choose:
            case 1:
                if hero["capital"] >= goods_arr[0]["cost"]:
                    hero["capital"] -= goods_arr[0]["cost"]
                    hero["social_status"] += goods_arr[0]["additional_social_status"]
                    hero["endpoint"] += goods_arr[0]["additional_lifetime"]
                    hero["bag"].append(goods_arr[0]['name'])
                    print(hero["bag"])
                else:
                    print("U have no money")

            case 2:
                if hero["capital"] >= goods_arr[1]["cost"]:
                    hero["capital"] -= goods_arr[1]["cost"]
                    hero["social_status"] += goods_arr[1]["additional_social_status"]
                    hero["endpoint"] += goods_arr[1]["additional_lifetime"]
                    hero["bag"].append(goods_arr[1]['name'])
                    print(hero["bag"])
                else:
                    print("U have no money")

            case 3:
                if hero["capital"] >= goods_arr[2]["cost"]:
                    hero["capital"] -= goods_arr[2]["cost"]
                    hero["social_status"] += goods_arr[2]["additional_social_status"]
                    hero["bag"].append(goods_arr[2]['name'])
                    print(hero["bag"])
                else:
                    print("U have no money")

            case 4:
                if hero["capital"] >= goods_arr[3]["cost"]:
                    hero["capital"] -= goods_arr[3]["cost"]
                    hero["social_status"] += goods_arr[3]["additional_social_status"]
                    hero["bag"].append(goods_arr[3]['name'])
                    print(hero["bag"])
                else:
                    print("U have no money")
