import math

number = 600851475143
temp = number
factor = 2
lastFactor = 1
if (temp % 2) == 0:
    temp /= 2
    lastFactor = 2
    while (temp % 2) == 0:
        temp /= 2
else:
    lastFactor = 1
factor = 3
maxFactor = math.sqrt(temp)
while temp > 1 and factor <= maxFactor:
    if (temp % factor) == 0:
        lastFactor = factor
        temp /= factor
        while (temp % factor) == 0:
            temp /= factor
        maxFactor = math.sqrt(temp)
    factor += 2
if temp != 1:
    lastFactor = temp

print("The largest prime factor of the number", number, "is", lastFactor)