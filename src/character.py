class Character:
    """Represents a D&D character."""
    
    def __init__(self, name: str, race: str, character_class: str, level: int, hit_points: int):
        if not name.strip() or not isinstance(name, str):
            raise ValueError("Character name cannot be empty.")
        if not race.strip() or not isinstance(race, str):
            raise ValueError("Character race cannot be empty")
        if not character_class.strip() or not isinstance(character_class, str):
            raise ValueError("Character class cannot be empty.")
        if not isinstance(level, int):
            raise ValueError("Character level must be an integer.")
        if level < 1:
            raise ValueError("Character level mus be at least 1.")
        if not isinstance(hit_points, int):
            raise ValueError("Hit points must be an integer.")
        if hit_points < 0:
            raise ValueError("Hit points cannot be negative.")
        
        self.name = name
        self.race = race
        self.character_class = character_class
        self.level = level
        self.hit_points = hit_points
        
        
    def take_damage(self, amount:int):
        """Reduce the character's hit points."""
        if amount < 0:
            raise ValueError("Damage cannot be negative.")
        
        self.hit_points = max(0, self.hit_points - amount)
        
    def heal(self, amount:int):
        """Restores the character's hit points."""
        if amount < 0:
            raise ValueError("Healing cannot be negative.")
        
        self.hit_points += amount
    
    def get_summary(self) -> str:
        """Return a formatted summary of the character."""
        return(
            f"{self.name} | "
            f"{self.race} {self.character_class} | "
            f"Level {self.level} | "
            f"{self.hit_points} HP"
        )
        
    
    def to_dict(self) -> dict:
        """Convert the character into a dictionary."""
        return{
            "name": self.name,
            "race": self.race,
            "character_class": self.character_class,
            "level": self.level,
            "hit_points": self.hit_points
        }
    @classmethod
    def from_dict(cls, data: dict) -> "Character":
        """Create a character from a disctionary."""
        return cls(
            data["name"],
            data["race"],
            data["character_class"],
            data["level"],
            data["hit_points"]
        )
