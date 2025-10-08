from .cli.sport_cli import sport_menu
from .cli.tournament_cli import tournament_menu
from .cli.team_cli import team_menu
from .cli.player_cli import player_menu
from .cli.match_cli import match_menu


def main_menu():
    while True:
        print("\n=== Tournament / League Management System ===")
        print("1. Sports")
        print("2. Tournaments")
        print("3. Teams")
        print("4. Players")
        print("5. Matches")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            sport_menu()
        elif choice == '2':
            tournament_menu()
        elif choice == '3':
            team_menu()
        elif choice == '4':
            player_menu()
        elif choice == '5':
            match_menu()
        elif choice == '6':
            print("Exiting... Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice! Please try again.")

if __name__ == "__main__":
    main_menu()