---
date: 2025-06-23
authors: [ e.loomeijer ]
type: kb
slug: "7"
tags: [ "Umbrella", "Knowledge Base", "Slurm" ]
categories: [ "Slurm", "Umbrella" ]
---

# Maximum run time for batch jobs

All jobs submitted **without a specified maximum run time** will be automatically **limited to 1 hour** (`01:00:00`). This new policy is designed to prevent “runaway” jobs and improve scheduling efficiency across the cluster.

## How to specify (or increase) maximum run time

If your job needs more than 1 hour, **explicitly set the maximum run time** in your job script.
To do this, add the following line to your script, replacing `<time>` with your estimated need:

```bash
#SBATCH --time=<time>
```

You can specify the time in either **hours**, **minutes**, and **seconds** (`hh:mm:ss`), or include **days** (`days-hours:minutes:seconds`).

### Examples:

- **3 hours and 30 minutes:**
  ```bash
  #SBATCH --time=03:30:00
  ```

- **1 day, 2 hours, and 15 minutes:**
  ```bash
  #SBATCH --time=1-02:15:00
  ```

## Troubleshooting

There are a few ways to see if your job reached its time limit:

- Check Slurm's job output log.  (Default: `slurm-nnnn.out`, otherwise whatever
  you specified with `--output` or `--error`.)  Running out of time is
  indicated as follows:
  ```
  slurmstepd-...: error: *** JOB 3161915 ON ... CANCELLED AT 2025-07-08T15:13:52 DUE TO TIME LIMIT ***
  ```
  An overview of your job's state is also shown at the end of this file.

- Check Slurm's accounting info.  Run `sacct -j <job_id>`.  If `State` is
  `TIMEOUT`, your job reached its time limit and was therefore terminated.
  For your convenience, the output of the `sacct` command is also made at the
  end of your job's output log.

## Best practices

- **Always specify the run time in your job scripts**

    This ensures that your job has enough time to complete, and helps the scheduler optimize cluster usage.

- **How to estimate**

    If unsure, slightly overestimate your job's run time—but avoid excessively long requests, as these can delay your job's start time.

## FAQ

- **What happens if I don’t specify the --time option?**

    Your job will be allowed to run for one hour, after which it will be
    terminated.

- **What happens if I ask for too little time for my job?**

    Your job will run until the time limit, and will then be terminated.

- **What happens if I ask for too much time for my job?**

    A number of things can happen:

    - If you ask for more time than the partition allows, your job will not
      start.
    - Your job will start and will run to completion, but it may take longer
      than for it too start.  Slurm tries to find holes in its schedule in
      which it can fit jobs.  Longer jobs are more difficult to find holes for,
      so these may take longer to start.
