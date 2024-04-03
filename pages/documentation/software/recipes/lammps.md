---
title: LAMMPS
tags: [Software, Module]
---

[LAMMPS](https://www.lammps.org/){:target="_blank"} (Molecular Dynamics Simulator) is a classical molecular dynamics code with a focus on materials modeling. It's an acronym for Large-scale Atomic/Molecular Massively Parallel Simulator.

## LAMMPS MPI and Threaded jobscript example 

```shell
#!/bin/bash
#SBATCH --job-name=test_lammps
#SBATCH --output=test_lammps-%j.log
#SBATCH --partition=tue.default.q
#SBATCH --nodes=1
#SBATCH --ntasks=4
#SBATCH --cpus-per-task=2
#SBATCH --mem-per-cpu=2gb
#SBATCH --time=00:05:00

module purge
module load LAMMPS/23Jun2022-foss-2022a-kokkos

cd $HOME/Jobs/LAMMPS

export OMP_NUM_THREADS=${SLURM_CPUS_PER_TASK}

mpirun lmp < in.friction
```