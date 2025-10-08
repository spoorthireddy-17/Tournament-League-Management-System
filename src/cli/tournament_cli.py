from src.services.tournament_service import TournamentService

def tournament_menu():
    while True:
        print("\n--- Tournament Menu ---")
        print("1. Add Tournament")
        print("2. View All Tournaments")
        print("3. View Tournament by ID")
        print("4. Update Tournament")
        print("5. Delete Tournament")
        print("6. Back")

        choice = input("Enter choice: ")

        if choice == '1':
            name = input("Tournament Name: ")
            type = input("Type (League/Knockout): ")
            start_date = input("Start Date (YYYY-MM-DD): ")
            end_date = input("End Date (YYYY-MM-DD): ")
            sport_id = int(input("Sport ID: "))
            tournament = TournamentService.add_tournament(name, type, start_date, end_date, sport_id)
            print(f"✅ Tournament added: {tournament}")

        elif choice == '2':
            tournaments = TournamentService.list_tournaments()
            if tournaments:
                for t in tournaments:
                    print(t)
            else:
                print("⚠️ No tournaments found.")

        elif choice == '3':
            tournament_id = int(input("Enter Tournament ID: "))
            tournament = TournamentService.get_tournament(tournament_id)
            print(tournament if tournament else "⚠️ Tournament not found.")

        elif choice == '4':
            tournament_id = int(input("Enter Tournament ID to update: "))
            name = input("New Name (leave blank to skip): ").strip()
            type = input("New Type (League/Knockout, leave blank to skip): ").strip()
            start_date = input("New Start Date (YYYY-MM-DD, leave blank to skip): ").strip()
            end_date = input("New End Date (YYYY-MM-DD, leave blank to skip): ").strip()
            sport_id = input("New Sport ID (leave blank to skip): ").strip()
            sport_id = int(sport_id) if sport_id else None

            updated = TournamentService.update_tournament(
                tournament_id,
                name if name else None,
                type if type else None,
                start_date if start_date else None,
                end_date if end_date else None,
                sport_id
            )
            print(f"✅ Updated: {updated}" if updated else "⚠️ Update failed.")

        elif choice == '5':
            tournament_id = int(input("Enter Tournament ID to delete: "))
            deleted = TournamentService.delete_tournament(tournament_id)
            print("✅ Tournament deleted." if deleted else "⚠️ Delete failed.")

        elif choice == '6':
            break
        else:
            print("❌ Invalid choice!")