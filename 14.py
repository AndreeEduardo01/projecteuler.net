# Longest Collatz sequence
# The following iterative sequence is defined for the set of positive integers:
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
# Although it has not been proved yet (Collatz Problem),
#  it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?
# N0TE: Once the chain starts the terms are allowed to go above one million.
# SPOILER: THIS PROGRAM COULD TAKE AROUND 1 MINTUE TO FINISH 
def is_even(a):
    if a%2==0:
        return True
    else:
        return False
n = 1
chains = []
numbers = []
while n <= 1000000:
    chain = []
    chain.append(n)
    while chain[-1]!=1:
        if is_even(chain[-1]) == True:
            chain.append(chain[-1]/2)
            #print("es par")
        elif is_even(chain[-1]) == False:
            chain.append((3*chain[-1]) + 1)
            #print("Es impar")
    chains.append(chain)
    numbers.append(n)
    n +=1
lens = []
for x in chains:
    lens.append(len(x))
dict_from_list = dict(zip(lens,numbers))
print(f"ANSWER IS: {dict_from_list[max(lens)]}")    
