# 3-(2^(input))-1
strt = ''
bin = []
def decToBin(inp):
    global strt
    #0
    if inp == 0:
        strt += "0"
        j = strt
        strt = ""
        return j[::-1]
    #1
    elif inp == 1:
        strt += "1"
        j = strt
        strt = ""
        return j[::-1]
    else:
        if inp%2 == 0:
            inp = inp/2
            strt += "0"
            return decToBin(inp)
        else:
            inp = inp//2
            strt += "1"
            return decToBin(inp)

def printBin(inp,numbit):
    global bin
    st = ''
    if inp < 0:
        return bin
    else:
        l = decToBin(inp)
        Div = numbit - len(l)
        if len(l) < numbit:
            st += '0'*Div + str(l)
            bin.append(st)
        else:
            bin.append(l)
        return printBin(inp-1,numbit)

def printAll(inp):
    if inp == []:
        return 
    else:
        print(inp[-1])
        inp.pop(-1)
        return printAll(inp)


inp = input("Enter Number : ")
inp = int(inp)
numbit = inp
allPoss = (2**inp)-1
if inp < 0:
    print("Only Positive & Zero Number ! ! !")
else:
    printAll(printBin(allPoss,numbit))
    