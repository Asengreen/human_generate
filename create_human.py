import json
from random import choice as rand_choice
from random import randint


class Human:
    def __init__(self, sex):
        if sex == 'Male':
            self.first_name = get_first_male_name()
        if sex == 'Female':
            self.first_name = get_first_female_name()
        self.last_name = get_last_name()
        self.sex = sex
        self.birth_day = get_birth_day()
        self.birth_month = get_birth_month()
        self.birth_year = get_birth_year()

    def info(self):
        print(self.first_name, self.last_name, self.sex, f'{self.birth_day}.{self.birth_month}.{self.birth_year}')


def get_first_male_name():
    with open('base\\male_names.json', 'r') as file:
        names = json.loads(file.read())
    return rand_choice(names)


def get_first_female_name():
    with open('base\\female_names.json', 'r') as file:
        names = json.loads(file.read())
    return rand_choice(names)


def get_last_name():
    with open('base\\last_names.json', 'r') as file:
        names = json.loads(file.read())
    return rand_choice(names)


def get_birth_day():
    return randint(1, 28)


def get_birth_month():
    return randint(1, 12)


def get_birth_year():
    return randint(1960, 2000)
