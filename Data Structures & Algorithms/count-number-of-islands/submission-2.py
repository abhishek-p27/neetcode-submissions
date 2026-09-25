class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(row, col): 
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == '0':
                return 

            grid[row][col] = '0'
            dfs(row + 1, col) #down
            dfs(row - 1, col) #up
            dfs(row, col + 1) #right
            dfs(row, col - 1) #left

            
        count = 0 
        rows, cols = len(grid), len(grid[0])

        for row in range(rows): 
            for col in range(cols):
                if grid[row][col] == '1': 
                    dfs(row, col)
                    count += 1
                else: 
                    continue 
        return count
        