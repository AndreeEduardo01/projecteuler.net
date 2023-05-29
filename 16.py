# Power digit sum
# 2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2**1000?

monster = 2**1000
monstr = str(monster)
base = int(monstr[0]) + int(monstr[1])
for i in range(2,len(monstr)):
    base = base + int(monstr[i])
    # print(base)
print(base)