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
    
    def get_character(self, index:int) -> Character:
        """Return a character by its index."""
        return self.characters[index]
    
    def remove_character(self, index:int) -> Character:
        """Remove and return a character by its index."""
        return self.characters.pop(index)
    