---
tags: [Software, Module]
---
# ANTs

Advanced Normalization Tools

First, load the `cmake` module for a newer version of this software by
typing `module load cmake`.

In the [ANTs page](https://stnava.github.io/ANTs/), choose to build it
from source-code and follow the instructions provided there.

*Or try this*:

ANTs (https://github.com/ANTsX/ANTs) is available as an experimental
module build using easybuild (https://easybuild.io/).

To get access to the module fisrt load the module NewBuild/AMD then load
the ANTs module.

An example slurm batch script:

<div class="toccolours mw-collapsible mw-collapsed">
<div style="font-weight: bold; line-height: 1.6;">

`ants_example.sbatch`

</div>

    #!/bin/bash
    #SBATCH --job-name=ants_example
    #SBATCH --partition=tue.default.q
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=4
    #SBATCH --mem-per-cpu=2gb
    #SBATCH --output=slurm-%j.out
    #SBATCH --time=01:00:00

    cd $HOME/Jobs/ANTs
    module purge
    module load slurm
    module load NewBuild/AMD
    module load ANTs
    antsRegistrationSyNQuick.sh -d 2 -f data/r16slice.jpg -m data/r64slice.jpg -t r -o ./output/rigid

</div>

