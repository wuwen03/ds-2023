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
    
a=List()
a.insert("cyq",a.size())
print(a.find(0))
a.find(0).data=3
a.insert("sdf",a.size())
a.insert(234324,1)
a.find(1).data=324
a.insert(34)
a.insert(-1)
a.erase(1)
arr=[]
for i in range(0,a.size()):
    arr.append(a.find(i).data)
print(arr)

            
    