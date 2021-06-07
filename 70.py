class Solution:
    
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        if n==2:
            return 2
        
        ways=[0 for _ in range(n)]
        ways[-1],ways[-2],ways[-3]=0,1,2
        
        for i in range(n-4,-1,-1):
            ways[i]=ways[i+1]+ways[i+2]
        return ways[0]+ways[1]