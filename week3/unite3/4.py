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
a.append("cyq")
print(a.all())

a.find(0).data=3
print(a.all())

a.append("sdf")
print(a.all())

a.insert(234324,1)
print(a.all())

a.find(1).data=324
print(a.all())

a.insert(34)
print(a.all())

a.insert("ad",2)
print(a.all())

a.insert(-1)
print(a.all())

a.erase(1)
print(a.all())


            
    