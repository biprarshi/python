from multiprocessing import Queue, Process, Lock,Value
import array
import datetime

def parallel_function(id, counter, lock):
    MAX = 50
     
    while counter.value < MAX:
        lock.acquire()
        counter.value += 1

        print(datetime.datetime.now())
        array3 = array.array('Q', range(1000000000))
        print(array3[-1])
        print(datetime.datetime.now())

        lock.release()

counter = Value('d', 0.0)
lock = Lock()
q = Queue()
p1 = Process(target=parallel_function,  args=(0, counter, lock,))
p1.start()

r1 = q.get()
p1.join()

print(r1)