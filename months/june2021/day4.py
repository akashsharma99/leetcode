# https://leetcode.com/problems/open-the-lock/
from typing import List
from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        lookupEnds=set(deadends)
        queue=deque(["0000","#"])
        depth=0
        while(len(queue)!=0):
            current=queue.popleft()
            if current==target:
                return depth
            if(current!="#"):
                if not (current in lookupEnds):
                    #for positive rotation
                    for pos in range(1,5):
                        queue.append(self.rot(current,1,pos))
                    #for negative rotation
                    for pos in range(1,5):
                        queue.append(self.rot(current,-1,pos))
                    lookupEnds.add(current)
            else:
                if len(queue)!=0:
                    queue.append("#")
                    depth+=1
                else:
                    return -1
        return -1


    # function to rotate the digit for a given position and direction
    def rot(self,n:str,mode:int,pos:int)->str:
        pos-=1
        return(n[:pos] + f"{(int(n[pos])+mode)%10}" + n[pos+1:])
# below is an attempt to solve using dynamic programming but its wrong.
# class Solution:
# 	visited={}
# 	lookupEnds={}
# 	dp={}
# 	def findPath(self,target:str,current:str)->int:
# 		if current in self.lookupEnds or current in self.visited.k:
# 			return -1
# 		if current==target:
# 			return 0
        
# 		self.visited[current]=True
# 		paths=[]
        
# 		if current not in self.dp:
# 			#for positive rotation
# 			for pos in range(1,5):
                
# 				nxt=self.rot(current,1,pos)
# 				path=self.findPath(target,nxt)
# 				if path!=-1:
# 					paths.append(path)
# 			#for negative rotation
# 			for pos in range(1,5):
                
# 				nxt=self.rot(current,-1,pos)
# 				path=self.findPath(target,nxt)
# 				if path!=-1:
# 					paths.append(path)
            
# 			if(len(paths)==0):
# 				self.dp[current]=-1
# 			else:
# 				self.dp[current]=1+min(paths)
        
# 		return self.dp[current]

# 	def openLock(self, deadends: List[str], target: str) -> int:
# 		self.lookupEnds=set(deadends)
# 		res=self.findPath(target,"0000")
# 		print(res,self.dp)
        
# 	# function to rotate the digit for a given position and direction
# 	def rot(self,n:str,mode:int,pos:int)->str:
# 		pos-=1
# 		return(n[:pos]+f"{(int(n[pos])+mode)%10}" + n[pos+1:])
        
#print(toggle("9000",2,1))
if __name__=="__main__":
    deadends=["0201","0101","0102","1212","2002"]
    target = "0202"
    obj=Solution()
    print(obj.openLock(deadends,target))
