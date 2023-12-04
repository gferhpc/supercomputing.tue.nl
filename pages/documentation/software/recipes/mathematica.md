# Mathematica

It is straightforward to run
[Mathematica](https://www.wolfram.com/mathematica/){:target=_blank} scripts on the
cluster: `module load mathematica` followed by `math -script script.wl`
in a Slurm batch script is all you need. However, these scripts will
only use a single core. To fully leverage the parallel character of the
HPC cluster, one can/should use (remote) subkernels. This can be done by
embedding your script into the following template.

??? example "hpc.wl"

    ```mathematica
    
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
    ```

You can call the above script, after you have embedded your script into
it, using the following Slurm batch script.

??? example "math.cmd"

    ```shell
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
    ```

Of course, you can modify the number of nodes and CPUs in the parameters
of the Slurm batch script to suit your needs. You should also modify the [partition](../../steps/jobs/index.md)
and time limit. Finally, just `sbatch math.cmd`.
