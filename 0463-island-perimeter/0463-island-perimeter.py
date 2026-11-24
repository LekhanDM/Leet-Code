class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            rows = len(grid)
            cols = len(grid[0])

            perimeter = 0

            for i in range(rows):
                for j in range(cols):

                    if grid[i][j] == 1:

                        for dx, dy in directions:
                            x = i + dx
                            y = j + dy

                            if x < 0 or x >= rows or y < 0 or y >= cols:
                                perimeter += 1

                            elif grid[x][y] == 0:
                                perimeter += 1

            return perimeter