import concurrent.futures
import threading
import queue

def map_fn(lol):
    return 1

open_gates = False
lock = threading.Lock()
def idle():
    global open_gates
    while True:
        with lock:
            if threading.active_count() == THREAD_COUNT or open_gates == True:
                open_gates = True
                return


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
THREAD_COUNT = 1000
jobs = []
with concurrent.futures.ThreadPoolExecutor(max_workers=THREAD_COUNT) as executor:
    for i in range(THREAD_COUNT):
        future = executor.submit(idle) # occupy each thread so that cpu is slowed down
        future.add_done_callback(jobs[1][0], args=)