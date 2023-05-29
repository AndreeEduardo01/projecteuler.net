# n! means n × (n − 1) × ... × 3 × 2 × 1
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
# Find the sum of the digits in the number 100!
def find_sum_n(x):
    l_num=[]
    for x in list(str(x)):
        l_num.append(int(x))
    return sum(l_num)

def find_factorial(a):
    i = 2 # <- contador "i"
    factorials=[1]
    while i < a:
        factorials.append(factorials[-1]*i)
        # print(factorials[-1])
        # print(dict(factorials[-1]))
        i = i + 1
    return factorials[-1]
print(f"ANSWER IS: {find_sum_n(find_factorial(100))}")