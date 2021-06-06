#https://leetcode.com/problems/minimum-space-wasted-from-packaging/
from bisect import bisect_right

class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        modd=1000000007
        for supp in boxes:
            supp.sort()
        packages.sort()
        prefixSum = [0]
        for x in packages:
            prefixSum.append(prefixSum[-1] + x)
        lenPacks,lenBoxes=len(packages),len(boxes)
        possible=False
        minWaste=9999999999
        #while(i<lenBoxes):
        for B in boxes:
            wastage=0
            prevLargest=0
            if packages[-1]<=B[-1]:
                for box in B: 
                    largestFittingPackage = bisect_right(packages, box)
                    wastage+= (largestFittingPackage - prevLargest) * box - (prefixSum[largestFittingPackage] - prefixSum[prevLargest])
                    prevLargest = largestFittingPackage
                minWaste = min(minWaste, wastage)
                possible=True
                
            
        if possible:
            return minWaste%modd
        else:
            return -1