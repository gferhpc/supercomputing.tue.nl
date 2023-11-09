---
title: Ansys Fluent
tags: [Software, Module]
---

## Start-up Fluent with GUI (interactive)

By default we run Ansys Fluent jobs in batch mode with sbatch on the HPC
cluster. For the model and mesh generation Ansys Fluent can be start
interactive in the following way:

Use your browser to connect to https://hpc.tue.nl

Obtain a Slurm job allocation (a set of nodes), execute a command, and
then release the allocation when the command is finished.

[`salloc`](https://slurm.schedmd.com/salloc.html)` -N 1  -n `<number of tasks>` -p `<partition name>

With the standard Ansys Fluent license 4 cores can be used in parallel
the number of tasks is then 4. If you have access to the HPC licenses
you can set the number of tasks according your needs.

Start a ssh session with the allocated resources with x11 enabled

`ssh -X $SLURM_NODELIST`

Depending on the configuration of the system you can be asked for your
password.

On the cluster different versions of Ansys are installed. A list of the
installed versions can be displayed with

`module avail ansys`

Load the ansys module version of your choice with

`module load ansys/`<version>

Start Ansys Fluent interactive

`fluent &`

If you are ready with your interactive Ansys Fluent job exit from the
ssh session with exit and release the reserved resources scancel <JOBID>
or just type exit again.

## How to submit Ansys Fluent jobs

1.  Create a batch script myfluent_job_xx.sbatch with the following
    contents, and adjust as needed for your job:
        #!/usr/bin/bash

        #SBATCH --partition=be.student.q            # Partition
        #SBATCH --job-name=myfluent_job_xx          # Job name
        #SBATCH --mail-type=END                     # Mail events (NONE, BEGIN, END, FAIL, ARRAY_TAKS, ALL)
        #SBATCH --mail-user=your_email@tue.nl       # Where to send mail
        #SBATCH --nodes=1                           # Use one node
        #SBATCH --cpus-per-task=1                   # use 1 cpu/core per task
        #SBATCH --ntasks-per-node=4                 # Run 4 tasks per node
        #SBATCH --time=48:00:00                     # Time limit for simulation job hrs:min:sec
        #SBATCH --output=./myfluent_job_xx_%a.out   # Standard output and error log

        # load ansys module
        module load ansys/2021r1

        # Run Fluent 3d double precision without GUI on 1 node using OpenMPI and 4 processors/cores
        fluent 3ddp -g -t${SLURM_NTASKS} -mpi=openmpi -ssh -i fluent_job_xx.jou

    NOTE: by default fluent uses intel-mpi to run multi processor jobs,
    as of version 2021/R1 this no longer works on the Cluster, use
    **-mpi=openmpi** to force fluent to use the OpenMPI version of MPI.
2.  Submit your batch job with `sbatch myfluent_job_xx.sbatch`
