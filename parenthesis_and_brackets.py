# This script checks if a string of parentheses and brackets is balanced and properly nested.
# Enter a string containing parentheses and brackets
print("Enter a string containing parentheses and brackets, i.e. \"([]())\" or \"([)]\" (default ([)])")
# read input from user
user_input = input().strip()
if user_input:
    input = user_input
else:
    input = "([)]"

# create two stacks and a broken flag
pstack = []
bstack = []
broken = False

for i in range(len(input)):
    char = input[i]
    if char == '(':
        # push to pstack
        pstack.append(len(bstack)) # store current bstack size
    elif char == ')':
        # pop from pstack if not empty
        if pstack:
            if pstack and pstack[-1] > len(bstack): # check if brackets are trapped inside parentheses
                broken = True
                break
            pstack.pop()
        else:
            broken = True
            break
    elif char == '[':
        # push to bstack
        bstack.append(len(pstack)) # store current pstack size
    elif char == ']':
        # pop from bstack if not empty
        if bstack:
            if bstack and bstack[-1] > len(pstack): # check if parentheses are trapped inside brackets
                broken = True
                break
            bstack.pop()
        else:
            broken = True
            break

if broken or pstack or bstack:
    print("NOT OK!")
else:
    print("OK!")