class Stack():

    def __init__(self, l = None):
        if l == None:
            self.items = []
        else :
            self.items = l
    
    def add(self, i):
        self.items.append(int(i))

    def pop(self):
        self.items.pop()
                    
ls = [e for e in input("Enter Input : ").split(",")]

s = Stack()
temp = Stack()

for data in ls:
    x = data.split()
    
    if x[0] == "A":
        s.add(x[1])
        print("Add =",x[1])

    elif x[0] == "P":
        if not s.items:
            print("-1")   
        else:
            last = len(s.items) - 1     #['apple','banana'] --> 2 ตัว แต่ index สุดท้ายต้องเป็น len - 1
            print ("Pop =",s.items[last])
            s.pop()

    elif x[0] == "D":
        if not s.items:
            print("-1") 
        else:    
            temp.items = s.items
            s.items = []       #ทำให้ stack1 ว่าง
            for value in temp.items:
                if value == int(x[1]):
                    print ("Delete =", value)  #ไม่เก็บเข้า stack
                else:
                    s.add(value)    #แอดเข้ามาจาก arr ว่าง จากบรรทัด 40

    elif x[0] == "LD":
        if not s.items:
            print("-1") 
        else: 
            temp.items = s.items
            temp.items.reverse()    #เพื่อให้ลบจากหลังก่อน
            s.items = []
            for value in temp.items:
                if value < int(x[1]):
                    print ("Delete =",value, "Because",value,"is less than", x[1])    
                else:
                    s.add(value)
            s.items.reverse()   #เพื่อเรียงจากหน้ามาหลังอีกรอบ
                    
    elif x[0] == "MD":
        if not s.items:
            print("-1")
        else:
            temp.items = s.items
            temp.items.reverse()
            s.items = []
            for value in temp.items:
                if value > int(x[1]):
                    print ("Delete =",value, "Because",value,"is more than", x[1])
                else:
                    s.add(value)
            s.items.reverse()

print("Value in Stack =",s.items)