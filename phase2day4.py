#TAKING MULTIPLE INPUTS USING MAP
'''
a=list(map(int,input().split(',')))

for i in a:
    print(i,end=' ')
           
                      '''

'-------------------------------------------------------------------------------------------------------------'
'''
n=int(input('enter size'))
a=list(map(int,input().split(' ')))[ :n]
total=0
for i in a:
    total=total+i
print(total)
                      '''
'--------------------------------------------------------------------------------------------------------------'
 #circular queue
'''
class CircularQueue():
    def __init__(self,size):
        self.size=size
        self.queue=[None for i in range(size)]
        self.front=self.rear=-1

    def enqueue(self,data):
        if ((self.rear+1)%self.size==self.front):
            print('Queue is Full\n')
        elif (self.front==-1):
            self.front=0
            self.rear=0
            self.queue(self.rear)=data
        else:
            self.rear=(self.rear+1)%self.size
            self.queue(self.rare)=data

    def dequeue(self):
        if(self.front==-1):
            for empty queue:
                print("Queuue is empty\n")
        elif (self.front==self.rear):
            temp=self.queue[self.front]
            self.front=-1
            self.rear=-1
            return temp
        else:
            temp = self.queue(self.front)
            self.front=(self.front+1)% self.size
            return temp
    def display(self):
        if(self.front==-1):
            print("Queue is empty")

        elif (self.rear >=self.front):
            print("Elements in the circular queue",end=" ")

            for i in range(self.front,self.rear +  ):
                print(self.queue[i],end =" ")
            print()

        else:
            print("Elements in circular queue are : ",end=' ')

            for i in range(self.front,self.size):
                print(self.queue[i],end=" ")
            for i in range(0,self.rear+1):
                print(self.queue[i],end=" ")
            print()

        if((self.rear +1)%self.size=self.front):
                                                  '''
                
#-----------------------------------------------------------------------------------------------
#inorder traversal of a binary tree
'''#print Preorder,Inorder,Postorder
class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key
def printInorder(root):
    if root:
        #First recur on left child
        printInorder(root.left)
        #then print the data of node
        print(root.val,end = " ")
        #now recur on right child
        printInorder(root.right)
#FUNCTION-POSTORDER
def printPostorder(root):
    if root:
        # First recur on left child
        printPostorder(root.left)
        # now recur on right child
        printPostorder(root.right)
        # now print the data of node
        print(root.val, end=" ")
def printPreorder(root):
    if root:
        # First print the data of node
        print(root.val, end=" ")
        # Then recur on left child
        printPreorder(root.left)
        # now recur on right child
        printPreorder(root.right)
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("PREORDER:")
printPreorder(root)
print()
print("INORDER:")
printInorder(root)
print()
print("POSTORDER:")
printPostorder(root)'''
#####################################################################################
#BST-INSERT
'''
class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key
#a new node with the given key
def insert(root,key):
    if root is None:
        return  Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right,key)
        else:
            root.left = insert(root.left,key)
    return root
#Inorder traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)
#                 (1)
#                 / \ 
#                /   \ 
#               /     \ 
#              (2)    (3)
#              / \     /\ 
#             /   \   /  \ 
#           (4)  (5) (6)  (7)
r = Node(50)
r = insert(r,30)
r = insert(r,20)
r = insert(r,40)
r = insert(r,70)
r = insert(r,60)
r = insert(r,80)
inorder(r)
                               '''

#-------------------------------------------------------------------
 #BINARY TREE
'''  

class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
node1 = BinaryTreeNode(50)
node2 = BinaryTreeNode(20)
node3 = BinaryTreeNode(45)
node4 = BinaryTreeNode(11)
node5 = BinaryTreeNode(15)
node6 = BinaryTreeNode(30)
node7 = BinaryTreeNode(78)
node1.leftChild = node2
node1.rightChild = node3
node2.leftChild = node4
node2.rightChild = node5
node3.leftChild = node6
node3.rightChild = node7

#                                                       50
#                                                     /     \
#                                                20             45 
#                                             /       \      /      \ 
#                                          11        15    30        78  


print("Root node is",node1.data)
print("Left child of root node is",node1.leftChild.data)
print("Right child of root node is",node1.rightChild.data)
print("Node is",node2.data)
print(node1.rightChild.leftChild.data)                 
                                          '''
    
#-------------------------------------------------------------
#print Preorder,Inorder,Postorder
'''
class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key
def printInorder(root):
    if root:
        #First recur on left child
        printInorder(root.left)
        #then print the data of node
        print(root.val,end = " ")
        #now recur on right child
        printInorder(root.right)
#FUNCTION-POSTORDER
def printPostorder(root):
    if root:
        # First recur on left child
        printPostorder(root.left)
        # now recur on right child
        printPostorder(root.right)
        # now print the data of node
        print(root.val, end=" ")
def printPreorder(root):
    if root:
        # First print the data of node
        print(root.val, end=" ")
        # Then recur on left child
        printPreorder(root.left)
        # now recur on right child
        printPreorder(root.right)
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("PREORDER:")
printPreorder(root)
print()
print("INORDER:")
printInorder(root)
print()
print("POSTORDER:")
printPostorder(root)
                               

                                  '''
