from random import randint


def get_a_job(hero: dict, job: list):
    if hero["iq"] == 86:
        human_job = job[0]

    else:
        i = randint(0, len(job) - 1)
        human_job = job[i]

    print(f"You have a job. Your profession is :\n"
          f"{human_job['prof']}".upper())

    return human_job
