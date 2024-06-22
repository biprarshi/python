import pp


def parallel_function():
    for i in range(1000000000):
        i += 1
    return i


job_server = pp.Server(ncpus='autodetect', ppservers=())


f1 = job_server.submit(parallel_function)

r1 = f1()
job_server.print_stats()
print(r1)
job_server.print_stats()
