import math

isPrime = False
numberPrime = 0
i = 1

while numberPrime != 10001 :
    i += 1
    isPrime = True
    j = 2
    while j <= math.sqrt(i):
        if (i % j) == 0 :
            isPrime = False
        j += 1
    if isPrime == True :
        numberPrime += 1

print("The 10001st prime number is", i)