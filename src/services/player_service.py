from src.dao.player_dao import PlayerDAO
from src.dao.team_dao import TeamDAO
from src.dao.sport_dao import SportDAO



class PlayerService:
    @staticmethod
    def add_player(player_name, age, position, team_id):
        team = TeamDAO.get_by_id(team_id)
        if not team:
            print("⚠️ Team not found")
            return None

        tournament = TeamDAO.get_tournament(team_id)
        if not tournament:
            print("⚠️ Tournament not found for this team")
            return None

        sport_id = tournament['sport_id']
        sport = SportDAO.get_by_id(sport_id)
        if not sport:
            print("⚠️ Sport not found for this tournament")
            return None

        required_players = sport['players_required']
        current_players = PlayerDAO.count_players_in_team(team_id)

        print(f"Debug: Team has {current_players} players, sport requires {required_players} players")

        if current_players >= required_players:
            print(f"⚠️ Team already has enough players ({current_players}/{required_players})")
            return None

        return PlayerDAO.insert(player_name, age, position, team_id)

    @staticmethod
    def list_players():
        return PlayerDAO.get_all()

    @staticmethod
    def get_player(player_id):
        player = PlayerDAO.get_by_id(player_id)
        if player is None:
            return {"message": "Player not found"}
        return player
    @staticmethod
    def update_player(player_id, name=None, age=None, position=None, team_id=None):
        return PlayerDAO.update(player_id, name, age, position, team_id)

    @staticmethod
    def delete_player(player_id):
        return PlayerDAO.delete(player_id)
    
   