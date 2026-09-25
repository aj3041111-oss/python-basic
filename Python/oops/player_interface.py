"""
player_interface.py — Text-Based Media Player Interface

Simulates a simple media player: maintains a playlist and supports
play, pause, stop, next, previous, and volume controls via a text menu.
"""

from typing import List, Optional


class PlayerInterface:
    def __init__(self):
        self.playlist: List[str] = []
        self.current_index: Optional[int] = None
        self.is_playing: bool = False
        self.volume: int = 50  # 0-100

    def add_track(self, track: str):
        self.playlist.append(track)
        if self.current_index is None:
            self.current_index = 0

    def remove_track(self, track: str) -> bool:
        if track in self.playlist:
            idx = self.playlist.index(track)
            self.playlist.remove(track)
            if not self.playlist:
                self.current_index = None
                self.is_playing = False
            elif self.current_index is not None and idx <= self.current_index:
                self.current_index = max(0, self.current_index - 1)
            return True
        return False

    def play(self):
        if not self.playlist:
            raise ValueError("Playlist is empty.")
        self.is_playing = True

    def pause(self):
        self.is_playing = False

    def stop(self):
        self.is_playing = False
        self.current_index = 0 if self.playlist else None

    def next_track(self):
        if not self.playlist:
            raise ValueError("Playlist is empty.")
        self.current_index = (self.current_index + 1) % len(self.playlist)

    def previous_track(self):
        if not self.playlist:
            raise ValueError("Playlist is empty.")
        self.current_index = (self.current_index - 1) % len(self.playlist)

    def set_volume(self, level: int):
        if not (0 <= level <= 100):
            raise ValueError("Volume must be between 0 and 100.")
        self.volume = level

    def current_track(self) -> Optional[str]:
        if self.current_index is None or not self.playlist:
            return None
        return self.playlist[self.current_index]

    def display(self):
        status = "Playing" if self.is_playing else "Paused/Stopped"
        track = self.current_track() or "(none)"
        print(
            f"\n--- Player Status ---\n"
            f"  Track  : {track}\n"
            f"  State  : {status}\n"
            f"  Volume : {self.volume}\n"
            f"  Playlist ({len(self.playlist)} tracks):\n"
        )
        for i, t in enumerate(self.playlist):
            marker = "-> " if i == self.current_index else "   "
            print(f"  {marker}{i + 1}. {t}")
        print()


MENU = """
Choose an action:
  1) Add track
  2) Remove track
  3) Play
  4) Pause
  5) Stop
  6) Next track
  7) Previous track
  8) Set volume
  9) Show status
  q) Quit
"""


def main():
    player = PlayerInterface()
    print("=== Media Player Interface ===")
    print(MENU)

    while True:
        choice = input("Action: ").strip().lower()

        try:
            if choice == "1":
                track = input("  Track name: ").strip()
                player.add_track(track)
                print(f"  Added: {track}")
            elif choice == "2":
                track = input("  Track name to remove: ").strip()
                print("  Removed." if player.remove_track(track) else "  Track not found.")
            elif choice == "3":
                player.play()
                print(f"  Now playing: {player.current_track()}")
            elif choice == "4":
                player.pause()
                print("  Paused.")
            elif choice == "5":
                player.stop()
                print("  Stopped.")
            elif choice == "6":
                player.next_track()
                print(f"  Now playing: {player.current_track()}")
            elif choice == "7":
                player.previous_track()
                print(f"  Now playing: {player.current_track()}")
            elif choice == "8":
                level = int(input("  Volume (0-100): ").strip())
                player.set_volume(level)
                print(f"  Volume set to {level}")
            elif choice == "9":
                player.display()
            elif choice == "q":
                print("Goodbye!")
                break
            else:
                print(MENU)
        except ValueError as e:
            print(f"  Error: {e}")


if __name__ == "__main__":
    main()