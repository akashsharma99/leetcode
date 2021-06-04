# https://leetcode.com/explore/challenge/card/june-leetcoding-challenge-2021/603/week-1-june-1st-june-7th/3765/
class Solution:
    def isInterleave2(self,s1: str, s2: str, s3: str,dp) -> bool:
        if not s1 and not s2 and not s3:
            return True
        if not s3:
            return False
        key=(s1,s2,s3)
        if key not in dp:
            x = (len(s1) and s3[0] == s1[0]) and self.isInterleave2(s1[1:], s2, s3[1:],dp)
            y = (len(s2) and s3[0] == s2[0]) and self.isInterleave2(s1, s2[1:], s3[1:],dp)
            dp[key]=x or y
        return dp[key]
    
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp={}
        return self.isInterleave2(s1,s2,s3,dp)
    