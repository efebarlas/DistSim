#How to keep n futures running at any given time when jobs exceed workers?

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
WORKER_COUNT =10
a = 0
def job(num):
    global a
    try:
        with lock:
            a += num
    except Exception as e:
        print('exception', e)
jobs = [(job, i) for i in range(1 + WORKER_COUNT)]

exitCounter = 0

timePrev = 0

def jobWrapper(jobFn, *args):
    def cb():
        global exitCounter,a, timePrev
        while threading.active_count() < WORKER_COUNT:
            pass
        temp = jobFn(*args)
        with lock:
            exitCounter += 1
        while exitCounter < len(jobs):
            #if job scheduled, do job
            pass
    return cb

b = threading.Barrier(WORKER_COUNT)
def idle():
    return 0
def barrierFn():
    b.wait()



futures = []
futuresOccupied = [] # -1 ->
tasksCompleted = False
with concurrent.futures.ThreadPoolExecutor(max_workers=WORKER_COUNT, initializer=barrierFn) as executor:
    ax = time.time()
    for i in range(len(jobs)):
        futures.append(executor.submit(jobWrapper(jobs[i][0], jobs[i][1])))
    for i in range(WORKER_COUNT - len(jobs)):
        futures.append(executor.submit(jobWrapper(idle)))
    bx = time.time()
    print(bx - ax)
concurrent.futures.wait(futures, return_when='ALL_COMPLETED')
tasksCompleted = True
print(time.time() - bx)
print(a)

#CLUSTER OBJ
#what can you do?
#get a computer out of cluster
#give job to said computer
#communicate computer to computer
#each computer is a thread