class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class Doublylinkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
    def insertbegin(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
            self.tail=newNode
        else:
            newNode.next=self.head
            self.head.prev=newNode
            self.head=newNode
    def insertEnd(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
            self.tail=newNode
        else:
            newNode.prev=self.tail
            self.tail.next=newNode
            self.tail=newNode     
    def delbegin(self):
        if self.head is None:
            print("dll is empty")
        else:
            temp=self.head
            self.head=self.head.next
            temp.next=None
            self.head.prev=None
            del temp
    def delEnd(self):
        if self.head is None:
            print("dll is empty")
        else:
            temp=self.tail
            self.tail=self.tail.prev
            temp.prev=None
            self.tail.next=None
            del temp
    def search(self):
        if self.head is None:
            print("dll is empty")
        else:
            temp=self.tail
            self.tail=self.tail.prev
            temp.prev=None
            self.tail.next=None
            del temp
         
             
    def display(self):
        if self.head is None:
            print("dll is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,end=' ')
                temp=temp.next
            
dll=Doublylinkedlist()
dll.display()
dll.insertbegin(10) 
dll.insertbegin(20)
dll.insertbegin(30)
dll.insertbegin(40)
print()
dll.display()
dll.insertEnd(200)
print()
dll.display()
print()
dll.delbegin()
dll.display()
print()
dll.search()
dll.display()
print()
dll.delEnd()
dll.display()














