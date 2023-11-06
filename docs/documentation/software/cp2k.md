---
title: CP2K
---

Version 8.2 available as a module

```shell
module purge
module load slurm
module load CP2K
```

Slurm sbatch file:

```shell 
#!/bin/bash

#SBATCH --job-name=test_cp2k
#SBATCH --output=test_cp2k-%j.out
#SBATCH --error=test_cp2k-%j.err
#SBATCH --partition=tue.default.q
#SBATCH --ntasks=4

module purge
module load slurm
module load NewBuild/AMD CP2K
mpirun cp2k.popt H2O-32.inp
```