---
draft: false 
date: 2023-02-21
categories: [Umbrella HPC Cluster]
tags: [HPC]
authors: [a.van.hoof@tue.nl, e.loomeijer@tue.nl]
---

# 2023-Q1 Umbrella HPC Cluster maintenance completed

Cluster maintenance completed. For more details click on the "Continue reading" link.

<!-- more -->

### GPU reservation/allocation mandatory

`--gres=gpu:1`

### New default module gcc/8.2.0 (gcc/7.2.0 no longer available)

Try to load foss/2022a toolchain which includes a working version of gcc
with a more recent version:

> $ gcc --version
>
> gcc (GCC) 8.2.0
>
> $ module purge
>
> $ module load slurm NewBuild/AMD foss/2022a
>
> $ gcc --version
>
> gcc (GCC) 11.3.0


===SSH to a node only when the user has a job running on that node.===
Either use srun or salloc from a login node to run a job on a node, then
open a second SSH session to the node.