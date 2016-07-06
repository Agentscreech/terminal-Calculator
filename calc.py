# ! python 3
# This program will take inputs one at a time from the user and do the operation
# instructed in the order it was given then print out that function with the result.


def getNums(message):
    while True:
        try:
            userInput = int(input(message))
        except ValueError:
            print("Sorry, that wasn't a number, try again")
            continue
        else:
            return userInput
            break
qty = getNums('How many numbers are we dealing with ')
numLst = []
opLst = []
for i in range(int(qty)):
    if i == 0:
        numLst.append(getNums("First Number "))
    elif i == int(qty) - 1:
        numLst.append(getNums("Last Number "))
    else:
        numLst.append(getNums("Next number "))
    if i != (int(qty)) - 1:
        while True:
            opLst.append(input('what are we doing with it? (+,-,*,/,^) '))
            if opLst[i] not in ("+", "-", "*", "/", "^"):
                print("Not an appropriate choice.")
                del opLst[i]
            else:
                break
total = int(numLst[0])
n = 1
print(total, end=''),
for i in opLst:
    if i == "+":
            total += int(numLst[n])
            print(i, end='')
            print(numLst[n], end='')
            n += 1
    elif i == "-":
            total -= int(numLst[n])
            print(i, end='')
            print(numLst[n], end='')
            n += 1
    elif i == "*":
            if total == 0:
                total = 1
            total *= int(numLst[n])
            print(i, end='')
            print(numLst[n], end='')
            n += 1
    elif i == "/":
            if total == 0:
                total = 1
            total /= float(int(numLst[n]))
            print(i, end='')
            print(numLst[n], end='')
            n += 1
    elif i == "^":
            if total == 0:
                total = 1
            total ^= int(numLst[n])
            print(i, end='')
            print(numLst[n], end='')
            n += 1
    else:
        print ("I don't know how to do that")
print("=", end=''),
print(total)
