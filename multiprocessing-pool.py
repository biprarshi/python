import multiprocessing
import datetime
import array

# def parallel_function():
#     for i in range(1000000000):
#         i += 1
#     print(i)
"""Function to be executed by each process."""
# Perform computation using data
# ...


def parallel_function():
    print(datetime.datetime.now())
    array3 = array.array('Q', range(1000000000))
    print(array3[-1])
    print(datetime.datetime.now())


if __name__ == '__main__':
    num_processes = multiprocessing.cpu_count()

    with multiprocessing.Pool(processes=num_processes) as pool:
        p = multiprocessing.Process(target=parallel_function)
        p.start()
        p.join()


# if __name__ == '__main__':
#     num_processes = multiprocessing.cpu_count()  # Get the number of available CPU cores

#     processes = []
#     for _ in range(num_processes):
#         p = multiprocessing.Process(target=parallel_function)
#         p.start()
#         processes.append(p)

#     # Wait for all processes to finish
#     for p in processes:
#         p.join()


# if __name__ == '__main__':
#     num_processes = multiprocessing.cpu_count()  # Get the number of available CPU cores

#     with multiprocessing.Pool(processes=num_processes) as pool:
#         # Prepare the data to be processed
#         data = [1000000000]  # Your data goes here

#         # Distribute the workload evenly among the processes
#         pool.map(parallel_function, data)
