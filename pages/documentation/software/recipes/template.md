---
draft: true
title: Application
tags: [Software, Module]
---

[Application](URL){:target="_blank"} Small Description

![Application in Umbrella On Demdand](application-ood.png){: align=right style="height:150px"}

## Using Application interactive<br>(Graphical User Interface)

Use your browser to connect to [Umbrella On Demand](https://hpc.tue.nl){:target="_blank"}

## Using Application in SLURM batch jobs<br>(Command Line Interface)

### Test Application

Load the modules

``` shell
[user@umbrella]$ module purge
[user@umbrella]$ module load Application/
```
Check commandline version of Application
```shell
[user@umbrella]$ Application --version
```

### Application SLURM sbatch jobscript example using Shared Memory

```slurm
#!/bin/bash
#SBATCH --job-name=test_application
#SBATCH --output=test_application-%j.log
#SBATCH --partition=tue.default.q
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem-per-cpu=2gb
#SBATCH --time=00:05:00

module purge
module load Application

cd $HOME/Jobs/Application
```

