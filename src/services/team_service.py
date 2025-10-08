from src.dao.team_dao import TeamDAO

class TeamService:
    @staticmethod
    def add_team(name, coach, tournament_id):
        return TeamDAO.insert(name, coach, tournament_id)

    @staticmethod
    def list_teams():
        return TeamDAO.get_all()

    @staticmethod
    def get_team(team_id):
        team = TeamDAO.get_by_id(team_id)
        if team is None:
            return {"message": "Team not found"}
        return team

    @staticmethod
    def update_team(team_id, name=None, coach=None, tournament_id=None):
        return TeamDAO.update(team_id, name, coach, tournament_id)

    @staticmethod
    def delete_team(team_id):
        return TeamDAO.delete(team_id)