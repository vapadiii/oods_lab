#Into the wood
class Stack():
    
    def __init__(self, l = None):
        if l == None:
            self.items = []
        else :
            self.items = l
            
    def add(self, i):
        self.items.append(i)
        
    def pop(self):
        return self.items.pop()
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return str(len(self.items))
    
    def returnList(self):
        return self.items
    
def check(ch):
    S = Stack()
    if len(ch) == 0:
        return "0"
    else:
        test = int(ch[len(ch)-1])
        S.add(test)
        for i in range(len(ch) -2, -1, -1):
            if int(ch[i]) > test:
                test = int(ch[i])
                S.add(test)
        return S.size()
    
S = Stack()
inp = input("Enter Input : ").split(",")
for i in inp:
    l = i.split()
    if l[0] == "A":
        S.add(l[1])
    elif l[0] == "B":
        print(check(S.returnList()))