import glob
import os.path
import json

from random import choice as rand_choice
from random import randint


def get_name_base(name_base):
    path = os.path.join(COMMON_PATH, name_base)
    with open(path, 'r') as file:
        names = json.loads(file.read())
    return names


if __name__ == '__main__':
    find_path = 'base'
else:
    find_path = '**/human_generate/base'

COMMON_PATH = glob.glob(find_path, recursive=True)[0]
FIRST_NAME_MALE_BASE = get_name_base('male_names.json')
FIRST_NAME_FEMALE_BASE = get_name_base('female_names.json')
LAST_NAME_BASE = get_name_base('last_names.json')


class Human:
    def __init__(self, sex=None):
        if not sex:
            sex = rand_choice(['Male', 'Female'])
            self.sex = sex
        else:
            self.sex = sex
        if self.sex == 'Male':
            self.first_name = rand_choice(FIRST_NAME_MALE_BASE)

        if self.sex == 'Female':
            self.first_name = rand_choice(FIRST_NAME_FEMALE_BASE)

        self.last_name = rand_choice(LAST_NAME_BASE)
        self.birth_day = get_birth_day()
        self.birth_month = get_birth_month()
        self.birth_year = get_birth_year()

    def info(self):
        print(self.first_name, self.last_name, self.sex, f'{self.birth_day}.{self.birth_month}.{self.birth_year}')


def get_birth_day():
    return randint(1, 28)


def get_birth_month():
    return randint(1, 12)


def get_birth_year():
    return randint(1960, 2000)