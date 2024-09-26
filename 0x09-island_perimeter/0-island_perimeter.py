#!/usr/bin/python3
"""Island perimeter computing module.
"""

def island_perimeter(grid):
    """Computes the perimeter of an island with no lakes."""
    
    # Input validation
    if not grid or not isinstance(grid, list) or not all(isinstance(row, list) for row in grid):
        return 0
    
    n = len(grid)  # Number of rows
    if n == 0:
        return 0
    m = len(grid[0])  # Number of columns

    perimeter = 0
    
    # Iterate through each cell in the grid
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == 1:
                # For each land cell, check all four sides
                # Check top (if on the first row or top cell is water)
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                # Check right (if on the last column or right cell is water)
                if j == m - 1 or grid[i][j + 1] == 0:
                    perimeter += 1
                # Check bottom (if on the last row or bottom cell is water)
                if i == n - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                # Check left (if on the first column or left cell is water)
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1

    return perimeter
