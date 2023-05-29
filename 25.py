#The Fibonacci sequence is defined by the recurrence relation:
#Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
#The 12th term, F12, is the first term to contain three digits.
#What is the index of the first term in
#the Fibonacci sequence to contain 1000 digits?
fib_seq = [1,1]
base_cases = 2
def num_digits(x):
    num_digits1 = len(str(x))
    return num_digits1
iterator = 0
while num_digits(fib_seq[-1])!=1000:
    new_fib = fib_seq[0]+fib_seq[1]
    fib_seq.append(new_fib)
    fib_seq.pop(0)
    #print(fib_seq)
    iterator = iterator + 1
print(f'ANSWER IS: {iterator+base_cases}')



    