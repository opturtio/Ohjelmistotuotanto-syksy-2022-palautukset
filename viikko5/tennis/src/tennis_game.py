class TennisGame:
    def __init__(self):
        self._m_score1 = 0
        self._m_score2 = 0
        self._scores = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty", 4: "Deuce"}

    def player1_won(self):
        self._m_score1 += 1

    def player2_won(self):
        self._m_score2 += 1

    def get_score(self):
        if self._m_score1 == self._m_score2:
            return self._draw(self._m_score1)

        elif self._m_score1 >= 4 or self._m_score2 >= 4:
            return self._scores_more_than_four()

        else:
            return self._last_option()


    def _draw(self, score):
        if score == 4:
            return "Deuce"
        return f"{self._scores[score]}-All"

    def _scores_more_than_four(self):
        minus_result = self._m_score1 - self._m_score2

        if minus_result == 1:
            return "Advantage player1"
        elif minus_result == -1:
            return "Advantage player2"
        elif minus_result >= 2:
            return "Win for player1"
        else:
            return "Win for player2"

    def _last_option(self):
        for i in range(1, 3):
            return f"{self._scores[self._m_score1]}-{self._scores[self._m_score2]}"
