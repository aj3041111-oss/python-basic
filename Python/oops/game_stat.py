"""
game_status.py — Game Status Tracker

Tracks a player's health, score, and level during a play session.
Lets the player apply damage/healing, add score, level up, and
view a formatted status display, all from a simple text menu.
"""


class GameStatus:
    def __init__(self, name: str = "Player", max_health: int = 100):
        self.name = name
        self.max_health = max_health
        self.health = max_health
        self.score = 0
        self.level = 1
        self.alive = True

    def damage(self, amount: int):
        if amount < 0:
            raise ValueError("Damage amount cannot be negative.")
        self.health = max(0, self.health - amount)
        if self.health == 0:
            self.alive = False

    def heal(self, amount: int):
        if amount < 0:
            raise ValueError("Heal amount cannot be negative.")
        if not self.alive:
            raise ValueError("Cannot heal a defeated player. Revive first.")
        self.health = min(self.max_health, self.health + amount)

    def add_score(self, points: int):
        self.score += points

    def level_up(self):
        self.level += 1
        self.max_health += 10
        self.health = self.max_health  # full heal on level up

    def revive(self):
        self.alive = True
        self.health = self.max_health

    def status_bar(self, width: int = 20) -> str:
        filled = int(width * self.health / self.max_health)
        return "[" + "#" * filled + "-" * (width - filled) + "]"

    def display(self):
        state = "ALIVE" if self.alive else "DEFEATED"
        print(
            f"\n--- {self.name}'s Status ---\n"
            f"  Level : {self.level}\n"
            f"  Health: {self.health}/{self.max_health} {self.status_bar()}\n"
            f"  Score : {self.score}\n"
            f"  State : {state}\n"
        )


MENU = """
Choose an action:
  1) Show status
  2) Take damage
  3) Heal
  4) Add score
  5) Level up
  6) Revive
  q) Quit
"""


def main():
    name = input("Enter player name (or press Enter for 'Player'): ").strip() or "Player"
    player = GameStatus(name=name)

    print(MENU)
    player.display()

    while True:
        choice = input("Action: ").strip().lower()

        if choice == "1":
            player.display()
        elif choice == "2":
            try:
                amount = int(input("  Damage amount: ").strip())
                player.damage(amount)
                player.display()
            except ValueError as e:
                print(f"  Error: {e}")
        elif choice == "3":
            try:
                amount = int(input("  Heal amount: ").strip())
                player.heal(amount)
                player.display()
            except ValueError as e:
                print(f"  Error: {e}")
        elif choice == "4":
            try:
                points = int(input("  Points to add: ").strip())
                player.add_score(points)
                player.display()
            except ValueError:
                print("  Please enter a valid integer.")
        elif choice == "5":
            player.level_up()
            print("  Level up!")
            player.display()
        elif choice == "6":
            player.revive()
            print("  Player revived.")
            player.display()
        elif choice == "q":
            print("Goodbye!")
            break
        else:
            print(MENU)


if __name__ == "__main__":
    main()