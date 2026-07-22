class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlylinkedlist:
    def __init__(self):
        self.head=None
    def insertbegin(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
        else:
            newNode.next=self.head
            self.head=newNode
    def insertEnd(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=newNode
    def search(self,target):
        if self.head is None:
            print("SLL is empty")
        else:
            temp=self.head
            while temp:
                if temp.data==target:
                    print("found")
                    break
                else:
                    temp=temp.next
            else:
                print("not found")
    def delbegin(self):
        if self.head is None:
            print("SLL is empty")
        else:
            temp=self.head
            self.head=self.head.next
            temp.next=None
            del temp
    def delEnd(self):
        if self.head is None:
            print("SLL is empty")
        else:
            temp=self.head
            while temp.next.next:
                temp=temp.next
            delNode=temp.next
            temp.next=None
            del delNode
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end=' ')
            temp=temp.next
            
SLL=singlylinkedlist()
SLL.insertbegin(10)
SLL.insertbegin(11)
SLL.insertbegin(12)
SLL.insertbegin(6)
SLL.insertbegin(2)
SLL.display()
print()
SLL.insertEnd(15)
SLL.insertEnd(25)
SLL.insertbegin(200)
print()
SLL.search(12)
SLL.search(2000)
SLL.display()
print()
SLL.delbegin()
SLL.display()
print()
SLL.delEnd()
SLL.display()














