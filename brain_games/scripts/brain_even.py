#!/usr/bin/env python3

import prompt
import random


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name

def get_answer():
    rand_number = random.randint(1, 1000)
    answer = prompt.string(f'Question: {rand_number}\n')
    return rand_number, answer

def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    counter = 0
    while counter < 3:
        print("Answer 'yes' if the number is even, otherwise answer 'no'.")
        rand_number, answer = get_answer()
        if (rand_number % 2 == 0 and answer == "yes") or (rand_number % 2 != 0 and answer == "no"):
            print('Correct!')
            counter += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')

