---
title: Matlab
---

To use Matlab, simply load the module. You do however need to pass some
parameters to run a script headless.

<div class="toccolours mw-collapsible mw-collapsed">
<div style="font-weight: bold; line-height: 1.6;">

`matlab.cmd`

</div>

    #!/usr/bin/bash
    #SBATCH --nodes=1
    #SBATCH --exclusive
    #SBATCH --partition=your.partition.q
    #SBATCH --output=slurm-%j.out
    #SBATCH --time=00:01:00

    module load matlab/current
    matlab -nodisplay -nojvm -nosplash -r "run('main.m'), quit"
    module unload matlab

</div>
<div class="toccolours mw-collapsible mw-collapsed">
<div style="font-weight: bold; line-height: 1.6;">

`main.m`

</div>

    fprintf('Hello, world!\n')

</div>

Run as `sbatch matlab.cmd`. You will notice the script reserves a full
compute node to run the Matlab script. This is because it does not seem
to be possible currently to restrict the number of cores Matlab will
use.
