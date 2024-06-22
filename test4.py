def tomato1():
    return 5


print(tomato1)
print(type(tomato1))
print(id(tomato1))
print(tomato1())

# returns the id() in hex if '()' not specified

print(locals())

i = 0
for x in range(10):
    print(i)
    i += 1
    print(i)
    input()

size = eval(input('Enter size: '))
for i in range(size):
    print('*', end='')
print()
for i in range(size-2):
    print('*')
for i in range(size):
    print('*', end='')
print()
