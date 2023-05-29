#Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
# By starting with 1 and 2, the first 10 terms will be:
#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#By considering the terms in the Fibonacci sequence whose values do not exceed four million,
#find the sum of the even-valued terms.

FIBONACCI = [1,2]
FIBONACCI2 = []
while FIBONACCI[-1] < 4000000:
    FIBONACCI.append(FIBONACCI[-1]+FIBONACCI[-2])
for i in FIBONACCI:
    if i%2 == 0:
        FIBONACCI2.append(i)
print("ANSWER IS: ")
print(sum(FIBONACCI2))


