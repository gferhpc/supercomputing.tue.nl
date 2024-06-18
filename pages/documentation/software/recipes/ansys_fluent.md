---
title: Ansys Fluent
tags: [Software, Module]
---

[ANSYS Fluent](https://www.ansys.com/products/fluids/ansys-fluent){:target="_blank"} is the industry-leading fluid simulation software known for its advanced physics modeling capabilities and industry leading accuracy

![ANSYS Fluent in Umbrella On Demdand](ansys-fluent-ood.png){: align=right style="height:150px"}


## Using Application interactive (Graphical User Interface)

Use your browser to connect to [Umbrella On Demand](https://hpc.tue.nl){:target="_blank"}

## Using Application in SLURM batch jobs (Command Line Interface)

### Test ANSYS Fluent

Load the module(s)

```shell 
[user@umbrella]$ module purge
[user@umbrella]$ module load foss/2023a # or intel/2023a for -mpi=intel)
[user@umbrella]$ module load ANSYS/2023R2
```

Check ANSYS Fluent:

```shell 
[user@umbrella]$ fluent 3ddp -g -t2 -mpitest -mpi=openmpi

FLUENT MPI test started ... 

Ping pong latency test ...
ping..pong..latency(usec)...count..host
-------------------------------------------------------------
0.....1.....0.607091........10000..0:tue-login002.icts.tue.nl
1.....0.....0.602129........10000..1:tue-login002.icts.tue.nl

Ping pong bandwidth test ...
ping..pong..bandwidth(MB)...count.msg-size(MB)..host
-------------------------------------------------------------
0.....1.....3777.73.........10....4.............0:tue-login002.icts.tue.nl
1.....0.....3769.36.........10....4.............1:tue-login002.icts.tue.nl

Global reduction test ...
MPI-function...time-per-msg(usec)..count...total-time(sec)..
-------------------------------------------------------------
Bcast..........0.248226............5000....0.00124113.......
Reduce.........0.263078............5000....0.00131539.......
Barier.........0.616867............5000....0.00308433.......

FLUENT MPI test done.

```

### ANSYS Fluent SLURM sbatch jobscript example using OpenMPI

```shell
#!/bin/bash
#
#SBATCH --job-name=test_ansys
#SBATCH --error=test_ansys-%j.log
#SBATCH --partition=tue.default.q
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=8
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=2gb
#SBATCH --time=00:05:00

module purge
module load foss/2023a
module load ANSYS/2023R2

fluent 3ddp -g -t${SLURM_NTASKS} -mpitest -mpi=openmpi
```
