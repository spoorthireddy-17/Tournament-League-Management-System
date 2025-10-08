from src.db_client import supabase

class PlayerDAO:
    @staticmethod
    def count_players_in_team(team_id):
        response = supabase.table("players").select("*").eq("team_id", team_id).execute()
        if response.data:
            return len(response.data)
        return 0
    @staticmethod
    def insert(player_name, age, position, team_id):
        response = supabase.table("players").insert({
            "player_name": player_name,
            "age": age,
            "position": position,
            "team_id": team_id
        }).execute()
        return response.data[0] if response.data else None

    @staticmethod
    def get_all():
        response = supabase.table("players").select("*").execute()
        return response.data

    @staticmethod
    def get_by_id(player_id):
        response = supabase.table("players").select("*").eq("player_id", player_id).execute()
        return response.data[0] if response.data else None

    @staticmethod
    def update(player_id, player_name=None, age=None, position=None, team_id=None):
        update_data = {}
        if player_name:
            update_data["player_name"] = player_name
        if age is not None:
            update_data["age"] = age
        if position:
            update_data["position"] = position
        if team_id:
            update_data["team_id"] = team_id
        if not update_data:
            return None
        response = supabase.table("players").update(update_data).eq("player_id", player_id).execute()
        return response.data[0] if response.data else None

    @staticmethod
    def delete(player_id):
        response = supabase.table("players").delete().eq("player_id", player_id).execute()
        return response.data