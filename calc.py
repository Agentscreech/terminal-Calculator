# ! python 3
# This program will take inputs one at a time from the user and do the operation
# instructed in the order it was given then print out that function with the result.

# Function that asks for input and tests if it's a number or not
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
# Get how many numbers are we going to do operations to
qty = getNums('How many numbers are we dealing with ')

# create blank lists, one for numbers and the other for operators
numLst = []
opLst = []
# Use natural language for the input. Discerns between the first, last or other numbers
for i in range(int(qty)):
    if i == 0:
        numLst.append(getNums("First Number "))
    elif i == int(qty) - 1:
        numLst.append(getNums("Last Number "))
    else:
        numLst.append(getNums("Next number "))
# Only ask for what operation we want done if it's not the last number
    if i != (int(qty)) - 1:
        while True:
            opLst.append(input('what are we doing with it? (+,-,*,/,^) '))
            if opLst[i] not in ("+", "-", "*", "/", "^"):
                print("Not an appropriate choice.")
                del opLst[i]
            else:
                break
# start the math portion where the running total is the first number input
total = int(numLst[0])
# counter for how many numbers in the list of operators
n = 1
# start the print out of the calculations
print(total, end=''),
# check to see what the first operation to do is, then do that and store new total plus print out the symbol for what we did, otherwise say "I don't know how"
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
# add final = sign and print total
print("=", end=''),
print(total)
