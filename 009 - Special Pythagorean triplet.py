import math

a = 0
b = 0
c = 0

for i in range(1, 999) :
    for j in range(i, 999 - i) :
        if  (math.pow(i, 2) + math.pow(j, 2)) == math.pow(1000 - i - j, 2) :
            a = i
            b = j
            c = 1000 - i - j

print("The one Pythagorean triplet for which a + b + c = 1000 is a =", a,", b =", b, "and c = ", c, "\nThe product of abc is ", a*b*c)