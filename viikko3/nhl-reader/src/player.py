class Player:
    def __init__(self, name, nationality, assists, goals, penalties, team, games):
        self.name = name
        self.nationality = nationality
        self.assists = assists
        self.goals = goals
        self.penalties = penalties
        self.team = team
        self.games = games
        self.scores = goals+assists
    
    def __str__(self):
        return f"{self.name:22}{self.team:4} {self.goals:2} + {self.assists:2} = {self.scores:2}"
