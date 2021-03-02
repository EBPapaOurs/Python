number = 0
answer = 0
answerFirstDigit = 0
answerSecondDigit = 0

for i in range(999, 100, -1):
    for j in range(999, 100, -1):
        number = i * j
        res = [int(x) for x in str(number)] 
        if number >= 100000 and res[0] == res[5] and res[1] == res[4] and res[2] == res[3] and (answer < number):
            answer = number
            answerFirstDigit = i
            answerSecondDigit = j

print("The largest palindrome product of two 3-digits is :", answerFirstDigit, "x", answerSecondDigit, "=", answer)