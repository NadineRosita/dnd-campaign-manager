from character import Character

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