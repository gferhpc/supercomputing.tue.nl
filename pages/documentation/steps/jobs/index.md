---
title: 5. Submit Jobs
tags: [SLURM]
---
# Submit Jobs

To run any significant program or workload on a supercomputer, generally a Batch-Scheduler is employed. Alongside the above-mentioned Login Nodes there are usually far more Backend Nodes in the system (computers exclusively reserved for computing, to which you cannot connect directly, also referred to as "batch system"). A program called Batch-scheduler decides who gets how many of those compute resources for which amount of time. Please use the Backend Nodes for everything which is not a simple small test and only runs for a few minutes., otherwise you will block the Login Nodes for everybody when you run your calculations there. These Backend Nodes make up more than 98% of a supercomputer and can only be accessed via the scheduler.

When you log into a supercomputer, you can run commands on the Login Nodes interactively. You type, you hit return, the command gets executed. Schedulers work differently. You submit a series of commands (in form of a file) and tell it, how much resources it will approximately need in terms of:

time: If the specified time runs out, before your application finishes and exits, it will be terminated by the scheduler.
compute resources: how many cpus ('calculation thingies'), sockets ('cpu-houses') and nodes ('computers')
memory resources: how much RAM ('very fast memory, similar to the few books you have at home')
This combination of specified commands and required resources is commonly referred to as a "(batch) job".

If later compute resources become free, which match the requirements of your application, the scheduler will run your specified commands on the requested hardware. This is usually delayed (sometimes you have to wait a day or two) and not instant, because other users are currently using the compute resources and you have to wait until their program runs finish. Furthermore you cannot change the series of commands after submitting, but just terminate the job and submit a new one in case of an error.

The file specifying this series of commands and the required resources is called a jobscript. Its format and syntax depends on the installed scheduler. When you have this jobscript ready with the help of jobscript-examples, colleagues or your local support, you can submit it to the respective scheduler of your facility. The scheduler then waits until a set of nodes (computers) are free and later allocates those to execute your job as soon as possible. Sometimes there is (an optional) email notification, which is send when your job starts execution/finished running.

Be aware that your specified requirements have to fit within the boundaries of the system of your facility. If you ask for more than there is, chances are, the scheduler will accept your job and wait until missing hardware is bought and installed - although this will not happen in 99.9% of cases. Information over the available hardware can be found in the overview of the Gauss Allianz or the documentation of the different sites. You can find more information about parallelizing programs here. Also there is an overview of the schedulers used at the different sites.


The HPC Umbrella Cluster uses SLURM (Simple Linux Utility for Resource
Management) as its scheduler. SLURM uses the term partition to describe
a part of the Cluster, a partition groups a number of nodes with the
same characteristics like the number of CPUs per node, the CPU/GPU type
and Memory size. Note that nodes can be part of more than 1 partition.
These partitions are also named queues and those names are often used
interchangeable. Access to partitions is given to a group or groups.
Accounts on the HPC Umbrella Cluster can be a member of 1 or more
groups. Each partition or queue can have different constrains such as
the maximum wall time (how long a job can run) the maximum nodes per
job.

After logging in on the login node:

Checking access to partition/queues: **sinfo**

Checking group membership: **id**

## Per-partition constraints

The table below lists all configured partitions, and per partition also
lists the following:

-   constraints on maximum job wall-time (the maximum time a job can
    run);
-   constraints on maximum number of nodes per job;
-   priority tier of jobs in this partition; and
-   user groups that can use this partition.

Note that if you're not in one of the groups that is allowed to use a
certain partition, the scheduler will not accept your job and instead
give the following error:

    sbatch: error: Batch job submission failed: User's group not permitted to use this partition

| Partition         | Max wall-time[1] | Max nodes/job[2] | PriorityTier[3] | Allowed groups                 |
|-------------------|------------------|------------------|-----------------|--------------------------------|
| be.gpuresearch.q  | UNLIMITED        | UNLIMITED        | 1               | be-research                    |
| be.gpustudent.q   | UNLIMITED        | UNLIMITED        | 1               | be-student                     |
| be.research.q     | UNLIMITED        | UNLIMITED        | 1               | be-research                    |
| be.student.q      | UNLIMITED        | UNLIMITED        | 1               | be-student                     |
| bme.gpuresearch.q | UNLIMITED        | UNLIMITED        | 1               | bme-research                   |
| bme.gpustudent.q  | 7-00:00:00       | UNLIMITED        | 1               | bme-student                    |
| chem.6ema08.q     | 5-00:00:00       | UNLIMITED        | 2               |                                |
| chem.default.q    | 5-00:00:00       | UNLIMITED        | 1               | chem,chem-guest                |
| chem.gpu.q        | UNLIMITED        | UNLIMITED        | 1               | chem,chem-guest                |
| chem.longterm.q   | 14-00:00:00      | UNLIMITED        | 2               | chem,chem-guest                |
| chem.smm01.q      | UNLIMITED        | UNLIMITED        | 1               | chem-smm                       |
| chem.smm02.q      | UNLIMITED        | UNLIMITED        | 1               | chem-smm                       |
| elec.default.q    | UNLIMITED        | UNLIMITED        | 1               | elec                           |
| elec-em.gpu.q     | UNLIMITED        | UNLIMITED        | 1               | elec-em,elec-em-guest          |
| elec.gpu-es02.q   | UNLIMITED        | UNLIMITED        | 1               | elec-es                        |
| elec.gpu.q        | UNLIMITED        | UNLIMITED        | 1               | elec-es,elec-5LIL0             |
| elec-phi.gpu.q    | UNLIMITED        | UNLIMITED        | 1               | elec-phi                       |
| id.fe.q           | 5-00:00:00       | UNLIMITED        | 1               | id-fe                          |
| mcs.default.q     | 7-00:00:00       | 3                | 1               | mcs                            |
| mcs.gpu.q         | UNLIMITED        | UNLIMITED        | 1               | mcs                            |
| mech.cm.q         | 5-00:00:00       | UNLIMITED        | 1               | mech-cm,tue-support            |
| mech.pf.q         | UNLIMITED        | UNLIMITED        | 1               | mech-pf,mech-et                |
| mech.student.q    | 5-00:00:00       | UNLIMITED        | 1               | mech-student                   |
| phys.and.q        | UNLIMITED        | UNLIMITED        | 1               | phys-and                       |
| phys.bigmem.q     | UNLIMITED        | UNLIMITED        | 1               | phys                           |
| phys.default.q    | UNLIMITED        | UNLIMITED        | 1               | phys                           |
| phys.edu.q        | UNLIMITED        | UNLIMITED        | 1               | phys-3mq110,phys-ccer          |
| phys.gpu.q        | UNLIMITED        | UNLIMITED        | 1               | phys                           |
| phys.psn.q        | UNLIMITED        | UNLIMITED        | 1               | phys-psn                       |
| phys.simbeyond.q  | 5-00:00:00       | 1                | 1               | phys                           |
| tue.default.q     | 7-00:00:00       | 2                | 1               | elec,tue,ieis,tue-hpc,chem,bme |

Partition/Queue constraints on TU/e HPC Umbrella Cluster

<references />

[1] Maximum time a job can run (Days-Hours:Minutes:Seconds). The job
will be killed if **Max wall-time** is reached.

[2] Maximum number of nodes a job can allocate

[3] A higher priority schedules a job sooner, applicable when node(s)
are in more than one partition

## Check status

Check which queues are available to you and their status by using:

`$ sinfo`

The following table summarizes the main possible states and their
meaning:

| Code      | State     | Meaning                                                                                                                                     |
|-----------|-----------|---------------------------------------------------------------------------------------------------------------------------------------------|
| alloc     | ALLOCATED | The node has been assigned to one or more jobs                                                                                              |
| drain     | DRAINED   | The node Has been declared unavailable by the system administrator                                                                          |
| drng      | DRAINING  | The node is currently running a job, but it will not be allocated to additional jobs, changing to DRAINED when the last job on it completes |
| idle      | IDLE      | The node is not allocated to any jobs and is available for use                                                                              |
| mix       | MIXED     | The node has some of its CPUs ALLOCATED while others are IDLE                                                                               |
| <state>\* | \*        | The asterisk after a state code means that the node is not responding                                                                       |

Slurm sinfo states

## Submit a job

Check the tutorial about [submitting a
job](/Scheduling_calculation_jobs_(Slurm) "wikilink") using Slurm for
scripts for single and multi core jobs and the step-by-step procedure.

## Job arrays

Slurm has a feature called job arrays which is very useful if you need
to run many similar simulations across a large parameter space. E.g.
using:

`$ sbatch --array=1-5 myjob.run`

you will get 5 actual jobs running. Inside each job script, the array
index can be found as the variable `$SLURM_ARRAY_TASK_ID`. If you need
to do very large job arrays, you may ease your load on the cluster by
specifying a maximum simultaneously active number of jobs from the
array, e.g. to run 1000 jobs such that no more than 100 run
simultaneously:

`$ sbatch --array=1-1000%100 myjob.run`

## Job arrays with bash loops

Array jobs are convenient for running lots of tasks, but if each task is
short, they quickly become inefficient, taking more time to schedule
than they spend doing any work and bogging down the scheduler for all
users. A combination of job arrays and bash loops is a better solution
for this kind of problems.

`#!/bin/bash                                                                                                                                                                                    `
`#SBATCH --partition=partition_name       # Partition name`
`#SBATCH --job-name=mega_array            # Job name`
`#SBATCH --mail-type=ALL                  # Mail events (NONE, BEGIN, END, FAIL, ALL)`
`#SBATCH --mail-user=Your_email@tue.nl    # Where to send mail  `
`#SBATCH --nodes=1                        # Use one node`
`#SBATCH --ntasks=1                       # Run a single task                                                                                                                                                `
`#SBATCH --mem-per-cpu=2gb                # Memory per processor`
`#SBATCH --time=06:00:00                  # Time limit hrs:min:sec`
`#SBATCH --output=array_%A-%a.out         # Standard output and error log`
`#SBATCH --array=1-5                      # Array range`
`# This is an example script that combines array tasks with`
`# bash loops to process many short runs. Array jobs are convenient`
`# for running lots of tasks, but if each task is short, they`
`# quickly become inefficient, taking more time to schedule than`
`# they spend doing any work and bogging down the scheduler for`
`# all users. `
`pwd; hostname; date`

`#Set the number of runs that each SLURM task should do`
`PER_TASK=10000`

`# Calculate the starting and ending values for this task based`
`# on the SLURM task and the number of runs per task.`
`START_NUM=$(( ($SLURM_ARRAY_TASK_ID - 1) * $PER_TASK + 1 ))`
`END_NUM=$(( $SLURM_ARRAY_TASK_ID * $PER_TASK ))`

`# Print the task and run range`
`echo This is task $SLURM_ARRAY_TASK_ID, which will do runs $START_NUM to $END_NUM`

`# Run the loop of runs for this task.`
`for (( run=$START_NUM; run<=END_NUM; run++ )); do`
`  echo This is SLURM task $SLURM_ARRAY_TASK_ID, run number $run`
`  #Do your stuff here`
`done`

`date`

Source: [University of Florida instructional
video](https://mediasite.video.ufl.edu/Mediasite/Play/5bbd7cfb22b2416bbb0541e79875def51d)

## Information on jobs

List all current jobs for a user:

`squeue -u `<username>

List all pending jobs for a user:

`squeue -u `<username>` -t RUNNING`

List priority order of jobs for the current user (you) in a given
partition:

`showq-slurm -o -u -q `<partition>

List detailed information for a job (useful for troubleshooting):

`scontrol show jobid -dd `<jobid>

List status info for a currently running job:

`sstat --format=AveCPU,AvePages,AveRSS,AveVMSize,JobID -j `<jobid>` --allsteps`

Once your job has completed, you can get additional information that was
not available during the run. This includes run time, memory used, etc.

To get statistics on completed jobs by jobID:

`sacct -j `<jobid>` --format=JobID,JobName,MaxRSS,Elapsed`

To view the same information for all jobs of a user:

`sacct -u `<username>` --format=JobID,JobName,MaxRSS,Elapsed`

If you are curious how many cpu cores every user is currently running on
and/or waiting for, see [usercores script](/usercores_script "wikilink")

## Controling jobs

To cancel one job:

`scancel `<jobid>

To cancel all the jobs for a user:

`scancel -u `<username>

To cancel one or more jobs by name:

`scancel --name `<myJobName>

To cancel an indexed job in a job array:

`scancel `<jobid>`_`<index>

To hold a particular job from being scheduled:

`scontrol hold `<jobid>

To release a particular job to be scheduled:

`scontrol release `<jobid>

To requeue (cancel and rerun) a particular job:

`scontrol requeue `<jobid>

To run a computing job on the cluster, it has to be submitted to the
queueing system. This queueing system decides which jobs will run when
and on which nodes/processors based on certain policies that are
designed to make the usage of the cluster as fair as possible for
everyone in an efficient way. The most convenient way to submit a job is
to use SLURM (Simple Linux Utility for Resource Management), which is
the queueing system used in the 2018+ Umbrella HPC Cluster environment.

This page describes how to run computation jobs using Slurm. For
in-depth information on submitting jobs with Slurm, see the online
documentation provided at the [Slurm
website](https://slurm.schedmd.com/sbatch.html), or their [Slurm Cheat
Sheet (PDF)](https://slurm.schedmd.com/pdfs/summary.pdf). For a quick
start, see below.

## Slurm scripts

A Slurm script is simply a Unix-style shell script with some additional
comments the sbatch-program can parse in order to determine information
about the job, e.g., the number of required processors. This page
contains a few example Slurm scripts.

### Script for a single core job

Below is an example Slurm script that attempts to run the program
"my_program" using a single core, assuming the program is located in the
same directory as the Slurm script:

`#!/usr/bin/bash`
`#SBATCH --nodes=1`
`#SBATCH --ntasks=1`
`#SBATCH --partition=tue.default.q`
`#SBATCH --error=slurm-%j.err`
`#SBATCH --output=slurm-%j.out`
`#SBATCH --time=24:00:00`
` `
`./my_program`

We'll go through the lines one by one:

-   **#!/usr/bin/bash** tells the GNU/Linux shell that the script should
    be run by bash.

<!-- -->

-   **#SBATCH --nodes=** is the first comment intended for Slurm to
    interpret: It tells Slurm (the queueing system) that this job wants
    to run on 1 node.

<!-- -->

-   **#SBATCH --ntasks=1** tells Slurm that this job wants a total of 1
    tasks. On our cluster, this means 1 core of a processor (in PBS
    langauge this would be called 1 processor).

<!-- -->

-   **#SBATCH --partition=tue.test.q** tells Slurm the partition it
    should use (this used to be called "queue" in the old system).
    Select a partition based on the [technical
    specifications](/technical_specifications "wikilink") of the cluster
    you are using.

<!-- -->

-   **#SBATCH --error=slurm-%j.err** tells Slurm to write standard error
    messages (errors and warnings from the job itself) to a file named
    "slurm-<jobid>.err". If this line is omitted, the standard error
    stream is merged with the standard output into a single file
    "slurm-<jobid>.out".

<!-- -->

-   **#SBATCH --output=slurm-%j.out** tells Slurm to write standard
    output of the job to a file named "slurm-<jobid>.out". This is the
    default behavior (included for reference reasons).

<!-- -->

-   **#SBATCH --time=24:00:00** tells Slurm to respect a "walltime"
    limit; limiting the job to be run for a maximum of 1 day (24 hours).
    Acceptable time formats include "minutes", "minutes:seconds",
    "hours:minutes:seconds", "days-hours", "days-hours:minutes" and
    "days-hours:minutes:seconds". If the job runs longer than the
    specified walltime limit, it will be terminated by Slurm, so make
    sure it is long enough to make sure your job finishes in that
    walltime limit. Note that jobs with a low walltime limit might get
    extra priority in the queue, so it is in *your* interest to specify
    a walltime limit that is realistic for your jobs. Finally, note that
    you specify a walltime limit rather than a cpu time limit, which is
    an important distinction for multi-core jobs.

<!-- -->

-   **./my_program** runs the program called "my_program" that is
    located in the current directory, which, in our configuration, is
    the directory from which the script was submitted. Unlike in the old
    PBS system, there is no need to change directories here for this to
    work.

*NFO: \*Normally bash-script lines marked with a \`#\` character are
considered a comment only that do not get executed when the script is
ran from the cli, however Slurm explicitly DOES use these specific "bash
comments" and interprets them as INSTRUCTIONS instead!*

### Script for a multi core job

Suppose you want to run another program, "parallel_program", which
supports parallel computation via MPI using multiple processor cores,
and you want to run it using 16 cores. This can be achieved with some
minor modifications to the single core script. Below is an example,
where the differences are highlighted in bold:

`#!/bin/bash`
`#SBATCH --nodes=1`
`#SBATCH --ntasks=16`
`#SBATCH --partition=tue.default.q`
`#SBATCH --error=slurm-%j.err`
`#SBATCH --output=slurm-%j.out`
`#SBATCH --time=24:00:00`

`module load openmpi`
`mpirun ./my_program`

The essential changes are in lines:

-   **#SBATCH --nodes=1** In order to properly run in parallel on 16
    cores, you need to request 16 processor cores. At the time of
    writing, the maximum number of cores a node can have is 20, but most
    nodes only have 16 processor cores. Some nodes have only 8 cores, so
    if the only available nodes are of that type, you would also need to
    change the preceding line to --nodes=2. Unlike in PBS, the number
    requested with --ntasks is the TOTAL number of tasks, not the number
    of tasks/processors per node.

<!-- -->

-   **module load openmpi** In order to run MPI programs in parallel,
    you need to load a module that provides MPI support. If you compiled
    the software yourself, the common thing to do at this point is to
    load the same module that you needed to load when you were compiling
    the code. In this example, I am assuming the openmpi module was
    serving this purpose.

<!-- -->

-   **mpirun ./my_program**The actual start of parallel execution
    requires starting your program via the "mpirun" program. Unlike in
    the old PBS setup, the Open MPI version of mpirun that we have on
    the 2018+ cluster figures out automatically which nodes have been
    assigned to your job, and how many tasks each node is getting.
    Hence, the only arguments to mpirun should be the program you want
    to run, followed by any arguments to the program you want to run.

***NB: If the requested number of cores are not available, your job
enters the queue. In the waiting queue, the more cores and nodes you
claim, the longer you have to wait for it to start. Furthermore, others
will have to wait for your job to start before their jobs in the queue
start, so it is in everyone's interest to not request more resources
than needed.***

## Save a script on the cluster

In order to save the script, or any file, to the cluster, it is
recommended to create a subdirectory in your [home
directory](/Connecting_to_the_cluster#Personal_homedir "wikilink"). Use
command

`$ ls`

to see what directories already exist. If you do this for the first
time, it is most likely empty. To create a directory, called 'myjob',
you can use the following command:

`$ mkdir myjob`

To save the script in this directory, go to this directory using
command:

`$ cd myjob`

Then open a text editor in the terminal, using, e.g., command: `nano` ,
and type in the script. Save it with 'ctrl + O'. You can also choose to
use a GUI, like WinSCP, to save your scripts to the cluster.

## Submitting a script

To submit the script, you have to save this script somewhere on the
cluster (recommended is a subdirectory of your [home
directory](/Connecting_to_the_cluster#Personal_homedir "wikilink")).
Assuming you named it "myjob.run", to submit it, simply run:

`$ sbatch myjob.run`

in the same directory as you saved the script. Upon submitting this
script, the system will check to see if there are nodes available that
have at least 1 idle processor, and if so, it will dispatch this script
to that node. If not, the job will enter the queue system and will
accumulate priority depending on various things, including the time it
was in the queue, the walltime limit, and possibly your recent usage on
the cluster.

## Selecting a partition (queue) and/or specific features

The `--partition` option takes care of selecting a queue (partition in
Slurm terminology). Select a partition based on the [technical
specifications](/technical_specifications "wikilink") of the cluster you
are using.

In case there are different types of nodes within the partition you
select, and you require specific hardware to run your job on, you can
further constrain where your job can run using *features*. First, query
which features the nodes have. For example:

`$ sinfo -o "%16N  %16f  %8G" -p mcs.gpu.q   `
`NODELIST          AVAIL_FEATURES    GRES     `
`mcs-gpuA001       tesla,v100        gpu:2    `
`mcs-gpuB001       gforce,2080ti     gpu:8`

To use the V100 GPU in your Slurm batch script, you can now add the
parameter `--constraint=v100`. Refer to the
[documentation](https://slurm.schedmd.com/sbatch.html) for details and
other options, such as combining features.

Note that to actually see and use the GPU(s), you will need to load the
CUDA toolkit module (or other relevant software) by executing
`module load cuda10.2/toolkit/10.2.89` or similar in your sbatch script.

## Interactive use

In order to use a node interactively (e.g. for debugging modules or
dependencies, or simply to use it as an extension of your own computer),
you can issue the command

`srun --nodes=1 --ntasks-per-node=1 --time=01:00:00 --pty bash -i`

You can add the common SLURM modifications to your command as you would
otherwise do in the job script, for instance to select a particular
queue to run use:

`srun --nodes=1 --ntasks-per-node=1 --time=01:00:00  --partition=tue.default.q --pty bash -i`

## Troubleshooting
### Errors when trying to submit a job using `sbatch`

`sbatch: error: Batch job submission failed: Invalid account or account/partition combination specified`

You may first want to verify that your `--partition` (or `-p` for short)
parameter is set correctly. To list all partitions you have access to,
execute `sinfo`. Only partitions you have access to are listed by
default, pass the `-a` flag to list all partitions.

If you made no typo and have access to the partition you specify in your
job, check that your batch script is executable: `ls -l` should list
`-rwxr-xr-x` as the access rights for your file. You can issue
`chmod a+x `<your batch script> to make it executable.

`sbatch: error: Batch job submission failed: User's group not permitted to use this partition`

Please verify that you specified a partition you have access to (see the
above troubleshooting help).

`ImportError: No module named <script.py>`

When importing another file from the script you submitted to the hpc,
you need to add

`import sys, os`

`sys.path.append(os.getcwd())`

near the beginning of your script, as Slurm copies the submission script
to a specific location on the compute node to run it. Your Python script
will not find the modules that are in the submission directory if you do
not explicitly add it to the python path.

### Error when running pip install

When installing modules for python via pip in your home directory the
install might fail with: "Could not install packages due to an OSError:
\[Errno 28\] No space left on device"

This is mostly due to pip using /tmp which is limited to 2GB and shared
with other users, to resolve this, set the environment variable TMPDIR
to the /local filesystem (100GB+) before executing pip:

`TMPDIR=/local pip install tensorflow`