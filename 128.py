#https://leetcode.com/problems/longest-consecutive-sequence/
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        ans=1
        seqLen=1
        nums=sorted(list(set(nums)))
        prev=nums[0]
        for curr in nums[1:]:
            if curr==prev+1:
                seqLen+=1    
            else:
                seqLen=1
            ans=max(ans,seqLen)
            prev=curr
        return ans