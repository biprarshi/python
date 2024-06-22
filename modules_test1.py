import module_one
a = module_one.sum(10,20)
print(a)
print(module_one.mul(20,6))

from module_one import sum
print(sum(25,26))

from module_one import *
print(sum(25,56))
print(mul(11,6))

import module_one as M     #Alias
print(M.sum(11,23))
print(M.mul(22,5))