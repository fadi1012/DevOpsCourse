import random
import time


class MemoryGame:
    def __init__(self):
        self.difficulty = None
        self.num_of_tries = 0
        self.user_random_guesses_list = []

    def generate_sequence(self):
        random_numbers_list = []
        for i in range(self.difficulty):
            random_numbers_list.append(random.randint(1, 101))
        start = time.time()
        end = 0.7
        while time.time() - start <= end:
            print(random_numbers_list)
        return random_numbers_list

    def get_list_from_user(self):
        while self.num_of_tries < self.difficulty:
            guess = int(input(f"Please guess a number from 1 to 101"))
            if not type(guess) is int:
                print(f"You've entered wrong input, please choose a number from 1 to 101")
                continue
            else:
                self.num_of_tries += 1
                self.user_random_guesses_list.append(guess)
        return self.user_random_guesses_list

    def is_list_equal(self, random_numbers_list):
        return self.user_random_guesses_list == random_numbers_list

    def play(self, difficulty_level):
        self.difficulty = difficulty_level
        random_numbers_list = self.generate_sequence()
        self.get_list_from_user()
        return self.is_list_equal(random_numbers_list)
