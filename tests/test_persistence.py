from src.character import Character
from src.character_manager import CharacterManager
import json

def test_save_characters(tmp_path):
    manager = CharacterManager()

    character = Character(
        "Aria",
        "Elf",
        "Wizard",
        3,
        18
    )

    manager.add_character(character)

    file_path = tmp_path / "characters.json"

    manager.save_to_file(str(file_path))

    assert file_path.exists()
    
    with file_path.open("r", encoding='utf-8') as file:
        data = json.load(file)
        
    assert len(data) == 1
    assert data[0]["name"] == "Aria"
    assert data[0]["race"] == "Elf"
    assert data[0]["character_class"] == "Wizard"
    assert data[0]["level"] == 3
    assert data[0]["hit_points"] == 18
    

def test_load_characters(tmp_path):
    file_path = tmp_path / "characters.json"

    manager = CharacterManager()

    character = Character(
        "Aria",
        "Elf",
        "Wizard",
        3,
        18
    )

    manager.add_character(character)
    manager.save_to_file(str(file_path))

    new_manager = CharacterManager()
    new_manager.load_from_file(str(file_path))

    characters = new_manager.get_characters()

    assert len(characters) == 1
    assert characters[0].name == "Aria"
    assert characters[0].race == "Elf"
    assert characters[0].character_class == "Wizard"
    assert characters[0].level == 3
    assert characters[0].hit_points == 18