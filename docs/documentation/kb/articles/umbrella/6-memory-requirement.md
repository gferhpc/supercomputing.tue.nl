---
date: 2025-06-23
authors: [ e.loomeijer ]
type: kb
slug: "6"
tags: [ "Umbrella", "Knowledge Base", "Slurm" ]
categories: [ "Slurm", "Umbrella" ]
---

# Memory requirement for Slurm jobs

All Slurm jobs must specify how much memory they require. If no memory request is specified, your job will automatically be allocated **1 GB RAM per CPU core** by default. This change ensures optimal sharing and utilization of cluster resources and helps prevent job failures due to insufficient memory allocation.

## Specifying memory requirements in Slurm

Add one of the options shown below to your job script’s `#SBATCH` header.  You cannot request more RAM than a node has; see [Technical Specifications](../../../specifications/index.md#hardware).

### Allocate a fixed amount of memory for the entire job

```bash
#SBATCH --mem=10G
```
*Requests 10 GB RAM per node for the job.  For single-node jobs this is the total amount of RAM for the entire job, regardless of the number of cores.*

### Allocate memory per CPU core

```bash
#SBATCH --mem-per-cpu=2G
```
*Requests 2 GB RAM for every requested CPU core. For example, if you request 4 cores, your job will get 8 GB in total.*

### Allocate memory per GPU (for CPU RAM, NOT VRAM)

```bash
#SBATCH --mem-per-gpu=2G
```
*Requests 2 GB RAM for every GPU requested. **This memory is allocated from the system RAM (CPU RAM), not the GPU’s VRAM.***

## Assessing memory usage

To view the memory usage of your job, use any of the following commands:

- `seff <job_id>`
  ```
  Job ID: 17026
  Cluster: cluster
  User/Group: 20231234/test-umb
  State: OUT_OF_MEMORY (exit code 0)
  Cores: 1
  CPU Utilized: 00:00:06
  CPU Efficiency: 1.68% of 00:05:57 core-walltime
  Job Wall-clock time: 00:05:57
  Memory Utilized: 1.01 GB
  Memory Efficiency: 100.68% of 1.00 GB
  ```
  `seff` stands for "Slurm efficiency".  It should help you in finding the
  right amount of CPU cores, memory, and time for your jobs.  In this case, as
  the last line shows, we've used all of our requested RAM, and it would be
  wise to request a bit more.

- `sacct -j <job_id> -o jobid,state,reqmem,averss,maxrss,maxrssnode,maxrsstask`
  ```
  JobID             State     ReqMem     AveRSS     MaxRSS MaxRSSNode MaxRSSTask
  ------------ ---------- ---------- ---------- ---------- ---------- ----------
  17029            FAILED         1G
  17029.batch      FAILED                 4076K      4076K test-comp+          0
  17029.extern  COMPLETED                   76K        76K test-comp+          0
  17029.0       COMPLETED               112628K    112628K test-comp+          0
  ...
  ```
  This command will query Slurm's accounting database for info about your job.
  It shows how much physical memory each of your job's steps occupied.  In case
  you're using multiple tasks (e.g. with MPI), it shows how much memory each
  task used on average (`AveRSS`), and how much memory the largest task used
  (`MaxRSS`).

## Troubleshooting out-of-memory (OOM) events

To see if your job suffered an out-of-memory (OOM) event, you can do any of the following:

- Check Slurm's job output log.  (Default: `slurm-nnnn.out`, otherwise whatever
  you specified with `--output` or `--error`.)  Out-of-memory events are
  indicated as follows:
  ```
  slurmstepd-...: error: Detected 1 oom_kill event in StepId=17020.18. Some of the step tasks have been OOM Killed.
  ```
  An overview of OOM events is also shown at the end of this file.

- Check Slurm's accounting info.  Run `sacct -j <job_id>`.  If `State` is
  `OUT_OF_MEMORY`, your job (or some of its `srun` steps) ran out of memory.
  For your convenience, the output of the `sacct` command is also made at the
  end of your job's output log.

If your job indeed sufferent an OOM event, you'll need to change your job script to request more memory (see above), and resubmit your job.

## Recommendations

- **Assess your workload**

    Estimate how much RAM your code actually needs to avoid out-of-memory errors or wasting resources.

- **Test incrementally**

    Start with a conservative value and increase as needed if jobs fail with out-of-memory errors.

## FAQ

- **What happens if I don’t specify any --mem option?**

    Your job is allocated 1 GB RAM per requested CPU core by default.  If that
    is not enough for your job, it will run out of memory, and will be
    terminated as soon as that happens.

- **What happens if I ask for too little memory for my job?**

    Your job will run out of memory, and will be terminated as soon as this
    happens.

- **What happens if I ask for too much memory for my job?**

    A number of things can happen:

    - If you ask for more memory than the nodes have available, your job will
      not start.
    - Your job will start and will run to completion, but other people's jobs
      cannot run because you claimed all the memory for your job.  Also, Slurm
      will lower the priority of your future jobs, because it tries to share
      resources (including memory) fairly.

- **What happens if I always reserve way more RAM than I need? At least my jobs
  will always run...**

    Short answer: you'll shoot yourself in the foot: your job won't start,
    and/or Slurm will let your jobs wait in the queue longer.

    Long answer 1: if you request more memory than the nodes have available,
    Slurm will conclude that your job cannot start, because it cannot offer you
    the amount of memory you requested.

    Long answer 2: whenever Slurm can start a new job, it must decide which job
    from the queue it will take: yours, or that of another user?  To this end
    Slurm calculates all queued jobs' priorities based on the historical
    resource requests (including memory) of their respective owners.  If you
    have recently requested more resources than the average user, your priority
    will drop below that of the average user, which ensures all users get to
    fairly share the cluster.

- **Does --mem-per-gpu allocate GPU VRAM?**

    No. It allocates *system RAM*, not VRAM.

- **Can I use both `--mem` and `--mem-per-cpu`?**

    No. Slurm will error if both are provided; use one or the other.

**Remember:** Always request only what you need. Overestimating memory reduces overall cluster efficiency. Underestimating may cause job failures.
