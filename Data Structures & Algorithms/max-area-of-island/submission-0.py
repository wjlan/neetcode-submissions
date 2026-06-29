import collections
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        max_area = 0
        visited = set() 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in visited:
                    area = self.bfs(grid, i, j, visited)
                    max_area = max(max_area, area)

        return max_area

    
    def bfs(self, grid, x, y, visited):
        queue = collections.deque([(x, y)])
        visited.add((x, y))
        area = 1
        DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while queue:
            x, y = queue.popleft()
            for dx, dy in DIRECTIONS:
                curr_x = x + dx
                curr_y = y + dy
                if self.is_valid(grid, curr_x, curr_y, visited):
                    queue.append((curr_x, curr_y))
                    visited.add((curr_x, curr_y))
                    area += 1  
        return area
    

    def is_valid(self, grid, x, y, visited):
        n, m = len(grid), len(grid[0])
        if not (0 <= x < n and 0 <= y < m):
            return False
        if (x, y) in visited:
            return False
        return grid[x][y] == 1

    
        

            

        
        


        
        