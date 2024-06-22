import random

# Return a random integer N such that a<=N<=b. Alias for randrange(a, b+1)
ri1 = random.randint(2, 11)
print(ri1)

# Return a randomly selected element N(integer) from range(start, stop, step) such that start<=N<stop
rr1 = random.randrange(5, 50, 5)
print(rr1)

# Return a random element from the non-empty sequence
list1 = [11, 22, 33, 76, 65, 90, 25]
ch1 = random.choice(list1)
print(ch1)

# Returns any random float value between 0 and 1. Return the next random floating point number in the range 0.0 <= X < 1.0
rndm1 = random.random()
print(rndm1)
# from math import floor
# print(floor(r1*100), end=' ')

list2 = [10, 20, 30, 40, 50]
random.shuffle(list2)  # Shuffle the sequence
print(list2)

# Returns the generated floating point random number between lower limit and upper limit
# Return a random floating point number N such that a <= N <= b if a <= b and b <= N <= a if b < a. The end-point value b may or may not be included in the range depending on floating-point rounding in the expression a + (b-a) * random().
unifrm1 = random.uniform(1, 5)
print(unifrm1)
