from src.services.sport_service import SportService

def sport_menu():
    while True:
        print("\n--- Sports Menu ---")
        print("1. Add Sport")
        print("2. View All Sports")
        print("3. View Sport by ID")
        print("4. Update Sport")
        print("5. Delete Sport")
        print("6. Back")

        choice = input("Enter choice: ")

        if choice == '1':
            name = input("Sport Name: ")
            players_required = int(input("Players required per team: "))
            sport = SportService.add_sport(name, players_required)
            print(f"✅ Sport added: {sport}")

        elif choice == '2':
            sports = SportService.list_sports()
            if sports:
                for s in sports:
                    print(s)
            else:
                print("⚠️ No sports found.")

        elif choice == '3':
            sport_id = int(input("Enter Sport ID: "))
            sport = SportService.get_sport(sport_id)
            print(sport if sport else "⚠️ Sport not found.")

        elif choice == '4':
            sport_id = int(input("Enter Sport ID to update: "))
            name = input("New Sport Name (leave blank to skip): ").strip()
            players_required = input("New Players Required (leave blank to skip): ").strip()
            players_required = int(players_required) if players_required else None
            updated = SportService.update_sport(sport_id, name if name else None, players_required)
            print(f"✅ Updated: {updated}" if updated else "⚠️ Update failed.")

        elif choice == '5':
            sport_id = int(input("Enter Sport ID to delete: "))
            deleted = SportService.delete_sport(sport_id)
            print("✅ Sport deleted." if deleted else "⚠️ Delete failed.")

        elif choice == '6':
            break
        else:
            print("❌ Invalid choice!")