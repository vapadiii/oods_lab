def hbd(year):
    age = 20 + (year % 2)   # year % 2 --> 0,1
    base = year//2
    
    return "saimai is just %d, in base %d!" % (age, base)

year = int(input("Enter year : "))
print(hbd(year))