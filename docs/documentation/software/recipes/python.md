---
title: Python
tags: [Software, Module]
---

This tutorial assumes you've read all previous
[tutorials](/Novice_information#Tutorials "wikilink"). So, please open a
terminal and log in to the cluster.

To open an interactive Python session, simply type `python3`. If you
then type in `print("This is clearly working")`, the text will appear in
the output of this line. Exit the session by typing `exit()` or press
\`Ctrl + D\`.

If you want to run a script (a `*.py` file), you must first
create/upload the `*.py` file. Open a text editor and write your own
Python script, or use this dummy example:

`#!/usr/bin/env python3`
`#SBATCH --partition=tue.test.q`
`#SBATCH --output=openme.out`

`print("This is clearly working") `

Save it as `test.py`. Then use, e.g., Command Prompt to transfer this
file to the cluster by typing in:

`scp test.py `<yourid>`@hpc.tue.nl:myjob/`

You could now run the script on the login node by typing the command
`python3 test.py`. This runs your script on Python 3.6.1. You could also
choose to run it on Python 2.7.5 by changing it into `python2 test.py`.

**However**, the login node of the cluster is not meant to run heavy
calculations and your job will be terminated when it takes too much
resources (CPU, memory, time). To properly
[schedule](/Scheduling_calculation_jobs_(Slurm) "wikilink") the job like
we did [before](/Submit_a_job_for_the_first_time "wikilink"), you have
to run

`sbatch test.py`

Once the job completes, you will see that a file `openme.out` has been
created which contains `This is clearly working` as expected.