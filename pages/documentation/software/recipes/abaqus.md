---
tags: [Software, Module]
---
Abaqus (https://www.3ds.com/products-services/simulia/products/abaqus/)
is licensed software and only usable the the user is a member of the
correct group.

```shell 
module purge
module load intel/2023a
module load Abaqus/2024
```

Check the fortran compiler

```shell
[user@umbrella]$ ifort --version
ifort (IFORT) 2021.2.0 20210228
Copyright (C) 1985-2021 Intel Corporation.  All rights reserved.
```

Check abaqus:

```shell 
[user@umbrella]$ abaqus verify -user_std

Abaqus Product Install Verification...

Wed Mar  8 14:54:18 2023

Making /path/to/Jobs/verify. All verification files will reside in
this directory.

-----------------------------------------------------------------------------
Abaqus/Standard with user subroutines

         ...PASS
         Continuing...

-----------------------------------------------------------------------------
Clean-up...

Verification directory /path/to/Jobs/verify has been deleted.
```
