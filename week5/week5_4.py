class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.tail, str(self.tail.value) + " "
        while cur.previous != None:
            s += str(cur.previous.value) + " "
            cur = cur.previous
        return s

    def isEmpty(self):
        return self.head == None
    
    def append(self, item):
        n = Node(item)
        if self.isEmpty():
            self.head = n
            self.tail = n
        else:
            n.previous = self.tail
            self.tail.next = n
            self.tail = n
            
    def addHead(self, item):
        n = Node(item)
        if self.isEmpty():
            self.head = n
            self.tail = n
        else:
            n.next = self.head
            self.head.previous = n
            self.head = n

    def insert(self, pos, item):
        n = Node(item)
        x = self.size()
        if self.isEmpty():
            self.head = n
            self.tail = n
        elif pos == 0 or -1*pos > x:
            self.head.previous = n
            n.next = self.head
            self.head = n
        elif pos > x-1:
            self.tail.next = n
            n.previous = self.tail
            self.tail = n
        elif pos > 0:
            t = self.head
            i = 0
            while i < pos-1:
                i += 1
                t = t.next
            n.next = t.next
            t.next.previous = n
            t.next = n
            n.previous = t
        else:
            t = self.tail
            i = 1
            while i < -1*pos:
                i += 1
                t = t.previous
            n.previous = t.previous
            t.previous.next = n
            t.previous = n
            n.next = t

    def search(self, item):
        t = self.head
        while t != None:
            if t.value == item:
                return "Found"
            t = t.next
        return "Not Found"
            
    def index(self, item):
        t = self.head
        count = 0
        while t != None:
            if t.value == item:
                return count
            t = t.next
            count += 1
        return -1

    def size(self):
        s = 0
        t = self.head
        while t != None:
            s += 1
            t = t.next
        return s

    def pop(self, pos):
        s = self.size()
        i = 0
        t = self.head
        while i<pos and pos < s:
            t = t.next
            i += 1
        if s == 1:
            self.head=None
            self.previous=None
        elif i == 0:
            self.head = t.next
            self.head.previous = None
        elif i == s-1:
            self.tail = t.previous
            self.tail.next = None
        else:
            t.next.previous = t.previous
            t.previous.next = t.next
            

ll = LinkedList()

ll.append('|')
id = 0
inp = input('Enter Input : ')

for i in inp.split(','):
    if i[0] == 'I':
        ll.insert(id,i[2:])
        id += 1
    elif i[0] == 'L':
        if id != 0:
            ll.pop(id)
            id -= 1
            ll.insert(id, '|')
    elif i[0] == 'R':
        if id != ll.size() - 1:
            ll.pop(id)
            id += 1
            ll.insert(id,'|')
    elif i[0] == 'B':
        if id != 0:
            id -= 1
            ll.pop(id)
    elif i[0] == 'D':
        if id != ll.size() - 1:
            ll.pop(id + 1)
        
print(ll.__str__())
