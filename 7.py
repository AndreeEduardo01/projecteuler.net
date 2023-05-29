# By listing the first six prime numbers:
#  2, 3, 5, 7, 11, and 13, 
# we can see that the 6th prime is 13.
# What is the 10 001st prime number?

#THIS PROGRAM COULD TAKE A WHILE (MORE THAN 2 MINUTES)
n = 2
primes = []
while len(primes) <= 10001 :
    prov=[]
    for i in range(1,n+1):
        if (n>2) and (n%2==0):
            break
        #print(f"{n} / {i}")    
        if len(prov) > 2:
            break
        elif n % i==0:
            prov.append(i)
    if len(prov) == 2:
        primes.append(n)
        n = n + 1
    n = n + 1
print(f"ANSWER IS: {primes[-3]}")
#primes[-3] es el correcto

