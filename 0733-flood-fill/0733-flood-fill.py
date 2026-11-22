class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        old_color = image[sr][sc]

        if old_color == color:

            return image

        rows = len(image)

        cols = len(image[0])

        stack = [(sr, sc)]

        image[sr][sc] = color

        while stack:

            r, c = stack.pop()

            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            for dr, dc in directions:

                nr = r + dr

                nc = c + dc


                if 0 <= nr < rows and 0 <= nc < cols:

                    if image[nr][nc] == old_color:

                        image[nr][nc] = color

                        stack.append((nr, nc))

        return image