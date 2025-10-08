from src.services.team_service import TeamService

def team_menu():
    while True:
        print("\n--- Team Menu ---")
        print("1. Add Team")
        print("2. View All Teams")
        print("3. View Team by ID")
        print("4. Update Team")
        print("5. Delete Team")
        print("6. Back")

        choice = input("Enter choice: ")

        if choice == '1':
            name = input("Team Name: ")
            coach = input("Coach Name: ")
            tournament_id = int(input("Tournament ID: "))
            team = TeamService.add_team(name, coach, tournament_id)
            print(f"✅ Team added: {team}")

        elif choice == '2':
            teams = TeamService.list_teams()
            if teams:
                for t in teams:
                    print(t)
            else:
                print("⚠️ No teams found.")

        elif choice == '3':
            team_id = int(input("Enter Team ID: "))
            team = TeamService.get_team(team_id)
            print(team if team else "⚠️ Team not found.")

        elif choice == '4':
            team_id = int(input("Enter Team ID to update: "))
            name = input("New Team Name (leave blank to skip): ").strip()
            coach = input("New Coach Name (leave blank to skip): ").strip()
            tournament_id = input("New Tournament ID (leave blank to skip): ").strip()
            tournament_id = int(tournament_id) if tournament_id else None

            updated = TeamService.update_team(
                team_id,
                name if name else None,
                coach if coach else None,
                tournament_id
            )
            print(f"✅ Updated: {updated}" if updated else "⚠️ Update failed.")

        elif choice == '5':
            team_id = int(input("Enter Team ID to delete: "))
            deleted = TeamService.delete_team(team_id)
            print("✅ Team deleted." if deleted else "⚠️ Delete failed.")

        elif choice == '6':
            break
        else:
            print("❌ Invalid choice!")