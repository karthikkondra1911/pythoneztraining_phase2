#STACK IMPLEMENTATION USING LIST-----------------------
'''
stack=[]
def push():
    element=int(input("Enter the element"))
    stack.append(element)
    print(stack)

def pop_element():
    if not stack:
        print("Stack is empty")
    else:
        e=stack.pop()
        print("Remove elemnet: ",e)
        print(stack)
        
while True:
    print("Select operation 1.push 2.pop 3.quit")
    choice=int(input())
    if choice==1:
        push()
    elif choice==2:
        pop_element()
    elif choice==3:
        break
    else:
        print("Enter the correct operation")    
                                                '''
'------------------------------------------------------------------'
#STACK IMPLEMENTATION USING LINKED LIST

'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Stack:
    def __init__(self):
        self.head=None
    def isempty(self):
        if self.head==None:
            return True
        else:
            return False
    def push(self,data):
        if self.head==None:
            self.head=Node(data)
        else:
            newnode=Node(data)
            newnode.next=self.head
            self.head=newnode
    def pop(self):
        if self.isempty():
            return None
        else:
            poppednode=self.head
            self.head=self.head.next
            poppednode.next=None
            return poppednode.data
    def peek(self):
        if self.isempty():
            return None
        else:
            return self.head.data
    def display(self):
        t=self.head
        if self.isempty():
            print("Stack underflow")
        else:
            while(t!=None):
                print(t.data,end=" ")
                t=t.next
                if(t!=None):
                    print("->",end=" ")
            return

if __name__=="__main__":
    s=Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.display()
    print(" ")
    print(s.peek())
    s.pop()
    s.pop()
    print(" ")
    s.display()
    print("peek",s.peek())

                                   '''
'------------------------------------------------------------------------------'
#IMPLEMENTATION OF STACK BY QUEUE
'''
from queue import LifoQueue

s=LifoQueue(maxsize=3)

print(s.qsize())

s.put('a')
s.put('b')
s.put('c')

print(s.full())
print(s.qsize())
print(s.get())
print(s.get())
print(s.get())
print(s.empty())
                '''

'---------------------------------------------------------------------------------'
#QUEUE IMPLEMENTATION USING LIST
'''
queue=[]
def enqueue():
    element=input("enter element: ")
    queue.append(element)
    print(element," is added in the queue")

def dequeue():
    if not queue:
        print("Q is empty")
    else:
        e=queue.pop(0)
        print("removed element",e)
def display():
    print(queue)
while True:
    print("Select operation 1.enque 2.deque 3.show 4.quit")
    choice=int(input())
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        display()
    else:
        break
    '''
        
'-----------------------------------------------------------------------------------'
#QUEUE MODULE
'''    
import queue
L=queue.Queue(maxsize=5)
L.put(10)
L.put(20)
print(type(L))
print(L.get())
print(L.get())
                '''
      
'----------------------------------------------------------------------------------'
#prog:
#define size of both stacks as 5
#if your input is even it nhas to be pushed
#in stack 1 and other inpts it has to be pushed in stack2
#options :push/ pop/ display_stack
'''
stack1=[]
stack2=[]
i=0

def push():
    for i in range(5):
        element=int(input("Enter the element"))
        if element%2==0:
            
            stack1.append(element)
        else:
            stack2.append(element)
        
    
        

def pop_element():
    a=int(input("Remove from stack1/2?"))
    if a==1:
        stack1.pop()
    elif a==2:
        stack2.pop()
def display():
    b=int(input("show stack 1/2 "))
    if b==1:
        print(stack1)
    elif b==2:
        print(stack2)
        
    
    
        
while True:
    print("Select operation 1.push 2.pop 3.show 4.quit")
    choice=int(input())
    if choice==1:
        push()
    elif choice==2:
        pop_element()
    elif choice==3:
        display()
    elif choice==4:
        break
    
    else:
        print("Enter the correct operation")

                                            '''

'----------------------------------------------------------------------------------'

#IMPLEMENTATION OF QUEUE USING LINKED LIST
'''
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head=None
        self.last = None
        
    def enqueue(self,data):
        if self.last is None:
            self.head=Node(data)
            self.last = self.head

        else:
            self.last.next = Node(data)
            self.last = self.last.next

    def dequeue(self):
        if self.head is None:
            return None
        else:
            to_return = self.head.data
            self.head=self.head.next
            return to_return
a_queue = Queue()
while True:
    print('enqueue ')
    print('dequeue ')
    print('quit ')
    do= input('what would you like to do? ').split()
    operation = do[0].strip().lower()

    if operation=='enqueue':
        a_queue.enqueue(int(do[1]))
    elif operation =='dequeue':
        dequeued =a_queue.dequeue()
        if dequeued is None:
            print('Queue is empty')
        else:
            print('Dequeued element: ',int(dequeued))
    elif operation == 'quit':
        break
                                          '''

'-------------------------------------------------------------------------------'
