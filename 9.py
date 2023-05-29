# Special Pythagorean triplet
# A Pythagorean triplet is a set of three natural 
# numbers, a < b < c, for which,
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# There exists exactly one Pythagorean 
# triplet for which a + b + c = 1000.
# Find the product abc.

la = []
lb = []
lc = []

for a in range(1,1001):
    for b in range(1,1001):
        if ((a**2 + b**2)**(0.5)).is_integer() and ((a+b+(a**2 + b**2)**(0.5))==1000):
            la.append(a)
            lb.append(b)
            lc.append((a**2 + b**2)**(0.5))
            #print(f"{a}**2 + {b}**2")
            #print(a*b*(a**2 + b**2)**(0.5))
            break
    
print(f'Triplet is: {la[-1],lb[-1],lc[-1]}')
print(f'And its product is: {la[-1]*lb[-1]*lc[-1]}')

