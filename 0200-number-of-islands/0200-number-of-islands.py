class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0

        def dfs(i,j):
            if(i<0 or j<0 or i>=m or j>=n or grid[i][j] == '0'):
                return
            grid[i][j] = '0'

            dfs(i-1, j) #up
            dfs(i+1, j) #down
            dfs(i, j-1) #left
            dfs(i, j+1) #right
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count+=1
                    dfs(i,j)
        return count

