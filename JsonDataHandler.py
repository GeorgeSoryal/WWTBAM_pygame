import json
from random import randint

with open("Assets/WWTBAM JSON File.json", encoding="utf-8") as filepath:
    data_file = json.load(filepath)


def populate_question_list() -> list:
    questions_list = []
    for i in range(15):
        random_index = randint(0, 546)
        new_item = data_file[random_index]

        while new_item in questions_list:
            random_index = randint(0, 546)
            new_item = data_file[random_index]

        questions_list.append(new_item)
    return questions_list
