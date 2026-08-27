class Character:
    """Represent a D&D character."""

    def __init__(
        self,
        name: str,
        race: str,
        character_class: str,
        level: int,
        hit_points: int
    ) -> None:
        """Initialize a D&D character with validated attributes."""

        if not isinstance(name, str) or not name.strip():
            raise ValueError("Character name cannot be empty.")

        if not isinstance(race, str) or not race.strip():
            raise ValueError("Character race cannot be empty.")

        if not isinstance(character_class, str) or not character_class.strip():
            raise ValueError("Character class cannot be empty.")

        if not isinstance(level, int):
            raise ValueError("Character level must be an integer.")

        if level < 1:
            raise ValueError("Character level must be at least 1.")

        if not isinstance(hit_points, int):
            raise ValueError("Hit points must be an integer.")

        if hit_points < 0:
            raise ValueError("Hit points cannot be negative.")

        self.name = name
        self.race = race
        self.character_class = character_class
        self.level = level
        self.hit_points = hit_points

    def take_damage(self, amount: int) -> None:
        """Reduce the character's hit points by the specified amount."""

        if amount < 0:
            raise ValueError("Damage cannot be negative.")

        self.hit_points = max(0, self.hit_points - amount)

    def heal(self, amount: int) -> None:
        """Restore the character's hit points by the specified amount."""

        if amount < 0:
            raise ValueError("Healing cannot be negative.")

        self.hit_points += amount

    def get_summary(self) -> str:
        """Return a formatted summary of the character."""

        return (
            f"{self.name} | "
            f"{self.race} {self.character_class} | "
            f"Level {self.level} | "
            f"{self.hit_points} HP"
        )

    def to_dict(self) -> dict:
        """Convert the character into a dictionary."""

        return {
            "name": self.name,
            "race": self.race,
            "character_class": self.character_class,
            "level": self.level,
            "hit_points": self.hit_points
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Character":
        """Create a character from a dictionary."""

        return cls(
            data["name"],
            data["race"],
            data["character_class"],
            data["level"],
            data["hit_points"]
        )