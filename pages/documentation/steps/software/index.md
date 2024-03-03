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
| CP2K           | 2023.1-foss-2023a                    | `module avail CP2K`      | |
| GROMACS        | 2023.3-foss-2023a                    | `module avail GROMACS`   | |
| Julia          | 1.9.3 1.10.1                         | `module avail Julia`     | |
| LAMMPS         | 23Jun2022-foss-2022a-kokkos          | `module avail LAMMPS`    | |
| NetLogo        | 6.3.0-64 6.4.0-64                    | `module avail NetLogo`   | |
| OpenFOAM       | 8-foss-2022a                         | `module avail OpenFOAM`  | |
| ParaViews      | 5.11.2-foss-2023a                    | `module avail ParaView`  | Yes |
| R              | 4.2.1-foss-2022a  4.3.2-gfbf-2023a   | `module avail R/`        | |
| Rstudio        | 2022.07.2+576-foss-2022a-Java-11-R-4.2.1 | `module avail RStudio` | Yes |
 
### Python and related software.

| Name           | Supported Versions                   | Module(s)                | https://hpc.tue.nl |
| -------------- | ------------------------------------ | ------------------------ | ------------------ |
| Anaconda3      | Anaconda3-2023.09-0                  | `module avail Anaconda3` | |
| dask           | 2022.10.0-foss-2022a 2023.9.2-foss-2023a | `module avail dask`      | |
| IPython        | 8.5.0 8.14.0                         | `module avail IPython`   | |
| Jax            | 0.4.4-foss-2022a                     | `module avail IPython`   | |
| JupyterLab     | 4.0.5-GCCcore-12.3.0                 | `module avail Jupyter`   | Yes, via Jupyter |
| numba          | 0.56.4-foss-2022a                    | `module avail numba`     | |
| Python         | 2.7.18 3.10.4 3.10.13 3.11.3.        | `module avail Python/`   | |
| PyTorch        | 1.12.0-foss-2022a 2.1.2-foss-2022a   | `module avail PyTorch`   | Yes, included in Jupyter|
| scikit-bio     | 0.5.7-foss-2022a                     | `module avail scikit-bio` | |
| scikit-learn   | 1.1.2-foss-2022a                     | `module avail scikit-learn` | |
| SciPy          | 2022.05-foss-2022a 2023.07-gfbf-2023a | `module avail SciPy-bundle` | Yes, included in Jupyter |
| Tensorflow     | 2.11.0-foss-2022a    2.13.0-foss-2023a  | `module avail TensorFlow` | Yes, included in Jupyter |

??? example "available pip packages after running "module load SciPy-bundle/2023.07-gfbf-2023a"
    ```shell
    $ mdule load SciPy-bundle/2023.07-gfbf-2023a
    $ pp list
    Package                          Version
    --------------------------------- -----------
    alabaster                         0.7.13
    appdirs                           1.4.4
    asn1crypto                        1.5.1
    atomicwrites                      1.4.1
    attrs                             23.1.0
    Babel                             2.12.1
    backports.entry-points-selectable 1.2.0
    backports.functools-lru-cache     1.6.5
    beniget                           0.4.1
    bitstring                         4.0.2
    blist                             1.3.6
    Bottleneck                        1.3.7
    CacheControl                      0.12.14
    cachy                             0.3.0
    certifi                           2023.5.7
    cffi                              1.15.1
    chardet                           5.1.0
    charset-normalizer                3.1.0
    cleo                              2.0.1
    click                             8.1.3
    cloudpickle                       2.2.1
    colorama                          0.4.6
    commonmark                        0.9.1
    crashtest                         0.4.1
    cryptography                      41.0.1
    Cython                            0.29.35
    deap                              1.4.0
    decorator                         5.1.1
    distlib                           0.3.6
    distro                            1.8.0
    docopt                            0.6.2
    docutils                          0.20.1
    doit                              0.36.0
    dulwich                           0.21.5
    ecdsa                             0.18.0
    editables                         0.3
    exceptiongroup                    1.1.1
    execnet                           1.9.0
    filelock                          3.12.2
    flit_core                         3.9.0
    fsspec                            2023.6.0
    future                            0.18.3
    gast                              0.5.4
    glob2                             0.7
    html5lib                          1.1
    idna                              3.4
    imagesize                         1.4.1
    importlib-metadata                6.7.0
    importlib-resources               5.12.0
    iniconfig                         2.0.0
    intervaltree                      3.1.0
    intreehooks                       1.0
    ipaddress                         1.0.23
    jaraco.classes                    3.2.3
    jeepney                           0.8.0
    Jinja2                            3.1.2
    joblib                            1.2.0
    jsonschema                        4.17.3
    keyring                           23.13.1
    keyrings.alt                      4.2.0
    liac-arff                         2.5.0
    lockfile                          0.12.2
    markdown-it-py                    3.0.0
    MarkupSafe                        2.1.3
    mdurl                             0.1.2
    mock                              5.0.2
    more-itertools                    9.1.0
    mpmath                            1.3.0
    msgpack                           1.0.5
    netaddr                           0.8.0
    netifaces                         0.11.0
    numexpr                           2.8.4
    numpy                             1.25.1
    packaging                         23.1
    pandas                            2.0.3
    pastel                            0.2.1
    pathlib2                          2.3.7.post1
    pathspec                          0.11.1
    pbr                               5.11.1
    pexpect                           4.8.0
    pip                               23.1.2
    pkginfo                           1.9.6
    platformdirs                      3.8.0
    pluggy                            1.2.0
    ply                               3.11
    pooch                             1.7.0
    psutil                            5.9.5
    ptyprocess                        0.7.0
    py                                1.11.0
    py-expression-eval                0.3.14
    pyasn1                            0.5.0
    pybind11                          2.11.1
    pycparser                         2.21
    pycryptodome                      3.18.0
    pydevtool                         0.3.0
    Pygments                          2.15.1
    pylev                             1.4.0
    PyNaCl                            1.5.0
    pyparsing                         3.1.0
    pyrsistent                        0.19.3
    pytest                            7.4.0
    pytest-xdist                      3.3.1
    python-dateutil                   2.8.2
    pythran                           0.13.1
    pytoml                            0.1.21
    pytz                              2023.3
    rapidfuzz                         2.15.1
    regex                             2023.6.3
    requests                          2.31.0
    requests-toolbelt                 1.0.0
    rich                              13.4.2
    rich-click                        1.6.1
    scandir                           1.10.0
    scipy                             1.11.1
    SecretStorage                     3.3.3
    semantic-version                  2.10.0
    setuptools                        67.7.2
    shellingham                       1.5.0.post1
    simplegeneric                     0.8.1
    simplejson                        3.19.1
    six                               1.16.0
    snowballstemmer                   2.2.0
    sortedcontainers                  2.4.0
    Sphinx                            7.0.1
    sphinx-bootstrap-theme            0.8.1
    sphinxcontrib-applehelp           1.0.4
    sphinxcontrib-devhelp             1.0.2
    sphinxcontrib-htmlhelp            2.0.1
    sphinxcontrib-jsmath              1.0.1
    sphinxcontrib-qthelp              1.0.3
    sphinxcontrib-serializinghtml     1.1.5
    sphinxcontrib-websupport          1.2.4
    tabulate                          0.9.0
    threadpoolctl                     3.1.0
    toml                              0.10.2
    tomli                             2.0.1
    tomli_w                           1.0.0
    tomlkit                           0.11.8
    typing_extensions                 4.6.3
    tzdata                            2023.3
    ujson                             5.8.0
    urllib3                           1.26.16
    versioneer                        0.29
    virtualenv                        20.23.1
    wcwidth                           0.2.6
    webencodings                      0.5.1
    wheel                             0.40.0
    xlrd                              2.0.1
    zipfile36                         0.1.3
    zipp                              3.15.0

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
