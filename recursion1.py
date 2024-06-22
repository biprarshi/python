def function1(k):
    if k > 0:
        result1 = k + function1(k - 1)
        print(result1)
    else:
        result1 = 0
    return (result1)


print(function1(6))


def factorial_calc1(num1):
    if num1 > 0:
        temp1 = num1 * factorial_calc1(num1-1)
        # print(temp1)
        return temp1
    else:
        print("last")
        return 1


print("factorial")
print(factorial_calc1(7))
