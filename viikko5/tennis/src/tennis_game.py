LOVE = 0
FIFTEEN = 1
THIRTY = 2
FORTY = 3

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def get_score(self):

        if self.m_score1 == self.m_score2:
            return self._equal_score()
        elif self.m_score1 > FORTY or self.m_score2 > FORTY:
            return self._runoff_score()
        else:
            return self._unequal_score()
    
    def _equal_score(self) -> str:
        if self.m_score1 == LOVE:
            score = "Love-All"
        elif self.m_score1 == FIFTEEN:
            score = "Fifteen-All"
        elif self.m_score1 == THIRTY:
            score = "Thirty-All"
        else:
            score = "Deuce"
        return score
    
    def _runoff_score(self) -> str:
        minus_result = self.m_score1 - self.m_score2

        if minus_result == 1:
            score = "Advantage player1"
        elif minus_result == -1:
            score = "Advantage player2"
        elif minus_result >= 2:
            score = "Win for player1"
        else:
            score = "Win for player2"
        
        return score
    
    def _unequal_score(self) -> str:
        score = ""
        for player in ["Player One", "Player Two"]:
            if player == "Player One":
                player_score = self.m_score1
            else:
                score = score + "-"
                player_score = self.m_score2

            if player_score == LOVE:
                score = score + "Love"
            elif player_score == FIFTEEN:
                score = score + "Fifteen"
            elif player_score == THIRTY:
                score = score + "Thirty"
            elif player_score == FORTY:
                score = score + "Forty"
        return score

