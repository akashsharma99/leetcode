#https://leetcode.com/problems/longest-consecutive-sequence/
from typing import List
import heapq
class SolutionA:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        ans=1
        seqLen=1
        nums=list(set(nums))
        heapq.heapify(nums)
        #print(nums,seqLen)

        prev=heapq.heappop(nums)
        while(nums):
            #print(nums,seqLen)
            curr = heapq.heappop(nums)
            if curr==prev+1:
                seqLen+=1
                
            else:
                seqLen=1
            ans=max(ans,seqLen)
            prev=curr
        return ans
class SolutionB:
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
if __name__=="__main__":
    nums=[9,1,4,7,3,-1,0,5,8,-1,6]
    obj=SolutionB()
    print(obj.longestConsecutive(nums))
