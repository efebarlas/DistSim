class Cluster():
    def __init__(self):
        __futures__ = []
        __jobs__ 
        # computer instances should be stored
        # job queue
        # job status register array for scheduling
        # assign new jobs with a lock
    def runJobs(self):
        futures = []
    futuresOccupied = [] # -1 ->
    tasksCompleted = False
    with concurrent.futures.ThreadPoolExecutor(max_workers=WORKER_COUNT, initializer=barrierFn) as executor:
        ax = time.time()
        for i in range(len(jobs)):
            futures.append(executor.submit(jobWrapper(jobs[i][0], jobs[i][1])))
        while not all jobs complete:
            if threading.active_count() < WORKER_COUNT:
                job = jobWrapper(jobs[i][0], jobs[i][1]) if not all jobs complete else idle
                futures.append(executor.submit(job))    
class Computer():
    def __init__(self):
        # local memory
        # future / job
        # a port to receive information from
        # another port to serve return information to other computers
        # a lock per port that can be accessed by other computer objects to let computer know the info in the port is complete


# future features: random job failures, random decreases in performance, assign jobs after you call runJobs on a cluster, create new ports for each computer on demand, unpredictable port values (main computer supporting computers practice for mission critical applications)

# how to sleep all other threads while main thread is assigning a job????