import concurrent.futures
import threading
from uuid import uuid4

def printer(future):
    print(str(future.result()) + '\n')
class Cluster():
    def __barrierFn__(self):
        self.__barrier__.wait()
    def __job_done__(self, uid):
        with self.__job_lock__:
            self.__jobs__['assigned'].remove(uid)
            self.__jobs__['completed'].add(uid)
    def __exit__(self):
        with self.__job_lock__:
            self.__count__ -= 1
    def __jobs_running__(self):
        with self.__job_lock__:
            return len(self.__jobs__['assigned']) > 0
    def __jobs_left__(self):
        with self.__job_lock__:
            return len(self.__jobs__['pending']) > 0
    def __job_wrap__(self, jobFn, *args):
        uid = uuid4()
        def cb():
            while threading.active_count() < self.__worker_count__:
                pass
            return_value = jobFn(*args)
            self.__job_done__(uid)
            while self.__jobs_running__() and not self.__jobs_left__():
                    pass
            self.__exit__()
            return return_value
        return uid, cb
    def __init__(self, WORKER_COUNT):
        self.__futures__ = []
        self.__count__ = 0
        self.__jobs__ = dict()
        self.__jobs__['pending'] = dict()
        self.__jobs__['completed'] = set()
        self.__jobs__['assigned'] = set()
        self.__barrier__ = threading.Barrier(WORKER_COUNT)
        self.__worker_count__ = WORKER_COUNT
        self.__job_lock__ = threading.Lock()
        # computer instances should be stored
        # job queue
        # job status register array for scheduling
        # assign new jobs with a lock
    def __idle__(self):
        return
    def runJobs(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.__worker_count__, initializer=self.__barrierFn__) as executor:
            while len(self.__jobs__['pending']) != 0  or self.__count__ < self.__worker_count__:
                if self.__count__ == self.__worker_count__:
                    continue
                if len(self.__jobs__['pending']) == 0:
                    uid, job = self.__job_wrap__(self.__idle__)
                else:
                    uid, job = self.__jobs__['pending'].popitem()
                self.__jobs__['assigned'].add(uid)
                self.__count__ += 1
                self.__futures__.append(executor.submit(job)) #.add_done_callback(printer))
    def addJob(self, jobFn, *jobArgs):
        uid, job = self.__job_wrap__(jobFn, *jobArgs)
        with self.__job_lock__:
            self.__jobs__['pending'][uid] = job
    def removeJob(self, uid):
        with self.__job_lock__:     
            self.__jobs__['pending'].pop(uid, None)
#class Computer():
#    def __init__(self):
        # local memory
        # future / job
        # a port to receive information from
        # another port to serve return information to other computers
        # a lock per port that can be accessed by other computer objects to let computer know the info in the port is complete


# future features: random job failures, random decreases in performance, assign jobs after you call runJobs on a cluster, create new ports for each computer on demand, unpredictable port values (main computer supporting computers practice for mission critical applications)

# how to sleep all other threads while main thread is assigning a job????