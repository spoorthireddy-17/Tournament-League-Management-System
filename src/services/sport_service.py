from src.dao.sport_dao import SportDAO

class SportService:
    @staticmethod
    def add_sport(name, players_required):
        return SportDAO.insert(name, players_required)

    @staticmethod
    def list_sports():
        return SportDAO.get_all()

    @staticmethod
    def get_sport(sport_id):
        sport = SportDAO.get_by_id(sport_id)
        if sport is None:
            return {"message": "Sport not found"}
        return sport

    @staticmethod
    def update_sport(sport_id, name=None, players_required=None):
        return SportDAO.update(sport_id, name, players_required)

    @staticmethod
    def delete_sport(sport_id):
        return SportDAO.delete(sport_id)
    
    