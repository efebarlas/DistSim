from DistSim import Cluster
import time

cluster = Cluster(5)

def job(arg):
    with cluster.__job_lock__:
        cluster.__storage__['sum'] += arg ** 3

listt = [2, 20, 200, 400, 800, 1600]
thread_cnt = [1, 5, 25, 125, 625]
for i in listt:
    for k in thread_cnt:
        cluster = Cluster(k)
        for j in range(i):
            cluster.addJob(job, j)
        a = time.time()
        cluster.runJobs()
        print(time.time()- a)
        print(cluster.__storage__['sum'])
        cluster.__storage__['sum'] = 0
