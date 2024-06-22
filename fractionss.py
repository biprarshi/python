from fractions import Fraction
import math
x = Fraction(1/2)
the_pi = Fraction(math.pi)

print(x/3)
print(the_pi)
print(the_pi.limit_denominator(10))
print(math.floor(the_pi))