---
title: LAMMPS
---

LAMMPS Molecular Dynamics Simulator

LAMMPS (https://www.lammps.org/) is available as an experimental module
build using easybuild (https://easybuild.io/)

To get access to the module fisrt load the module NewBuild/AMD then load
the LAMMPS module.

An example slurm batch script:

<div class="toccolours mw-collapsible mw-collapsed">
<div style="font-weight: bold; line-height: 1.6;">

`lammps_example.sbatch`

</div>

    #!/bin/bash
    #SBATCH --job-name=friction
    #SBATCH --partition=tue.default.q
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=4
    #SBATCH --mem-per-cpu=2gb
    #SBATCH --output=slurm-%j.out
    #SBATCH --time=00:00:05

    cd $HOME/Jobs/LAMMPS
    module load NewBuild/AMD
    module load LAMMPS
    mpirun lmp < in.friction

</div>
