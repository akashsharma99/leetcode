class MyCalendar:
    def __init__(self):
        self.bookings=[]

    def book(self, start: int, end: int) -> bool:
        print(self.bookings)
        if not self.bookings:
            self.bookings.append((start,end))
            return True
        for booking in self.bookings:
            if (start>=booking[0] and end<=booking[1]) or (start<=booking[0] and end>booking[0]) or (start<=booking[0] and end>=booking[1]) or (start<booking[1] and end>=booking[1]):
                return False
            
        self.bookings.append((start,end))
        return True

obj=MyCalendar()

#inp=[[47,50],[33,41],[39,45],[33,42],[25,32],[26,35],[19,25],[3,8],[8,13],[18,27]]
inp=[[23,32],[42,50],[6,14],[0,7],[21,30],[26,31],[46,50],[28,36],[0,6],[27,36],[6,11],[20,25],[32,37],[14,20],[7,16],[13,22],[39,47],[37,46],[42,50],[9,17],[49,50],[31,37],[43,49],[2,10],[3,12],[8,14],[14,21],[42,47],[43,49],[36,43]]
exp_output=[True,True,True,False,False,False,False,False,True,False,False,False,True,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
#inp=[[10,20],[15,25],[20,30]]
res=[]
for node,exp in zip(inp,exp_output):
    out=obj.book(node[0],node[1])
    res.append(out)
    if exp!=out:
        print('failed: ',node,out,exp)
print(obj.bookings)
print(res)
