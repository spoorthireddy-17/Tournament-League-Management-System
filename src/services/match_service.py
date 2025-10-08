from src.dao.match_dao import MatchDAO

class MatchService:
    @staticmethod
    def add_match(tournament_id, team1_id, team2_id, score_team1=0, score_team2=0, winner=None, match_date=None):
        return MatchDAO.insert(tournament_id, team1_id, team2_id, score_team1, score_team2, winner, match_date)

    @staticmethod
    def list_matches():
        return MatchDAO.get_all()

    @staticmethod
    def get_match(match_id):
        return MatchDAO.get_by_id(match_id)

    @staticmethod
    def update_match(match_id, tournament_id=None, team1_id=None, team2_id=None,
                     score_team1=None, score_team2=None, winner=None, match_date=None):
        return MatchDAO.update(match_id, tournament_id, team1_id, team2_id,
                               score_team1, score_team2, winner, match_date)

    @staticmethod
    def delete_match(match_id):
        return MatchDAO.delete(match_id)
    def get_match_by_id(match_id):
        match = MatchDAO.get_by_id(match_id)  # Or however you access your DAO
        return match