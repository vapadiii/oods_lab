class Queue:
    def __init__(self):
        self.items = []
        
    def enQueue(self,i):
        self.items.append(i)
        
    def deQueue(self):
        return self.items.pop(0)
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
    
en = Queue()
es = Queue()
inp = input("Enter Input : ").split(',')

for i in inp:
    temp = i.split()
    if temp[0] == "EN":
        en.enQueue(temp[1])
    elif temp[0] == "ES":
        es.enQueue(temp[1])
    elif temp[0] == "D":
        if en.size() == 0 and es.size() == 0:
            print("Empty")
        elif es.size() != 0:
            temp = es.deQueue()
            print(str(temp))
        else:
            temp = en.deQueue()
            print(str(temp))