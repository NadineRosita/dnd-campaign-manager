"""Main entry point for the D&D Campaign Manager."""

from character import Character

aria = Character("Aria", "Elf", "Wizard", 3, 18)

print(aria.get_summary())
aria.take_damage(5)
print(aria.get_summary())
aria.heal(3)
print(aria.get_summary())
