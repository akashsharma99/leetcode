# https://leetcode.com/problems/jump-game-ii/
class SolutionA:
    def jump(self, nums: List[int]) -> int:
        dp=[9999999 for _ in range(len(nums))]
        lastIndex=len(nums)-1
        dp[lastIndex]=0
        i=lastIndex-1
        while(i>=0):
            j=i+1
            while(j<=i+nums[i] and j<=lastIndex):
                dp[i]=min(dp[i],1+dp[j])
                j+=1
            i-=1
        
        return dp[0]
        
class SolutionB:
    def jumps(self,nums:List[int],curr:int,dp)->int:
        if curr==len(nums)-1:
            return 0
        if(dp[curr]!=9999999):
            return dp[curr]
        i=curr+1
        while(i<len(nums) and i<=curr+nums[curr]):
            dp[curr]=min(dp[curr],1+self.jumps(nums,i,dp))
            i+=1
        
        return dp[curr]
    def jump(self, nums: List[int]) -> int:
        dp=[9999999 for _ in range(len(nums))]
        res=self.jumps(nums,0,dp)
        return res
        