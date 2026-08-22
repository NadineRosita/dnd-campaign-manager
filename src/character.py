class Character:
    """Represents a D&D character."""
    
    def __init__(self, name, race, character_class, level, hit_points):
        self.name = name
        self.race = race
        self.character_class = character_class
        self.level = level
        self.hit_points = hit_points