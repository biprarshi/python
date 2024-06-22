# from multiprocessing import Pool
import multiprocessing
# import threading
import concurrent.futures

def parallel_function():
    for i in range(1000000000):
        i += 1
    print(i)

print(multiprocessing.cpu_count())

# pool = multiprocessing.Pool()
# # result1 = pool.apply_async(solve1, [A])    # evaluate "solve1(A)" asynchronously
# # answer1 = result1.get(timeout=10)
# result1 = pool.apply(parallel_function)
# pool.close() 
# pool.join()

# t1 = threading.Thread(target=parallel_function)
# t1.start()
# t1.join()

# # create a thread pool with 2 threads
# pool = concurrent.futures.ThreadPoolExecutor(max_workers=multiprocessing.cpu_count())

 
# # submit tasks to the pool
# # pool.submit(parallel_function)

# pool.map(parallel_function 

# # wait for all tasks to complete
# pool.shutdown(wait=True)

# executor1 = concurrent.futures.ProcessPoolExecutor(max_workers=multiprocessing.cpu_count())
# executor1.submit(parallel_function)
# executor1.shutdown(wait=True,cancel_futures=False)

# from multiprocessing import Process
# if __name__ == '__main__':
#     p = Process(target=parallel_function)
#     p.start()
#     p.join()

# from multiprocessing import Pool
# import time
# import math
# N = 5000000
# def cube(x):
#     return math.sqrt(x)
# if __name__ == "__main__":
#     with Pool() as pool:
#       result = pool.map(cube, range(10,N))
#     print("Program finished!")