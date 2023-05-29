# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is
#  9009 = 91 × 99.
# Find the largest palindrome made from
#  the product of two 3-digit numbers.

def ispalindrom(c):
    i = 0
    c_str = str(c)
    if len(c_str) % 2 == 0:
        while i < len(c_str)/2:
            if c_str[i] == c_str[-(i+1)]:
                i = 1 + i
            else:
                break
        return i == len(c_str)/2

    else:
        while i < (len(c_str)-1)/2:
            if c_str[i] == c_str[-(i+1)]:
                i = i + 1
            else:
                break
        return i == (len(c_str)-1)/2

products = []
for a in range(100,1000):
    for b in range(100,1000):
        if ispalindrom(a*b):
            products.append(a*b)
            #print(f"{a} x {b}")
print("ANSWER IS: ")
print(max(products))