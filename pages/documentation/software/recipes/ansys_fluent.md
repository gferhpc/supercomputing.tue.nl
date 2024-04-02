---
title: Ansys Fluent
tags: [Software, Module]
---

[ANSYS Fluent](https://www.ansys.com/products/fluids/ansys-fluent) is the industry-leading fluid simulation software known for its advanced physics modeling capabilities and industry leading accuracy

## Start-up ANSYS Fluent with GUI (interactive)

For the model and mesh generation Ansys Fluent can be started
interactive in the following way:

Use your browser to connect to https://hpc.tue.nl

## ANSYS Fluent jobscript example

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
