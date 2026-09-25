"""
mediacatalogue.py — Media Catalogue

An in-memory catalogue for tracking media items (books, movies, music, etc.).
Supports adding, removing, listing, and searching items by title or type.
"""

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class MediaItem:
    title: str
    media_type: str  # e.g. "Book", "Movie", "Music"
    creator: str      # author, director, artist
    year: Optional[int] = None
    rating: Optional[float] = None  # 0-10

    def __str__(self):
        year_str = f" ({self.year})" if self.year else ""
        rating_str = f" — {self.rating}/10" if self.rating is not None else ""
        return f"[{self.media_type}] {self.title}{year_str} by {self.creator}{rating_str}"


class MediaCatalogue:
    def __init__(self):
        self.items: List[MediaItem] = []

    def add(self, item: MediaItem):
        self.items.append(item)

    def remove(self, title: str) -> bool:
        for item in self.items:
            if item.title.lower() == title.lower():
                self.items.remove(item)
                return True
        return False

    def search(self, keyword: str) -> List[MediaItem]:
        keyword = keyword.lower()
        return [
            item for item in self.items
            if keyword in item.title.lower()
            or keyword in item.creator.lower()
            or keyword in item.media_type.lower()
        ]

    def list_all(self) -> List[MediaItem]:
        return list(self.items)

    def filter_by_type(self, media_type: str) -> List[MediaItem]:
        return [i for i in self.items if i.media_type.lower() == media_type.lower()]


MENU = """
Choose an action:
  1) Add item
  2) Remove item
  3) List all items
  4) Search
  5) Filter by type
  q) Quit
"""


def prompt_optional_float(message: str):
    raw = input(message).strip()
    if not raw:
        return None
    try:
        return float(raw)
    except ValueError:
        print("  Invalid number, skipping rating.")
        return None


def prompt_optional_int(message: str):
    raw = input(message).strip()
    if not raw:
        return None
    try:
        return int(raw)
    except ValueError:
        print("  Invalid number, skipping year.")
        return None


def main():
    catalogue = MediaCatalogue()
    print("=== Media Catalogue ===")
    print(MENU)

    while True:
        choice = input("Action: ").strip().lower()

        if choice == "1":
            title = input("  Title: ").strip()
            media_type = input("  Type (Book/Movie/Music/...): ").strip()
            creator = input("  Creator (author/director/artist): ").strip()
            year = prompt_optional_int("  Year (optional): ")
            rating = prompt_optional_float("  Rating out of 10 (optional): ")
            catalogue.add(MediaItem(title, media_type, creator, year, rating))
            print(f"  Added: {title}")

        elif choice == "2":
            title = input("  Title to remove: ").strip()
            if catalogue.remove(title):
                print(f"  Removed: {title}")
            else:
                print("  Item not found.")

        elif choice == "3":
            items = catalogue.list_all()
            if not items:
                print("  Catalogue is empty.")
            for item in items:
                print(f"  {item}")

        elif choice == "4":
            keyword = input("  Search keyword: ").strip()
            results = catalogue.search(keyword)
            if not results:
                print("  No matches found.")
            for item in results:
                print(f"  {item}")

        elif choice == "5":
            media_type = input("  Type to filter by: ").strip()
            results = catalogue.filter_by_type(media_type)
            if not results:
                print("  No matches found.")
            for item in results:
                print(f"  {item}")

        elif choice == "q":
            print("Goodbye!")
            break

        else:
            print(MENU)


if __name__ == "__main__":
    main()