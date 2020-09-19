welcome_text_template = "Hello %s and welcome to the World of Games(WoG).\n" \
                        "Here you can find many cool games to play"
games_indexes_list = [1, 2, 3]


class Live:

    def __init__(self, num_of_tries=10):
        self.num_of_tries = num_of_tries
        print("Please choose a game to play:\n"
              "1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess back\n"
              "2. Guess Game - guess a number and see if you chose like the computer\n"
              "3. Currency Roulette - try and guess the value of a random amount of USD in ILS")

    def welcome(self, name):
        print(welcome_text_template % name)

        while self.num_of_tries < 10:
            self.num_of_tries += 1
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

                        break
                break
