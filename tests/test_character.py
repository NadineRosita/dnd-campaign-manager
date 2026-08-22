from src.character import Character
import pytest

def test_character_creation():
    character = Character(
        "Aria",
        "Elf",
        "Wizard",
        3,
        18
    )
    
    assert character.name == "Aria"
    assert character.race == "Elf"
    assert character.character_class == "Wizard"
    assert character.level == 3
    assert character.hit_points == 18

def test_character_invalid_level():
    with pytest.raises(ValueError):
        Character(
            "Aria",
            "Elf",
            "Wizard",
            0,
            18
        )
        

def test_character_invalid_hit_points():
    with pytest.raises(ValueError):
        Character(
            "Aria",
            "Elf",
            "Wizard",
            3,
            -1
        )

def test_character_damage():
    character = Character(
            "Aria",
            "Elf",
            "Wizard",
            3,
            18
        )
    
    character.take_damage(5)
    assert character.hit_points == 13
    

def test_character_healing():
    character = Character(
            "Aria",
            "Elf",
            "Wizard",
            3,
            18
        )
    
    character.take_damage(5)
    character.heal(3)
    
    assert character.hit_points == 16
