---
title: CP2K
tags: [Software, Module]
---

[CP2K](https://www.cp2k.org/) is a quantum chemistry and solid state physics software package that can perform atomistic simulations of solid state, liquid, molecular, periodic, material, crystal, and biological systems.

## CP2K jobscript example 


``` 
#!/bin/bash
#SBATCH --job-name=test_cp2k
#SBATCH --output=test_cp2k-%j.log
#SBATCH --partition=tue.default.q
#SBATCH --nodes=1
#SBATCH --ntasks=2
#SBATCH --cpus-per-task=4
#SBATCH --mem-per-cpu=2gb
#SBATCH --time=00:05:00

module purge
module load CP2K/2023.1-foss-2023a

cd $HOME/Jobs/CP2K

mpirun cp2k.popt H2O-32.inp
```
