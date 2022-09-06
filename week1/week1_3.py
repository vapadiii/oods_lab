print("*** Election ***")
voter = int(input("Enter a number of voter(s) : "))

votes = map(int,input("").split())

point = []
for i in range(20):
    point.append(0)

for i in votes:
    if(i>0 and i<=20):
        point[i-1] = point[i-1] + 1
        
x = 0
for i in votes:
    if(i == max(point)):
        x = x + 1
if(x>=2 or sum(point)==0):
    print("*** No Candidate Wins ***")
else:
    print(point.index(max(point))+1)
