class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        count = 0 
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def bfs(row, col): 
            q = deque([(row, col)])
            grid[row][col] = '0'

            while len(q) != 0:   
                r, c = q.popleft() 
                for d_row, d_col in directions: 
                    n_row, n_col = r + d_row, c + d_col 
                    if 0 <= n_row < rows and 0 <= n_col < cols and grid[n_row][n_col] == '1': 
                        grid[n_row][n_col] = '0'
                        q.append((n_row, n_col))


            
        

        for row in range(rows): 
            for col in range(cols):
                if grid[row][col] == '1': 
                    bfs(row, col)
                    count += 1
                else: 
                    continue 
        return count