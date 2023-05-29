# 2520 is the smallest number 
# that can be divided by each of the numbers 
# from 1 to 10 without any remainder.
# What is the smallest positive number that is
#  evenly divisible by all of the numbers from 1 to 20?

collection = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
results = ['a','b']
i=1
while True:
    if results[-1] == results[-2]:
        break
    for x in collection:
        if i % x == 0:
            pass
        else:
            i = i + 1
    results.append(i)
print(f"ANSWER IS: {i}")
