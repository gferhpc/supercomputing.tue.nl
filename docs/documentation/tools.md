On this page, we collect some useful tips and tricks for experienced HPC
users.

## COMSOL Multiphysics

[thumb\|Settings for cluster computing using COMSOL
locally](/File:COMSOLClusterComputingSettings.jpg "wikilink")

### Getting a license

Check the
[intranet](https://intranet.tue.nl/en/university/services/information-management-services/software/comsol-multiphysics/)
for the procedure on how to get a license for using COMSOL.

### Running simulations on the cluster

If you want to use the cluster to compute COMSOL simulations, you have
two possibilities. One is to [submit your
job](/Scheduling_calculation_jobs_(Slurm) "wikilink") similarly as you
do for other programs. Another possibility is to use the COMSOL
interface in your local computer. This short tutorial is about this
second possibility. It is focused on configuring your simulation using a
TU/e cluster. For more information, visit the [COMSOL
blog](https://www.comsol.com/blogs/how-to-run-on-clusters-from-the-comsol-desktop-environment/)
where the procedure is explained in detail.

Once you are done with building your model and specifying the physics of
your study on COMSOL, you can configure your simulation on a cluster.
Check the settings used in the figure or follow the instructions bellow.

On the *Model Builder* menu, click on *Study \#* with the left button of
your mouse and selecting *Cluster Computing* from the menu. This will
add *Cluster Computing* as an item under *Study \#*. By clicking on this
item, the settings for cluster computing are open on the right of the
*Model Builder* menu.

On the *Computer cluster settings* submenu, choose from the dropdown
menu `user controlled` in *Settings* and `SLURM` in *Scheduler type*.
Leave the next two fields, *i.e.* the fields *Scheduler type* and
*User*, empty. In the field *Queue name*, fill the queue you want to
use, *e.g.* `tue.default.q`. Choose the queue according to your
department and the information in [technical
specifications](/technical_specifications "wikilink") of the clusters.

In the same submenu, check the boxes of *Specify external COMSOL batch
directory path* and *Specify external COMSOL installation directory
path* and respectively type the paths `/home/tue/`<user> (or
`home/phys/`<user> if you belong to the Applied Physics department) and
`/cm/shared/apps/comsol/5.5/multiphysics/`.

Assuming that you are using PuTTY and that you have generated a [SSH
key](/Passwordless_login "wikilink") to log in, you can fill the
remainder fields as follows. On the *Remote and Cloud Access* submenu,
choose from the dropdown menu `user controlled` in *Settings* and
\`check the box of *Run remote*. In the dropdown menu select `SSH` in
*Remote invoke command* and `Putty` in *Remote invoke command*. In the
*SSH directory* field, browse to the directory where PuTTY is installed
and, in the SSH key file, browse to the directory where you save you
private key, select the key, and click *Open*. You do not need to fill
the fields *Forward ports* and *Port host*. As *SSH user*, fill your
cluster username.

For the *File transfer command* field, choose from the dropdown menu
`SCP`. Fill the SCP fields similarly to the SSH fields, *i.e.*, choose
PuTTY and fill the directory for the program and public key. Once again
use you cluster username in *SCP user*. In the *Remote hosts* table, add
the cluster address `hpc.tue.nl` (or `compass.phys.tue.nl` if you belong
to the Applied Physics department).

You are nearly done, before pressing the *run* button to have your
simulations calculated on the cluster, read the next sections to learn
how to select the number of cores in your calculation and to log out
your computer while a simulation is running on the cluster.

### Selecting the number of cores

By default, COMSOL uses the total amount of available cores in a
computing node. This means that, depending on the queue that you are
going to use, the job can use up to 64 cores, which may (probably) be
too many for your calculation.

You can choose the number of cores by expanding the options under *Study
\#* on the *Model Builder* menu. Do the same with *Job configurations*
and select *Batch 1* to open the *Settings* menu. If this menu is not
visible, select the *eye* icon on the *Model Builder* menu to show more
options. This will open a popup menu from which you can check the
*Solver and Job Configurations* option. On the *Batch 1* settings, check
the option *Number of cores* and type the desired number of cores.

Finally, click on *run* to submit your job on the cluster. Follow the
status of your simulation in the table in the *External process* tab.

### Detaching/attaching/stopping jobs

If you want to log out or close the local interface, you should detach
your job first by clicking on the button in the right bottom corner of
the local interface (near the progress bar).

If you want to keep your job running on the cluster while you are logged
out of your computer or the COMSOL interface is closed, just close it
and click *yes* when asked if you want to save the changes to the file.
When you open your file again to resume your work, open the *External
process* tab on the right side under *Graphics*. Click on the first icon
to attach the job. The table below should update the current status of
your simulation.

If, instead, you want to stop your simulation, click on the second icon
in the *External process* tab. If you think that there is a problem with
your simulation or if the program did not respond as expected, you can
also log in on the cluster and cancel your jobs with `scancel`. Learn
more about the scheduler commands in [Using
Slurm](/Using_Slurm "wikilink") page of this wiki.

## Mathematica

It is straightforward to run
[Mathematica](https://www.wolfram.com/mathematica/) scripts on the
cluster: `module load mathematica` followed by `math -script script.wl`
in a Slurm batch script is all you need. However, these scripts will
only use a single core. To fully leverage the parallel character of the
HPC cluster, one can/should use (remote) subkernels. This can be done by
embedding your script into the following template.

<div class="toccolours mw-collapsible mw-collapsed">
<div style="font-weight: bold; line-height: 1.6;">

`hpc.wl`

</div>

    (*
     * This script must be invoked by Slurm on a compute node, and will spawn remote
     * kernels on the nodes assigned to the job. To this end some environment
     * variables set by Slurm are read and parsed. It is assumed that compute nodes
     * can communicate freely with one another (no passwords, firewalls).
     *
     *)

    (*DEBUG*) (*turn on WSTP link debugging*)
    (*DEBUG*) Needs["Parallel`Debug`"];
    (*DEBUG*) SetOptions[$Parallel,Tracers->{MathLink}];


    Needs["SubKernels`RemoteKernels`"];


    (* get hostnames of nodes to run on *)
    nodes = StringSplit[
        RunProcess[
          {"scontrol", "show", "hostnames", Environment["SLURM_JOB_NODELIST"]},
          "StandardOutput"
        ],
        "\n"
      ];

    (* determine number of CPUs per node - this is the number of kernels *)
    cpusRaw = StringSplit[Environment["SLURM_JOB_CPUS_PER_NODE"], ","];
    cpus = {};
    For[i = 1, i <= Length[cpusRaw], i++,
      cpu = cpusRaw[[/i|i]];
      matches = StringCases[cpu, RegularExpression["^(\\d+)(?:\\(x(\\d+)\\))?$"] -> {"$1", "$2"}];
      repeat = ToExpression[matches[[/1|1]][[/2|2]]];
      If[NumericQ[repeat], Null, repeat = 1];
      For[j = 0, j < repeat, j++, AppendTo[cpus, ToExpression[matches[[/1|1]][[/1|1]]]]]
    ];
    cpus[[/Position[nodes,_Environment["SLURMD_NODENAME"|Position[nodes, Environment["SLURMD_NODENAME"]][[/1|1]]]]--;

    (*DEBUG*) (*print job resources, and Wolfram Kernel path, to screen*)
    (*DEBUG*) Print["nodes = ", nodes];
    (*DEBUG*) Print["jobs per node = ", cpus];

    (* start remote kernels and connect them to the controlling Wolfram Kernel *)
    SetOptions[$Output, FormatType->OutputForm];
    For[i = 1, i <= Length[nodes], i++,
      If[cpus[[/i|i]] > 0, LaunchKernels[RemoteMachine[
        nodes[[/i|i]],
        "ssh -x -f -l `3` `1` \"module load mathematica && wolfram -wstp -linkmode Connect `4` -linkname '`2`' -subkernel -noinit\"",
        cpus[[/i|i]]
      ]]]
    ];

    (*DEBUG*) (*check that kernels were launched correctly*)
    (*DEBUG*) Print["Kernels = ", Kernels[]];
    (*DEBUG*) Print["Kernel count = ", $KernelCount];

    (* ===== Your script, leveraging HPC, starts here ===== *)

    (* For example: *)
    result = ParallelTable[Prime[i], {i, 11111115}];
    Save["result.txt", result];

    (* ===== end of your HPC script ===== *)

    CloseKernels[];
    Quit[];

</div>

You can call the above script, after you have embedded your script into
it, using the following Slurm batch script.

<div class="toccolours mw-collapsible mw-collapsed">
<div style="font-weight: bold; line-height: 1.6;">

`math.cmd`

</div>

    #!/usr/bin/bash
    #SBATCH --nodes=3
    #SBATCH --ntasks=3
    #SBATCH --cpus-per-task=2
    #SBATCH --partition=tue.default.q
    #SBATCH --error=slurm-%j.err
    #SBATCH --output=slurm-%j.out
    #SBATCH --time=00:01:00

    module load mathematica
    math -script hpc.wl

</div>

Of course, you can modify the number of nodes and CPUs in the parameters
of the Slurm batch script to suit your needs. You should also modify the
[partition](/Scheduling_calculation_jobs_(Slurm)#Selecting_a_partition_(queue) "wikilink")
and time limit. Finally, just `sbatch math.cmd`.

## Python

There is no need to load modules to work with Python: it is installed
and available by default on the system. Run `python -V` or `python3 -V`
to test that you can run Python, and to see the currently installed
version. At the time of writing, Python 2.7.5 and 3.6.8 are installed.

### Virtual environments

We recommend you to work within a [virtual
environment](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
if you work with Python packages. This is essentially a local directory
where all packages you install are stored, so as to not interfere with
system packages or other projects you might have. Usage is quite
straightforward. First, create an environment and chose a name for it
(and the directory):

`python3 -m venv my-python-environment`

After that one-time step, you can activate the environment at any time
using

`source my-python-environment/bin/activate`

and deactivate the environment by executing `deactivate`. Your prompt
should indicate if a virtual environment is active, if you use it in an
interactive session.

Within this environment, you can freely install and upgrade packages
using pip. You can start with `pip install --upgrade pip` to make sure
the package manager is on the latest version, followed by
`pip install `<package> to install whatever you need.

#### Check availability and install packages

To check the availability of a package, use the command
`pip show `<package>. If the package is installed, the command will
return the version and some other information about it. Otherwise the
command will issue a warning, and you can then install the package as
follows:

` pip install `<package>

### Using Anaconda

If you want to use [Anaconda](https://www.anaconda.com/), you will have
to load a module: `module load anaconda`. Several versions are
available, as you can see by running `module avail anaconda`. The former
command will load the current version of Anaconda (which is kept
up-to-date on a best effort basis). Loading this module will make
several executables available, among which `anaconda`, `conda`, `flask`
and `jupyter`. You *can* then directly use those in your script. We do
however recommend you to always work in a [virtual
environment](/#Virtual_environments "wikilink").

`conda` in fact allows you to create
[environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
and even to install a specific version of Python for an environment.
This enables even more flexibility. As opposed to the built-in `venv`
module of Python, Anaconda environments are stored in a central location
in your home directory. You can thus activate environments regardless of
your current working directory.

`$ module load anaconda`
`$ conda config --set auto_activate_base false`
`$ conda init bash`
*`log out and back in, or`*` ``$ source ~/.bashrc`
`$ conda create --name my-python-3.9 python=3.9`

After that, you can at all times activate your environment as follows:

`$ module load anaconda`
`$ conda activate my-python-3.9`

In an sbatch script, be sure to `source ~/.bashrc` as well, because
Slurm does not do that automatically.

To list your environments, use:

`$ conda env list`

And clean up environments you no longer need by running:

`$ conda env remove --name my-python-3.9`

Within an environment, you can `pip install` libraries just like in
Python `venv` without impacting other environments.

### Using TensorFlow

If you want to use [TensorFlow](https://www.tensorflow.org/), you should
create a [virtual environment](/#Virtual_environments "wikilink"),
activate it and then
`TMPDIR=~/.tmp/ pip install --build ~/.tmp/ tensorflow`. This is a
slight variation on the `pip install tensorflow` command you might
expect, which is needed because of the limited size of the `/tmp`
partition you get on the HPC cluster. Please try rerunning the command
once or twice if it fails due to too little disk space, before reporting
the problem. Please `rm -rf ~/.tmp` after the installation succeeds to
clean up the temporary build files.

When done, you can verify if the installation was successful by
executing

`python -c $'import tensorflow as tf\nprint(tf.__version__)'`

which should print something like `2.2.0`.

Now that you have installed TensorFlow, using it is a matter of
activating the virtual environment and importing it in your script.

## Spark

It is possible to set up a [Spark](https://spark.apache.org/) cluster in
a Slurm job as follows. First, create a directory to work in:

` mkdir -p -- ~/spark/{logs,temp} ; cd ~/spark`

Then, upload the following Slurm batch script into that directory.
Please update the values for the `--output` and `--error` parameters if
needed - some departments have [their own storage
server](/Technical_specifications "wikilink") and therefore a different
path to their home directories.

<div class="toccolours mw-collapsible mw-collapsed">
<div style="font-weight: bold; line-height: 1.6;">

`spark.cmd`

</div>

    #!/bin/bash

    #SBATCH --partition=tue.test.q
    #SBATCH --nodes=3
    #SBATCH --cpus-per-task=4
    #SBATCH --mem-per-cpu=500
    #SBATCH --exclusive

    #SBATCH --time=01:00:00

    #SBATCH --output=/home/tue/%u/spark/logs/%j.out
    #SBATCH --error=/home/tue/%u/spark/logs/%j.err

    # can only have one Spark slave per node in this script (otherwise would need
    # increasing ports and take care in general)
    #SBATCH --ntasks-per-node=1

    # this section will be run by sbatch initially
    if [ "$1x" != "srunningx" ]; then
        export _SPARK_LOGS="$HOME/spark/logs/"
        export _SPARK_TEMP="$HOME/spark/temp/"
        mkdir -p -- "$_SPARK_LOGS" "$_SPARK_TEMP"
        export _SPARK_MASTER_NODE="$_SPARK_TEMP/${SLURM_JOBID}_spark_master"

        # because Slurm copies this script temporarily and deletes it before we can
        # call it, we make our own copy
        _SCRIPT="$_SPARK_TEMP/${SLURM_JOBID}_$(basename -- "$0")"
        cp "$0" "$_SCRIPT"

        srun "$_SCRIPT" srunning
    else # if run by srun, decide via the Slurm procid whether we are master or worker
        module load spark

        # trim "bin/spark-submit" from the below path to get Spark root
        _SPARK_LOC="$(whereis spark-submit | awk -F' ' '{print $2}')"
        export SPARK_HOME="${_SPARK_LOC%/*/*}"
        export SPARK_WORKER_DIR="$_SPARK_LOGS"
        export SPARK_LOCAL_DIRS="$_SPARK_LOGS"
        export SPARK_MASTER_PORT=7077
        export SPARK_MASTER_WEBUI_PORT=8080
        export SPARK_WORKER_CORES=$SLURM_CPUS_PER_TASK
        export SPARK_DAEMON_MEMORY=$(( $SLURM_MEM_PER_CPU * $SLURM_CPUS_PER_TASK / 2 ))m
        export SPARK_MEM=$SPARK_DAEMON_MEMORY

        source "$SPARK_HOME/sbin/spark-config.sh"
        source "$SPARK_HOME/bin/load-spark-env.sh"

        if [ "$SLURM_PROCID" -eq 0 ]; then
            export SPARK_MASTER_IP=$(hostname)
            MASTER_NODE=$(scontrol show hostname $SLURM_NODELIST | head -n 1)

            # save host and port so that slaves know where to submit jobs
            echo "spark://$SPARK_MASTER_IP:$SPARK_MASTER_PORT" > "$_SPARK_MASTER_NODE"
            "$SPARK_HOME/bin/spark-class" org.apache.spark.deploy.master.Master \
                --ip "$SPARK_MASTER_IP" \
                --port "$SPARK_MASTER_PORT" \
                --webui-port "$SPARK_MASTER_WEBUI_PORT"
        else
            MASTER_NODE=""
            while [ -z "$MASTER_NODE" ]; do
                sleep 1s
                if [ -f "$_SPARK_MASTER_NODE" ]; then
                    MASTER_NODE=$(<"$_SPARK_MASTER_NODE")
                fi
            done
            "$SPARK_HOME/bin/spark-class" org.apache.spark.deploy.worker.Worker "$MASTER_NODE"
        fi
    fi

</div>

Modify the parameters near the top to suit your needs:

-   the
    [partition](/Scheduling_calculation_jobs_(Slurm)#Selecting_a_partition_(queue) "wikilink"),
-   number of nodes (master plus number of workers),
-   CPUs per task (number of CPUs that can be used by each worker and
    the master), and
-   memory per CPU (default unit is megabytes, unit can be specified as
    K\|M\|G\|T after the number).

You can also change the time limit, which is the time after which the
cluster is destroyed. Consult the [sbatch man
page](https://slurm.schedmd.com/sbatch.html) to find accepted time
formats.

Finally, you may want to change where Slurm writes output from Spark. If
you don't change the defaults in the above script, you'll find the logs
in the same directory where Spark will write its log files to.

### Starting a Spark cluster and submitting applications

Now that you have set up this batch script, you can start a cluster as
follows.

` [you@tue-login001 spark]$ sbatch spark.cmd`
` Submitted batch job `<job ID>

Note the Slurm job ID; you'll need it later to work with the Spark
cluster.

Monitor the status of the job by issuing `squeue -u $USER` until you see
it has started (time greater than 00:00, nodelist nonempty). You will
(soon after) find the address of the master node in the
`temp/`<job ID>`_spark_master` file. This can be used as follows to run
an example:

` [you@tue-login001 spark]$ module load spark`
` [you@tue-login001 spark]$ run-example --master $(<temp/`<job ID>`_spark_master) SparkPi 100`

This uses a Bash construct to read the value from the file that contains
the master node address, and pass it as an argument to the `run-example`
executable. In a similar manner you can use `spark-submit` to submit
your application to the Spark cluster and monitor its status.

### Stopping a Spark cluster

Stopping the cluster is a matter of cancelling the Slurm job:
`scancel `<job ID>.

### Opening the Spark web UI

If you open the `temp/`<job ID>`_spark_master` file, you'll see on which
node it runs. This might be `tue-computeZ042.cm.cluster` for example.
Given that the web UI can be accessed via port 8082 on that node, you
can access it in your browser if you set up local port forwarding. When
connecting to the HPC cluster on Linux, that might look as follows:

` ssh -L 8000:tue-computeB005.cm.cluster:8082 you@hpc.tue.nl`

You will then be able to open `localhost:8000` in your browser to access
the Spark web UI.

__FORCETOC__