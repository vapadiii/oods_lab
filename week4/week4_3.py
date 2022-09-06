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
    
    def front(self):
        return self.items[0] if self.size()>0 else -1
    
queue = Queue()
a,b = input("Enter code,hint : ").split(",")
s=ord(b)-ord(a[0])
for i in a:
    queue.enQueue(chr(ord(i)+s))
    print(queue.items)