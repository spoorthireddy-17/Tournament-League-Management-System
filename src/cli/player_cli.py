from src.services.player_service import PlayerService

def player_menu():
    while True:
        print("\n--- Player Menu ---")
        print("1. Add Player")
        print("2. View All Players")
        print("3. View Player by ID")
        print("4. Update Player")
        print("5. Delete Player")
        print("6. Back")

        choice = input("Enter choice: ")

        if choice == '1':
            name = input("Player Name: ")
            age = int(input("Age: "))
            position = input("Position: ")
            team_id = int(input("Team ID: "))
            player = PlayerService.add_player(name, age, position, team_id)
            print(f"✅ Player added: {player}")

        elif choice == '2':
            players = PlayerService.list_players()
            if players:
                for p in players:
                    print(p)
            else:
                print("⚠️ No players found.")

        elif choice == '3':
            player_id = int(input("Enter Player ID: "))
            player = PlayerService.get_player(player_id)
            print(player if player else "⚠️ Player not found.")

        elif choice == '4':
            player_id = int(input("Enter Player ID to update: "))
            name = input("New Name (leave blank to skip): ").strip()
            age = input("New Age (leave blank to skip): ").strip()
            age = int(age) if age else None
            position = input("New Position (leave blank to skip): ").strip()
            team_id = input("New Team ID (leave blank to skip): ").strip()
            team_id = int(team_id) if team_id else None

            updated = PlayerService.update_player(
                player_id,
                name if name else None,
                age,
                position if position else None,
                team_id
            )
            print(f"✅ Updated: {updated}" if updated else "⚠️ Update failed.")

        elif choice == '5':
            player_id = int(input("Enter Player ID to delete: "))
            deleted = PlayerService.delete_player(player_id)
            print("✅ Player deleted." if deleted else "⚠️ Delete failed.")

        elif choice == '6':
            break
        else:
            print("❌ Invalid choice!")