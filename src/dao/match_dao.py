from src.db_client import supabase

class MatchDAO:
    @staticmethod
    def insert(tournament_id, team1_id, team2_id, score_team1=0, score_team2=0, winner=None, match_date=None):
        response = supabase.table("matches").insert({
            "tournament_id": tournament_id,
            "team1_id": team1_id,
            "team2_id": team2_id,
            "score_team1": score_team1,
            "score_team2": score_team2,
            "winner": winner,
            "match_date": match_date
        }).execute()
        return response.data[0] if response.data else None

    @staticmethod
    def get_all():
        response = supabase.table("matches").select("*").execute()
        return response.data

    @staticmethod
    def get_by_id(match_id):
        response = supabase.table("matches").select("*").eq("match_id", match_id).execute()
        return response.data[0] if response.data else None

    @staticmethod
    def update(match_id, tournament_id=None, team1_id=None, team2_id=None,
               score_team1=None, score_team2=None, winner=None, match_date=None):
        update_data = {}
        if tournament_id:
            update_data["tournament_id"] = tournament_id
        if team1_id:
            update_data["team1_id"] = team1_id
        if team2_id:
            update_data["team2_id"] = team2_id
        if score_team1 is not None:
            update_data["score_team1"] = score_team1
        if score_team2 is not None:
            update_data["score_team2"] = score_team2
        if winner:
            update_data["winner"] = winner
        if match_date:
            update_data["match_date"] = match_date
        if not update_data:
            return None
        response = supabase.table("matches").update(update_data).eq("match_id", match_id).execute()
        return response.data[0] if response.data else None

    @staticmethod
    def delete(match_id):
        response = supabase.table("matches").delete().eq("match_id", match_id).execute()
        return response.data