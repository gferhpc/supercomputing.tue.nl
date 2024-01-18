# SLURM User Guide

## Introduction to SLURM

SLURM (Simple Linux Utility for Resource Management) is a powerful cluster management and job scheduling system. SLURM allows users to submit jobs to be performed on one or many nodes in a cluster, manage job queues, and query the status of jobs and queues.

This guide will cover the essentials of using SLURM, focusing on the `sbatch` command for job submission and discussing SLURM partitions.

## Understanding SLURM Partitions

A partition is a logical grouping of nodes, kind of like a queue, that specifies which nodes and job configurations are available to the jobs associated with it. Your cluster administrator will configure partitions according to the cluster's policies and available resources. You should choose a partition based on your job requirements and the partition specifications.

List available partitions (Also known as Queues):

```bash
sinfo
```

## Writing a Batch Job Script

A batch job script is a shell script that includes SLURM directives within commented lines (prefixed with `#SBATCH`) followed by the commands you want to execute.

Here's an example job script for a CPU only node:

```bash
#!/bin/bash

#SBATCH --job-name=my_job
#SBATCH --output=my_job_output_%j.txt
#SBATCH --partition=tue.default.q
#SBATCH --time=02:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=2G

# Load modules or software if needed
# module load python3

# Execute the script or command
python my_script.py
```
Here's an example job script for a GPU node:

```bash
#!/bin/bash

#SBATCH --job-name=my_job
#SBATCH --output=my_job_output_%j.txt
#SBATCH --partition=tue.gpu.q
#SBATCH --time=16:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=2G
#SBATCH --gpus=1

# Load modules or software if needed
# module load python3

# Execute the script or command
python my_script.py
```

Here's what some of the key `sbatch` options mean:

- `--job-name`: Set the name of the job.
- `--output`: Designate the file to which SLURM will write the standard output (%j is the jobID).
- `--partition`: Choose the partition on which the job should run (check with 'sinfo').
- `--time`: Specify the wall clock limit for the job (format 00-00:00:00 Days-Hours:Minutes:Seconds).
- `--nodes`: The number of nodes on which to run.
- `--ntasks-per-node`: The number of tasks to launch on each node.
- `--cpus-per-task`: The number of CPU cores per task.
- `--mem-per-cpu`: The memory required per CPU core.
- `--gpus`: The number of GPU to use.


## Submitting a Job with `sbatch`

Once you have written your job script, you can submit it to SLURM using `sbatch`.

```bash
sbatch my_job_script.sh
```

## Monitoring and Controlling Jobs

To check the status of your job, use `squeue`.

```bash
squeue --job [JOBID]
```

You can cancel a submitted job using `scancel`.

```bash
scancel [JOBID]
```

You may want to monitor the resources being used by your job in real-time. This can be done using the `sstat` command.

```bash
sstat --format=MaxVMSize,MaxRSS,MaxDiskWrite,MaxDiskRead -j [JOBID]
```

## Advanced `sbatch` Options

SLURM allows for a range of advanced options to precisely control the resources that a job requires. Here are some common advanced options:

- `--gres`: Specifies generic resources, often used for requesting GPUs.
- `--dependency`: Configures job dependencies, allowing jobs to be scheduled after certain other jobs complete.
- `--array`: Submits an array of similar jobs with a single `sbatch` command to iterate over different datasets or parameters.
- `--exclusive`: Requests exclusive node access for the job, even if requesting CPUs (or memory) that don't require the entire node.
- `--qos`: Specifies the Quality of Service for the job which may affect job priority or limits.
- `--reservation`: Submits a job to a reserved set of resources.

## Conclusion

This guide provides an overview of how to use SLURM, with an emphasis on utilizing the `sbatch` command for job submission and understanding partition allocations. For complete details on each command and advanced configuration options, consult the [official SLURM documentation](https://slurm.schedmd.com/documentation.html) or your cluster's user guide. Always be sure to follow best practices and policies of your specific cluster when submitting and managing jobs with SLURM.
