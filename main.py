import concurrent.futures
import threading
import queue
import time
def map_fn(lol):
    return 1

open_gates = False
lock = threading.Lock()
"""
def idle():
    global open_gates
    while True:
        with lock:
            if threading.active_count() == THREAD_COUNT or open_gates == True:
                open_gates = True
                return
"""


''' JOB TO demonstrate race condition
summer = 0
faulty_sum = 0
def job(self):
    print('JOB' + str(threading.current_thread()))
    global summer, faulty_sum
    x = 0
    while x < 10:
        x += 1
    temp = faulty_sum
    while x < 100:
        x += 0.001
    faulty_sum = temp + 10
    with lock:
        summer += 10
    print('EXIT JOB')
'''
MAX_WORKERS = 1000
MIN_WORKERS = 800 # 200 threads allowed to fail
a = 0
def job(num):
    global a
    temp = 0
    try:
        with lock:
            a += num
            temp = a
    except Exception as e:
        print('exception', e)
jobs = [(job, i) for i in range(1000)]

 
def jobWrapper(jobFn, *args):
    def cb():
        while threading.active_count() < MIN_WORKERS:
            pass
        return jobFn(*args)
    return cb
b = threading.Barrier(MIN_WORKERS)
def barrierFn():
    b.wait()



futures = []
with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS, initializer=barrierFn) as executor:
    ax = time.time()
    for i in range(len(jobs)):
        futures.append(executor.submit(jobWrapper(jobs[i][0], jobs[i][1])))
    bx = time.time()
    print(bx - ax)
concurrent.futures.wait(futures, return_when='ALL_COMPLETED')
print(time.time() - bx)
print(a)

#CLUSTER OBJ
#what can you do?
#get a computer out of cluster
#give job to said computer
#communicate computer to computer
#each computer is a thread