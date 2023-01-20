#!/usr/bin/env python3

import random
import brain_games.common


def main():
    name = brain_games.common.welcome_user()
    print("What is the result of the expression?")
    counter = 0
    while counter < 3:
        rand_number1 = random.randint(1, 10)
        rand_number2 = random.randint(1, 10)
        action = random.choice(['+', '-', '*'])

        if action == '+':
            result = rand_number1 + rand_number2
        elif action == '-':
            result = rand_number1 - rand_number2
        else:
            result = rand_number1 * rand_number2

        print(f'Question: {rand_number1} {action} {rand_number2}')

        answer = brain_games.common.get_answer()
        counter = brain_games.common.check_answer(result, answer, counter, name)

    if counter == 3:
        print(f'Congratulations, {name}!')
