current = 1
previous = 0
sumEven = previous % 2 + current % 2
tempTerm = current + previous
while tempTerm < 4000000:
    if tempTerm % 2:
        sumEven += tempTerm
    previous = current
    current = tempTerm
    tempTerm = current + previous

print("The sum of the even-valued terms (not excedd four million) is", sumEven)