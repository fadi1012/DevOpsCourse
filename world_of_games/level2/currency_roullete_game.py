from forex_python.converter import CurrencyRates
import random


class CurrencyRouletteGame:
    def __init__(self, max_num_of_tries=2):
        self.difficulty = None
        self.max_num_of_tries = max_num_of_tries

    def get_money_interval(self, amount):
        c = CurrencyRates()
        usd_to_ils = c.get_rate('USD', 'ILS')
        min_interval = amount * usd_to_ils - (5 - usd_to_ils)
        max_interval = amount * usd_to_ils + (5 - usd_to_ils)
        return min_interval, max_interval

    def get_guess_from_user(self, amount):
        num_of_tries = 0

        while num_of_tries <= self.max_num_of_tries:
            num_of_tries += 1
            guess = int(input(f"How much is {amount}$ in ILS?"))
            if not type(guess) is int:
                print(f"You've entered wrong input, please choose a number not a string or a special character")
                continue
            else:
                return guess

    def play(self, difficulty_level):
        self.difficulty = difficulty_level
        random_amount = random.randint(1, 101)
        money_interval = self.get_money_interval(random_amount)
        guess = self.get_guess_from_user(random_amount)
        return True if (guess <= money_interval[1] and guess >= money_interval[0]) else False
