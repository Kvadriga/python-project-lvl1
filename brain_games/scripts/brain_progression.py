#!/usr/bin/env python3

import random
import brain_games.common


def main():
    name = brain_games.common.welcome_user()
    print("What number is missing in the progression?")
    counter = 0
    while counter < 3:
        length = random.randint(5, 15)
        l = [random.randint(1, 10)]
        step = random.randint(1, 5)
        i = 1
        while i < length:
            l.append(l[i - 1] + step)
            i +=1
        index = random.randint(0, length)
        result = l[index]
        l[index] = '..'

        print(f'Question: {l}')
        answer = brain_games.common.get_answer()
        counter = brain_games.common.check_answer(result, answer, counter, name)

    if counter == 3:
        print(f'Congratulations, {name}!')
        