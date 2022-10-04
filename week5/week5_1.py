class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class Linkedlist:
    def __init__(self):
        self.head = None
        
    def __str__(self):
        current = self.head
        s = ''
        while(current != None):
            s+=str(current.data)
            current = current.next
        return ' <- '.join(s)
    
    def push_tail(self,new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return 
        current = self.head
        while(current.next):
            current = current.next
        current.next = new_node
        new_node.next = None

l1 = Linkedlist()
l2 = Linkedlist()

print(' *** Locomotive ***')
inp = [int(e) for e in input('Enter Input : ').split()]

for i in inp:
    l1.push_tail(i)
j = 0
for i in inp:
    if i == 0:
        j = 1
    if j == 1:
        l2.push_tail(i)
for i in inp:
    if i == 0:
        break
    l2.push_tail(i)
    
print('Before :',l1)
print('After :',l2)