class Player:
    def __init__(self, player_info: str):
        self.name = player_info["name"]
        self.team = player_info["team"]
        self.goals = player_info["goals"]
        self.assists = player_info["assists"]
        self.nationality = player_info["nationality"]
    
    def __str__(self):
        string = f"{self.name:22} {self.team} {self.goals:2} + {self.assists:2} = {self.goals + self.assists:3}"
        return string
