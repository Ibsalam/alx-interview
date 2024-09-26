#!/usr/bin/python3
"""Island perimeter computing module.
"""

def island_perimeter(grid):
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # Each land cell contributes 4 to the perimeter
                perimeter += 4

                # If there's land to the top, subtract 2 from the perimeter
                if r > 0 and grid[r - 1][c] == 1:
                    perimeter -= 2

                # If there's land to the left, subtract 2 from the perimeter
                if c > 0 and grid[r][c - 1] == 1:
                    perimeter -= 2

    return perimeter
