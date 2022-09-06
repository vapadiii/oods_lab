# Color Crush 2
class Queue:
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
            
    def enQueue(self, value):
        self.items.append(value)
          
    def deQueue(self):
        return self.items.pop(0)
    
    def size(self):
        return len(self.items)
    
    def isEmpty(self):
        return self.items== []
    
    def peek(self):
        return self.items[0]

class Stack:
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
            
    def push(self, value):
        self.items.append(value)
             
    def pop(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    
    def isEmpty(self):
        return self.items== []


normal,mirror = input("Enter Input (Normal, Mirror) : ").split( )

reMirror = mirror[::-1]
q = Queue()
stack1 = Stack()
stack2 = Stack()
comboMirror = 0
comboNormal = 0
failed = 0

for newMirror in reMirror:
    if stack1.size() < 2:
        stack1.push(newMirror)
    else:
        mirror2 = stack1.pop()
        mirror1 = stack1.pop()
        if newMirror != mirror2 or newMirror != mirror1:
            stack1.push(mirror1)
            stack1.push(mirror2)
            stack1.push(newMirror)
        else:
            q.enQueue(newMirror)
            comboMirror += 1

for newNormal in normal:
    if stack2.size() < 2:
        stack2.push(newNormal)
    else:
        normal2 = stack2.pop()
        normal1 = stack2.pop()
        if newNormal != normal2 or newNormal != normal1:
            stack2.push(normal1)
            stack2.push(normal2)
            stack2.push(newNormal)
        else:
            if q.size() != 0:
                item = q.deQueue()
                if item != normal2 or item != normal1:
                    stack2.push(normal1)
                    stack2.push(normal2)
                    stack2.push(item)
                    stack2.push(newNormal)
                else:
                    stack2.push(newNormal)
                    failed += 1
            else:
                comboNormal += 1
print("NORMAL :")
print(stack2.size())

if stack2.size() == 0:
    print("Empty")
else:
    for out_num in range(stack2.size()):
        print(stack2.pop(),end = '')
    print()
print(comboNormal,"Explosive(s) ! ! ! (NORMAL)")

if failed > 0:
    print("Failed Interrupted",failed,"Bomb(s)")

print("------------MIRROR------------")
print(": RORRIM")
print(stack1.size())

if stack1.size() == 0:
    print("ytpmE")
else:
    for out_num in range(stack1.size()):
        print(stack1.pop(),end = '')
    print()
print("(RORRIM) ! ! ! (s)evisolpxE",comboMirror)