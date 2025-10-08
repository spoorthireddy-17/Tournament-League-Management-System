from src.db_client import supabase

class SportDAO:
    @staticmethod
    def insert(sport_name, players_required):
        response = supabase.table("sports").insert({
            "sport_name": sport_name,
            "players_required": players_required
        }).execute()
        return response.data[0] if response.data else None

    @staticmethod
    def get_all():
        response = supabase.table("sports").select("*").execute()
        return response.data

    @staticmethod
    def get_by_id(sport_id):
        response = supabase.table("sports").select("*").eq("sport_id", sport_id).execute()
        return response.data[0] if response.data else None

    @staticmethod
    def update(sport_id, sport_name=None, players_required=None):
        update_data = {}
        if sport_name:
            update_data["sport_name"] = sport_name
        if players_required:
            update_data["players_required"] = players_required
        if not update_data:
            return None
        response = supabase.table("sports").update(update_data).eq("sport_id", sport_id).execute()
        return response.data[0] if response.data else None

    @staticmethod
    def delete(sport_id):
        response = supabase.table("sports").delete().eq("sport_id", sport_id).execute()
        return response.data