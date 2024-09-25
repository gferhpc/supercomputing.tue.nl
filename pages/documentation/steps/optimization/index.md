---
title: 6. Workload Optimization
---

# Workload Optimization

Some software spontaneously spawns many threads to speed up certain
tasks. In an HPC environment in which nodes are shared between different
jobs, each of which requested a certain number of tasks or cpus, this is
undesirable. The scheduler assigns jobs to nodes assuming each job will
use exactly the resources requested.

This behaviour occurs in many programs, usually by means of an OpenMP
(OMP) implementation (note that this is different from MPI
parallelisation which can be used across nodes while OpenMP only
provides multithreading within a single machine). Most software that
does this has means to control this automatic multithreading. In our
cluster environment, users should instruct their software to use the
correct number of threads. This page contains instructions for how to do
this in various programs (please add to the list if you can).

The examples below assume your slurm script uses 1 node (`-N 1`) and a
certain number of tasks set using the `-n` option. Some sources advise
to use a single task (`-n 1`) for OpenMP work and control the number of
cpus using the `--cpus-per-task` option, in which case you should
replace any occurrences of `$SLURM_NTASKS` below with
`$SLURM_CPUS_PER_TASK`.

## Python / Numpy

Numpy implementations may vary, but for example the
`anaconda/2021.11-pth39` module does automatic multithreading for some
common numpy operations. In order to limit the number of CPU cores it
uses to the number actually requested in your slurm script, include
either

    export MKL_NUM_THREADS=$SLURM_NTASKS

or

    export OMP_NUM_THREADS=$SLURM_NTASKS

in your slurm script, before the invocation of your python script.
(Note: It is not clear to the author if these are supposed to be
equivalent statements, but in case of the mentioned anaconda module they
give the same result.)

## Python / Pytorch

Pytorch has its own feature to control multithreading. Simply call
`torch.set_num_threads(num_threads)` within your program, where
`num_threads` is a variable containing the number of CPU cores your job
should use. See
[1](https://pytorch.org/docs/stable/generated/torch.set_num_threads.html)
for details.

## Matlab

You can use the `-singleCompThread` command line option to limit Matlab
to use only a single thread. Alternatively one can call
`maxNumCompThreads(num_threads)` from within the Matlab script. See the
documentation
[2](https://nl.mathworks.com/help/matlab/ref/maxnumcompthreads.html) for
further details.