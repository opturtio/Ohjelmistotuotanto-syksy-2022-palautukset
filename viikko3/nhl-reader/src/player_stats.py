class PlayerStats:
    def __init__(self, reader):
        self.reader = reader
        self.players = self.reader.get_players()
        
    def top_scorers_by_nationality(self, nationality):
        return sorted(list(filter(lambda player: player.nationality==nationality, self.players)), key= lambda player: player.scores, reverse=True)
    
    def top_scorers(self):
        return sorted(self.players, key= lambda player: player.scores)