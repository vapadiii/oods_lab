arr = [0, 1, 2, 3]
print (arr)
arr.insert(0,"T")
print (arr)

arr = [0, 1, 2, 3]
arr.insert(999,"T")
print (arr)

arr = [8, 11, 6, 9]
arr.insert(-3,"T")
print (arr)

arr = [8, 11, 6, 9, 7, 56, 9]
arr.insert(-10,"T")
print (arr)

i = 0
while i < len(arr):
    print(i,"-->",arr[i])
    i += 1

for i in arr:
    print(i)
   

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

