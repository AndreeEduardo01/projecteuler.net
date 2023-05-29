#Find the difference between the sum of the squares 
# of the first one hundred natural numbers
#  and the square of the sum.

b = range(1,101)
a = range(1,101)
squared = []
for n in b:
    squared.append(n**2)
sum_b = sum(squared)
sum_a = (sum(a))**2
print("ANSWER IS: ")
print(sum_a-sum_b)