# https://leetcode.com/explore/challenge/card/june-leetcoding-challenge-2021/603/week-1-june-1st-june-7th/3766/
class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        maxHorizontal=1
        hstart=0
        hend=0
        prev=0
        for hd in horizontalCuts:
            if(hd-prev >= maxHorizontal):
                hstart=prev
                hend=hd
                maxHorizontal=hend-hstart
                #print(hstart,hend,maxHorizontal)
            prev=hd
        if(h-prev >= maxHorizontal):
            hstart=prev
            hend=h
            maxHorizontal=hend-hstart
            #print(hstart,hend,maxHorizontal)
        maxVertical=1
        vstart=0
        vend=0
        prev=0
        for vd in verticalCuts:
            if(vd-prev > maxVertical):
                vstart=prev
                vend=vd
                maxVertical=vend-vstart
                #print(vstart,vend,maxVertical)
            prev=vd
        if(w-prev > maxVertical):
            vstart=prev
            vend=w
            maxVertical=vend-vstart
            #print(vstart,vend,maxVertical)
        return (maxVertical*maxHorizontal)%1000000007