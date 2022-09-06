print("*** multiplication or sum ***")
num1 ,num2 = [int(x) for x in input("Enter num1 num2 : ").split()]
if((num1*num2)>1000):
    res = num1 + num2
else:
    res = num1 * num2
print("The result is", res)