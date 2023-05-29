#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?

N = 600851475143
quotients = [N]
dividers = []

i =2
while quotients[-1] != 1:
    if quotients[-1] % i==0:
        quotients.append(quotients[-1]/i)
        dividers.append(i)
        #print(f"{quotients[-1]} || {dividers[-1]}")
    else:
        i = i + 1
print("ANSWER IS: ")
print(dividers[-1])
