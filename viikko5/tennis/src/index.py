from tennis_game import TennisGame


def main():
    game = TennisGame()

    print(game.get_score())

    game.player1_won()
    print(game.get_score())

    game.player1_won()
    print(game.get_score())

    game.player2_won()
    print(game.get_score())

    game.player1_won()
    print(game.get_score())

    game.player1_won()
    print(game.get_score())


if __name__ == "__main__":
    main()
