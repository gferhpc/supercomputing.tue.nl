---
title: R
tags: [Software, Module]
---
The Comprehensive R Archive Network (CRAN) has packages available that
can be used to extend R. On the HPC cluster specific version of R can be
loaded using modules. Packages are installed specific for the version of
R that was active during install; when the version of R is changed the
packages need to be reinstalled.

### Package installation

1.  Use ssh/putty to access a login node
2.  Load the module with a (newer) version of R
       ```shell
       module avail R
       ```
       R/(version 1)   R/(version 2)   ...

       ```shell
       module load R/(version of choice)
       ```

3.  Create a Rlibs directory in your home directory
        ```shell
        mkdir Rlibs
        ```
4.  Install a package and its dependency, in this example Rmpfr depends on gmp
        ```shell
        Rscript -e "install.packages('gmp','~/Rlibs','http://ftp.ussg.iu.edu/CRAN')"
        Rscript -e "install.packages('Rmpfr','~/Rlibs','http://ftp.ussg.iu.edu/CRAN')"
        ```

### Running a job

-   At the start of your job script, make sure that you load the same version of R that you used while installing the package, i.e. do a
    ```shell
    module load R/(version)
    ``` 
    at the start of your job script.

<!-- -->

-   In your job script, you **don't** need to install the package again!
    In the previous part you installed it in your home directory, which
    is also available on the compute nodes, hence the package is
    automatically also installed there.
