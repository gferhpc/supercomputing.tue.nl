---
title: Non commercial software modules
tags: [Software]
---
The HPC Umbrella Cluster uses the concept of Toolchains to build software, it includes specific Compilers and an MPI implementation, in case of foss also Open/FlexiBLAS, ScaLAPACK and FFTW(MPI) are included for example.   

| Toolchain Name | Supported Versions                   | Module(s)                | Remarks |
| -------------- | ------------------------------------ | ------------------------ | ------- |
| foss           | 2022a 2023a                          | `module avail foss`      | |
| gfbf           | 2023a                                | `module avail gfbf`      | gfbf is a subset of foss (no OpenMPI) |
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
| ADIOS2         | 2.10.1-gompi-2023a                   | `ADIOS2`    | |
| Blender        | 4.2.0-linux-x86_64-CUDA-12.1.1.      | `Blender`   | Yes |
| CP2K           | 2023.1-foss-2023a                    | `CP2K`      | |
| dask           | 2023.12.1-foss-2023a | `dask`  | |
| GROMACS        | 2023.3-foss-2023a                    | `GROMACS`   | |
| Julia          | 1.11.1                         | `Julia`     | |
| LAMMPS         | 2Aug2023_update2-foss-2023a-kokkos | `LAMMPS`    | |
| MCL            | 22.282-GCCcore-12.3.0                | `MCL`       | |
| NetLogo        | 6.4.0-64                    | `NetLogo`   | Yes |
| OpenFOAM (ESI)      | v2206-foss-2022a<br>v2312-foss-2023a<br>v2406-foss-2023a | `OpenFOAM`  | |
| OpenFOAM (Foundation)       | 10-foss-2023a<br>11-foss-2023a<br>12-foss-2023a | `OpenFOAM`  | |
| OpenModelica   | 1.22.0-foss-2022a                    | `OpenModelica` | |
| OpenSceneGraph | 3.6.5-foss-2022a                     | `OpenSceneGraph`  | Yes via Interactive Desktop |
| ORCA           | 6.0.0-gompi-2023a<br>5.0.4-gompi-2023a                   | `ORCA`      | |
| ParaView       | 5.12.1-foss-2023a                    | `ParaView`  | Yes |
| QCG-PilotJob   | 0.14.1-foss-2023a | `QCG-PilotJob` | |
| QuantumESPRESSO| 7.3.1-foss-2023a    | `QuantumESPRESSO` | |
| R              | 4.4.0-gfbf-2023a<br>4.4.1-gfbf-2023a  | `R/`        | |
| Rstudio        | 2022.07.2+576-foss-2022a-Java-11-R-4.2.1<br>2023.12.1+402-gfbf-2023a-Java-11-R-4.4.1 | `RStudio` | Yes |
| Spark          | 3.5.0-foss-2023a<br>3.5.1-foss-2023a-Java-17 | `Spark`        | |
| VSCode         | 1.92.2<br>1.93.1      | `VSCode`   | Yes via codeserver |
 
