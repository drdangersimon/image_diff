from ../__init__ import Reduice_chi
import mpi4py.MPI as mpi
import sys


video = Reduice_chi(sys.argv[1])
# time run
t_multi = mpi.Wtime()
work_array = video.mpi_work_split()
frame_no, frame_time, frame_chi = video.parallel_moving_ave(work_array)
video.aggrigate_to_root(frame_no, frame_time, frame_chi)
video.comm.barrier()
video.save_result()
t_multi -= mpi.Wtime()
if video.rank == 0:
    # Make plot
    video.plot()
    #video.make_movie()
