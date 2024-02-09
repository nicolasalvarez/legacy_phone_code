print("hello")
import ipdb; ipdb.set_trace()


class Solution:

    def is_it_land(self, grid, y, x):
        if 0 <= x < len(grid[0]) and 0 <= y < len(grid):
            if grid[y][x] == "1":
                grid[y][x] = "0"
                self.is_it_land(grid, y, x + 1)
                self.is_it_land(grid, y, x - 1)
                self.is_it_land(grid, y + 1, x)
                self.is_it_land(grid, y - 1, x)
        

    def numIslands(self, grid: List[List[str]]) -> int:
        no_islands = 0

        for g_y in range(len(grid)):
            for g_x in range(len(grid[0])):
                if grid[g_y][g_x] == "1":
                    no_islands += 1
                    self.is_it_land(grid, g_y, g_x)

        return no_islands







        