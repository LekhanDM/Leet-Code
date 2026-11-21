class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)

        cols = len(grid[0])

        islands = 0

        for i in range(rows):

            for j in range(cols):

                if grid[i][j] == "1":

                    islands += 1

                    stack = [(i, j)]

                    grid[i][j] = "0"

                    while stack:

                        r, c = stack.pop()

                        directions = [(0, 1), (0, -1),

                                      (1, 0), (-1, 0)]

                        for dr, dc in directions:

                            nr = r + dr

                            nc = c + dc
                            if (0 <= nr < rows and

                                0 <= nc < cols and

                                grid[nr][nc] == "1"):

                                grid[nr][nc] = "0"

                                stack.append((nr, nc))

        return islands