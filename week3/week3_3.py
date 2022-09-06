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
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
    
inp = input("Enter Input : ").split()
S = Stack()

combo = 0

for i in range(len(inp)):
    if S.size() < 2:
        S.push(inp[i])
    else:
        e2 = S.pop()
        e1 = S.pop()
        if e1 == e2 == inp[i]:
            combo = combo + 1
        else:
            S.push(e1)
            S.push(e2)
            S.push(inp[i])
        
print (S.size())

S2 = Stack()

for i in range(S.size()):
    S2.push(S.pop())
    
if S2.isEmpty():
    print("Empty")
else:
    print(''.join(S2.items))
    
if combo > 1:
    print ("Combo :",combo,"! ! !")