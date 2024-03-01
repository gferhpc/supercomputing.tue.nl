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

To use commercial software a license is needed, depending on the software this is a user or group sprecific license or a TU/e wide available license.

Available as [modules](#Modules):

| Name            | Website                              | Module(s)                | https://hpc.tue.nl |
| --------------- | ------------------------------------ | ------------------------ | ------------------ |
| Abacus          | [3ds.com](https://www.3ds.com/products/simulia/abaqus){:target="_blank"} | `module avail abacus`    | Yes |
| ANSYS Fluent    | [ansys.com](https://www.ansys.com/products/fluids/ansys-fluent){:target="_blank"} | `module avail ansys`     | Yes |
| AMD-μProf       | [amd.com](https://www.amd.com/en/developer/uprof.html){:target="_blank"} | `module avail amd-uprof` | Yes |
| AMS             | [scm.com](https://www.scm.com/amsterdam-modeling-suite/){:target="_blank"} | `module avail ams` | Yes |
| COMSOL          | [colsol.com](https://www.comsol.com/){:target="_blank"} | `module avail comsol`    | Yes |
| CONVERGE        | [convergecfd.com](https://convergecfd.com/){:target="_blank"} | `module avail convergentscience` | Yes |
| ANSYS Lumerical | [ansys.com](https://www.ansys.com/products/optics){:target="_blank"} | `module avail lumerical` | Yes |
| Mathematica     | [wolfram.com](https://www.wolfram.com/mathematica/){:target="_blank"} | `module avail mathematica` | Yes |
| MATLAB          | [mathworks.com](https://www.mathworks.com/products/matlab.html){:target="_blank"} | `module avail matlab` | Yes |
| StarCCM+        | [siemens.com](https://plm.sw.siemens.com/en-US/simcenter/fluids-thermal-simulation/star-ccm/){:target="_blank"} | `module avail starccm+` | Yes |
| TecPlot 360     | [tecplot.com](https://tecplot.com/products/tecplot-360/){:target="_blank"} | `module avail tecplot` | Yes |
| VTune           | [intel.com](https://www.intel.com/content/www/us/en/developer/tools/oneapi/vtune-profiler.html){:target="_blank"} | `module avail vtune` | Yes |

### Non-Commercial software

Toolchains this are the tools to build software, it includes specific Compilers and an MPI implementation, in case of foss also Open/FlexiBLAS, ScaLAPACK and FFTW(MPI) are included for example.   

| Toolchain Name | Supported Versions                   | Module(s)                | Remarks |
| -------------- | ------------------------------------ | ------------------------ | ------- |
| foss           | 2022a 2023a                          | `module avail foss`      | |
| gfbf           | 2023a                                | `module avail gfbf`      | gfbf is a subset of foss |
| intel          | 2022a 2023a                          | `module avail intel`     | |

foss = "Free and Open Source Software" gfbf = "Gcc + FlexiBlas + Fftw"

??? example "module load foss/2023a"
    ```shell
    $ module list

    Currently Loaded Modules:
      1) GCCcore/12.3.0
      2) zlib/1.2.13-GCCcore-12.3.0
      3) binutils/2.40-GCCcore-12.3.0
      4) GCC/12.3.0
      5) numactl/2.0.16-GCCcore-12.3.0
      6) XZ/5.4.2-GCCcore-12.3.0
      7) libxml2/2.11.4-GCCcore-12.3.0
      8) libpciaccess/0.17-GCCcore-12.3.0
      9) hwloc/2.9.1-GCCcore-12.3.0
     10) OpenSSL/1.1
     11) libevent/2.1.12-GCCcore-12.3.0
     12) UCX/1.14.1-GCCcore-12.3.0
     13) libfabric/1.18.0-GCCcore-12.3.0
     14) PMIx/4.2.4-GCCcore-12.3.0
     15) UCC/1.2.0-GCCcore-12.3.0
     16) OpenMPI/4.1.5-GCC-12.3.0
     17) OpenBLAS/0.3.23-GCC-12.3.0
     18) FlexiBLAS/3.3.1-GCC-12.3.0
     19) FFTW/3.3.10-GCC-12.3.0
     20) gompi/2023a
     21) FFTW.MPI/3.3.10-gompi-2023a
     22) ScaLAPACK/2.2.0-gompi-2023a-fb
     23) foss/2023a
    ```
??? example "module load gfbf/2023a"
    ```shell
    $ module list

    Currently Loaded Modules:
      1) GCCcore/12.3.0
      2) zlib/1.2.13-GCCcore-12.3.0
      3) binutils/2.40-GCCcore-12.3.0
      4) GCC/12.3.0
      5) OpenBLAS/0.3.23-GCC-12.3.0
      6) FlexiBLAS/3.3.1-GCC-12.3.0
      7) FFTW/3.3.10-GCC-12.3.0
      8) gfbf/2023a
    ```

??? example "module load intel/2023a"
    ```shell
    $ module list

    Currently Loaded Modules:
      1) GCCcore/12.3.0
      2) zlib/1.2.13-GCCcore-12.3.0
      3) binutils/2.40-GCCcore-12.3.0
      4) intel-compilers/2023.1.0
      5) numactl/2.0.16-GCCcore-12.3.0
      6) UCX/1.14.1-GCCcore-12.3.0
      7) impi/2021.9.0-intel-compilers-2023.1.0
      8) imkl/2023.1.0
      9) iimpi/2023a
     10) imkl-FFTW/2023.1.0-iimpi-2023a
     11) intel/2023a
    ```

Using the toolchain(s) the following software is avaiable. When the module is loaded the toolchain it depends on is automatically loaded.

| Name           | Supported Versions                   | Module(s)                | https://hpc.tue.nl |
| -------------- | ------------------------------------ | ------------------------ | ------------------ |
| Blender        | 4.0.2-linux-x86_64-CUDA-12.1.1       | `module avail Blender`   | Yes |
| GROMACS        | 2023.3-foss-2023a                    | `module avail GROMACS`   | |
| Julia          | 1.9.3 1.10.1                         | `module avail Julia`     | |
| OpenFOAM       | 8-foss-2022a                         | `module avail OpenFOAM`  | |
| ParaViews      | 5.11.2-foss-2023a                    | `module avail ParaView`  | Yes |
| R              | 4.2.1-foss-2022a  4.3.2-gfbf-2023a   | `module avail R/`        | |
| Rstudio        | 2022.07.2+576-foss-2022a-Java-11-R-4.2.1 | `module avail RStudio` | Yes |
 
Python and related software available.

| Name           | Supported Versions                   | Module(s)                | https://hpc.tue.nl |
| -------------- | ------------------------------------ | ------------------------ | ------------------ |
| Anaconda3      | Anaconda3-2023.09-0                  | `module avail Anaconda3` | |
| IPython        | 8.5.0 8.14.0                         | `module avail IPython`   | |
| Jax.           | 0.4.4-foss-2022a                     | `module avail IPython`   | |
| JupyterLab     | 4.0.5-GCCcore-12.3.0                 | `module avail Jupyter`   | Yes, via Jupyter |
| Python         | 2.7.18 3.10.4 3.10.13 3.11.3.        | `module avail Python/`   | |
| PyTorch        | 1.12.0-foss-2022a 2.1.2-foss-2022a   | `module avail PyTorch`   | Yes, included in Jupyter|
| SciPy          | 2022.05-foss-2022a 2023.07-gfbf-2023a | `module avail SciPy-bundle` | Yes, included in Jupyter |
| Tensorflow     | 2.11.0-foss-2022a 2.13.0-foss-2023a  | `module avail TensorFlow` | Yes, included in Jupyter |



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
