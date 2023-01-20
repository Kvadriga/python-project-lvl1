#!/usr/bin/env python3

import random
import brain_games.common


def main():
    name = brain_games.common.welcome_user()
    print("Find the greatest common divisor of given numbers.")
    counter = 0
    while counter < 3:
        rand_number1 = random.randint(1, 100)
        rand_number2 = random.randint(1, 100)
        print(f'Question: {rand_number1} {rand_number2}')

        if rand_number1 == rand_number2:
            result = rand_number1
        else:
            while rand_number1 != 0 and rand_number2 != 0:
                if rand_number1 > rand_number2:
                    rand_number1 = rand_number1 % rand_number2
                else:
                    rand_number2 = rand_number2 % rand_number1
                result = rand_number1 + rand_number2

        answer = brain_games.common.get_answer()
        counter = brain_games.common.check_answer(result, answer, counter, name)

    if counter == 3:
        print(f'Congratulations, {name}!')
