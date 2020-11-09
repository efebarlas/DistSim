from DistSim import Cluster
import time

cluster = Cluster(5)

def job(arg):
    with cluster.__job_locks__['storage']:
        cluster.storage['sum'] += arg ** 3
a = time.time()

listt = [2, 20, 200, 400, 800, 1600]
thread_cnt = [1, 5, 25, 125, 625]
for i in listt:
    for k in thread_cnt:
        cluster = Cluster(k)
        for j in range(i):
            cluster.addJob(job, j)
        cluster.runJobs()
        
        print(cluster.storage['sum'])
        cluster.storage['sum'] = 0
print(time.time()- a)