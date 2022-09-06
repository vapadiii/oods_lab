import math

print("*** New Range ***")
n = list(map(float, input("Enter Input : ").split(" ")))

arr = []
if len(n) == 3:
    start = n[0]
    end = n[1]
    off = n[2]
    while (start < end):
        arr.append(round(start, 3))
        start += n[2]
elif len(n) == 2:
    off = n[0] % 1
    arr = list(map(float, range(math.floor(n[0]), math.ceil(n[1]), 1)))
    for e in range(len(arr)): arr[e] += off
else:
    arr = list(map(float, range(0, math.ceil(n[0]), 1)))
r = str(arr).replace("\'", "")
r = r.replace("[", "(").replace("]", ")")
print(r)