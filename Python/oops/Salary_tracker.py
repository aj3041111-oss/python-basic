"""
salary_tracker.py — Salary Tracker

Logs salary/income entries (date, amount, source) in memory and
provides summaries: totals, monthly breakdown, and averages.
"""

from dataclasses import dataclass
from datetime import datetime
from collections import defaultdict
from typing import List, Optional


@dataclass
class SalaryEntry:
    date: datetime
    amount: float
    source: str
    note: Optional[str] = None

    def __str__(self):
        note_str = f" ({self.note})" if self.note else ""
        return f"{self.date.strftime('%Y-%m-%d')}  ${self.amount:,.2f}  [{self.source}]{note_str}"


class SalaryTracker:
    def __init__(self):
        self.entries: List[SalaryEntry] = []

    def add_entry(self, date: datetime, amount: float, source: str, note: Optional[str] = None):
        if amount < 0:
            raise ValueError("Amount cannot be negative.")
        self.entries.append(SalaryEntry(date, amount, source, note))

    def remove_entry(self, index: int) -> bool:
        if 0 <= index < len(self.entries):
            del self.entries[index]
            return True
        return False

    def total(self) -> float:
        return sum(e.amount for e in self.entries)

    def average(self) -> float:
        if not self.entries:
            return 0.0
        return self.total() / len(self.entries)

    def monthly_breakdown(self) -> dict:
        breakdown = defaultdict(float)
        for e in self.entries:
            key = e.date.strftime("%Y-%m")
            breakdown[key] += e.amount
        return dict(sorted(breakdown.items()))

    def by_source(self) -> dict:
        breakdown = defaultdict(float)
        for e in self.entries:
            breakdown[e.source] += e.amount
        return dict(sorted(breakdown.items(), key=lambda kv: -kv[1]))

    def sorted_entries(self) -> List[SalaryEntry]:
        return sorted(self.entries, key=lambda e: e.date)


MENU = """
Choose an action:
  1) Add entry
  2) Remove entry
  3) List all entries
  4) Show total & average
  5) Monthly breakdown
  6) Breakdown by source
  q) Quit
"""


def prompt_date(message: str) -> datetime:
    while True:
        raw = input(message).strip()
        if not raw:
            return datetime.today()
        try:
            return datetime.strptime(raw, "%Y-%m-%d")
        except ValueError:
            print("  Please enter a date as YYYY-MM-DD, or leave blank for today.")


def prompt_float(message: str) -> float:
    while True:
        raw = input(message).strip()
        try:
            value = float(raw)
            if value < 0:
                print("  Amount cannot be negative.")
                continue
            return value
        except ValueError:
            print("  Please enter a valid number.")


def main():
    tracker = SalaryTracker()
    print("=== Salary Tracker ===")
    print(MENU)

    while True:
        choice = input("Action: ").strip().lower()

        if choice == "1":
            date = prompt_date("  Date (YYYY-MM-DD, blank for today): ")
            amount = prompt_float("  Amount: ")
            source = input("  Source (e.g. Employer, Freelance): ").strip() or "Unspecified"
            note = input("  Note (optional): ").strip() or None
            tracker.add_entry(date, amount, source, note)
            print(f"  Added: {tracker.entries[-1]}")

        elif choice == "2":
            if not tracker.entries:
                print("  No entries to remove.")
                continue
            for i, e in enumerate(tracker.entries):
                print(f"  {i}. {e}")
            try:
                idx = int(input("  Index to remove: ").strip())
                if tracker.remove_entry(idx):
                    print("  Removed.")
                else:
                    print("  Invalid index.")
            except ValueError:
                print("  Please enter a valid integer.")

        elif choice == "3":
            entries = tracker.sorted_entries()
            if not entries:
                print("  No entries yet.")
            for e in entries:
                print(f"  {e}")

        elif choice == "4":
            print(f"  Total entries : {len(tracker.entries)}")
            print(f"  Total income  : ${tracker.total():,.2f}")
            print(f"  Average/entry : ${tracker.average():,.2f}")

        elif choice == "5":
            breakdown = tracker.monthly_breakdown()
            if not breakdown:
                print("  No entries yet.")
            for month, total in breakdown.items():
                print(f"  {month}: ${total:,.2f}")

        elif choice == "6":
            breakdown = tracker.by_source()
            if not breakdown:
                print("  No entries yet.")
            for source, total in breakdown.items():
                print(f"  {source}: ${total:,.2f}")

        elif choice == "q":
            print("Goodbye!")
            break

        else:
            print(MENU)


if __name__ == "__main__":
    main()