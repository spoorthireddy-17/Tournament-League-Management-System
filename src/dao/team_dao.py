from src.db_client import supabase

class TeamDAO:
    @staticmethod
    def insert(team_name, coach_name, tournament_id):
        response = supabase.table("teams").insert({
            "team_name": team_name,
            "coach_name": coach_name,
            "tournament_id": tournament_id
        }).execute()
        return response.data[0] if response.data else None

    @staticmethod
    def get_all():
        response = supabase.table("teams").select("*").execute()
        return response.data

    @staticmethod
    def get_by_id(team_id):
        response = supabase.table("teams").select("*").eq("team_id", team_id).execute()
        return response.data[0] if response.data else None

    @staticmethod
    def update(team_id, team_name=None, coach_name=None, tournament_id=None):
        update_data = {}
        if team_name:
            update_data["team_name"] = team_name
        if coach_name:
            update_data["coach_name"] = coach_name
        if tournament_id:
            update_data["tournament_id"] = tournament_id
        if not update_data:
            return None
        response = supabase.table("teams").update(update_data).eq("team_id", team_id).execute()
        return response.data[0] if response.data else None

    @staticmethod
    def delete(team_id):
        response = supabase.table("teams").delete().eq("team_id", team_id).execute()
        return response.data
    @staticmethod
    def get_tournament(team_id):
        team = TeamDAO.get_by_id(team_id)
        if not team:
            return None
        tournament_id = team['tournament_id']
        response = supabase.table("tournaments").select("*").eq("tournament_id", tournament_id).execute()
        return response.data[0] if response.data else None