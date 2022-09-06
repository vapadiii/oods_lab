class Stack():

    def __init__(self, l = None):
        if l == None:
            self.items = []
        else :
            self.items = l
    
    def add(self, i):
        self.items.append(int(i))

    def dec2bin(self,decnum):

        while(decnum != 0):
            n = decnum % 2
            decnum = int(decnum / 2)
            self.add(n)

        self.items.reverse()    
        
print(" ***Decimal to Binary use Stack***")
n = input("Enter decimal number : ")
#print(n)
s = Stack()
s.dec2bin(int(n))

str_list = ''.join(str(i) for i in s.items)
print("Binary number :", str_list)