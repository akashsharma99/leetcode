#https://leetcode.com/problems/keys-and-rooms/
from typing import List
from collections import deque
class Solution1:#using depth first search
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        stack=[]
        visited=set([0])
        for i in rooms[0]:
            if(i not in visited):
                visited.add(i)
                stack.append(i)
        while(stack):
            top=stack.pop()
            for i in rooms[top]:
                if(i not in visited):
                    visited.add(i)
                    stack.append(i)
        return len(visited)==len(rooms)

class Solution2:#using breadth first search
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        dq=deque()
        visited=set([0])
        for i in rooms[0]:
            if(i not in visited):
                visited.add(i)
                dq.append(i)
        while(dq):
            front=dq.popleft()
            for i in rooms[front]:
                if(i not in visited):
                    visited.add(i)
                    dq.append(i)
        return len(visited)==len(rooms)

if __name__=="__main__":
    rooms=[[1,3],[3,0,1],[2],[0]]
    obj=Solution2()

    print(obj.canVisitAllRooms(rooms))