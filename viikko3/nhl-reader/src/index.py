import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    response = requests.get(url).json()

    players = []

    for player_dict in response:
        player = Player(
            player_dict['name'],
            player_dict["nationality"],
            player_dict["assists"],
            player_dict["goals"],
            player_dict["penalties"],
            player_dict["team"],
            player_dict["games"]
        )

        players.append(player)

    print("Oliot:")
    fin_players = sorted(list(filter(lambda player: player.nationality=="FIN", players)), key= lambda player: player.scores, reverse=True)
    
    for player in fin_players:
        print(player)
    


if __name__ == "__main__":
    main()
