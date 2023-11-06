---
title: TU/e Umbrella HPC Cluster
---
# The TU/e Umbrella HPC Cluster

![The Umbrella Cluster](/images/hpc-umbrella-full.png){ align=right width=350 }

The TU/e Umbrella HPC Cluster is the HPC cluster of the TU/e consisting of Faculty supplied compute (CPU and GPU) resources and managed by the HPC Lab. It is one of the High Performance Computing solutions the HPC Lab offers.

As the TU/e Umbrella HPC Cluster is managed centrally, you can get access with your TU/e account. Depending on your department/research group, you can get access to certain part of TU/e Umbrella HPC Cluster. Note that at the TU/e, some departments/research groups have several local computation facilities. These are not part of the TU/e HPC Umbrella Cluster, please contact the [Reasearch IT contact of your department](https://tuenl.sharepoint.com/sites/intranet-LIS/SitePages/Research-IT.aspx) for more information.

## Access

*"How-to-be-allowed-onto-the-TU/e-Umbrella-HPC-cluster"*

Use the Selfservice request formm supplied by the TU/e to request login credentails.

[Create a Service Request :material-ticket:](https://tue.topdesk.net/tas/public/ssp/content/serviceflow?unid=a745121fa0ab45f2b24aaaf64060760f){ .md-button .md-button--primary }

After this is done and login credentials are supplied, one can proceed to login.

## Login

*"How-to-now-actually-connect-to-the-TU/e-Umbrella-HPC-cluster"*

The TU/e Umbrella HPC Cluster is unix-based (Linux) environments with shell (commandline) access.
To log in, one usually uses ssh to reach the respective Login Nodes (computers reserved for people just like you that want to connect to the HPC Cluster). This access is restricted, so you can only connect, when you are within the university/facility and its network. To still access the Login Nodes externally, one can 'pretend to be inside the network' by using the TU/e provided Virtual Private Network (VPN).

Once there, the user can interact with the system and run (small) programs to generally test the system/software.

## File Transfer

*"How-to-get-your-data-onto-or-off-the-TU/e-Umbrella-HPC-cluster"*

To get your data (files) onto the TU/e Umbrella HPC Cluster or back to your local machine, there are usually different ways.

Commonly used and widely supported copying tools are rsync which mirrors directories (folders) between the supercomputer and your local machine. scp which is useful for a few single files or specified file-lists, and lastly the commonly used ftp or the encrypted version sftp (or ftps). A little bit more information can be found in the File Transfer article.

## Scheduler

*"How-To-Run-Applications-on-the-TU/e-Umbrella-HPC-cluster"*

To run any significant program or workload on a supercomputer, generally a Batch-Scheduler is employed. Alongside the above-mentioned Login Nodes there are usually far more Backend Nodes in the system (computers exclusively reserved for computing, to which you cannot connect directly, also referred to as "batch system"). A program called Batch-scheduler decides who gets how many of those compute resources for which amount of time. Please use the Backend Nodes for everything which is not a simple small test and only runs for a few minutes., otherwise you will block the Login Nodes for everybody when you run your calculations there. These Backend Nodes make up more than 98% of a supercomputer and can only be accessed via the scheduler.

When you log into a supercomputer, you can run commands on the Login Nodes interactively. You type, you hit return, the command gets executed. Schedulers work differently. You submit a series of commands (in form of a file) and tell it, how much resources it will approximately need in terms of:

time: If the specified time runs out, before your application finishes and exits, it will be terminated by the scheduler.
compute resources: how many cpus ('calculation thingies'), sockets ('cpu-houses') and nodes ('computers')
memory resources: how much RAM ('very fast memory, similar to the few books you have at home')
This combination of specified commands and required resources is commonly referred to as a "(batch) job".

If later compute resources become free, which match the requirements of your application, the scheduler will run your specified commands on the requested hardware. This is usually delayed (sometimes you have to wait a day or two) and not instant, because other users are currently using the compute resources and you have to wait until their program runs finish. Furthermore you cannot change the series of commands after submitting, but just terminate the job and submit a new one in case of an error.

The file specifying this series of commands and the required resources is called a jobscript. Its format and syntax depends on the installed scheduler. When you have this jobscript ready with the help of jobscript-examples, colleagues or your local support, you can submit it to the respective scheduler of your facility. The scheduler then waits until a set of nodes (computers) are free and later allocates those to execute your job as soon as possible. Sometimes there is (an optional) email notification, which is send when your job starts execution/finished running.

Be aware that your specified requirements have to fit within the boundaries of the system of your facility. If you ask for more than there is, chances are, the scheduler will accept your job and wait until missing hardware is bought and installed - although this will not happen in 99.9% of cases. Information over the available hardware can be found in the overview of the Gauss Allianz or the documentation of the different sites. You can find more information about parallelizing programs here. Also there is an overview of the schedulers used at the different sites.

## Software

*"What-can-I-run-on-the-TU/e-Umbrella-HPC-Cluster"*

### Commercial software

To use commercial software a license is needed, depending on the software this is a user or group sprecific license or a TU/e wide avaiable license.

Available as [modules](#Modules):

| Name         | Website                              | Module(s)                |
| ------------ | ------------------------------------ | ------------------------ |
| ANSYS/Fluent | [www.ansys.com](https://www.ansys.com/){:target="_blank"}             | `module avail ansys`     |
| COMSOL       | :material-check-all: Update resource | `module avail comsol`    |
| abacus       | :material-close:     Delete resource | `module avail abacus`    | 


### Non-Commercial software

Use `module load NewBuild/AMD` to activate:

| Name           | VBuild                               | Module(s)                |
| -------------- | ------------------------------------ | ------------------------ |
| Foss Toolchain | :material-check:     Fetch resource  | `module avail foss`      |
| Openfoam       | :material-check-all: Update resource | `module avail OpenFOAM`    |
| abacus         | :material-close:     Delete resource | `module avail abacus`    | 

## Modules

*"How-To-Use-Software-Without-installing-everything-yourself"*

Since a lot of applications rely on 3rd party software, there is a program on most supercomputers, called the Module system. With this system, other software, like compilers or special math libraries, are easily loadable and usable. Depending on the institution, different modules might be available, but there are usually common ones like the Intel or GCC Compilers.

A few common commands, to enter into the supercomputer commandline and talk to the module system, are

- module list   lists loaded modules
- module avail  lists available (loadable) modules
- module load   loads module x
- module purge  unload all modules

If you recurrently need lots of modules, this loading can be automated with an (ba)sh-file, so that you just have to execute the file once and it loads all modules, you need.

## Parallel Programming

*"How-To-Use-More-Than-One-Core"*

Currently development of computers is at a point, where you cannot just make a processor run faster (e.g. by increasing its clock frequency), because limits of physics have been reached in semiconductor development. Therefore the current approach is to split the work into multiple, ideally independent parts, which are then executed in parallel. Similar to cleaning your house, where everybody takes care of a few rooms, on a supercomputer this is usually done with parallel programming paradigms like Open Multi-Processing (OpenMP) or Message Passing Interface (MPI). However like the fact that you only have one vacuum cleaner in the whole house which not everybody can use at the same time, there are limits on how fast you can get, even with a big number of processing units/cpus/cores (analogous to people in the metaphor) working on your problem (cleaning the house) in parallel.