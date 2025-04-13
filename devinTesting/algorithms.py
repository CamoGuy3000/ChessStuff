# This module will house algorithms to determine which electromagnets (board positions)
# should be activated to move a piece from one location to another.
# Each algorithm will return a list of (row, col) tuples that represent the path.

from typing import List, Tuple

Position = Tuple[int, int]


def simple_straight_path(start: Position, end: Position) -> List[Position]:
    """
    Moves in a straight line first along rows, then columns (or vice versa).
    Avoids diagonal movement.
    """
    path = []
    r1, c1 = start
    r2, c2 = end

    # Move vertically first
    step = 1 if r2 > r1 else -1
    for r in range(r1, r2, step):
        path.append((r, c1))

    # Move horizontally
    step = 1 if c2 > c1 else -1
    for c in range(c1, c2 + step, step):
        path.append((r2, c))

    return path


def diagonal_or_straight_path(start: Position, end: Position) -> List[Position]:
    """
    Attempts diagonal movement first, then straight.
    """
    path = []
    r1, c1 = start
    r2, c2 = end

    dr = 1 if r2 > r1 else -1
    dc = 1 if c2 > c1 else -1

    while r1 != r2 and c1 != c2:
        path.append((r1, c1))
        r1 += dr
        c1 += dc

    # Finish row or column movement
    while r1 != r2:
        path.append((r1, c1))
        r1 += dr

    while c1 != c2:
        path.append((r1, c1))
        c1 += dc

    path.append((r1, c1))
    return path


# Add more pathing algorithms below as needed.

if __name__ == "__main__":
    print("Straight path (2, 2) to (5, 6):")
    print(simple_straight_path((2, 2), (5, 6)))

    print("Diagonal then straight path (2, 2) to (5, 6):")
    print(diagonal_or_straight_path((2, 2), (5, 6)))