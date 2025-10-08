from src.db_client import supabase

class TournamentDAO:
    @staticmethod
    def insert(name, type, start_date, end_date, sport_id):
        response = supabase.table("tournaments").insert({
            "name": name,
            "type": type,
            "start_date": start_date,
            "end_date": end_date,
            "sport_id": sport_id
        }).execute()
        return response.data[0] if response.data else None

    @staticmethod
    def get_all():
        response = supabase.table("tournaments").select("*").execute()
        return response.data

    @staticmethod
    def get_by_id(tournament_id):
        response = supabase.table("tournaments").select("*").eq("tournament_id", tournament_id).execute()
        return response.data[0] if response.data else None

    @staticmethod
    def update(tournament_id, name=None, type=None, start_date=None, end_date=None, sport_id=None):
        update_data = {}
        if name:
            update_data["name"] = name
        if type:
            update_data["type"] = type
        if start_date:
            update_data["start_date"] = start_date
        if end_date:
            update_data["end_date"] = end_date
        if sport_id:
            update_data["sport_id"] = sport_id
        if not update_data:
            return None
        response = supabase.table("tournaments").update(update_data).eq("tournament_id", tournament_id).execute()
        return response.data[0] if response.data else None

    @staticmethod
    def delete(tournament_id):
        response = supabase.table("tournaments").delete().eq("tournament_id", tournament_id).execute()
        return response.data