from world_of_games.level2.currency_roullete_game import CurrencyRouletteGame
from world_of_games.level2.guess_game import GuessGame
from world_of_games.level2.memory_game import MemoryGame

welcome_text_template = "Hello %s and welcome to the World of Games(WoG).\n" \
                        "Here you can find many cool games to play"
games_indexes_list = [1, 2, 3]


class Live:

    def __init__(self, max_num_of_tries=10):
        self.max_num_of_tries = max_num_of_tries
        print("Please choose a game to play:\n"
              "1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess back\n"
              "2. Guess Game - guess a number and see if you chose like the computer\n"
              "3. Currency Roulette - try and guess the value of a random amount of USD in ILS")

    def welcome(self, name):
        print(welcome_text_template % name)
        num_of_tries = 0
        while num_of_tries < self.max_num_of_tries:
            num_of_tries += 1
            game_index = int(input("Please enter the number of the game you want to play"))
            if not game_index in games_indexes_list or not type(game_index) is int:
                print("Sorry, your provided a game index which is not from 1 to 3, please try again.")
                continue
            else:
                while True:
                    difficulty_level = int(input("Please enter the difficulty level from 1 to 5"))
                    if difficulty_level < 1 or difficulty_level > 5:
                        print("Sorry, your provided a a difficulty level which is not from 1 to 5, please try again.")
                        continue
                    else:
                        if game_index == 1:
                            memory_game = MemoryGame()
                            print("Success!!") if memory_game.play(difficulty_level) else print("Failed!!")

                        elif game_index == 2:
                            guess_game = GuessGame()
                            guess_game.play(difficulty_level)

                        elif game_index == 3:
                            currency_roulette_game = CurrencyRouletteGame()
                            print("Success!!") if currency_roulette_game.play(difficulty_level) else print("Failed!!")
                        break
            break
