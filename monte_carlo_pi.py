import math
import random
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    for i in range(1, size):
        pi += comm.recv(source=i, tag=i)
    pi = pi / size
    print(pi)
else:
    for count in range(0, 1000):
        d = math.hypot(random.random(), random.random())
        if d < 1:
            count_inside += 1
    count += 1
    pi = (4.0 * count_inside / count)
    comm.send(pi, dest=0, tag=rank)

comm.Barrier()