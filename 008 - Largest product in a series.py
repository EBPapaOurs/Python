file = open("Resources/SerieFor008.txt", "r")
greatestProduct = 0
indexGreatestProduct = 0
listNumber = []
for i in file :
    if (int(i) >= 0) and (int(i) <= 9):
        listNumber.append(int(i))

for i in range(0, len(listNumber) - 13) :
    tempProduct = listNumber[i]
    for j in range(1, 13) :
        tempProduct *= listNumber[i + j]

    if tempProduct > greatestProduct :
        indexGreatestProduct = i
        greatestProduct = tempProduct

print("The thirteen adjacent digits in the 1000-digit number that have the greatest product are :")
for i in range(0, 12) :
    print(listNumber[indexGreatestProduct + i], "x ", end="")
print(listNumber[indexGreatestProduct + 12], "=", greatestProduct)