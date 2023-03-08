'''class'''
'''class happy:
    a=100
    def method(self):
        b=12
        print(self.a)
        print(b)
obj=happy()
print(obj.a)
obj.method()'''

#-------------------------------------
'''protecred encapsulation'''
'''class encap:
    _a=10
    c=20
    def encapfunction(self):
        _b=200
        print("Encap function-accessing protected")
        print(self._a+10)
obj=encap()
print(obj._a)
obj.encapfunction()
print(obj.c)'''

#---------------------------------------
'''private encapsulation'''
'''class encap:
     __a=10
     print(__a)
     def encapfunction(self):
         print("Encap function")
         print(self.__a)
obj=encap()

obj.encapfunction()
print(obj.__a)'''

#---------------------------------------

'''class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class SLL:
    def __init__(self):
        self.head=None
    def display(self):
            if self.head is None:
                print("LL is empty")
            else:
                temp=self.head
                while(temp):
                    print(temp.data,"==>",end="  ")
                    temp=temp.next
                                
obj=SLL()
n1=Node(100)
obj.head=n1
n2=Node(200)
obj.head.next=n2
n3=Node(300)
n2.next=n3
obj.display()'''
#------------------------------------------
"inserting a node at the beginning of SLL"

'''class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class singlelinkedlist:
    def __init__(self):
        self.head=None
    def insert_beginning(self,data):
        nb=Node(data)
        nb.next=self.head
        self.head=nb
    def display(self):    
            if self.head is None:
                print("LL is empty")
            else:
                temp=self.head
                while(temp):
                    print(temp.data,"==>",end="  ")
                    temp=temp.next
                                
obj=singlelinkedlist()
n=Node(10)
obj.head=n
n1=Node(20)
n.next=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4
print("before inserting 100")
obj.display()
print(" ")
print("After inserting 100")
obj.insert_beginning(100)
obj.display()'''


#----------------------------------------------------------------------
#SINGLE LINKED LIST - INSERTING AT END
'''class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class singlelinkedlist:
    def __init__(self):
        self.head = None

    def insert_end(self,data):
        ne = Node(data)
        temp=self.head
        while temp.next:
            temp = temp.next
        temp.next = ne


    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, "->", end=" ")
                temp = temp.next
obj = singlelinkedlist()
n = Node(10)
obj.head = n
n1 = Node(20)
n.next = n1
n2 = Node(30)
n1.next = n2
print("Before inserting 100")
obj.display()
print("")
print("After inserting 100")
obj.insert_end(100)
obj.display()
print("")   '''









