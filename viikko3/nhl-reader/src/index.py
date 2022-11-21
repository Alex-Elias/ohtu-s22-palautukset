import requests
from player import Player


class PlayerReader:
    def __init__(self, url: str):
        self.url = url
    
    def get_players(self) -> list:
        try:
            response = requests.get(self.url).json()
        except:
            response = []
        return [Player(x) for x in response]
            

class PlayerStats:
    def __init__(self, reader: PlayerReader):
        if isinstance(reader, PlayerReader):
            self.reader = reader
        else:
            self.reader = PlayerReader("")

    def top_scorers_by_nationality(self, nationality: str) -> list:
        players = self.reader.get_players()
        player_nat = list(filter(lambda x: x.nationality == nationality, players))
        player_nat.sort(reverse=True, key=(lambda x: x.goals + x.assists))
        return player_nat


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    for player in players:
        print(player)

if __name__ == "__main__":
    main()
