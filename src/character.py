class Character:
    """Represents a D&D character."""
    
    def __init__(self, name: str, race: str, character_class: str, level: int, hit_points: int):
        if not name.strip():
            raise ValueError("Character name cannot be empty.")
        if not race.strip():
            raise ValueError("Character race cannot be empty")
        if not character_class.strip():
            raise ValueError("Character class cannot be empty.")
        if level < 1:
            raise ValueError("Character level mus be at least 1.")
        if hit_points < 0:
            raise ValueError("Hit points cannot be negative.")
        
        self.name = name
        self.race = race
        self.character_class = character_class
        self.level = level
        self.hit_points = hit_points
        