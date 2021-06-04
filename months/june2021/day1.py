# https://leetcode.com/explore/challenge/card/june-leetcoding-challenge-2021/603/week-1-june-1st-june-7th/3764/
class Solution:
    def area(self,grid,visited,r,c):
        if r<0 or r>=len(grid) or c<0 or c>=len(grid[0]) or grid[r][c]==0 or visited[r][c]:
            return 0
        else:
            visited[r][c]=True
            return 1+self.area(grid,visited,r+1,c)+self.area(grid,visited,r-1,c)+self.area(grid,visited,r,c+1)+self.area(grid,visited,r,c-1)
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        visited=[[False for _ in range(cols)] for _ in range(rows)]
        result=0;
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                result=max(result,self.area(grid,visited,r,c))
        return result