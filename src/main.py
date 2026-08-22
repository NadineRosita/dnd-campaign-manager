"""Main entry point for the D&D Campaign Manager."""

from character import Character
from character_manager import CharacterManager

def display_menu() -> None:
    """Display the main menu."""
    print()
    print("====================================")
    print("|       D&D CAMPAIGN MANAGER       |")
    print("====================================")
    print()
    print("1. Create character")
    print("2. List character")
    print("3. View character")
    print("4. Delete character")
    print("5. Exit")
    

def main() -> None:
    """Run the application."""
    manager = CharacterManager()
    
    while True:
        display_menu()
        
        choice = input("\n Choose an option:")
        if choice == "1":
            print("Create character")
        elif choice == "2":
            print("List characters")
        elif choice == "3":
            print("View character")
        elif choice == "4":
            print("Delete character")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
            
            
    

if __name__ == "__main__":
    main()