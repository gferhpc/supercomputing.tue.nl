---
title: Long-running jobs & job stringing
---

# Long-running jobs & job stringing

Most partitions are limited to a wall-clock time of 5 days, which means that jobs that need longer than 5 days cannot be submitted.  If you need to run a job for longer than that, there are a few options:

1. use more CPU cores, this may cause your job to run faster and finish in less time;
2. _job stringing_ (described here); or
3. contact the system administrators to get special permission.

_Job stringing_ is splitting a long-running job (> 5 days) into multiple smaller jobs (_subjobs_, < 5 days each), that are strung together, i.e. they are run one after another.  Each of the subjobs performs a part of the calculation.

To allow for job stringing, the software you're using must support the following:

* It must support checkpointing or snapshotting.  This allows one subjob to pick up where the previous left off.
* It must run for a fixed number of iterations (or for a fixed amount of time), or run until it is killed.

## Guide

The idea is to submit an array job, where each element of the array is a subjob.  It must be submitted so that:

* The number of elements is equal to or larger than the expected number of subjobs; and
* At most one element (subjob) can run at a time.

Then, if the calculation is completely finished, i.e. the remaining/unused subjobs are not needed anymore, the job script cancels the array job.  (If the number of array elements equals the expected number of subjobs, this is not needed, because the array job's end and the calculation's end will coincide.)

A rough sketch of the job script is as follows:

1. Run the calculation.
2. Check if the calculation is completely finished.
3. If it is, cancel the array job.

Again, steps #2 and #3 are not needed if the number of array elements equals the number of subjobs.

## Case #1: software with limited no. of iterations (or limited running time)

Suppose that:

* we have a wall-clock time limit of 1 minute;
* we have a calculation of which each iteration takes 25 seconds;
* the total number of iterations to be done is 8; and
* our software _can_ run a limited number of iterations per subjob (or for a limited amount of time).

Since 2 iterations is 50 seconds, which is slightly less than 1 minute, we can fit 2 iterations in one subjob and still have some slack.  It is important to have some slack, for e.g. I/O and job starting/stopping.  We decide to run our calculation as follows:

* 2 iterations per subjob; and
* 4 subjobs (thus 4 array elements).

The job script would then be:

```bash title="job-stringing-limited.job"
--8<-- "job-stringing-limited.job"
```

## Case #2: software unlimited no. of iterations

Suppose that:

* we have a wall-clock time limit of 1 minute;
* we have a calculation of which each iteration takes 25 seconds;
* the total number of iterations to be done is 8; and
* our software _cannot_ run a limited number of iterations; it runs until completely finished or until it gets killed.

Unlike in case #1, our software doesn't stop after 2 iterations.  Instead it will start a 3rd iteration, which may finish if Slurm doesn't kill the subjob in time.  (Slurm is not exact down to the second.)  As a result, we cannot really predict how many subjobs we'll need, so we'll need to check if our calculation is completely finished.

Note that if our calculation is not finished, Slurm will kill the subjob half-way, i.e. it will kill at the `bash calculation.sh` line.  The rest of the job script will not be executed.  However, if the calculation _is_ finished, `bash calculation.sh` will be done, and the job script will proceed to the next line.  The next line can then tell Slurm to cancel all remaining subjobs.

So:

```bash title="job-stringing-unlimited.job"
--8<-- "job-stringing-unlimited.job"
```

## Alternatives

The problem that cases #1 and #2 above try to solve, is to see whether or not the calculation is finished.  In case #1 we could exactly calculate how many subjobs we need, so we didn't need to check.  In case #2 we couldn't calculate how many subjobs we need, so instead we relied on _somehow_ detecting if the calculation was finished, and if so, we cancelled the remaining subjobs.  In particular, we relied on the subjob being cancelled due to over-time, or not.

There are other ways to detect if the calculation is finished:

* It may be possible to read the checkpoint file, e.g. to see if a calculation converged.
* It may be possible to read a log file or so, to see if the calculation finished.
* Maybe to software exits with a different exit code if it is finished.

These are very advanced methods, that are not detailed here.

## Example calculation

The above examples rely on a calculation `job-stringing-calculation.sh`, which can be downloaded [here](job-stringing-calculation.sh).  It isn't really a calculation: in each iteration it just sleeps for 25 seconds, and does so for at most `max_iterations` iterations.

The code does the following:

1. At the start it reads the last `iteration_counter` from the checkpoint file.
2. It makes sure the `iteration_counter` is less than `max_iterations`, and increments it by 1.
3. It makes sure the `sub_iteration` number is not 0, and decrements it by 1.
4. It sleeps 25 seconds.  (This is our "work".)
5. It saves the current `iteration_counter` to the checkpoint file.
6. It goes back to step #2.

Steps #1 and #5 are for checkpointing.  Steps #2 and 6 are really just a for loop.  The for loop is written as a while-true loop, so that it can start at any given index, which is needed for checkpointing.
