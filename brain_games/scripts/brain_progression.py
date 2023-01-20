#!/usr/bin/env python3

import random
import brain_games.common


def main():
    name = brain_games.common.welcome_user()
    print("What number is missing in the progression?")
    counter = 0
    while counter < 3:
        rand_number = random.randint(5, 15)

        if rand_number % 2 == 0:
            result = "yes"
        else:
            result = "no"

        print(f'Question: {rand_number}')
        answer = brain_games.common.get_answer()
        counter = brain_games.common.check_answer(result, answer, counter, name)

    if counter == 3:
        print(f'Congratulations, {name}!')