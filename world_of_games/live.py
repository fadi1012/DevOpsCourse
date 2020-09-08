class Live:
    welcome_text_template = "Hello %s and welcome to the World of Games(WoG).\n" \
                            "Here you can find many cool games to play"
    
    # think about more effective way to manage this, if ill ask you to add 100 more dificulty levels for example?
    games_indexes_list = [1, 2, 3]
    difficulty_level_list = [1, 2, 3, 4, 5]

    def welcome(self, name):
        print(self.welcome_text_template % name)

    # if you are using classes, why not put this as the constructor of the class? because right now there is no point in using classes in the way you implemented it
    def load_game(self):
        print("Please choose a game to play:\n"
              "1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess back\n"
              "2. Guess Game - guess a number and see if you chose like the computer\n"
              "3. Currency Roulette - try and guess the value of a random amount of USD in ILS")

        # Its better not to use this infinite way but set some expiring condition
        while True:
            # input validation please, if you put a string here the code will crash
            game_index = int(input("Please enter the number of the game you want to play"))
            if not game_index in self.games_indexes_list:
                print("Sorry, your provided a game index which is not from 1 to 3, please try again.")
                continue
            else:
                while True:
                    difficulty_level = int(input("Please enter the difficulty level from 1 to 5"))
                    if not difficulty_level in self.difficulty_level_list:
                        print("Sorry, your provided a a difficulty level which is not from 1 to 5, please try again.")
                        continue
                    else:
                        break
                break
