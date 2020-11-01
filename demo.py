from DistSim import Cluster


cluster = Cluster(5)

def job(arg):
    return arg ** 3

for i in range(1):
    cluster.addJob(job, i)
cluster.runJobs()

for i in range(50):
    cluster.addJob(job, i)
cluster.runJobs()