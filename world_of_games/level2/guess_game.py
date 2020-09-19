import random


class GuessGame:
    def __init__(self, max_num_of_tries=10):
        self.secret_number = None
        self.difficulty = None
        self.max_num_of_tries = max_num_of_tries

    def generate_number(self):
        self.secret_number = random.randint(0, self.difficulty)

    def get_guess_from_user(self):
        num_of_tries = 0
        while num_of_tries < self.max_num_of_tries:
            num_of_tries += 1
            guess = int(input(f"Please guess a number from 1 to {self.difficulty}"))
            if not type(guess) is int or (guess > self.difficulty or guess < 1):
                print(f"You've entered wrong input, please choose a number from 1 to {self.difficulty}")
                continue
            else:
                return guess
        print("You've exceeded the number of tries to properly play the game")
        return False

    def compare_results(self, guess):
        return self.secret_number == guess

    def play(self, difficulty_level):
        self.difficulty = difficulty_level
        self.generate_number()
        guess = self.get_guess_from_user()
        if not guess:
            print("Please restart the game and try again")
        return print("You've Won!!") if self.compare_results(guess) else print("You've Lost! good luck next time :)")
