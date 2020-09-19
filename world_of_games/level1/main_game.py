from world_of_games.level1.live import Live


class MainGame:
    @staticmethod
    def play():
        live = Live()
        live.welcome("Fadi")


def main():
    MainGame.play()


if __name__ == "__main__":
    main()
