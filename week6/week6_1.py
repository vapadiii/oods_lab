#Fibonacci
def recursion_fibo(num):
    #base case
    if num <= 1:
        return num
    #recursive case
    else :
        return(recursion_fibo(num - 1) + recursion_fibo(num-2))
    
num = int(input("Enter Number : "))
print("fibo({}) = {}".format(num,recursion_fibo(num)))
#print("fibo(",num,") = ",recursion_fibo(num))