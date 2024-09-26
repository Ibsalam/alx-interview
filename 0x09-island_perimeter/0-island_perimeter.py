#!/usr/bin/python3
"""Island perimeter computing module.
"""

def island_perimeter(grid):
    """Computes the perimeter of an island with no lakes."""
    perimeter = 0
    n = len(grid)
    
    for i, row in enumerate(grid):
        m = len(row)
        for j, cell in enumerate(row):
            if cell == 1:
                # Check if each side is water or the boundary
                if i == 0 or grid[i - 1][j] == 0:  # Top
                    perimeter += 1
                if j == m - 1 or row[j + 1] == 0:  # Right
                    perimeter += 1
                if i == n - 1 or grid[i + 1][j] == 0:  # Bottom
                    perimeter += 1
                if j == 0 or row[j - 1] == 0:  # Left
                    perimeter += 1

    return perimeter
