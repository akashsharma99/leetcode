# https://leetcode.com/problems/jump-game-vi/
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        dp={}
        n=len(nums)
        maxx={'val':nums[-1],'pos':n-1}
        
        dp[n-1]=nums[-1]
        for i in range(n-2,-1,-1):
            dp[i]=nums[i]+maxx['val']
            
            if maxx['pos']==i+k:
                maxx['pos']=i
                maxx['val']=dp[i]
                for j in range(i+k-1,i,-1):
                    if(dp[j]>=maxx['val']):
                        maxx['pos']=j
                        maxx['val']=dp[j]
                
            else:
                maxx['pos']=i if(dp[i]>=maxx['val']) else maxx['pos']
                maxx['val']=dp[maxx['pos']]
        return dp[0]