print("*** Fun with countdown ***")
numbers = map(int,input("Enter List : ").split())

n = -1
a = []
r = []
for e in numbers:
    if n == -1:
        n = e
        a.append(e)
        if n == 1:
            r.append(a)
            a = []
            n = -1
    elif e == 1:
        a.append(e)
        r.append(a)
        a = []
        n = -1
    elif n - 1 == e:
        a.append(e)
        n = e
    else:
        a = []
        a.append(e)
        n = e
ans = []
ans.append(len(r))
ans.append(r)
print(ans)
