"""Main entry point for the D&D Campaign Manager."""

from character import Character

aria = Character("", "Elf", "Wizard", 3, 18)

print(aria.name)
print(aria.race)
print(aria.character_class)
print(aria.level)
print(aria.hit_points)
