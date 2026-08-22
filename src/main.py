"""Main entry point for the D&D Campaign Manager."""
from character import *
from character_manager import *
## from character import Character
## from character_manager import CharacterManager


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
    

def create_character(manager: CharacterManager) -> None:
    """Create a new character from user input."""
    print("\n--- Create Character ---")
    
    while True:
        try:
            name = input("Name: ")
            race = input("Race: ")
            character_class = input("Character class: ")
            level = get_integer_input("Level: ")
            hit_points = get_integer_input("Hit points: ")
    
            character = Character(name, race, character_class, level, hit_points)
    
            manager.add_character(character)
            print(f"\nCharacter '{name} created successfully!")
            break
        
        except (ValueError, TypeError) as error:
            print(f"\nInvalid character data: {error}")
            print("Please try again.\n")

def get_integer_input(prompt: str) -> int:
    """Ask the user for an integer until a valid value is provided."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


def list_characters(manager: CharacterManager) -> None:
    """Display all characters."""
    print("\n---Characters---")
    
    characters = manager.get_characters()
    
    if not characters:
        print("No characters have been created yet.")
        return
    
    for index, character in enumerate(characters, start=1):
        print(f"{index}.{character.get_summary()}")

def view_character(manager: CharacterManager) -> None:
    """Display detailed information about a character."""
    characters = manager.get_characters()
    
    if not characters:
        print("\nNo characters have been created yet.")
        return
    
    list_characters(manager)
    index = get_integer_input("\nChoose a character: ")
    if index < 1 or index > len(characters):
        print("Invalid character selection.")
        return
    
    character = manager.get_character(index -1)
    
    print("\n---Character Details---")
    print(f"Name: {character.name}")
    print(f"Race: {character.race}")
    print(f"Class: {character.character_class}")
    print(f"Level: {character.level}")
    print(f"Hit Points: {character.hit_points}")

def delete_character(manager: CharacterManager) -> None:
    """Delete a character after confirmation."""
    characters = manager.get_characters()
    
    if not characters:
        print("\nNo characters have been created yet.")
        return
    
    list_characters(manager)
    index = get_integer_input("\nChoose a character to delete: ")
    if index <1 or index > len(characters):
        print("Invalid character selection.")
        return
    
    character = manager.get_character(index -1)
    confirmation = input(
        f"Are you sure you want to delete '{character.name}'? (y/n): "
    ).strip().lower()
    
    if confirmation != "y":
        print("Deletion cancelled.")
        return
    
    deleted_character = manager.remove_character(index -1)
    print(
        f"Character '{deleted_character.name}' has been deleted successfully."
    )
    

def main() -> None:
    """Run the application."""
    manager = CharacterManager()
    
    while True:
        display_menu()
        
        choice = input("\n Choose an option:")
        if choice == "1":
            create_character(manager)
        elif choice == "2":
            list_characters(manager)
        elif choice == "3":
            view_character(manager)
        elif choice == "4":
            delete_character(manager)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
            
            
    

if __name__ == "__main__":
    main()