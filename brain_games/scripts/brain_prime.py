#!/usr/bin/env python3

import random
import brain_games.common


def main():
    name = brain_games.common.welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    counter = 0
    while counter < 3:
        number = random.randint(1, 20)
        print(f'Question: {number}')
        i = 2
        result = 'yes'
        while i <= number // 2 + 1:
            if number % i == 0:
                result = 'no'
                break
            i += 1
        answer = brain_games.common.get_answer()
        counter = brain_games.common.check_answer(result, answer, counter, name)
    if counter == 3:
        print(f'Congratulations, {name}!')
