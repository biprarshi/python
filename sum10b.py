import pp

def parallel_function():
    for i in range(1000000000):
        i += 1
    print(i)

# Start pp execution server with the number of workers set to the number of processors in the system
job_server = pp.Server(ncpus="autodetect", ppservers=())


# jgan, jgn, jgs = job_server.get_active_nodes(), job_server.get_ncpus(), job_server.get_stats()

# print(jgan, jgn, jgs)


job_server.print_stats()

# Submit all the tasks for parallel execution
# f1 = job_server.submit(func1, args1, depfuncs1, modules1)
# f2 = job_server.submit(func1, args2, depfuncs1, modules1)
# f3 = job_server.submit(func2, args3, depfuncs2, modules2) 
f1 = job_server.submit(parallel_function)



job_server.print_stats()

# Retrieve the results as needed:
# r1 = f1()
# r2 = f2()
# r3 = f3() 
r1 = f1()