number = 0
result = 1
while result != 0:
    number += 5
    result = 0
    for i in range(1,20):
        result += (number % i)

print("Smallest positive number that is evenly divisible by all of the numbers from 1 to 20 is", number)