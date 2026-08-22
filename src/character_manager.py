from character import Character
import json
from pathlib import Path

class CharacterManager:
    """Manages a collection of D&D characters."""
    
    def __init__(self):
        self.characters: list[Character] = []
        
    
    def add_character(self, character: Character) -> None:
        """Add a character to the collection."""
        self.characters.append(character)
        
    
    def get_characters(self) -> list [Character]:
        """Return all characters."""
        return self.characters
    
    def get_character(self, index:int) -> Character:
        """Return a character by its index."""
        return self.characters[index]
    
    def remove_character(self, index:int) -> Character:
        """Remove and return a character by its index."""
        return self.characters.pop(index)
    
    def save_to_file(self, file_path: str) -> None:
        """Save all characters to a JSON file."""
        path = Path(file_path)
        
        data = [character.to_dict() for character in self.characters]
        
        with path.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
        
    
    def load_from_file(self, file_path:str) -> None:
        """Load characters from a JSON file."""
        path = Path(file_path)
        
        if not path.exists():
            return
        
        with path.open("r", encoding="utf-8") as file:
            data = json.load(file)
            
        self.characters = [
            Character.from_dict(character_data)
            for character_data in data
        ]
    
    