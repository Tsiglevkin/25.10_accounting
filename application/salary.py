import tqdm
from time import sleep
salary_dict = {
        'Jane': 15000,
        'David': 20000,
        'John': 50000,
        'Stanley': 100000,
    }


def calculate_salary(some_dict):
    print('Это функция calculate_salary')
    for name, salary in tqdm.tqdm(some_dict.items()):
        sleep(0.5)
        res = f"{name}'s salary is {salary}."
        tqdm.tqdm.write(res)
    print()