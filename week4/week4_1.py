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
    
    
inp = input("Enter Input : ").split(",")
queue = Queue()
dequeue = Queue()

for i in inp:
    word = i.split(" ")
    
    # E
    if word[0] == "E":
        queue.enQueue(int(word[1]))
        print(", " .join(map(str,queue.items)))
    # D
    elif word[0] == "D":
        if queue.size() > 1:
            dequeue.enQueue(queue.deQueue())
            print(str(dequeue.items[-1]) + " <- " + str(", " .join(map(str,queue.items))) )
        elif queue.size() ==1:
            dequeue.enQueue(queue.deQueue())
            print(str(dequeue.items[-1]) + " <- Empty")
        elif queue.size()==0:
            print("Empty")

        
if queue.size() == 0:
    queue.enQueue("Empty")
if dequeue.size() == 0:
    dequeue.enQueue("Empty")
print(str(", " .join(map(str,dequeue.items))) + " : "+str(", " .join(map(str,queue.items))))