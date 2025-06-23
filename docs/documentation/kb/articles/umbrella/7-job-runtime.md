---
date: 2025-06-23
authors: [ e.loomeijer ]
type: kb
slug: "7"
tags: [ "Umbrella", "Knowledge Base", "Slurm" ]
categories: [ "Slurm", "Umbrella" ]
draft: True
---

# Maximum Run Time for Batch Jobs

All jobs submitted **without a specified maximum run time** will be automatically **limited to 1 hour** (`01:00:00`). This new policy is designed to prevent “runaway” jobs and improve scheduling efficiency across the cluster.

## How to Specify (or Increase) Maximum Run Time

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

## Best Practices

- **Always specify the run time in your job scripts**

    This ensures that your job has enough time to complete, and helps the scheduler optimize cluster usage.

- **How to estimate**

    If unsure, slightly overestimate your job's run time—but avoid excessively long requests, as these can delay your job’s start time.
