from src.character import Character
from src.character_manager import CharacterManager


def create_test_character(
    name: str = "Aria",
    race: str = "Elf",
    character_class: str = "Wizard",
    level: int = 3,
    hit_points: int = 18
) -> Character:
    """Create a character for testing."""
    return Character(
        name,
        race,
        character_class,
        level,
        hit_points
    )


def test_add_character():
    manager = CharacterManager()
    character = create_test_character()
    
    manager.add_character(character)
    
    assert len(manager.get_characters()) == 1
    assert manager.get_characters()[0] == character

## For multiple characters:
def test_add_multiple_characters():
    manager = CharacterManager()
    
    character_one = create_test_character("Aria")
    character_two = create_test_character("Thorin")
    
    manager.add_character(character_one)
    manager.add_character(character_two)
    
    characters = manager.get_characters()
    
    assert len(characters) == 2
    assert characters[0] == character_one
    assert characters[1] == character_two

def test_get_character():
    manager = CharacterManager()
    
    character = create_test_character()
    manager.add_character(character)
    
    result = manager.get_character(0)
    
    assert result == character

def test_remove_character():
    manager = CharacterManager()
    
    character = create_test_character()
    manager.add_character(character)
    
    removed_character = manager.remove_character(0)
    
    assert removed_character == character
    assert len(manager.get_characters()) == 0
    