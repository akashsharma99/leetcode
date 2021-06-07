#https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        setOfReachableNodes=set([edge[1] for edge in edges])
        sol=[node for node in range(n) if node not in setOfReachableNodes]
        return sol