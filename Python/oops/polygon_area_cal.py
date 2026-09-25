"""
polygon_area_calculator.py — Polygon Area Calculator

Calculates the area (and perimeter) of a simple polygon given its
vertex coordinates, using the Shoelace formula. Accepts vertices
entered interactively, in order (clockwise or counter-clockwise).
"""

import math
from typing import List, Tuple

Point = Tuple[float, float]


def polygon_area(vertices: List[Point]) -> float:
    """Compute polygon area via the Shoelace formula."""
    n = len(vertices)
    if n < 3:
        raise ValueError("A polygon needs at least 3 vertices.")

    area = 0.0
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        area += x1 * y2 - x2 * y1

    return abs(area) / 2.0


def polygon_perimeter(vertices: List[Point]) -> float:
    n = len(vertices)
    if n < 2:
        return 0.0

    perimeter = 0.0
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        perimeter += math.hypot(x2 - x1, y2 - y1)

    return perimeter


def prompt_point(index: int) -> Point:
    while True:
        raw = input(f"  Vertex {index} (x,y): ").strip()
        parts = raw.replace(" ", "").split(",")
        if len(parts) != 2:
            print("  Please enter coordinates as: x,y")
            continue
        try:
            x, y = float(parts[0]), float(parts[1])
            return (x, y)
        except ValueError:
            print("  Please enter numeric coordinates, e.g. 3,4")


def main():
    print("=== Polygon Area Calculator ===")
    print("Enter vertices in order (clockwise or counter-clockwise).\n")

    while True:
        try:
            n_raw = input("Number of vertices (min 3, or 'q' to quit): ").strip()
        except EOFError:
            break

        if n_raw.lower() == "q":
            break

        try:
            n = int(n_raw)
            if n < 3:
                print("  A polygon needs at least 3 vertices.\n")
                continue
        except ValueError:
            print("  Please enter a valid integer.\n")
            continue

        vertices = [prompt_point(i + 1) for i in range(n)]

        area = polygon_area(vertices)
        perimeter = polygon_perimeter(vertices)

        print(
            f"\n  Vertices : {vertices}\n"
            f"  Area     : {area:.4f} square units\n"
            f"  Perimeter: {perimeter:.4f} units\n"
        )

    print("Goodbye!")


if __name__ == "__main__":
    main()