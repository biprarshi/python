# SuperFastPython.com
# example of a program that uses all cpu cores
# import math
# from concurrent.futures import ProcessPoolExecutor
 
# # define a cpu-intensive task
# def task(arg):
#     return sum([math.sqrt(i) for i in range(1, arg)])
 
# # protect the entry point
# if __name__ == '__main__':
#     # report a message
#     print('Starting task...')
#     # create the process pool
#     with ProcessPoolExecutor(200) as exe:
#         # perform calculations
#         results = exe.map(task, range(1,50000))
#     # report a message
#     print('Done.')

from concurrent.futures import ProcessPoolExecutor

def parallel_function(billion):
    for i in range(billion):
        i += 1
    return i

if __name__ == '__main__':
    billion = [1000000000]
    # report a message
    print('Starting task...')
    # create the process pool
    with ProcessPoolExecutor(500) as executor1:
        # perform calculations
        results1 = executor1.map(parallel_function, billion)
    # report a message
    # 
    # with ProcessPoolExecutor(5000) as executor1:
    #     # perform calculations
    #     results1 = executor1.map(print(sum(range(1000000000))))
    # print('Done.')

    for i in range(1):
        print(next(results1))
