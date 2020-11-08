from DistSim import Cluster
import time

cluster = Cluster(5)

def job(arg):
    return arg ** 3

for i in range(1):
    cluster.addJob(job, i)
cluster.runJobs()

for i in range(50):
    cluster.addJob(job, i)
a = time.time()
cluster.runJobs()
print(time.time()- a)

for i in range(100):
    cluster.addJob(job, i)
a = time.time()
cluster.runJobs()
print(time.time()- a)


for i in range(200):
    cluster.addJob(job, i)
a = time.time()
cluster.runJobs()
print(time.time()- a)


for i in range(400):
    cluster.addJob(job, i)
a = time.time()
cluster.runJobs()
print(time.time()- a)
