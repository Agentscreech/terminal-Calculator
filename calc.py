#! python3
# op = input("what do you want to do? ")
qty = input("how many numbers are we dealing with? ")
numLst = []
opLst = []
for i in range(int(qty)):
    numLst.append(input("next number "))
    opLst.append(input('what are we doing with it? (+,-,*,/,^) '))
#TODO still need to find a way to check if the input was valid
#before trying to iterate the array
print(numLst)
#TODO find a way to stop asking for the operator on the last number
#this just deletes the last one for now
opLst = opLst[0:-1]
print(opLst)


total = 0
n = 0
for i in numLst:
    # print(i)
    # print(opLst[n])
    if opLst[n] == "+":
            total += int(i)
            n += 1
    elif opLst[n] == "-":
            total -= int(i)
            n += 1
    elif opLst[n] == "*":
            if total == 0:
                total = 1
            total *= int(i)
            n += 1
    elif opLst[n] == "/":
            if total == 0:
                total = 1
            total /= int(i)
            n += 1
    elif opLst[n] == "^":
            if total == 0:
                total = 1
            total ^= int(i)
            n += 1
    else:
        print ("I don't know how to do that")
print(total)
