class Queue():
    def __init__(self):
        self.queue = []

    def aslist(self):
        return self.queue

    def enqueue(self, i):
            self.queue.append(i)

    def dequeue(self):
        if(self.isEmpty() != True):
            return self.queue.pop(0)

    def isEmpty(self):
        return self.queue == []

    def peek(self):
        if(self.isEmpty() != True):
            return self.queue[0]
        
    def size(self):
        return len(self.queue)
    
    
score = 0

my = Queue()
your = Queue()

myStr =[]
yourStr =[]

myList =[]
yourList =[]

inp = str(input("Enter Input : ")).split(",")

for i in inp:
    myStr,yourStr = i.split(" ")
    myList.append(myStr)
    yourList.append(yourStr)
    my.enqueue(myStr)
    your.enqueue(yourStr)
print("My   Queue = ",end="")

for i in range(len(myList)):
    print(myList[i],end="")
    if i != len(myList)-1:
        print(", ",end="")
print("")
print("Your Queue = ",end="")

for i in range(len(yourList)):
    print(yourList[i],end="")
    if i != len(yourList)-1:
        print(", ",end="")
print("")
print("My   Activity:Location = ",end="")

# my
for i in range(len(myList)):
    myEvent,myPlace = str(myList[i]).split(":")
    
    #Event
    if myEvent == "0":
        print("Eat:",end="")
    elif myEvent == "1":
        print("Game:",end="")
    elif myEvent == "2":
        print("Learn:",end="")
    elif myEvent == "3":
        print("Movie:",end="")
        
    #Place
    if myPlace == "0":
        print("Res.",end="")
    elif myPlace == "1":
        print("ClassR.",end="")
    elif myPlace == "2":
        print("SuperM.",end="")
    elif myPlace == "3":
        print("Home",end="")
    if i != len(myList)-1:
        print(", ",end="")
    else :
        print("")
print("Your Activity:Location = ",end="")

# your
for i in range(len(myList)):
    yourEvent,yourPlace = str(yourList[i]).split(":")
    
    #Event
    if yourEvent == "0":
        print("Eat:",end="")
    elif yourEvent == "1":
        print("Game:",end="")
    elif yourEvent == "2":
        print("Learn:",end="")
    elif yourEvent == "3":
        print("Movie:",end="")
        
    #Place
    if yourPlace == "0":
        print("Res.",end="")
    elif yourPlace == "1":
        print("ClassR.",end="")
    elif yourPlace == "2":
        print("SuperM.",end="")
    elif yourPlace == "3":
        print("Home",end="")
        
    if i != len(yourList)-1:
        print(", ",end="")
    else :
        print("")

    
while my.isEmpty() != True and your.isEmpty() != True:
    myEvent,myPlace = str(my.peek()).split(":")
    yourEvent,yourPlace = str(your.peek()).split(":")
    if myEvent == yourEvent and myPlace != yourPlace:
        score += 1
    elif myEvent != yourEvent and myPlace == yourPlace:
        score += 2
    elif myEvent == yourEvent and myPlace == yourPlace:
        score += 4
    elif myEvent != yourEvent and myPlace != yourPlace:
        score -= 5
    my.dequeue()
    your.dequeue()
    
if score >= 7:
    print("Yes! You're my love! : Score is {}.".format(score))
elif score <7 and score >0:
    print("Umm.. It's complicated relationship! : Score is {}.".format(score))
elif score <= 0:
    print("No! We're just friends. : Score is {}.".format(score))