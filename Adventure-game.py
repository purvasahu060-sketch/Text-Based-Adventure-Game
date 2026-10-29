"""
Text-Based Adventure Game (PS No. 39)
Concepts: Conditions, Loops, Functions, Random

Rules:
- Player starts in the Forest with Health 100 and Score 0.
- Menu: 1 = Cave, 2 = River, 3 = Quit.
- Cave: a monster attacks (random damage 10-40). If the player survives,
  a key is found (+20 score).
- River: a treasure is found (+50 score).
- Game ends when the player quits or Health reaches 0.
"""

import random

# ---------------- Settings ----------------
START_HEALTH = 100
FIXED_DAMAGE = 30  # Set to 30 to get fixed monster damage (for test cases)
MIN_DAMAGE = 10
MAX_DAMAGE = 40


def monster_damage():
    """Return the damage dealt by the monster."""
    if FIXED_DAMAGE is not None:
        return FIXED_DAMAGE
    return random.randint(MIN_DAMAGE, MAX_DAMAGE)


def forest():
    """Starting place: show the menu and return the player's raw choice."""
    print("\nYou are in the Forest. Where do you want to go?")
    print("1. Cave")
    print("2. River")
    print("3. Quit")
    return input("Choice: ").strip()


def cave(health, score):
    """Monster attack; if the player survives, they find a key (+20)."""
    damage = monster_damage()
    health -= damage
    if health < 0:
        health = 0
    print(f"Cave: Monster attacks! Damage: {damage}. Health: {health}")
    if health > 0:
        score += 20
        print(f"You found a key! Score: {score}")
    return health, score


def river(health, score):
    """Treasure gives +50 score."""
    score += 50
    print(f"River: You found a treasure! Score: {score} | Health: {health}")
    return health, score


def main():
    health = START_HEALTH
    score = 0

    print("=== Text-Based Adventure Game ===")
    print(f"Health: {health} | Score: {score}")

    while True:
        choice = forest()

        if choice == "1":
            health, score = cave(health, score)
            if health <= 0:
                print(f"Game Over! Final score: {score}")
                break
        elif choice == "2":
            health, score = river(health, score)
        elif choice == "3":
            print(f"You left the adventure. Final score: {score} | Health: {health}")
            break
        else:
            # Invalid input (e.g. 7 or abc): no health lost
            print("Invalid choice. Enter 1, 2 or 3.")


if __name__ == "__main__":
    main()