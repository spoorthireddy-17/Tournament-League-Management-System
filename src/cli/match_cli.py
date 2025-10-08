from src.services.match_service import MatchService

def match_menu():
    while True:
        print("\n--- Match Menu ---")
        print("1. Add Match")
        print("2. View All Matches")
        print("3. View Match by ID")
        print("4. Update Match")
        print("5. Delete Match")
        print("6. Back")

        choice = input("Enter choice: ")

        if choice == '1':
            tournament_id = int(input("Tournament ID: "))
            team1_id = int(input("Team 1 ID: "))
            team2_id = int(input("Team 2 ID: "))
            score_team1 = int(input("Score Team 1 (default 0): ") or 0)
            score_team2 = int(input("Score Team 2 (default 0): ") or 0)
            winner = input("Winner Team ID (leave blank if unknown): ").strip()
            winner = int(winner) if winner else None
            match_date = input("Match Date (YYYY-MM-DD, optional): ").strip() or None

            match = MatchService.add_match(tournament_id, team1_id, team2_id,
                                           score_team1, score_team2, winner, match_date)
            print(f"✅ Match added: {match}")

        elif choice == '2':
            matches = MatchService.list_matches()
            if matches:
                for m in matches:
                    print(m)
            else:
                print("⚠️ No matches found.")

        elif choice == '3':
            match_id = int(input("Enter Match ID: "))
            match = MatchService.get_match(match_id)
            print(match if match else "⚠️ Match not found.")

        elif choice == '4':
            match_id = int(input("Enter Match ID to update: "))
            tournament_id = input("New Tournament ID (leave blank to skip): ").strip()
            tournament_id = int(tournament_id) if tournament_id else None
            team1_id = input("New Team 1 ID (leave blank to skip): ").strip()
            team1_id = int(team1_id) if team1_id else None
            team2_id = input("New Team 2 ID (leave blank to skip): ").strip()
            team2_id = int(team2_id) if team2_id else None
            score_team1 = input("New Score Team 1 (leave blank to skip): ").strip()
            score_team1 = int(score_team1) if score_team1 else None
            score_team2 = input("New Score Team 2 (leave blank to skip): ").strip()
            score_team2 = int(score_team2) if score_team2 else None
            winner = input("New Winner Team ID (leave blank to skip): ").strip()
            winner = int(winner) if winner else None
            match_date = input("New Match Date (YYYY-MM-DD, leave blank to skip): ").strip() or None

            updated = MatchService.update_match(match_id, tournament_id, team1_id, team2_id,
                                                score_team1, score_team2, winner, match_date)
            print(f"✅ Updated: {updated}" if updated else "⚠️ Update failed.")

        elif choice == '5':
            match_id = int(input("Enter Match ID to delete: "))
            deleted = MatchService.delete_match(match_id)
            print("✅ Match deleted." if deleted else "⚠️ Delete failed.")

        elif choice == '6':
            break
        else:
            print("❌ Invalid choice!")