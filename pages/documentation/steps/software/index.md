---
title: 4. Using Software
---
# Using Software

## Modules

Since a lot of applications rely on 3rd party software, there is a program on most supercomputers, called the Module system. With this system, other software, like compilers or special math libraries, are easily loadable and usable. Depending on the institution, different modules might be available, but there are usually common ones like the Intel or GCC Compilers.

A few common commands, to enter into the supercomputer commandline and talk to the module system, are


- `module avail`  : lists available (loadable) modules
- `module list`   : lists loaded modules
- `module load x` : loads module x
- `module purge`  : unload all modules

If you recurrently need lots of modules, this loading can be automated with an (ba)sh-file, so that you just have to execute the file once and it loads all modules, you need.


### Commercial software

To use commercial software a license is needed, depending on the software this is a user or group sprecific license or a TU/e wide avaiable license.

Available as [modules](#Modules):

| Name            | Website                              | Module(s)                | https://hpc.tue.nl |
| --------------- | ------------------------------------ | ------------------------ | ------------------ |
| Abacus          | [www.3ds.com](https://www.3ds.com/products/simulia/abaqus){:target="_blank"} | `module avail abacus`    | Yes |
| ANSYS Fluent    | [www.ansys.com](https://www.ansys.com/products/fluids/ansys-fluent){:target="_blank"} | `module avail ansys`     | Yes |
| AMD-μProf       | [](){:target="_blank"} | `module avail amd-uprof` | Yes |
| AMS             | [www.scm.com](https://www.scm.com/amsterdam-modeling-suite/){:target="_blank"} | `module avail ams` | Yes |
| COMSOL          | [www.colsol.com](https://www.comsol.com/){:target="_blank"} | `module avail comsol`    | Yes |
| CONVERGE        | [convergecfd.com](https://convergecfd.com/){:target="_blank"} | `module avail convergentscience` | Yes |
| ANSYS Lumerical | [www.ansys.com](https://www.ansys.com/products/optics){:target="_blank"} | `module avail lumerical` | Yes |
| Mathematica     | [www.wolfram.com](https://www.wolfram.com/mathematica/){:target="_blank"} | `module avail mathematica` | Yes |
| MATLAB          | [www.mathworks.com](https://www.mathworks.com/products/matlab.html){:target="_blank"} | `module avail matlab` | Yes |
| StarCCM+        | [](){:target="_blank"} | `module avail starccm+` | Yes |
| TecPlot 360     | [](){:target="_blank"} | `module avail tecplot` | Yes |
| VTune           | [](){:target="_blank"} | `module avail vtune` | Yes |

### Non-Commercial software

Use `module load NewBuild/AMD` to activate:

| Name           | VBuild                               | Module(s)                |
| -------------- | ------------------------------------ | ------------------------ |
| Foss Toolchain | :material-check:     Fetch resource  | `module avail foss`      |
| Openfoam       | :material-check-all: Update resource | `module avail OpenFOAM`    |
| abacus         | :material-close:     Delete resource | `module avail abacus`    | 

## Parallel Programming

Currently development of computers is at a point, where you cannot just make a processor run faster (e.g. by increasing its clock frequency), because limits of physics have been reached in semiconductor development. Therefore the current approach is to split the work into multiple, ideally independent parts, which are then executed in parallel. Similar to cleaning your house, where everybody takes care of a few rooms, on a supercomputer this is usually done with parallel programming paradigms like Open Multi-Processing (OpenMP) or Message Passing Interface (MPI). However like the fact that you only have one vacuum cleaner in the whole house which not everybody can use at the same time, there are limits on how fast you can get, even with a big number of processing units/cpus/cores (analogous to people in the metaphor) working on your problem (cleaning the house) in parallel.

## Software Manipulation
### Generic software

The clusters have quite a few programs pre-installed. They are managed
as optional modules that you have to load before you can use them. One
reason for using them this way (I guess...) is that this makes it
possible to have multiple versions of the same program on the same
system, which can be relevant (multiple pythons for example). This page
explains the basic usage of modules. All module management is done
through the aptly named program "module".

#### Viewing available modules

To show the available modules, you should run `module avail` This prints
out a list of available modules to the screen.

#### Viewing loaded modules

To show which modules are already loaded, run `module list`

This will reveal that both "slurm/20.02.7" and "gcc/8.2.0" are loaded by
default. In order to use any other modules, you should explicitly load
them.

#### Loading modules

In order to use a module that is not loaded, run
`module load `<module name> For example, if you want to use the intel
compiler, "icc", if you try to run it from the command line, you will
get

    $ icc
    -bash: icc: command not found

After loading this becomes

    $ module load intel
    $ icc
    icc: command line error: no files specified; for help type "icc -help"

which is the expected behaviour.

#### Unloading modules

As easy as you can load modules, you can also unload them. The proper
command, as you might have guessed, is `module unload `<name of module>
So, to unload the intel module, you would run `module unload intel`.

### Specific software

#### Uploading

You can upload your specific (or even custom) software to your [personal homedir](../access/index.md).

For uploading modules, you should contact a system administrator.
