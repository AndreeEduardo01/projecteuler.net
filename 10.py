# Summation of primes
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
#Using from 7th Problem:

n = 3   
primes = [2]
while primes[-1] < 2000000 :
    for x in primes:
        # print(f"{n} / {x}")
        if n%x==0:
            n = n+1
            break
        elif (n%x != 0) and n/x < x:
            primes.append(n)
            n = n +1
            break
print(f"ANSWER IS: {sum(primes)}")