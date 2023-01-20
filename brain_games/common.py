#!/usr/bin/env python3
import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ', empty=True)
    print(f'Hello, {name}!')
    return name


def get_answer():
    answer = prompt.string('Your answer: ', empty=True)
    return answer


def check_answer(result, answer, counter, name):
    if str(result) == answer:
        print('Correct!')
        counter += 1
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'.")
        print(f"Let's try again, {name}!")
        return 10
    return counter
