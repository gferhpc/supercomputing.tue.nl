---
tags: [Software, Module]
---
# Ansys Lumerical
Ansys Lumerical, or Ansys Optics, is an optics simulation package. This
page contains various bits of information on running Lumerical on an HPC
system.

This is tested with Lumerical 2021-R1.

## Method 1

We will make Lumerical believe it is running on a "local computer"
(which is in fact the HPC system). The approach has some benefits:

-   It is relatively easy to set up.
-   It is slightly less prone to issues with e.g. MPI.

The downsides are:

-   Parameter sweeps cannot be done in parallel; for this a tighter
    integration with the scheduler (Slurm) is needed.
-   It is probably unsafe to run multiple instances of Lumerical
    simultaneously with this approach.
-   The user must set some maximum number of threads beforehand, and
    must consistently request the same amount from the scheduler, which
    is prone to errors.

In the following we will restrict Lumerical to at most 4 threads. Any
other number of threads would work as well, but using more threads can
lead to longer waiting times in the queue.

### Workflow

This is a suggested workflow for Lumerical on the Umbrella cluster:

1.  Initial setup of Lumerical (first-time use only!)
2.  Prepare LSF file using the Lumerical GUI on the cluster
3.  Submit Lumerical job
4.  Postprocess/view results using the Lumerical GUI on the cluster

Each of these steps is detailed below. It is also possible to run
non-interactive Python jobs; this is a detailed below as well.

### Initial setup

1.  Log on to the cluster using [Open
    OnDemand](/Open_OnDemand "wikilink"), and start an interactive
    Lumerical session.
2.  Within the interactive session, click "Solvers" → "New" → "FDTD". A
    new window opens.
3.  From the "Simulation" menu, choose "Resource configuration". A new
    window opens.
4.  In the "Resource configuration" window, in the FDTD solver tab,
    delete all but one profile.
5.  Click the "Edit" button to edit the remaining profile. A new window
    opens.
6.  In the "Resource advanced options" window, make the following
    changes, and then hit OK.
    -   Job launching preset: Local Computer
    -   FDTD options:
        -   extra command line options: (empty)
        -   checkpoint directory: (empty)
        -   no default options: unchecked
        -   create log for all processes: unchecked
7.  In the "Resource configuration window", make sure the one remaining
    profile has the following values set. Values can be changed by
    double clicking the value.
    -
    -   active: true
    -   threads: 4 (or whichever number you decided on)
    -   capacity: 1
8.  Optionally, hit "Run tests". After a few seconds it should say
    "Tests completed successfully".
9.  In the Design environment tab, make the following changes:
    -   auto detect: unchecked
    -   max threads: 4 (or whichever number you decided on)
10. Hit "Save".
11. Close Lumerical.

### Prepare/postprocess with Lumerical GUI

The Lumerical GUI can be run on the cluster through [Open
OnDemand](/Open_OnDemand "wikilink").

### Submitting a Lumerical job

**It may be unsafe to run multiple Lumerical jobs simultaneously!** This
is due to the use of the "local computer" resource configuration
profile.

This is an example job script:

    #!/usr/bin/bash

    #SBATCH --ntasks=1
    #SBATCH --cpus-per-task=4   # <--- replace with desired number of threads
    #SBATCH --partition=tue.default.q    # <--- replace with your partition

    module load lumerical/2021-R1

    xvfb-run fdtd-solutions -nw -run [script.lsf]   # <--- replace with your script

The above script uses `xvfb-run` to make Lumerical believe it is
connected to a monitor.

### Submitting a Lumerical Python job

**It may be unsafe to run multiple Lumerical jobs simultaneously!** This
is due to the use of the "local computer" resource configuration
profile.

This is an example job script:

    #!/usr/bin/bash

    #SBATCH --ntasks=1
    #SBATCH --cpus-per-task=4   # <--- replace with desired number of threads
    #SBATCH --partition=tue.default.q

    module load lumerical/2021-R1

    set -e

    LUMDIR=$(dirname $(dirname $(which fdtd-solutions)))
    #export PATH="$LUMDIR/python/bin:$PATH"  # <--- uncomment to use the version of Python bundled with Lumerical
    export PYTHONPATH="$LUMDIR/api/python"

    # -u to keep stdout/stderr unbuffered
    xvfb-run python3 -u myscript.py

Also see the following websites:

-   Setting Lumerical environment variables:
    [here](https://optics.ansys.com/hc/en-us/articles/7595785040403).

## Method 2

To be done: configure Lumerical so it makes use of the cluster's MPI
system. This implies a tighter integration with the scheduler, and is
therefore less prone to user error.

## Method 3

To be done: configure Lumerical so it can submit its own jobs. This
speeds up e.g. parameter sweeps.

## Troubleshooting

### Failed to start messaging, check licenses...

This is a poorly-worded error message that *may* indicate Lumerical
cannot connect to an X11 server. Lumerical is a GUI application; even
when started with **-nw** (no window) it needs to have an X11 server
available. Only the solvers themselves do not require X11.