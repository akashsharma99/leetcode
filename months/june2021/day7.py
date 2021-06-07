class Solution:
    dp={}
    def minCost(self,cost:List[int],currPos:int)->int:
        if currPos>=len(cost):
            return 0
        if currPos not in self.dp:
            self.dp[currPos]=cost[currPos]+min(self.minCost(cost,currPos+1),self.minCost(cost,currPos+2))
        return self.dp[currPos]
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.dp={}
        return min(self.minCost(cost,0),self.minCost(cost,1))