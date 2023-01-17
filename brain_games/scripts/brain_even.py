#!/usr/bin/env python3

import prompt
import random


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

def get_answer():
    rand_number = random.randint(1, 1000)
    answer = prompt.string(f'Question: {rand_number}\n')

def main():
    print("Welcome to the Brain Games!\nAnswer 'yes' if the number is even, otherwise answer 'no'.")
    welcome_user()
    get_answer()