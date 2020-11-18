import glob
import os.path
import json

from random import choice as rand_choice
from random import randint


if __name__ == '__main__':
    find_path = 'base'
else:
    find_path = '**/human_generate/base'

COMMON_PATH = glob.glob(find_path, recursive=True)[0]


class Human:
    def __init__(self, sex=None):
        if not sex:
            sex = rand_choice(['Male', 'Female'])
            self.sex = sex
        else:
            self.sex = sex
        if self.sex == 'Male':
            self.first_name = get_first_male_name()

        if self.sex == 'Female':
            self.first_name = get_first_female_name()

        self.last_name = get_last_name()
        self.birth_day = get_birth_day()
        self.birth_month = get_birth_month()
        self.birth_year = get_birth_year()

    def info(self):
        print(self.first_name, self.last_name, self.sex, f'{self.birth_day}.{self.birth_month}.{self.birth_year}')


def get_first_male_name():
    path = os.path.join(COMMON_PATH, 'male_names.json')
    with open(path, 'r') as file:
        names = json.loads(file.read())
    return rand_choice(names)


def get_first_female_name():
    path = os.path.join(COMMON_PATH, 'female_names.json')
    with open(path, 'r') as file:
        names = json.loads(file.read())
    return rand_choice(names)


def get_last_name():
    path = os.path.join(COMMON_PATH, 'last_names.json')
    with open(path, 'r') as file:
        names = json.loads(file.read())
    return rand_choice(names)


def get_birth_day():
    return randint(1, 28)


def get_birth_month():
    return randint(1, 12)


def get_birth_year():
    return randint(1960, 2000)


hum = Human()
hum.info()
