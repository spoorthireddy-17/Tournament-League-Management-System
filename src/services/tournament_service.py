from src.dao.tournament_dao import TournamentDAO

class TournamentService:
    @staticmethod
    def add_tournament(name, type, start_date, end_date, sport_id):
        return TournamentDAO.insert(name, type, start_date, end_date, sport_id)

    @staticmethod
    def list_tournaments():
        return TournamentDAO.get_all()

    @staticmethod
    def get_tournament(tournament_id):
        tournament = TournamentDAO.get_by_id(tournament_id)
        if tournament is None:
            return {"message": "Tournament not found"}
        return tournament
    
    @staticmethod
    def update_tournament(tournament_id, name=None, type=None, start_date=None, end_date=None, sport_id=None):
        return TournamentDAO.update(tournament_id, name, type, start_date, end_date, sport_id)

    @staticmethod
    def delete_tournament(tournament_id):
        return TournamentDAO.delete(tournament_id)
    