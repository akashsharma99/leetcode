#https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/
class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        count=0
        i,n=1,len(nums)
        curr=nums[0]
        while i < n:
            if nums[i]>curr:
                count+=n-i
                curr=nums[i]
            i+=1
        return count
        