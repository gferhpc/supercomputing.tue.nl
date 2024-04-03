---
Title: ANTs
tags: [Software, Module]
---

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

