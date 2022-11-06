from statistics import Statistics
from player_reader import PlayerReader
from sortby import SortBy

def main():
    stats = Statistics(PlayerReader())
    philadelphia_flyers_players = stats.team("PHI")
    top_scorers = stats.top(10)

    print("Philadelphia Flyers:")
    for player in philadelphia_flyers_players:
        print(player)
    print()
    
    # järjestetään kaikkien tehopisteiden eli maalit+syötöt perusteella
    print("Top point getters:")
    for player in stats.top(10, SortBy.POINTS.value):
        print(player)
    print()
    
    # metodi toimii samalla tavalla kuin yo. kutsu myös ilman toista parametria
    for player in stats.top(10):
        print(player)
    print()
    
    # järjestetään maalien perusteella
    print("Top point goal scorers:")
    for player in stats.top(10, SortBy.GOALS.value):
        print(player)
    print()
    
    # järjestetään syöttöjen perusteella
    print("Top by assists:")
    for player in stats.top(10, SortBy.ASSISTS.value):
        print(player)


if __name__ == "__main__":
    main()
