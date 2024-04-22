---
title: AMS
tags: [Software, Module]
---
The [Amsterdam Modeling Suite](https://www.scm.com){:target=_blank} is used by academic and
industrial researchers in all areas of chemistry, materials science, and
engineering.

## AMS OpenMPI jobscript example

```shell
#!/bin/bash

#SBATCH --job-name=test_ams
#SBATCH --output=test_ams-%j.out 
#SBATCH --error=test_ams-%j.err
#SBATCH --partition=tue.default.q
#SBATCH --nodes=1
#SBATCH --ntasks=16
#SBATCH --mem-per-cpu=2gb
#SBATCH --time=0-00:05:00

module purge
module load foss/2023a
module load AMS/2023.105

<AMS CODE HERE>
```
On some nodes, AMS is not running due to the processor type. Adding the following option the the AMS startup command might help:
```shell
-C "amd|haswell|cascadelake|broadwell"
```
