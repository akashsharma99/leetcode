#https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/
class Solution:
    def rotate(self, matrix)->List[List[int]]:
        matrix[:] = map(list, zip(*matrix[::-1]))
        return matrix
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if mat==target:
            return True
        for i in range(3):
            mat=self.rotate(mat)
            if mat==target:
                return True
        return False