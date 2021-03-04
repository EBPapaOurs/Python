sumSquare = 0
squareSum = 0

for i in range(1, 101):
    sumSquare += i ** 2
    squareSum += i

squareSum = squareSum ** 2
result = squareSum - sumSquare 
print("The difference between the sum of the squares of the first one hundred natural numbers and the square of the sum", result)