class Node:
    def __init__(self,data,next=None) -> None:
        self.data=data
        self.next:Node=next
    
class List:
    def __init__(self) -> None:
        self.head=Node(0) #头结点记录链表的大小

    def insert(self,data,position:int=0)->None:
        if position > self.head.data:
            return
        node=Node(data)
        now=self.head.next
        pre=self.head
        for i in range(0,position):
            pre=now
            now=now.next
        self.head.data+=1
        pre.next=node
        node.next=now
        return
    
    def append(self,data)->None:
        self.insert(data,self.size())
    
    def erase(self,position:int=0)->None:
        if position >= self.head.data:
            return
        now=self.head.next
        pre=self.head
        for i in range(0,position):
            pre=now
            now=now.next
        self.head.data-=1
        pre.next=now.next
        return
    
    def find(self,position:int=0):
        if position>=self.head.data:
            pass
            # return Node().data
        now=self.head.next
        for i in range(0,position):
            now=now.next
        return now
    
    def size(self):
        return self.head.data
    
    def all(self):
        arr=[self.find(i).data for i in range(self.size())]
        return arr
    
a=List()
b=List()
a.append(1)
a.append(3)
a.append(6)
a.append(10)
b.append(1)
b.append(4)
b.append(5)
b.append(19)

ita=a.head.next
itb=b.head.next
ans=List()
while ita or itb:
    if ita.data and itb.data:
        if ita.data>itb.data:
            ans.append(itb.data)
            ans.append(ita.data)
        else:
            ans.append(ita.data)
            ans.append(itb.data)
        ita=ita.next
        itb=itb.next
    elif ita:
        ans.append(ita.data)
        ita=ita.next
    elif itb:
        ans.append(itb.data)
        itb=itb.next
print("a:",a.all())
print("b:",b.all())
print("ans",ans.all())

