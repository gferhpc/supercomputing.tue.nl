---
tags: [Software, Module]
---
# ANTs

[ANTs](http://stnava.github.io/ANTs/) ( Advanced Normalization Tools) extracts information 
from complex datasets that include imaging. 
ANTs is useful for managing, interpreting and visualizing multidimensional data.

## ANTs jobscript example 

```shell
#!/bin/bash
#SBATCH --job-name=test_ants
#SBATCH --output=test_ants-%j.log
#SBATCH --partition=tue.default.q
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem-per-cpu=2gb
#SBATCH --time=00:05:00

module purge
module load ANTs/2.5.1-foss-2023a

cd $HOME/Jobs/ANTs

antsRegistrationSyNQuick.sh -d 2 -f data/r16slice.jpg -m data/r64slice.jpg -t r -o ./output/rigid
 
```


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

