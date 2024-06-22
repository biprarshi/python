def test():
    try:
        print('apple')
        return 1
    finally:
        print('orange')

test()