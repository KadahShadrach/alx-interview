#!/usr/bin/python3
"""
0. Island Perimeter
"""

def island_perimeter(grid):
    perimeter = 0
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                # Check each side of the cell
                if i == 0 or grid[i-1][j] == 0:  # Top
                    perimeter += 1
                if i == len(grid) - 1 or grid[i+1][j] == 0:  # Bottom
                    perimeter += 1
                if j == 0 or grid[i][j-1] == 0:  # Left
                    perimeter += 1
                if j == len(grid[i]) - 1 or grid[i][j+1] == 0:  # Right
                    perimeter += 1

    return perimeter
