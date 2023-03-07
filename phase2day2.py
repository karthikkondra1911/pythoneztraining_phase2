#linked list insertion at the end
'''
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class singlelinkedlist:
    def __init__(self):
        self.head = None

    def insert_position(self,pos,data):
        np = Node(data)
        temp=self.head
        for i in range(pos-1):
            temp = temp.next
        np.next = temp.next
        temp.next = np

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
n3 = Node(40)
n2.next=n3
n4 = Node(50)
n3.next=n4
print("Before inserting 1000")
obj.display()
print("")
print("After inserting 1000")
obj.insert_position(2,1000)
obj.display()
print("") '''

#------------------------------------------------------------------------------------
#Deletion at the position of the linked list
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class single_linkedlist:
    def __init__(self):
        self.head=None

    def delete_position(self,pos):
        temp=self.head.next
        prev=self.head
        for i in range(1,pos-1):
                temp=temp.next
        prev=prev.next
        prev.next=temp.next
        temp.next=None

    def display(self):
         
         
        if self.head is None:
            
            print("Linked list is empty")
        else:
             temp = self.head
             while temp:
                 print(temp.data, "->", end=" ")
                 temp = temp.next    
        
obj = single_linkedlist()
n=Node(10)
obj.head=n
n1 = Node(20)
n.next = n1
n2 = Node(30)
n1.next = n2
n3 = Node(40)
n2.next=n3
n4 = Node(50)
n3.next=n4

print("")

obj.display()
print("")
obj.delete_position(3)
obj.display()
print("")'''


#--------------------------------------------------------------------------
#Double linked list

"""
class Node:
    def __init__(self,data):
        self.data=data
        self.previous = None
        self.next = None

class dll:
    def __init__(self):
        self.head = None
    def display(self):
        if self.head == None:
            print("empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"<-->",end = "  ")
                temp=temp.next

l=dll()
n1=Node(100)
l.head=n1
n2=Node(200)
n2.prev=n1
n1.next=n2
l.display()"""

#-------------------------------------------------------------------------------------------------

#guesssing the number
'''
import random
i=random.randrange(1,100)
n=int(input("Enter any number: "))
while i!=n:
    if n<i:
        print("too low")
    elif n>i:
        print("too high")
        n=int(input("Enter any number: "))
    else:
        break
print("You guessed it right") '''   


#--------------------------------------------------------------------------------------------------    
    #DELETION OF NODE OF SINGLE LINKED LIST AT THE BEGINNING
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class single_linkedlist:
    def __init__(self):
        self.head=None

    def delete_begin(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
       

    def display(self):
         
         
        if self.head is None:
            
            print("Linked list is empty")
        else:
             temp = self.head
             while temp:
                 print(temp.data, "->", end=" ")
                 temp = temp.next    
        
obj = single_linkedlist()
n=Node(10)
obj.head=n
n1 = Node(20)
n.next = n1
n2 = Node(30)
n1.next = n2
n3 = Node(40)
n2.next=n3
n4 = Node(50)
n3.next=n4
obj.display()
print("")    
obj.delete_begin()
obj.display()
print("")   '''

        
#------------------------------------------------------------------------------
#INSERTION  OF NODE OF DOUBLE LINKED LIST AT THE end
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.previous = None
        self.next = None

class dll:
    def __init__(self):
        self.head = None
    def insert_end(self):
        n=Node(300)
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=n
        n.prev=temp    
        
    def display(self):
        if self.head == None:
            print("empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"<-->",end = "  ")
                temp=temp.next

l=dll()
n1=Node(100)
l.head=n1
n2=Node(200)
n2.prev=n1
n1.next=n2

l.insert_end()
l.display()
            '''
#--------------------------------------------------------------------
#INSERTION  OF NODE OF DOUBLE LINKED LIST AT THE BEGIN
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.previous = None
        self.next = None

class dll:
    def __init__(self):
        self.head = None
    def insert_begin(self):
        n=Node(300)
        temp=self.head
        temp.prev=n
        n.next=temp
        self.head=n
      
        
    def display(self):
        if self.head == None:
            print("empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"<-->",end = "  ")
                temp=temp.next

l=dll()
n1=Node(100)
l.head=n1
n2=Node(200)
n2.prev=n1
n1.next=n2

l.insert_begin()
l.display()
    '''
#----------------------------------------------------------------------
#INSERTION AT THE POSITION OF DOUBLE LINKED LIST
'''

class Node:
    def __init__(self,data):
        self.data=data
        self.previous = None
        self.next = None

class dll:
    def __init__(self):
        self.head = None
    def insert_pos(self,pos):
        n=Node(300)
        temp=self.head
        for  i in range (1,pos-1):
            temp=temp.next
        n.prev=temp
        n.next=temp.next
        temp.next.prev=n
        temp.next=n
      
        
    def display(self):
        if self.head == None:
            print("empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"<-->",end = "  ")
                temp=temp.next

l=dll()
n1=Node(100)
l.head=n1
n2=Node(200)
n2.prev=n1
n1.next=n2
n3=Node(300)
n3.prev=n2
n2.prev=n1
l.insert_pos(2)
l.display()
              '''
#-------------------------------------------------------------------------

